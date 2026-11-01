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

La cible s'écrit en fractions qui somment à 1 (0.80, pas 80). Un même fonds
détenu dans deux enveloppes (PEA et compte-titres, par exemple) peut figurer
sur deux lignes de même nom : les lignes sont regroupées pour les poids, le
versement et les arbitrages, qui sont donnés par fonds. Choisir ensuite
l'enveloppe où acheter ou vendre : la fiscalité n'y est pas la même.

Exemples :
  python3 allocation.py portefeuille.json            # état, écarts, versement sans vente
  python3 allocation.py portefeuille.json --arbitrage # ventes et achats pour revenir à la cible
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from entrees import montant  # noqa: E402

TOLERANCE_CIBLE = 0.02  # au-delà, la cible est refusée ; en deçà, normalisée avec un avertissement


class EntreeInvalide(ValueError):
    """Fichier d'entrée incohérent ; le message dit quoi corriger."""


def regrouper(positions):
    """Valeur par nom de position, lignes de même nom additionnées (même fonds dans deux enveloppes)."""
    valeurs = {}
    for p in positions:
        valeurs[p["nom"]] = valeurs.get(p["nom"], 0.0) + p["valeur"]
    return valeurs


def doublons(positions):
    """Noms présents sur plusieurs lignes, avec leur nombre de lignes."""
    compte = {}
    for p in positions:
        compte[p["nom"]] = compte.get(p["nom"], 0) + 1
    return {n: k for n, k in compte.items() if k > 1}


def _est_nombre(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def verifier(positions, cible):
    """Lève EntreeInvalide si une saisie est mal formée, si une valeur est négative ou si la cible n'est
    pas en fractions sommant à 1 (à 0,02 près). Renvoie la cible, normalisée si sa somme s'écarte un peu de 1."""
    if not isinstance(positions, list):
        raise EntreeInvalide("« positions » doit être une liste")
    for p in positions:
        if not isinstance(p, dict) or "nom" not in p or "valeur" not in p:
            raise EntreeInvalide("chaque position doit avoir un « nom » et une « valeur »")
        if not _est_nombre(p["valeur"]) or p["valeur"] < 0:
            raise EntreeInvalide(f"valeur invalide pour {p['nom']} : un montant positif ou nul est attendu")
        vent = p.get("ventilation")
        if vent is not None and (not isinstance(vent, dict) or not all(_est_nombre(w) and w >= 0 for w in vent.values())):
            raise EntreeInvalide(f"ventilation de {p['nom']} : un objet zone -> poids positif est attendu")
    if not cible:
        return cible
    if not isinstance(cible, dict):
        raise EntreeInvalide("« cible » doit être un objet nom -> fraction")
    for n, c in cible.items():
        if not _est_nombre(c) or c < 0:
            raise EntreeInvalide(f"cible invalide pour {n} : une fraction entre 0 et 1 est attendue")
        if c > 1:
            raise EntreeInvalide(f"cible de {n} à {c} : la cible s'écrit en fractions (0.8 pour 80 %), "
                                 f"pas en pourcentages")
    somme = sum(cible.values())
    if abs(somme - 1) > TOLERANCE_CIBLE:
        raise EntreeInvalide(f"la cible somme à {somme:.4f} : elle doit sommer à 1 (fractions)")
    if abs(somme - 1) > 1e-9:
        print(f"Attention : la cible somme à {somme:.4f} ; elle est ramenée à 1 en gardant ses proportions.")
        return {n: c / somme for n, c in cible.items()}
    return cible


def poids(positions):
    valeurs = regrouper(positions)
    total = sum(valeurs.values())
    return {n: (v / total if total else 0.0) for n, v in valeurs.items()}, total


def transparence(positions):
    """Exposition par zone, en euros et en part du total."""
    total = sum(p["valeur"] for p in positions)
    zones = {}
    for p in positions:
        vent = p.get("ventilation") or {p["nom"]: 1.0}
        somme = sum(vent.values())
        if somme <= 0:
            raise EntreeInvalide(f"ventilation de {p['nom']} vide ou nulle : renseigner des poids positifs")
        if abs(somme - 1) > 0.02:
            print(f"Attention : ventilation de {p['nom']} somme à {somme:.3f}, normalisée à 1.")
        for z, w in vent.items():
            zones[z] = zones.get(z, 0.0) + p["valeur"] * w / somme
    return {z: (v, v / total if total else 0.0) for z, v in sorted(zones.items(), key=lambda x: -x[1])}


def repartir_versement(positions, cible, versement):
    """Répartit le versement pour réduire l'écart à la cible sans rien vendre.
    Remplit d'abord les déficits ; s'il reste de l'argent, le répartit selon la cible."""
    valeurs = regrouper(positions)
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
    valeurs = regrouper(positions)
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
    p.add_argument("--versement", type=montant, default=None, help="remplace le versement du fichier")
    args = p.parse_args(argv)

    try:
        with open(args.fichier, encoding="utf-8-sig") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        p.error(f"lecture de {args.fichier} impossible : {e}")
    if not isinstance(data, dict):
        p.error("le fichier doit contenir un objet avec « positions », « cible » et « versement »")
    positions = data.get("positions") or []
    cible = data.get("cible") or {}
    versement = args.versement if args.versement is not None else data.get("versement", 0.0)
    if not positions:
        p.error("aucune position dans le fichier")
    if not _est_nombre(versement) or versement < 0:
        p.error("versement invalide : un montant positif ou nul est attendu (pour un retrait, utiliser --arbitrage)")
    try:
        cible = verifier(positions, cible)
        zones = transparence(positions)
    except EntreeInvalide as e:
        p.error(str(e))

    w, total = poids(positions)
    valeurs = regrouper(positions)
    print(f"Total : {_eur(total)}")
    multi = doublons(positions)
    if multi:
        print("Lignes de même nom regroupées : " + ", ".join(f"{n} ({k} lignes)" for n, k in multi.items())
              + ". Versement et arbitrages sont donnés par fonds : choisir ensuite l'enveloppe.")
    print("\nPar position : valeur, poids, cible, écart (points)")
    sources = {}
    for pos in positions:
        if pos.get("ventilation"):
            sources.setdefault(pos["nom"], f" [source : {pos.get('source', 'non renseignée')}, "
                                           f"{pos.get('date', 'non datée')}]")
    for n, v in valeurs.items():
        c = cible.get(n)
        src = sources.get(n, "")
        if c is not None:
            print(f"  {n} : {_eur(v)}, {_pct(w[n])}, cible {_pct(c)}, écart {(w[n] - c) * 100:+.1f}{src}")
        else:
            print(f"  {n} : {_eur(v)}, {_pct(w[n])}, hors cible{src}")

    print("\nExposition par zone (transparence)")
    for z, (v, part) in zones.items():
        print(f"  {z} : {_eur(v)}, {_pct(part)}")

    if cible and versement:
        rep = repartir_versement(positions, cible, versement)
        print(f"\nRépartition d'un versement de {_eur(versement)} sans vente :")
        for n, m in rep.items():
            print(f"  {n} : {_eur(m)}")
        apres = [{"nom": n, "valeur": v + rep.get(n, 0.0)} for n, v in valeurs.items()]
        apres += [{"nom": n, "valeur": m} for n, m in rep.items() if n not in valeurs]
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
