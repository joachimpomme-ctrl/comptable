#!/usr/bin/env python3
"""Exposition d'un portefeuille, écart à la cible, répartition d'un versement.

Entrée : un fichier JSON.

{
  "positions": [
    {"nom": "ETF MSCI World", "valeur": 40000,
     "ventilation": {"États-Unis": 0.72, "Europe": 0.16, "Japon": 0.05, "Autres développés": 0.07},
     "source": "fiche MSCI World", "date": "2026-10-31"},
    {"nom": "ETF MSCI Europe", "valeur": 3000, "ventilation": {"Europe": 1.0}},
    {"nom": "ETF MSCI EM", "valeur": 2000, "ventilation": {"Émergents": 1.0}}
  ],
  "cible": {"ETF MSCI World": 0.80, "ETF MSCI Europe": 0.10, "ETF MSCI EM": 0.10},
  "versement": 1500
}

Les poids de ventilation ci-dessus sont des exemples, pas des données : les
lire sur la fiche de l'indice ou de l'ETF, et renseigner source et date.

Exemples :
  python allocation.py portefeuille.json            # état, écarts, versement sans vente
  python allocation.py portefeuille.json --arbitrage # ventes et achats pour revenir à la cible
"""

import argparse
import json
import sys


def poids(positions):
    total = sum(p["valeur"] for p in positions)
    return {p["nom"]: (p["valeur"] / total if total else 0.0) for p in positions}, total


def transparence(positions):
    """Exposition par zone, en euros et en part du total."""
    total = sum(p["valeur"] for p in positions)
    zones = {}
    for p in positions:
        vent = p.get("ventilation") or {p["nom"]: 1.0}
        somme = sum(vent.values())
        if abs(somme - 1) > 0.02:
            print(f"Attention : ventilation de {p['nom']} somme à {somme:.3f}, normalisée à 1.")
        for z, w in vent.items():
            zones[z] = zones.get(z, 0.0) + p["valeur"] * w / somme
    return {z: (v, v / total if total else 0.0) for z, v in sorted(zones.items(), key=lambda x: -x[1])}


def repartir_versement(positions, cible, versement):
    """Répartit le versement pour réduire l'écart à la cible sans rien vendre.
    Remplit d'abord les déficits ; s'il reste de l'argent, le répartit selon la cible."""
    valeurs = {p["nom"]: p["valeur"] for p in positions}
    for nom in cible:
        valeurs.setdefault(nom, 0.0)
    total_apres = sum(valeurs.values()) + versement
    deficits = {n: max(cible[n] * total_apres - valeurs[n], 0.0) for n in cible}
    somme_def = sum(deficits.values())
    if somme_def <= 0:
        return {n: versement * cible[n] for n in cible}
    if somme_def >= versement:
        return {n: versement * d / somme_def for n, d in deficits.items()}
    reste = versement - somme_def
    return {n: deficits[n] + reste * cible[n] for n in cible}


def arbitrages(positions, cible):
    valeurs = {p["nom"]: p["valeur"] for p in positions}
    for nom in cible:
        valeurs.setdefault(nom, 0.0)
    total = sum(valeurs.values())
    return {n: cible.get(n, 0.0) * total - valeurs[n] for n in valeurs}


def _eur(x):
    return f"{x:,.0f} €".replace(",", " ")


def _pct(x):
    return f"{x * 100:.1f} %".replace(".", ",")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("fichier")
    p.add_argument("--arbitrage", action="store_true")
    p.add_argument("--versement", type=float, default=None, help="remplace le versement du fichier")
    args = p.parse_args(argv)

    with open(args.fichier, encoding="utf-8") as f:
        data = json.load(f)
    positions = data["positions"]
    cible = data.get("cible", {})
    versement = args.versement if args.versement is not None else data.get("versement", 0.0)

    if cible and abs(sum(cible.values()) - 1) > 1e-6:
        print(f"Attention : la cible somme à {sum(cible.values()):.4f}, pas à 1.")

    w, total = poids(positions)
    print(f"Total : {_eur(total)}")
    print("\nPar position : valeur, poids, cible, écart (points)")
    for pos in positions:
        n = pos["nom"]
        c = cible.get(n)
        ecart = f"{(w[n] - c) * 100:+.1f}" if c is not None else "n/a"
        src = f" [source : {pos.get('source', 'non renseignée')}, {pos.get('date', 'non datée')}]" if pos.get("ventilation") else ""
        print(f"  {n} : {_eur(pos['valeur'])}, {_pct(w[n])}, cible {_pct(c)}, écart {ecart}{src}" if c is not None
              else f"  {n} : {_eur(pos['valeur'])}, {_pct(w[n])}, hors cible{src}")

    print("\nExposition par zone (transparence)")
    for z, (v, part) in transparence(positions).items():
        print(f"  {z} : {_eur(v)}, {_pct(part)}")

    if cible and versement:
        rep = repartir_versement(positions, cible, versement)
        print(f"\nRépartition d'un versement de {_eur(versement)} sans vente :")
        for n, m in rep.items():
            print(f"  {n} : {_eur(m)}")
        apres = [dict(p, valeur=p["valeur"] + rep.get(p["nom"], 0.0)) for p in positions]
        noms = {p["nom"] for p in positions}
        apres += [{"nom": n, "valeur": m} for n, m in rep.items() if n not in noms]
        w2, _ = poids(apres)
        print("  Poids après versement : " + ", ".join(f"{n} {_pct(w2[n])}" for n in w2))

    if cible and args.arbitrage:
        print("\nArbitrages pour revenir exactement à la cible (positif = acheter) :")
        for n, m in arbitrages(positions, cible).items():
            print(f"  {n} : {_eur(m)}")
        print("  Dans un PEA ou une assurance-vie, pas d'impôt à l'arbitrage ; sur compte-titres, si.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
