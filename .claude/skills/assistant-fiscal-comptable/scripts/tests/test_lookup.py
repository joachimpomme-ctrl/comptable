#!/usr/bin/env python3
"""Tests de lookup.py. Lancer : python3 .claude/skills/assistant-fiscal-comptable/scripts/tests/test_lookup.py"""
import json
import os
import re
import subprocess
import sys
import unittest

LOOKUP = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lookup.py")
RACINE = os.path.join(os.path.dirname(LOOKUP), "..", "..", "..", "..")
SECTION = re.compile(r"^## Article (?P<num>[^\n]+?) \u2014 [^\n]+\n\n\*\*Source :\*\* [^\n]*\| \*\*Tags :\*\* (?P<tags>[^\n]+)\n\n"
                     r"\*\*Version du texte :\*\* (?P<version>[^\n]+)\n\n(?P<notes>(?:> [^\n]*\n\n)*)```\n(?P<texte>.*?)\n```\n",
                     re.S | re.M)


def run(*args):
    r = subprocess.run([sys.executable, LOOKUP, *args], capture_output=True, text=True)
    return r.returncode, r.stdout


def articles_md():
    with open(os.path.join(RACINE, "knowledge", "M_CGI_code_general_impots.md"), encoding="utf-8") as f:
        md = f.read()
    arts = [dict(num=m["num"], tags=[t.strip() for t in m["tags"].split(",")], version=m["version"],
                 notes=[n[2:] for n in m["notes"].split("\n\n") if n.strip()], texte=m["texte"])
            for m in SECTION.finditer(md)]
    # chaque titre d'article doit avoir ete lu (sinon le format d'un article a derive)
    assert len(arts) == len(re.findall(r"^## Article ", md, re.M)), "section d'article au format inattendu"
    return arts


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
        blocs = [(a["num"], a["texte"]) for a in articles_md()]
        self.assertEqual(len(blocs), 73)
        self.assertEqual([a for a, b in blocs if len(b) in (4000, 4001)], [])

    def test_md_et_jsonl_identiques(self):
        # Constat T17 de l'audit du 01/11/2026 : meme texte, meme date de version, memes notes et etiquettes.
        md = {a["num"]: a for a in articles_md()}
        jl = {}
        with open(os.path.join(RACINE, "knowledge", "chatgpt_only", "M_CGI_code_general_impots.jsonl"), encoding="utf-8") as f:
            for ligne in f:
                if ligne.strip():
                    e = json.loads(ligne)
                    jl[e["article"].replace("CGI Art. ", "")] = e
        self.assertEqual(sorted(md), sorted(jl))
        for num, a in md.items():
            e = jl[num]
            self.assertEqual(e["texte_complet"], a["texte"], num)
            self.assertEqual(e["version_texte"], a["version"], num)
            self.assertEqual(e["notes"], a["notes"], num)
            self.assertEqual(e["tags"], a["tags"], num)
            self.assertIn("30/10/2026", a["version"], num)
            self.assertTrue(e["regle"].strip(), num)
        self.assertNotIn("77700", jl["102 ter"]["tags"])

    def test_pas_de_ligne_vide_dans_les_textes(self):
        # 108 lignes vides de saut de page coupaient des phrases avant le 01/11/2026.
        self.assertEqual([a["num"] for a in articles_md() if re.search(r"\n\s*\n", a["texte"])], [])

    def test_tableaux_lisibles(self):
        code, out = run("cgi", "194")
        self.assertEqual(code, 0)
        self.assertRegex(out, r"\| Célibataire ou divorcé ayant un enfant à charge +\| 1,5 +\|")
        self.assertRegex(out, r"\| Marié ou veuf ayant deux enfants à charge +\| 3 +\|")
        code, out = run("cgi", "777")
        self.assertEqual(code, 0)
        lignes = out.splitlines()
        for intitule, suite in (("Tableau I", "en ligne directe"), ("Tableau II", "entre époux"),
                                ("Tableau III", "en ligne collatérale")):
            self.assertIn(suite, lignes[lignes.index(intitule) + 1], intitule)
        self.assertRegex(out, r"\| Comprise entre 15 932 € et 31 865 € +\| 15 +\|")
        self.assertRegex(out, r"\| Entre parents au-delà du 4e degré et entre personnes non-parentes \| 60 +\|")

    def test_articles_ajoutes(self):
        for num, extrait in (("32", "n'excède pas 15 000 €"), ("39 C", "dans la limite du montant du loyer"),
                             ("39 duodecies", "moins de deux ans"), ("150 V", "prix de cession et le prix d'acquisition"),
                             ("238 quindecies", "500 000 €"), ("239", "l'option devient irrévocable"),
                             ("302 septies A bis", "189 000 €"), ("790 E", "80 724 €"),
                             ("796-0 bis", "conjoint survivant"), ("978", "dans la limite de 50 000 €")):
            code, out = run("cgi", num)
            self.assertEqual(code, 0, num)
            self.assertIn(extrait, " ".join(out.split()), num)

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
