#!/usr/bin/env python3
"""Capacité d'emprunt et budget d'achat au taux d'effort HCSF.

Le taux d'effort, la durée et la part des loyers retenue sont des paramètres :
les vérifier (references/01-fraicheur.md) et les confirmer avec la banque.

Exemples :
  python3 capacite.py simple --revenus 7000 --taux 3.5 --duree-mois 300 \
      --assurance-taux 0.30 --apport 150000 --frais-acquisition-pct 7.5

  python3 capacite.py achat-revente --revenus 7000 --charges-credit 650 --loyers 800 \
      --taux 3.5 --duree-mois 300 --assurance-taux 0.30 --frais-acquisition-pct 7.5 \
      --valeur-vente 400000 --crd-a-solder 250000 --frais-vente 5000 \
      --epargne-apport 50000 --quotite-relais 0.6 --taux-relais 4.0 --mensualite-actuelle 1500

Conventions :
  --revenus : revenus nets mensuels du foyer avant impôt sur le revenu.
  --charges-credit : mensualités des crédits conservés, assurance comprise.
  --loyers : loyers mensuels perçus, retenus à --part-loyers (0.70 par défaut,
             pratique bancaire courante, à confirmer).
  --assurance-taux : coût annuel de l'assurance en % du capital emprunté.
  --part-loyers et --quotite-relais : fractions (0.70 pour 70 %), les autres taux en %.

Achat avant la vente : le budget à la signature vaut nouveau prêt + relais +
épargne. Le produit net de la vente au-delà du relais n'arrive qu'à la vente :
il ne finance pas l'achat. Deux montages sont chiffrés : relais simple (le prêt
en cours continue et compte dans le taux d'effort) et achat-revente (le relais
rachète le prêt en cours).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from credit import mensualite  # noqa: E402
from entrees import (entier_min, fraction, montant, montant_positif, pct_0_100,  # noqa: E402
                     pct_borne, pct_frais, taux_assurance, taux_pret)


def capital_max(mensualite_dispo, taux_pct, n_mois, assurance_taux_pct):
    """Capital C tel que mensualité(C) + assurance(C) = mensualité disponible."""
    if mensualite_dispo <= 0:
        return 0.0
    unitaire = mensualite(1.0, taux_pct, n_mois) + assurance_taux_pct / 100.0 / 12.0
    return mensualite_dispo / unitaire


def capacite(revenus, taux_pct, n_mois, assurance_taux_pct=0.0, charges_credit=0.0,
             loyers=0.0, part_loyers=0.70, taux_effort_max=35.0):
    revenus_retenus = revenus + loyers * part_loyers
    charge_max = revenus_retenus * taux_effort_max / 100.0
    dispo = charge_max - charges_credit
    c = capital_max(dispo, taux_pct, n_mois, assurance_taux_pct)
    m_credit = mensualite(c, taux_pct, n_mois) if c > 0 else 0.0
    m_ass = c * assurance_taux_pct / 100.0 / 12.0
    return {
        "revenus_retenus": revenus_retenus,
        "charge_max_totale": charge_max,
        "mensualite_disponible": max(dispo, 0.0),
        "capital_max": c,
        "mensualite_credit": m_credit,
        "mensualite_assurance": m_ass,
        "taux_effort": (charges_credit + m_credit + m_ass) / revenus_retenus * 100 if revenus_retenus else 0.0,
    }


def prix_max(capital, apport, frais_acquisition_pct, travaux=0.0, frais_garantie_pct=0.0):
    """Prix d'achat finançable : capital + apport couvrent prix, frais, travaux, garantie."""
    disponible = capital * (1 - frais_garantie_pct / 100.0) + apport - travaux
    return max(disponible / (1 + frais_acquisition_pct / 100.0), 0.0)


def relais_montant(valeur_vente, quotite_relais, crd_a_solder):
    """Prêt relais : quotité de la valeur estimée du bien vendu, moins le capital restant dû."""
    return max(valeur_vente * quotite_relais - crd_a_solder, 0.0)


