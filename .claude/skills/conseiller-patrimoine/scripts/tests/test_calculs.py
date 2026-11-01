#!/usr/bin/env python3
"""Tests des scripts de calcul. Lancer : python scripts/tests/test_calculs.py"""

import datetime as dt
import json
import os
import sys
import tempfile
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))

import allocation  # noqa: E402
import capacite  # noqa: E402
import credit  # noqa: E402
import louer_acheter  # noqa: E402
import projection  # noqa: E402
import tri  # noqa: E402


class TestCredit(unittest.TestCase):
    def test_mensualite_reference(self):
        # 200 000 € à 3 % sur 20 ans : 1 109,20 € (valeur de référence publiée par les simulateurs bancaires)
        self.assertAlmostEqual(credit.mensualite(200000, 3.0, 240), 1109.20, delta=0.01)

    def test_mensualite_taux_nul(self):
        self.assertAlmostEqual(credit.mensualite(120000, 0.0, 120), 1000.0)

    def test_empruntable_inverse(self):
        m = credit.mensualite(345678, 3.7, 300)
        self.assertAlmostEqual(credit.capital_empruntable(m, 3.7, 300), 345678, delta=0.01)

    def test_crd_bornes_et_tableau(self):
        self.assertEqual(credit.crd_apres(100000, 2.0, 120, 0), 100000)
        self.assertEqual(credit.crd_apres(100000, 2.0, 120, 120), 0.0)
        t = credit.tableau(100000, 2.0, 120)
        self.assertAlmostEqual(t[23]["crd"], credit.crd_apres(100000, 2.0, 120, 24), delta=0.05)
        self.assertAlmostEqual(sum(l["capital_amorti"] for l in t), 100000, delta=0.5)
        self.assertEqual(t[-1]["crd"], 0.0)

    def test_ira(self):
        d = credit.ira_plafond(100000, 150000, 4.0)
        self.assertAlmostEqual(d["six_mois_interets"], 2000.0)
        self.assertAlmostEqual(d["trois_pct_crd"], 4500.0)
        self.assertAlmostEqual(d["plafond"], 2000.0)
        d = credit.ira_plafond(100000, 100000, 8.0)
        self.assertAlmostEqual(d["plafond"], 3000.0)

    def test_anticipation_neutre_si_meme_taux(self):
        # Placement au taux effectif équivalent au taux du prêt : rembourser ou placer revient au même.
        taux = 3.0
        equivalent = ((1 + taux / 1200) ** 12 - 1) * 100
        for mode in ("duree", "mensualite"):
            d = credit.anticipation(200000, taux, 240, 50000, equivalent, mode=mode)
            self.assertAlmostEqual(d["avantage_A_moins_B"], 0.0, delta=1.0, msg=mode)

    def test_anticipation_sens(self):
        d = credit.anticipation(200000, 1.0, 240, 50000, 3.0)
        self.assertLess(d["avantage_A_moins_B"], 0)  # placer à 3 % bat rembourser un prêt à 1 %
        d = credit.anticipation(200000, 5.0, 240, 50000, 2.0)
        self.assertGreater(d["avantage_A_moins_B"], 0)
        self.assertGreater(d["interets_economises"], 0)

    def test_anticipation_assurance_mode_duree(self):
        # En mode durée, l'assurance s'arrête plus tôt en A : l'avantage de A augmente.
        sans = credit.anticipation(200000, 1.2, 216, 50000, 2.0, mode="duree")
        avec = credit.anticipation(200000, 1.2, 216, 50000, 2.0, mode="duree", assurance_mensuelle=62.5)
        self.assertGreater(avec["avantage_A_moins_B"], sans["avantage_A_moins_B"] + 2000)

    def test_anticipation_ira_reduit_avantage(self):
        a = credit.anticipation(200000, 4.0, 240, 50000, 2.0)
        b = credit.anticipation(200000, 4.0, 240, 50000, 2.0, ira=1000)
        self.assertLess(b["avantage_A_moins_B"], a["avantage_A_moins_B"])


