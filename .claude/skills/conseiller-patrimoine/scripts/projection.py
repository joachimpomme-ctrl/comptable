#!/usr/bin/env python3
"""Projections d'épargne et de retraite.

Aucun rendement, volatilité ou inflation par défaut : chaque hypothèse est
fournie par l'appelant, sourcée (references/00-sources.md section 8), et dite
nominale ou réelle. En rendement réel, les résultats sont en euros d'aujourd'hui.

Exemples :
  python projection.py epargne --capital 20000 --versement 1500 --annees 15 \
      --rendements 1,3,5 [--indexation 2] [--inflation 2]
  python projection.py montecarlo --capital 20000 --versement 1500 --annees 15 \
      --rendement-moyen 5 --volatilite 15 --objectif 400000 [--simulations 20000 --graine 1]
  python projection.py retraite --revenu-cible 5500 --pensions 3800 --autres-revenus 0 \
      --taux-retrait 3,3.5,4
  python projection.py retrait-mc --capital 600000 --retrait-annuel 21000 --annees 30 \
      --rendement-moyen 3 --volatilite 12 [--simulations 20000 --graine 1]
"""

import argparse
import math
import random
import sys


def valeur_future(capital, versement_mensuel, annees, rendement_annuel_pct, indexation_pct=0.0):
    """Capital + versements mensuels de fin de mois, rendement annuel composé
    mensuellement de façon équivalente, versements indexés une fois par an."""
    rm = (1 + rendement_annuel_pct / 100.0) ** (1 / 12.0) - 1
    v = capital
    vers = versement_mensuel
    for mois in range(1, int(round(annees * 12)) + 1):
        v = v * (1 + rm) + vers
        if mois % 12 == 0:
            vers *= 1 + indexation_pct / 100.0
    return v


def _params_lognormaux(moyenne_pct, vol_pct):
    """Paramètres mensuels d'un rendement lognormal dont la moyenne arithmétique
    annuelle et l'écart-type annuel sont donnés."""
    m = moyenne_pct / 100.0
    s = vol_pct / 100.0
    var_log = math.log(1 + (s * s) / ((1 + m) ** 2))
    mu_log = math.log(1 + m) - var_log / 2
    return mu_log / 12.0, math.sqrt(var_log / 12.0)


def _quantile(valeurs_triees, q):
    if not valeurs_triees:
        return float("nan")
    pos = q * (len(valeurs_triees) - 1)
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return valeurs_triees[lo]
    return valeurs_triees[lo] + (valeurs_triees[hi] - valeurs_triees[lo]) * (pos - lo)


def montecarlo(capital, versement, annees, moyenne_pct, vol_pct, simulations=10000, graine=None,
               indexation_pct=0.0):
    rnd = random.Random(graine)
    mu, sig = _params_lognormaux(moyenne_pct, vol_pct)
    n = int(round(annees * 12))
    finaux = []
    for _ in range(simulations):
        v = capital
        vers = versement
        for mois in range(1, n + 1):
            v = v * math.exp(rnd.gauss(mu, sig)) + vers
            if mois % 12 == 0:
                vers *= 1 + indexation_pct / 100.0
        finaux.append(v)
    finaux.sort()
    return finaux


def retrait_mc(capital, retrait_annuel, annees, moyenne_pct, vol_pct, simulations=10000, graine=None):
    """Probabilité que le capital tienne `annees` avec un retrait mensuel constant
    (en euros constants si les rendements saisis sont réels)."""
    rnd = random.Random(graine)
    mu, sig = _params_lognormaux(moyenne_pct, vol_pct)
    n = int(round(annees * 12))
    retrait = retrait_annuel / 12.0
    tenus = 0
    restes = []
    for _ in range(simulations):
        v = capital
        ok = True
        for _m in range(n):
            v -= retrait
            if v <= 0:
                ok = False
                v = 0.0
                break
            v *= math.exp(rnd.gauss(mu, sig))
        if ok:
            tenus += 1
        restes.append(v)
    restes.sort()
    return tenus / simulations, restes


def _eur(x):
    return f"{x:,.0f} €".replace(",", " ")