def budget_signature(capital, relais, epargne, frais_acquisition_pct, travaux=0.0, frais_garantie_pct=0.0):
    """Prix d'achat finançable le jour de la signature quand on achète avant de vendre :
    nouveau prêt + relais + épargne. Le reste du produit de la vente n'est pas encore là."""
    return prix_max(capital, relais + epargne, frais_acquisition_pct, travaux, frais_garantie_pct)


def _eur(x):
    return f"{x:,.0f} €".replace(",", " ")


def _pct(x):
    return f"{x:.0%}".replace("%", " %")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)

    def communs(a):
        a.add_argument("--revenus", type=montant_positif, required=True)
        a.add_argument("--charges-credit", type=montant, default=0.0)
        a.add_argument("--loyers", type=montant, default=0.0)
        a.add_argument("--part-loyers", type=fraction, default=0.70,
                       help="part des loyers retenue, en fraction (0.70 pour 70 %%)")
        a.add_argument("--taux", type=taux_pret, required=True, help="taux nominal annuel du nouveau prêt, en %%")
        a.add_argument("--duree-mois", type=entier_min(1), required=True)
        a.add_argument("--assurance-taux", type=taux_assurance, default=0.0)
        a.add_argument("--taux-effort-max", type=pct_borne(1, 100, "taux d'effort"), default=35.0)
        a.add_argument("--frais-acquisition-pct", type=pct_frais, required=True)
        a.add_argument("--frais-garantie-pct", type=pct_borne(0, 10, "frais de garantie"), default=0.0)
        a.add_argument("--travaux", type=montant, default=0.0)
        a.add_argument("--charges-fixes", type=montant, default=0.0,
                       help="dépenses fixes hors crédit, pour le reste à vivre")
        a.add_argument("--impot-mensuel", type=montant, default=0.0,
                       help="impôt sur le revenu mensualisé, pour le reste à vivre")
        a.add_argument("--charges-locatives", type=montant, default=0.0,
                       help="taxe foncière, charges et assurances des biens loués, par mois")

    a = sp.add_parser("simple")
    communs(a)
    a.add_argument("--apport", type=montant, default=0.0)

    a = sp.add_parser("achat-revente")
    communs(a)
    a.add_argument("--valeur-vente", type=montant_positif, required=True, help="prix net vendeur espéré")
    a.add_argument("--crd-a-solder", type=montant, required=True)
    a.add_argument("--ira-vente", type=montant, default=0.0)
    a.add_argument("--frais-vente", type=montant, default=0.0, help="diagnostics, mainlevée, etc.")
    a.add_argument("--epargne-apport", type=montant, default=0.0, help="épargne affectée à l'apport")
    a.add_argument("--quotite-relais", type=fraction, default=0.0,
                   help="part de la valeur du bien vendu avancée en relais, en fraction (0 = pas de relais)")
    a.add_argument("--taux-relais", type=taux_pret, default=0.0)
    a.add_argument("--mensualite-actuelle", type=montant, default=0.0,
                   help="mensualité du prêt à solder, assurance comprise, payée pendant le portage")
    a.add_argument("--decote-scenario", type=pct_0_100, default=10.0,
                   help="baisse du prix de vente testée dans le scénario défavorable, en %%")

    args = p.parse_args(argv)
    if (args.cmd == "achat-revente" and args.quotite_relais > 0 and args.crd_a_solder > 0
            and args.mensualite_actuelle == 0):
        p.error("avec un relais et un capital restant dû, renseigner --mensualite-actuelle (mensualité du prêt "
                "en cours, assurance comprise) : elle change la capacité d'emprunt pendant le portage")
    if 0 < args.taux < 0.5:
        print(f"Attention : taux de {args.taux} % ; vérifier l'unité (3.5 pour 3,5 %).")
    if args.duree_mois > 300:
        print("Attention : durée au-delà de 25 ans, hors norme HCSF sauf différé ou dérogation.")

    print(f"Hypothèses : revenus {_eur(args.revenus)}/mois, loyers {_eur(args.loyers)} retenus à "
          f"{_pct(args.part_loyers)}, charges de crédit conservées {_eur(args.charges_credit)}, "
          f"taux {args.taux} %, {args.duree_mois} mois, assurance {args.assurance_taux} %/an du capital, "
          f"taux d'effort max {args.taux_effort_max} %, frais d'acquisition {args.frais_acquisition_pct} %")

    if args.cmd == "simple":
        d = capacite(args.revenus, args.taux, args.duree_mois, args.assurance_taux,
                     args.charges_credit, args.loyers, args.part_loyers, args.taux_effort_max)
        pm = prix_max(d["capital_max"], args.apport, args.frais_acquisition_pct,
                      args.travaux, args.frais_garantie_pct)
        for k, v in d.items():
            print(f"{k} : {v:.1f} %" if k == "taux_effort" else f"{k} : {_eur(v)}")
        print(f"Prix d'achat maximal (apport {_eur(args.apport)}) : {_eur(pm)}")
        rav = (args.revenus - args.impot_mensuel + args.loyers - args.charges_locatives - args.charges_credit
               - d["mensualite_credit"] - d["mensualite_assurance"] - args.charges_fixes)
        libelle = "après impôt" if args.impot_mensuel else "avant impôt sur le revenu (renseigner --impot-mensuel)"
        print(f"Reste à vivre mensuel, {libelle} : {_eur(rav)}")
        if rav < 0:
            print("Alerte : reste à vivre négatif, le projet ne tient pas avec ces hypothèses.")
        return 0

    # achat-revente
    d = capacite(args.revenus, args.taux, args.duree_mois, args.assurance_taux,
                 args.charges_credit, args.loyers, args.part_loyers, args.taux_effort_max)
    print("\nA. Vendre d'abord, acheter ensuite (vente signée et encaissée avant l'achat)")
    print(f"  Capital maximal du nouveau prêt : {_eur(d['capital_max'])} (prêt en cours soldé par la vente)")
    prix_vente_d_abord = None
    for scenario, decote in (("central", 0.0), ("défavorable", args.decote_scenario)):
        vente = args.valeur_vente * (1 - decote / 100.0)
        net_vente = vente - args.crd_a_solder - args.ira_vente - args.frais_vente
        apport = net_vente + args.epargne_apport  # une vente déficitaire consomme l'épargne
        pm = prix_max(d["capital_max"], apport, args.frais_acquisition_pct, args.travaux, args.frais_garantie_pct)
        if prix_vente_d_abord is None:
            prix_vente_d_abord = pm
        print(f"  Scénario {scenario} : vente à {_eur(vente)}")
        print(f"    Produit net de la vente : {_eur(net_vente)}")
        if net_vente < 0:
            print(f"    Alerte : la vente ne solde pas le prêt en cours ; il manque {_eur(-net_vente)}.")
        print(f"    Apport total (produit net + épargne) : {_eur(max(apport, 0.0))}")
        print(f"    Prix d'achat maximal : {_eur(pm)}")

    print("\nB. Acheter d'abord, vendre ensuite")
    if args.crd_a_solder > 0 and args.mensualite_actuelle == 0:
        print("  Renseigner --mensualite-actuelle (prêt en cours, assurance comprise) pour chiffrer l'achat "
              "avant la vente : tant que ce prêt court, la banque le compte en principe dans le taux d'effort.")
    # B1 : le prêt en cours continue jusqu'à la vente et compte dans le taux d'effort.
    d1 = capacite(args.revenus, args.taux, args.duree_mois, args.assurance_taux,
                  args.charges_credit + args.mensualite_actuelle, args.loyers, args.part_loyers,
                  args.taux_effort_max)
    relais_net = relais_montant(args.valeur_vente, args.quotite_relais, args.crd_a_solder)
    pm1 = budget_signature(d1["capital_max"], relais_net, args.epargne_apport, args.frais_acquisition_pct,
                           args.travaux, args.frais_garantie_pct)
    titre1 = "B1. Relais simple" if args.quotite_relais > 0 else "B1. Sans prêt relais"
    print(f"  {titre1} : le prêt en cours continue jusqu'à la vente et compte dans le taux d'effort "
          f"(pratique bancaire, probable, à confirmer)")
    if args.quotite_relais > 0:
        print(f"    Prêt relais : {_eur(relais_net)} ({_pct(args.quotite_relais)} de la valeur estimée moins le CRD)")
    print(f"    Capital maximal du nouveau prêt : {_eur(d1['capital_max'])}")
    print(f"    Prix d'achat maximal à la signature (nouveau prêt + relais + épargne) : {_eur(pm1)}, soit "
          f"{_eur(max(prix_vente_d_abord - pm1, 0.0))} de moins que si la vente est encaissée avant")
    if args.quotite_relais == 0:
        return 0

    # B2 : achat-revente, le relais rachète le prêt en cours (une seule mensualité pendant le portage).
    relais_brut = args.valeur_vente * args.quotite_relais
    print("  B2. Achat-revente : le relais rachète le prêt en cours, plus d'ancienne mensualité pendant le portage")
    if relais_brut < args.crd_a_solder:
        print("    Impossible ici : le relais ne couvre pas le capital restant dû.")
        pm2 = None
    else:
        pm2 = budget_signature(d["capital_max"], relais_net, args.epargne_apport, args.frais_acquisition_pct,
                               args.travaux, args.frais_garantie_pct)
        print(f"    Relais : {_eur(relais_brut)} dont {_eur(args.crd_a_solder)} pour solder le prêt en cours, "
              f"{_eur(relais_net)} disponibles pour l'achat")
        print(f"    Capital maximal du nouveau prêt : {_eur(d['capital_max'])}")
        print(f"    Prix d'achat maximal à la signature : {_eur(pm2)}, soit "
              f"{_eur(max(prix_vente_d_abord - pm2, 0.0))} de moins que si la vente est encaissée avant")
    print("  Dans les deux montages, le produit de la vente au-delà du relais n'arrive qu'à la vente : il ne "
          "finance pas l'achat. Demander à la banque quel montage elle propose et comment elle compte le prêt en cours.")

    a_rembourser = max(relais_brut, args.crd_a_solder) + args.ira_vente + args.frais_vente
    for scenario, decote in (("central", 0.0), ("défavorable", args.decote_scenario)):
        vente = args.valeur_vente * (1 - decote / 100.0)
        if vente < a_rembourser:
            print(f"  Alerte, scénario {scenario} : la vente ne couvre pas relais + CRD + frais ; besoin de "
                  f"trésorerie de {_eur(a_rembourser - vente)}")
    if args.quotite_relais > 0.80:
        print("  Alerte : quotité du relais supérieure à 80 % de la valeur du bien vendu. Ses intérêts ne "
              "peuvent pas être exclus du taux d'effort (HCSF) : les capacités ci-dessus sont surestimées.")
    else:
        print("  Quotité d'au plus 80 % : les intérêts du relais peuvent être exclus du taux d'effort (HCSF, "
              "décembre 2023). À confirmer avec la banque.")

    interets1 = relais_net * args.taux_relais / 100.0 / 12.0
    interets2 = relais_brut * args.taux_relais / 100.0 / 12.0
    charge1 = (args.charges_credit + args.mensualite_actuelle + d1["mensualite_credit"]
               + d1["mensualite_assurance"] + interets1)
    print(f"  Charge mensuelle pendant le portage, B1 : {_eur(charge1)} (crédits conservés + prêt en cours + "
          f"nouveau prêt + {_eur(interets1)} d'intérêts du relais), soit "
          f"{charge1 / d['revenus_retenus'] * 100:.1f} % des revenus retenus")
    if pm2 is not None:
        charge2 = args.charges_credit + d["mensualite_credit"] + d["mensualite_assurance"] + interets2
        print(f"  Charge mensuelle pendant le portage, B2 : {_eur(charge2)} (crédits conservés + nouveau prêt + "
              f"{_eur(interets2)} d'intérêts du relais), soit {charge2 / d['revenus_retenus'] * 100:.1f} % des "
              f"revenus retenus")
    for mois in (6, 12, 24):
        ligne = (f"  Coût de portage sur {mois} mois (hors taxe foncière, charges et énergie du bien vide) : "
                 f"B1 {_eur((interets1 + args.mensualite_actuelle) * mois)} (ancienne mensualité comprise, "
                 f"capital compris)")
        if pm2 is not None:
            ligne += f" ; B2 {_eur(interets2 * mois)} (intérêts du relais)"
        print(ligne)
    return 0


if __name__ == "__main__":
    sys.exit(main())