class TestTriMontant(unittest.TestCase):
    def test_formats(self):
        self.assertAlmostEqual(tri._montant("1\u202f234,56"), 1234.56)
        self.assertAlmostEqual(tri._montant("-1.234,56 €"), -1234.56)
        self.assertAlmostEqual(tri._montant("1,234.56"), 1234.56)
        self.assertAlmostEqual(tri._montant("-500"), -500.0)


class TestCapacite(unittest.TestCase):
    def test_taux_effort_respecte(self):
        d = capacite.capacite(8000, 3.5, 300, assurance_taux_pct=0.3, charges_credit=500)
        self.assertAlmostEqual(d["taux_effort"], 35.0, delta=0.01)
        self.assertAlmostEqual(d["charge_max_totale"], 2800.0)
        self.assertAlmostEqual(d["mensualite_credit"] + d["mensualite_assurance"], 2300.0, delta=0.01)

    def test_loyers_retenus(self):
        d = capacite.capacite(5000, 3.0, 240, loyers=1000, part_loyers=0.7)
        self.assertAlmostEqual(d["revenus_retenus"], 5700.0)

    def test_charges_superieures(self):
        d = capacite.capacite(3000, 3.0, 240, charges_credit=2000)
        self.assertEqual(d["capital_max"], 0.0)

    def test_prix_max(self):
        # capital 300 000 + apport 100 000 = 400 000 = prix x 1,08 -> prix = 370 370
        self.assertAlmostEqual(capacite.prix_max(300000, 100000, 8.0), 400000 / 1.08, delta=0.01)


class TestProjection(unittest.TestCase):
    def test_rendement_nul(self):
        v = projection.valeur_future(1000, 100, 10, 0.0)
        self.assertAlmostEqual(v, 1000 + 100 * 120)

    def test_capital_seul(self):
        v = projection.valeur_future(10000, 0, 10, 5.0)
        self.assertAlmostEqual(v, 10000 * 1.05 ** 10, delta=0.01)

    def test_rente_formule(self):
        rm = 1.04 ** (1 / 12) - 1
        attendu = 500 * ((1 + rm) ** 240 - 1) / rm
        self.assertAlmostEqual(projection.valeur_future(0, 500, 20, 4.0), attendu, delta=0.01)

    def test_montecarlo_moyenne(self):
        f = projection.montecarlo(10000, 0, 10, 6.0, 15.0, simulations=20000, graine=42)
        moyenne = sum(f) / len(f)
        # espérance théorique 10 000 x 1,06^10 = 17 908 ; tolérance d'échantillonnage
        self.assertAlmostEqual(moyenne / (10000 * 1.06 ** 10), 1.0, delta=0.03)

    def test_montecarlo_volatilite_nulle(self):
        f = projection.montecarlo(10000, 0, 5, 4.0, 0.0, simulations=10, graine=1)
        self.assertAlmostEqual(f[0], 10000 * 1.04 ** 5, delta=0.01)

    def test_retrait_certain(self):
        p, _ = projection.retrait_mc(100000, 12000, 30, 0.0, 0.0, simulations=50, graine=1)
        self.assertEqual(p, 0.0)  # 30 ans x 12 000 > 100 000 sans rendement
        p, _ = projection.retrait_mc(100000, 3000, 30, 0.0, 0.0, simulations=50, graine=1)
        self.assertEqual(p, 1.0)


class TestTri(unittest.TestCase):
    def test_dix_pour_cent(self):
        flux = [(dt.date(2021, 1, 1), -1000), (dt.date(2022, 1, 1), 1100)]
        self.assertAlmostEqual(tri.xirr(flux), 0.10, delta=1e-6)

    def test_annee_bissextile(self):
        flux = [(dt.date(2020, 1, 1), -1000), (dt.date(2021, 1, 1), 1100)]
        self.assertAlmostEqual(tri.xirr(flux), 1.1 ** (365 / 366) - 1, delta=1e-6)

    def test_flux_multiples(self):
        # Deux versements de 1 000 à 1 an d'écart, valeur finale qui donne exactement 5 %.
        d0, d1, d2 = dt.date(2021, 1, 1), dt.date(2022, 1, 1), dt.date(2023, 1, 1)
        final = 1000 * 1.05 ** (730 / 365) + 1000 * 1.05 ** (365 / 365)
        self.assertAlmostEqual(tri.xirr([(d0, -1000), (d1, -1000), (d2, final)]), 0.05, delta=1e-6)

    def test_annualise(self):
        self.assertAlmostEqual(tri.annualise(100, 121, 2), 0.10, delta=1e-12)


