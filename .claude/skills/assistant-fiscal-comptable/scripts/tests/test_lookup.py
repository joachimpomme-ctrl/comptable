#!/usr/bin/env python3
"""Tests de lookup.py. Lancer : python3 .claude/skills/assistant-fiscal-comptable/scripts/tests/test_lookup.py"""
import os
import subprocess
import sys
import unittest

LOOKUP = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lookup.py")


def run(*args):
    r = subprocess.run([sys.executable, LOOKUP, *args], capture_output=True, text=True)
    return r.returncode, r.stdout


class TestLookup(unittest.TestCase):
    def test_regle_entiere_avec_correction(self):
        # Les corrections de ces regles etaient coupees par l'ancienne version (audit du 01/11/2026).
        for rid in ("LMN-025", "LMP-005", "ES-003", "PAT-015", "TRM-006", "TRM-008", "LMP-004", "LMP-006"):
            code, out = run("regles", rid)
            self.assertEqual(code, 0, rid)
            self.assertRegex(out.lower(), r"correction|pr[ée]cision", rid)

    def test_identifiant_normalise(self):
        self.assertEqual(run("regles", "lmn_025")[0], 0)
        code, out = run("crosswalk", "lmn-025")
        self.assertEqual(code, 0)
        self.assertIn("verdict", out)
        self.assertIn("preuve", out)

    def test_recherche_multi_mots_paginee(self):
        code, out = run("regles", "plus", "value")
        self.assertEqual(code, 0)
        self.assertIn("page 1 sur", out)
        self.assertLessEqual(out.count("### "), 5)

    def test_cgi_texte_integral(self):
        # 22 articles etaient coupes a 4 000 caracteres avant la reextraction du 01/11/2026.
        code, out = run("cgi", "150VB")
        self.assertEqual(code, 0)
        self.assertIn("III. – Le prix d'acquisition est minoré", out)
        code, out = run("cgi", "163 quatervicies")
        self.assertIn("l'une des cinq années", " ".join(out.split()))

    def test_aucun_article_coupe(self):
        import re
        base = os.path.join(os.path.dirname(LOOKUP), "..", "..", "..", "..", "knowledge", "M_CGI_code_general_impots.md")
        md = open(base, encoding="utf-8").read()
        blocs = re.findall(r"^## Article (.+?) —.*?\n```\n(.*?)\n```", md, re.S | re.M)
        self.assertEqual(len(blocs), 63)
        self.assertEqual([a for a, b in blocs if len(b) in (4000, 4001)], [])

    def test_lot2(self):
        code, out = run("cgi", "977")
        self.assertIn("17 500", out)
        for cle, valeur in (("carpimko_complementaire_taux", '"2026": 8.7'),
                            ("deficit_foncier_plafond_renovation_energetique", '"2027": 21400')):
            code, out = run("referentiel", cle)
            self.assertEqual(code, 0, cle)
            self.assertIn(valeur, out, cle)
        code, out = run("regles", "IFI-002")
        self.assertIn("17 500", out)

    def test_referentiel_lot1(self):
        for cle, valeur in (("seuil_micro_bic_classe", '"2026": 83600'), ("pfu_taux_global", '"2026": 31.4'),
                            ("ps_revenus_patrimoine", '"2025": 18.6')):
            code, out = run("referentiel", cle)
            self.assertEqual(code, 0, cle)
            self.assertIn(valeur, out, cle)

    def test_introuvable_et_usage(self):
        self.assertEqual(run("regles", "zzzz-inexistant")[0], 1)
        self.assertEqual(run("referentiel", "cle_inexistante")[0], 1)
        self.assertEqual(run("commande_inconnue", "x")[0], 2)

    def test_referentiel(self):
        code, out = run("referentiel", "PASS")
        self.assertEqual(code, 0)
        self.assertIn("48060", out.replace(" ", ""))


if __name__ == "__main__":
    unittest.main(verbosity=1)
