#!/usr/bin/env python3
"""Tests des scripts de calcul. Lancer : python3 scripts/tests/test_calculs.py"""

import argparse
import contextlib
import datetime as dt
import io
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
import entrees  # noqa: E402
import louer_acheter  # noqa: E402
import projection  # noqa: E402
import tri  # noqa: E402


def lancer(module, args):
    """Lance le main d'un script ; renvoie (code, sortie standard, sortie d'erreur)."""
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            code = module.main(args)
        except SystemExit as e:
            code = e.code
    return code, out.getvalue(), err.getvalue()


EXEMPLE_RELAIS = ["achat-revente", "--revenus", "7000", "--charges-credit", "650", "--loyers", "800",
                  "--taux", "3.5", "--duree-mois", "300", "--assurance-taux", "0.30",
                  "--frais-acquisition-pct", "7.5", "--valeur-vente", "400000", "--crd-a-solder", "250000",
                  "--frais-vente", "5000", "--epargne-apport", "50000", "--taux-relais", "4.0",
                  "--mensualite-actuelle", "1500"]


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

    def test_remboursement_total_modes_egaux(self):
        # Prêt soldé : les deux modes reviennent au même, primes d'assurance comprises (audit P6).
        d = credit.anticipation(150000, 3.0, 120, 150000, 2.5, mode="duree", assurance_mensuelle=40)
        m = credit.anticipation(150000, 3.0, 120, 150000, 2.5, mode="mensualite", assurance_mensuelle=40)
        self.assertAlmostEqual(d["avantage_A_moins_B"], 10372.80, delta=0.05)
        self.assertAlmostEqual(m["avantage_A_moins_B"], d["avantage_A_moins_B"], delta=0.01)

    def test_remboursement_total_baisse_de_prime_seule(self):
        # Seule la baisse de prime est saisie : quand le prêt est soldé, toute la prime cesse quand même.
        for mode in ("duree", "mensualite"):
            d = credit.anticipation(150000, 3.0, 120, 150000, 2.5, mode=mode, assurance_economisee=40)
            self.assertAlmostEqual(d["avantage_A_moins_B"], 10372.80, delta=0.05, msg=mode)

    def test_cli_entrees_refusees(self):
        self.assertEqual(lancer(credit, ["mensualite", "--capital", "1000", "--taux", "3", "--duree-mois", "0"])[0], 2)
        self.assertEqual(lancer(credit, ["mensualite", "--capital", "300,000", "--taux", "3.5",
                                         "--duree-mois", "300"])[0], 2)
        self.assertEqual(lancer(credit, ["anticipation", "--crd", "1000", "--taux", "3", "--mois-restants", "12",
                                         "--montant", "2000", "--rendement-net", "2"])[0], 2)
        self.assertEqual(lancer(credit, ["anticipation", "--crd", "1000", "--taux", "3", "--mois-restants", "12",
                                         "--montant", "500", "--rendement-net", "-150"])[0], 2)


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

    def test_relais(self):
        self.assertAlmostEqual(capacite.relais_montant(550000, 0.7, 300000), 85000.0)
        self.assertEqual(capacite.relais_montant(300000, 0.7, 250000), 0.0)

    def test_budget_signature_formule(self):
        # (capital + relais disponible + épargne) / (1 + frais) : (483 806 + 85 000 + 100 000) / 1,075.
        self.assertAlmostEqual(capacite.budget_signature(483806, 85000, 100000, 7.5), 622145.1, delta=1)

    def test_deux_montages_exemple_du_guide(self):
        code, sortie, _ = lancer(capacite, EXEMPLE_RELAIS + ["--quotite-relais", "0.7"])
        self.assertEqual(code, 0)
        self.assertIn("Prix d'achat maximal : 534 641 €", sortie)  # vente encaissée d'abord
        # B1 : prêt en cours conservé, compté dans le taux d'effort (650 + 1 500 € de charges).
        d1 = capacite.capacite(7000, 3.5, 300, 0.30, 650 + 1500, 800)
        b1 = capacite.budget_signature(d1["capital_max"], 30000, 50000, 7.5)
        self.assertAlmostEqual(b1, 162199, delta=1)
        self.assertIn(f"(nouveau prêt + relais + épargne) : {capacite._eur(b1)}", sortie)
        # B2 : achat-revente, le relais de 280 000 € rachète le prêt en cours ; 30 000 € disponibles.
        d2 = capacite.capacite(7000, 3.5, 300, 0.30, 650, 800)
        b2 = capacite.budget_signature(d2["capital_max"], 30000, 50000, 7.5)
        self.assertAlmostEqual(b2, 427665, delta=1)
        self.assertIn(f"Prix d'achat maximal à la signature : {capacite._eur(b2)}", sortie)
        self.assertIn("Relais : 280 000 € dont 250 000 €", sortie)

    def test_mensualite_actuelle_exigee_avec_relais(self):
        args = [a for a in EXEMPLE_RELAIS]
        i = args.index("--mensualite-actuelle")
        del args[i:i + 2]
        code, _, err = lancer(capacite, args + ["--quotite-relais", "0.7"])
        self.assertEqual(code, 2)
        self.assertIn("--mensualite-actuelle", err)

    def test_alerte_quotite_80(self):
        _, sortie, _ = lancer(capacite, EXEMPLE_RELAIS + ["--quotite-relais", "0.9"])
        self.assertIn("supérieure à 80 %", sortie)
        _, sortie, _ = lancer(capacite, EXEMPLE_RELAIS + ["--quotite-relais", "0.8"])
        self.assertNotIn("supérieure à 80 %", sortie)


    def test_pourcentage_au_lieu_de_fraction(self):
        code, sortie, err = lancer(capacite, ["simple", "--revenus", "9000", "--taux", "3.5", "--duree-mois", "300",
                                              "--frais-acquisition-pct", "7.5", "--part-loyers", "70",
                                              "--loyers", "1400"])
        self.assertEqual(code, 2)
        self.assertEqual(sortie, "")
        self.assertIn("fraction entre 0 et 1", err)

    def test_vente_deficitaire_signalee(self):
        _, sortie, _ = lancer(capacite, ["achat-revente", "--revenus", "6000", "--taux", "3.5", "--duree-mois", "300",
                                         "--frais-acquisition-pct", "7.5", "--valeur-vente", "200000",
                                         "--crd-a-solder", "330000"])
        self.assertIn("ne solde pas le prêt en cours", sortie)


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

    def test_cli_entrees_refusees(self):
        for args in (["retrait-mc", "--capital", "0", "--retrait-annuel", "1000", "--annees", "10",
                      "--rendement-moyen", "3", "--volatilite", "10"],
                     ["montecarlo", "--annees", "10", "--rendement-moyen", "5", "--volatilite", "15",
                      "--simulations", "0"],
                     ["retraite", "--revenu-cible", "5000", "--pensions", "3000", "--taux-retrait", "0"],
                     ["retraite", "--revenu-cible", "5000", "--pensions", "3000", "--taux-retrait", "4",
                      "--taux-prelevement-retraits", "100"]):
            self.assertEqual(lancer(projection, args)[0], 2, args)

    def test_liste_point_virgule_et_virgule_decimale(self):
        code, sortie, _ = lancer(projection, ["retraite", "--revenu-cible", "5500", "--pensions", "3800",
                                              "--taux-retrait", "3;3,5;4"])
        self.assertEqual(code, 0)
        self.assertIn("Taux de retrait 3.5 %", sortie)


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
        with self.assertRaises(ValueError):
            tri.annualise(100, -10, 2)

    def test_flux_point_virgule_decimales(self):
        code, sortie, _ = lancer(tri, ["xirr", "--flux", "2021-01-01:-1000,50;2022-01-01:1100,55"])
        self.assertEqual(code, 0)
        self.assertIn("Versé : 1 000,50 €", sortie)
        self.assertIn("TRI annuel : 10,00 %", sortie)

    def test_meme_date_et_extreme(self):
        with self.assertRaises(ValueError):
            tri.xirr([(dt.date(2026, 1, 1), -1000), (dt.date(2026, 1, 1), 1000)])
        with self.assertRaises(ValueError) as ctx:
            tri.xirr([(dt.date(2026, 1, 1), -1000), (dt.date(2026, 1, 5), 1500)])
        self.assertIn("1 000 %", str(ctx.exception))

    def test_csv_avec_bom(self):
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8-sig") as f:
            f.write("date;montant\n2021-01-01;-1 000,00\n2022-01-01;1 100,00\n")
            chemin = f.name
        try:
            code, sortie, _ = lancer(tri, ["xirr", "--csv", chemin])
        finally:
            os.unlink(chemin)
        self.assertEqual(code, 0)
        self.assertIn("TRI annuel : 10,00 %", sortie)

    def test_montant_ambigu_refuse(self):
        for ambigu in ("1.234", "1,234", "-12.500"):
            with self.assertRaises(ValueError):
                tri._montant(ambigu)
        self.assertAlmostEqual(tri._montant("0.5"), 0.5)
        self.assertAlmostEqual(tri._montant("1234,5"), 1234.5)


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
            self.assertEqual(lancer(allocation, [chemin, "--arbitrage"])[0], 0)
        finally:
            os.unlink(chemin)

    def test_meme_fonds_dans_deux_enveloppes(self):
        # Audit I4 : World 92,3 % pour une cible de 90 % ; vendre 1 500 € de World, acheter 1 500 € d'EM.
        pos = [{"nom": "ETF World", "valeur": 40000}, {"nom": "ETF World", "valeur": 20000},
               {"nom": "ETF EM", "valeur": 5000}]
        cible = {"ETF World": 0.9, "ETF EM": 0.1}
        w, total = allocation.poids(pos)
        self.assertAlmostEqual(w["ETF World"], 60000 / 65000)
        arb = allocation.arbitrages(pos, cible)
        self.assertAlmostEqual(arb["ETF World"], -1500.0)
        self.assertAlmostEqual(arb["ETF EM"], 1500.0)
        rep = allocation.repartir_versement(pos, cible, 1000)
        self.assertAlmostEqual(rep["ETF World"], 0.0)
        self.assertAlmostEqual(rep["ETF EM"], 1000.0)

    def test_cible_en_pourcentages_refusee(self):
        with self.assertRaises(allocation.EntreeInvalide):
            allocation.verifier(self.positions, {"A": 80, "B": 10, "C": 10})
        with self.assertRaises(allocation.EntreeInvalide):
            allocation.verifier(self.positions, {"A": 0.5, "B": 0.1, "C": 0.1})

    def test_cible_arrondie_normalisee(self):
        with contextlib.redirect_stdout(io.StringIO()):
            c = allocation.verifier(self.positions, {"A": 0.33, "B": 0.33, "C": 0.33})
        self.assertAlmostEqual(sum(c.values()), 1.0)
        self.assertAlmostEqual(c["A"], 1 / 3)

    def test_saisies_mal_formees(self):
        with self.assertRaises(allocation.EntreeInvalide):
            allocation.verifier([{"nom": "A", "valeur": "100"}], {})
        with self.assertRaises(allocation.EntreeInvalide):
            allocation.verifier([{"nom": "A", "valeur": 100, "ventilation": "monde"}], {})

    def test_ventilation_nulle_refusee(self):
        with self.assertRaises(allocation.EntreeInvalide):
            allocation.transparence([{"nom": "A", "valeur": 100, "ventilation": {"X": 0.0}}])


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

    def test_bascules_multiples(self):
        res = [(1, 90, 100), (2, 110, 100), (3, 95, 100), (4, 120, 100)]
        self.assertEqual(louer_acheter.bascules(res), [(2, "achat"), (3, "location"), (4, "achat")])
        self.assertEqual(louer_acheter.bascules([(1, 90, 100), (2, 95, 100)]), [])

    def test_horizon(self):
        args = ["--prix", "300000", "--frais-acquisition-pct", "7.5", "--apport", "60000", "--taux", "3",
                "--duree-mois", "240", "--entretien-pct", "1", "--valorisation-pct", "1", "--frais-revente-pct", "5",
                "--loyer", "1000", "--hausse-loyer-pct", "1", "--rendement-placement-pct", "3"]
        self.assertEqual(lancer(louer_acheter, args + ["--horizon", "0.5"])[0], 2)
        code, sortie, _ = lancer(louer_acheter, args + ["--horizon", "7.5"])
        self.assertEqual(code, 0)
        self.assertIn("Horizon ramené à 7 ans", sortie)
        self.assertIn("net d'impôt chaque année", sortie)


class TestEntrees(unittest.TestCase):
    def test_fraction(self):
        self.assertAlmostEqual(entrees.fraction("0.7"), 0.7)
        self.assertAlmostEqual(entrees.fraction("0,7"), 0.7)
        for mauvais in ("70", "-0.1", "150"):
            with self.assertRaises(argparse.ArgumentTypeError):
                entrees.fraction(mauvais)

    def test_rendement_et_taux(self):
        self.assertAlmostEqual(entrees.rendement("-50"), -50.0)
        with self.assertRaises(argparse.ArgumentTypeError):
            entrees.rendement("-100")
        with self.assertRaises(argparse.ArgumentTypeError):
            entrees.taux_pret("35")  # 3,5 % saisi 35

    def test_nombre_francais(self):
        self.assertAlmostEqual(entrees.nombre("1 234,5"), 1234.5)
        self.assertAlmostEqual(entrees.nombre("0.035"), 0.035)
        for mauvais in ("abc", "300,000", "1.234"):
            with self.assertRaises(argparse.ArgumentTypeError):
                entrees.nombre(mauvais)


if __name__ == "__main__":
    unittest.main(verbosity=1)