class TestAllocation(unittest.TestCase):
    def setUp(self):
        self.positions = [
            {"nom": "A", "valeur": 9000, "ventilation": {"X": 0.5, "Y": 0.5}},
            {"nom": "B", "valeur": 500, "ventilation": {"Y": 1.0}},
            {"nom": "C", "valeur": 500, "ventilation": {"Z": 1.0}},
        ]
        self.cible = {"A": 0.8, "B": 0.1, "C": 0.1}

    def test_transparence(self):
        z = allocation.transparence(self.positions)
        self.assertAlmostEqual(z["X"][0], 4500)
        self.assertAlmostEqual(z["Y"][0], 5000)
        self.assertAlmostEqual(z["Z"][1], 0.05)

    def test_versement_comble_deficits(self):
        rep = allocation.repartir_versement(self.positions, self.cible, 1000)
        # total après = 11 000 ; cibles B et C = 1 100 chacune ; déficits 600 + 600 > 1 000
        self.assertAlmostEqual(rep["A"], 0.0)
        self.assertAlmostEqual(rep["B"], 500.0)
        self.assertAlmostEqual(rep["C"], 500.0)
        self.assertAlmostEqual(sum(rep.values()), 1000.0)

    def test_versement_excedentaire(self):
        rep = allocation.repartir_versement(self.positions, self.cible, 10000)
        self.assertAlmostEqual(sum(rep.values()), 10000.0)
        valeurs = {p["nom"]: p["valeur"] + rep[p["nom"]] for p in self.positions}
        total = sum(valeurs.values())
        for n, c in self.cible.items():
            self.assertAlmostEqual(valeurs[n] / total, c, delta=1e-9)

    def test_arbitrages_somme_nulle(self):
        arb = allocation.arbitrages(self.positions, self.cible)
        self.assertAlmostEqual(sum(arb.values()), 0.0, delta=1e-9)

    def test_cli(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump({"positions": self.positions, "cible": self.cible, "versement": 1000}, f)
            chemin = f.name
        try:
            self.assertEqual(allocation.main([chemin, "--arbitrage"]), 0)
        finally:
            os.unlink(chemin)


class TestLouerAcheter(unittest.TestCase):
    def test_valorisation_forte_favorise_achat(self):
        commun = dict(prix=300000, frais_acquisition_pct=7.5, apport=60000, taux=3.0, duree_mois=240,
                      assurance_mensuelle=0, taxe_fonciere=1000, entretien_pct=1.0, charges_proprio=0,
                      frais_revente_pct=5, loyer=1000, hausse_loyer_pct=1.0,
                      rendement_placement_pct=3.0, horizon_annees=20)
        haut, _, _ = louer_acheter.simuler(valorisation_pct=5.0, **commun)
        bas, _, _ = louer_acheter.simuler(valorisation_pct=-1.0, **commun)
        self.assertGreater(haut[-1][1] - haut[-1][2], bas[-1][1] - bas[-1][2])

    def test_apport_excedentaire_conserve(self):
        res, emprunt, _ = louer_acheter.simuler(300000, 7.5, 400000, 3.0, 240, 0, 0, 0.0, 0, 0.0, 0,
                                                0.0, 0.0, 0.0, 1)
        self.assertEqual(emprunt, 0.0)
        annee, acheteur, locataire = res[0]
        # sans frais de revente, sans loyer ni rendement : 300 000 de bien + 77 500 d'excédent = 377 500
        self.assertAlmostEqual(acheteur, 377500, delta=1)
        self.assertAlmostEqual(locataire, 400000, delta=1)

    def test_premiere_annee_frais_penalisent_achat(self):
        res, _, _ = louer_acheter.simuler(300000, 7.5, 60000, 3.0, 240, 0, 1000, 1.0, 0, 0.0, 5,
                                          1000, 0.0, 3.0, 1)
        annee, acheteur, locataire = res[0]
        self.assertLess(acheteur, locataire)


if __name__ == "__main__":
    unittest.main(verbosity=1)
