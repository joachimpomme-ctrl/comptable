#!/usr/bin/env python3
"""Taux de rendement interne de flux datés (XIRR, base 365 jours) et rendement annualisé.

Convention de signe : argent sorti de la poche de l'investisseur (versement) en
négatif, argent reçu ou valeur de rachat finale en positif.

Exemples :
  python3 tri.py xirr --flux "2021-01-15:-10000;2022-03-01:-5000,50;2026-11-01:19500"
  python3 tri.py xirr --csv flux.csv          # colonnes date;montant, date AAAA-MM-JJ
  python3 tri.py annualise --initial 10000 --final 16000 --annees 6.5

Dans --flux, séparer les flux par des points-virgules : les montants acceptent
alors la virgule décimale. L'ancienne forme séparée par des virgules reste lue,
sans décimales à la française.
"""

import argparse
import csv
import datetime as dt
import re
import sys

BAS, HAUT = -0.9999, 10.0  # TRI cherché entre -99,99 % et +1 000 % par an


def _parse_date(s):
    try:
        return dt.date.fromisoformat(s.strip())
    except ValueError:
        raise ValueError(f"date illisible « {s.strip()} » : format attendu AAAA-MM-JJ")


def xnpv(taux, flux):
    d0 = flux[0][0]
    return sum(m / (1 + taux) ** ((d - d0).days / 365.0) for d, m in flux)


def xirr(flux, bas=BAS, haut=HAUT, tol=1e-10, max_iter=500):
    """flux : liste de (date, montant). Bissection robuste sur [bas, haut]."""
    flux = sorted(flux, key=lambda x: x[0])
    if not any(m < 0 for _, m in flux) or not any(m > 0 for _, m in flux):
        raise ValueError("il faut au moins un flux négatif (versement) et un flux positif (retrait ou valeur finale)")
    if flux[0][0] == flux[-1][0]:
        raise ValueError("tous les flux sont à la même date : un taux annuel n'a pas de sens")
    f_bas, f_haut = xnpv(bas, flux), xnpv(haut, flux)
    if f_bas * f_haut > 0:
        raise ValueError("TRI hors de l'intervalle -99,99 % à +1 000 % par an : durée très courte (quelques "
                         "jours) ou flux incohérents. Vérifier les dates et les signes ; sur une durée courte, "
                         "donner plutôt le gain en euros et en % non annualisé.")
    for _ in range(max_iter):
        mil = (bas + haut) / 2
        f_mil = xnpv(mil, flux)
        if abs(f_mil) < tol or (haut - bas) / 2 < tol:
            return mil
        if f_bas * f_mil < 0:
            haut, f_haut = mil, f_mil
        else:
            bas, f_bas = mil, f_mil
    return (bas + haut) / 2


def annualise(initial, final, annees):
    if initial <= 0:
        raise ValueError("la valeur initiale doit être strictement positive")
    if final < 0:
        raise ValueError("la valeur finale doit être positive ou nulle")
    if annees <= 0:
        raise ValueError("la durée doit être strictement positive")
    return (final / initial) ** (1 / annees) - 1


def _montant(txt):
    """Lit un montant au format français ou anglais (espaces insécables, 1.234,56 ou 1,234.56).
    Refuse les écritures ambiguës comme 1.234 ou 1,234 (milliers ou décimale ?)."""
    t = txt.strip().replace("\u00a0", "").replace("\u202f", "").replace(" ", "").replace("€", "")
    if not t:
        raise ValueError("montant vide")
    if re.fullmatch(r"-?[1-9]\d{0,2}([.,]\d{3})+", t):
        raise ValueError(f"montant ambigu « {txt.strip()} » (milliers ou décimale ?) : écrire 1234 ou 1234,00")
    if "," in t and "." in t:
        if t.rfind(",") > t.rfind("."):
            t = t.replace(".", "").replace(",", ".")
        else:
            t = t.replace(",", "")
    else:
        t = t.replace(",", ".")
    return float(t)


def _eur(x):
    return f"{x:,.2f} €".replace(",", " ").replace(".", ",")


def _lire_flux(args):
    flux = []
    if args.flux:
        sep = ";" if ";" in args.flux else ","
        for item in args.flux.split(sep):
            if not item.strip():
                continue
            if ":" not in item:
                raise ValueError(f"flux illisible « {item.strip()} » : format attendu AAAA-MM-JJ:montant")
            d, m = item.rsplit(":", 1)
            flux.append((_parse_date(d), _montant(m) if sep == ";" else float(m)))
    if args.csv:
        with open(args.csv, encoding="utf-8-sig") as f:
            lecteur = csv.reader(f, delimiter=";")
            for ligne in lecteur:
                if not ligne or ligne[0].lower().startswith("date"):
                    continue
                flux.append((_parse_date(ligne[0]), _montant(ligne[1])))
    return flux


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("xirr")
    a.add_argument("--flux")
    a.add_argument("--csv")
    a = sp.add_parser("annualise")
    a.add_argument("--initial", type=float, required=True)
    a.add_argument("--final", type=float, required=True)
    a.add_argument("--annees", type=float, required=True)
    args = p.parse_args(argv)

    if args.cmd == "xirr":
        if not args.flux and not args.csv:
            p.error("donner --flux ou --csv")
        try:
            flux = _lire_flux(args)
            t = xirr(flux)
        except (ValueError, OSError) as e:
            p.error(str(e))
        verse = -sum(m for _, m in flux if m < 0)
        recu = sum(m for _, m in flux if m > 0)
        print(f"{len(flux)} flux du {min(d for d, _ in flux)} au {max(d for d, _ in flux)}")
        print(f"Versé : {_eur(verse)} ; reçu ou valeur finale : {_eur(recu)} ; gain : {_eur(recu - verse)}")
        print(f"TRI annuel : {t * 100:.2f} %".replace(".", ","))
    else:
        try:
            r = annualise(args.initial, args.final, args.annees)
        except ValueError as e:
            p.error(str(e))
        print(f"Rendement annualisé : {r * 100:.2f} %".replace(".", ","))
    return 0


if __name__ == "__main__":
    sys.exit(main())
