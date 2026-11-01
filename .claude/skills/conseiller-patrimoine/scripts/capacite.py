#!/usr/bin/env python3
"""Capacité d'emprunt et budget d'achat au taux d'effort HCSF.

Le taux d'effort, la durée et la part des loyers retenue sont des paramètres :
les vérifier (references/01-fraicheur.md) et les confirmer avec la banque.

Exemples :
  python capacite.py simple --revenus 7000 --taux 3.5 --duree-mois 300 \
      --assurance-taux 0.30 --apport 150000 --frais-acquisition-pct 7.5

  python capacite.py achat-revente --revenus 7000 --charges-credit 650 --loyers 800 \
      --taux 3.5 --duree-mois 300 --assurance-taux 0.30 --frais-acquisition-pct 7.5 \
      --valeur-vente 400000 --crd-a-solder 250000 --frais-vente 5000 \
      --epargne-apport 50000 --quotite-relais 0.6 --taux-relais 4.0 --mensualite-actuelle 1500

Conventions :
  --revenus : revenus nets mensuels du foyer avant impôt sur le revenu.
  --charges-credit : mensualités des crédits conservés, assurance comprise.
  --loyers : loyers mensuels perçus, retenus à --part-loyers (0.70 par défaut,
             pratique bancaire courante, à confirmer).
  --assurance-taux : coût annuel de l'assurance en % du capital emprunté.
"""

import argparse
import sys

sys.path.insert(0, __import__("os").path.dirname(__file__))
from credit import mensualite  # noqa: E402


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


def _eur(x):
    return f"{x:,.0f} €".replace(",", " ")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)

    def communs(a):
        a.add_argument("--revenus", type=float, required=True)
        a.add_argument("--charges-credit", type=float, default=0.0)
        a.add_argument("--loyers", type=float, default=0.0)
        a.add_argument("--part-loyers", type=float, default=0.70)
        a.add_argument("--taux", type=float, required=True, help="taux nominal annuel du nouveau prêt, en %%")
        a.add_argument("--duree-mois", type=int, required=True)
        a.add_argument("--assurance-taux", type=float, default=0.0)
        a.add_argument("--taux-effort-max", type=float, default=35.0)
        a.add_argument("--frais-acquisition-pct", type=float, required=True)
        a.add_argument("--frais-garantie-pct", type=float, default=0.0)
        a.add_argument("--travaux", type=float, default=0.0)
        a.add_argument("--charges-fixes", type=float, default=0.0,
                       help="dépenses fixes hors crédit, pour le reste à vivre")
        a.add_argument("--impot-mensuel", type=float, default=0.0,
                       help="impôt sur le revenu mensualisé, pour le reste à vivre")
        a.add_argument("--charges-locatives", type=float, default=0.0,
                       help="taxe foncière, charges et assurances des biens loués, par mois")

    a = sp.add_parser("simple")
    communs(a)
    a.add_argument("--apport", type=float, default=0.0)

    a = sp.add_parser("achat-revente")
    communs(a)
    a.add_argument("--valeur-vente", type=float, required=True, help="prix net vendeur espéré")
    a.add_argument("--crd-a-solder", type=float, required=True)
    a.add_argument("--ira-vente", type=float, default=0.0)
    a.add_argument("--frais-vente", type=float, default=0.0, help="diagnostics, mainlevée, etc.")
    a.add_argument("--epargne-apport", type=float, default=0.0, help="épargne affectée à l'apport")
    a.add_argument("--quotite-relais", type=float, default=0.0,
                   help="part de la valeur du bien vendu avancée en relais (0 = pas de relais)")
    a.add_argument("--taux-relais", type=float, default=0.0)
    a.add_argument("--mensualite-actuelle", type=float, default=0.0,
                   help="mensualité du prêt à solder, assurance comprise, payée pendant le portage")
    a.add_argument("--decote-scenario", type=float, default=10.0,
                   help="baisse du prix de vente testée dans le scénario défavorable, en %%")

    args = p.parse_args(argv)
    if args.duree_mois > 300:
        print("Attention : durée au-delà de 25 ans, hors norme HCSF sauf différé ou dérogation.")

    print(f"Hypothèses : revenus {_eur(args.revenus)}/mois, loyers {_eur(args.loyers)} retenus à "
          f"{args.part_loyers:.0%}, charges de crédit conservées {_eur(args.charges_credit)}, "
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
        return 0

    # achat-revente
    d = capacite(args.revenus, args.taux, args.duree_mois, args.assurance_taux,
                 args.charges_credit, args.loyers, args.part_loyers, args.taux_effort_max)
    for scenario, decote in (("central", 0.0), ("défavorable", args.decote_scenario)):
        vente = args.valeur_vente * (1 - decote / 100.0)
        net_vente = vente - args.crd_a_solder - args.ira_vente - args.frais_vente
        apport = net_vente + args.epargne_apport
        pm = prix_max(d["capital_max"], apport, args.frais_acquisition_pct, args.travaux, args.frais_garantie_pct)
        print(f"\nScénario {scenario} : vente à {_eur(vente)}")
        print(f"  Produit net de la vente : {_eur(net_vente)}")
        print(f"  Apport total : {_eur(apport)}")
        print(f"  Capital du nouveau prêt (max) : {_eur(d['capital_max'])}")
        print(f"  Prix d'achat maximal : {_eur(pm)}")
        if args.quotite_relais > 0:
            relais_s = max(args.valeur_vente * args.quotite_relais - args.crd_a_solder, 0.0)
            a_rembourser = relais_s + args.crd_a_solder + args.ira_vente + args.frais_vente
            if vente < a_rembourser:
                print(f"  Alerte : la vente ne couvre pas relais + CRD + frais ; besoin de trésorerie de "
                      f"{_eur(a_rembourser - vente)}")

    if args.quotite_relais > 0:
        relais = max(args.valeur_vente * args.quotite_relais - args.crd_a_solder, 0.0)
        interets_relais = relais * args.taux_relais / 100.0 / 12.0
        charge_portage = (args.charges_credit + args.mensualite_actuelle + d["mensualite_credit"]
                          + d["mensualite_assurance"] + interets_relais)
        revenus_retenus = d["revenus_retenus"]
        print(f"\nPrêt relais : {_eur(relais)} ({args.quotite_relais:.0%} de la valeur moins le CRD), "
              f"intérêts {_eur(interets_relais)}/mois")
        if relais == 0:
            print("Relais nul : le CRD dépasse la part de la valeur avancée par la banque. Acheter avant de "
                  "vendre demande alors un montage achat-revente (rachat du prêt en cours par le nouveau "
                  "financement) ou une épargne suffisante : à étudier avec la banque.")
        print(f"Charge de trésorerie pendant le portage (ancien prêt + nouveau + intérêts du relais) : "
              f"{_eur(charge_portage)}, soit {charge_portage / revenus_retenus * 100:.1f} % des revenus retenus. "
              f"Ce n'est pas le taux d'effort HCSF.")
        if relais > args.valeur_vente * 0.80:
            print("Relais supérieur à 80 % de la valeur du bien vendu : ses intérêts ne peuvent pas être exclus du taux d'effort.")
        print("Depuis décembre 2023 (HCSF, probable), les intérêts d'un relais adossé d'au plus 80 % de la valeur "
              "du bien vendu peuvent être exclus du taux d'effort. À confirmer avec la banque.")
        for mois in (6, 12, 24):
            print(f"  Coût du portage sur {mois} mois (intérêts relais + ancienne mensualité) : "
                  f"{_eur((interets_relais + args.mensualite_actuelle) * mois)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