def _liste(txt):
    return [float(x) for x in txt.split(",") if x.strip()]


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)

    a = sp.add_parser("epargne")
    a.add_argument("--capital", type=float, default=0.0)
    a.add_argument("--versement", type=float, default=0.0, help="versement mensuel")
    a.add_argument("--annees", type=float, required=True)
    a.add_argument("--rendements", required=True, help="liste de rendements annuels en %%, ex. 1,3,5")
    a.add_argument("--indexation", type=float, default=0.0, help="hausse annuelle des versements, en %%")
    a.add_argument("--inflation", type=float, default=None,
                   help="si les rendements sont nominaux : inflation pour convertir en euros d'aujourd'hui")

    a = sp.add_parser("montecarlo")
    a.add_argument("--capital", type=float, default=0.0)
    a.add_argument("--versement", type=float, default=0.0)
    a.add_argument("--annees", type=float, required=True)
    a.add_argument("--rendement-moyen", type=float, required=True, help="moyenne arithmétique annuelle, en %%")
    a.add_argument("--volatilite", type=float, required=True, help="écart-type annuel, en %%")
    a.add_argument("--indexation", type=float, default=0.0)
    a.add_argument("--objectif", type=float, default=None)
    a.add_argument("--simulations", type=int, default=10000)
    a.add_argument("--graine", type=int, default=None)

    a = sp.add_parser("retraite")
    a.add_argument("--revenu-cible", type=float, required=True, help="mensuel, euros d'aujourd'hui")
    a.add_argument("--pensions", type=float, required=True, help="mensuelles nettes estimées, euros d'aujourd'hui")
    a.add_argument("--autres-revenus", type=float, default=0.0)
    a.add_argument("--taux-retrait", required=True, help="liste en %%, ex. 3,3.5,4")
    a.add_argument("--taux-prelevement-retraits", type=float, default=0.0,
                   help="impôt et prélèvements sociaux moyens sur les retraits, en %% (via assistant-fiscal-comptable)")

    a = sp.add_parser("retrait-mc")
    a.add_argument("--capital", type=float, required=True)
    a.add_argument("--retrait-annuel", type=float, required=True)
    a.add_argument("--annees", type=float, required=True)
    a.add_argument("--rendement-moyen", type=float, required=True, help="réel de préférence, en %%")
    a.add_argument("--volatilite", type=float, required=True)
    a.add_argument("--simulations", type=int, default=10000)
    a.add_argument("--graine", type=int, default=None)

    args = p.parse_args(argv)

    if args.cmd == "epargne":
        print(f"Hypothèses : capital {_eur(args.capital)}, versement {_eur(args.versement)}/mois "
              f"indexé de {args.indexation} %/an, {args.annees} ans")
        for r in _liste(args.rendements):
            v = valeur_future(args.capital, args.versement, args.annees, r, args.indexation)
            ligne = f"Rendement {r} %/an : {_eur(v)}"
            if args.inflation is not None:
                ligne += f" ; en euros d'aujourd'hui (inflation {args.inflation} %) : {_eur(v / (1 + args.inflation / 100) ** args.annees)}"
            print(ligne)
        verse = valeur_future(args.capital, args.versement, args.annees, 0.0, args.indexation)
        print(f"Total versé, capital initial compris : {_eur(verse)}")
    elif args.cmd == "montecarlo":
        f = montecarlo(args.capital, args.versement, args.annees, args.rendement_moyen,
                       args.volatilite, args.simulations, args.graine, args.indexation)
        print(f"Hypothèses : rendement moyen {args.rendement_moyen} %/an, volatilité {args.volatilite} %, "
              f"{args.simulations} simulations, rendements indépendants (lognormaux)")
        for q in (0.05, 0.25, 0.5, 0.75, 0.95):
            print(f"Percentile {int(q * 100)} : {_eur(_quantile(f, q))}")
        if args.objectif is not None:
            proba = sum(1 for x in f if x >= args.objectif) / len(f)
            print(f"Probabilité d'atteindre {_eur(args.objectif)} : {proba:.0%}")
        print("Limite : modèle sans krach groupé ni retour à la moyenne ; ne remplace pas un scénario défavorable chiffré.")
    elif args.cmd == "retraite":
        ecart = args.revenu_cible - args.pensions - args.autres_revenus
        print(f"Écart mensuel à combler : {_eur(ecart)} (euros d'aujourd'hui)")
        if ecart <= 0:
            print("Pas d'écart : les revenus estimés couvrent la cible.")
            return 0
        brut = ecart / (1 - args.taux_prelevement_retraits / 100.0)
        if args.taux_prelevement_retraits:
            print(f"Retrait brut nécessaire pour {_eur(ecart)} nets : {_eur(brut)} par mois "
                  f"(prélèvements {args.taux_prelevement_retraits} %)")
        else:
            print("Attention : aucun impôt ni prélèvement sur les retraits n'est compté (--taux-prelevement-retraits).")
        for t in _liste(args.taux_retrait):
            print(f"Taux de retrait {t} % : capital nécessaire {_eur(brut * 12 / (t / 100))}")
        print("Hypothèse réglementaire : pensions selon les règles vérifiées à la date du calcul.")
    elif args.cmd == "retrait-mc":
        proba, restes = retrait_mc(args.capital, args.retrait_annuel, args.annees, args.rendement_moyen,
                                   args.volatilite, args.simulations, args.graine)
        print(f"Hypothèses : capital {_eur(args.capital)}, retrait {_eur(args.retrait_annuel)}/an "
              f"({args.retrait_annuel / args.capital:.2%} du capital initial), {args.annees} ans, "
              f"rendement {args.rendement_moyen} %, volatilité {args.volatilite} %")
        print(f"Probabilité que le capital tienne : {proba:.0%}")
        print(f"Capital restant médian : {_eur(_quantile(restes, 0.5))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
