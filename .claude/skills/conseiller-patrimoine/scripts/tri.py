#!/usr/bin/env python3
"""Taux de rendement interne de flux datés (XIRR, base 365 jours) et rendement annualisé.

Convention de signe : argent sorti de la poche de l'investisseur (versement) en
négatif, argent reçu ou valeur de rachat finale en positif.

Exemples :
  python tri.py xirr --flux "2021-01-15:-10000,2022-03-01:-5000,2026-11-01:19500"
  python tri.py xirr --csv flux.csv          # colonnes date;montant, date AAAA-MM-JJ
  python tri.py annualise --initial 10000 --final 16000 --annees 6.5
"""

import argparse
import csv
import datetime as dt
import sys


def _parse_date(s):
    return dt.date.fromisoformat(s.strip())


def xnpv(taux, flux):
    d0 = flux[0][0]
    return sum(m / (1 + taux) ** ((d - d0).days / 365.0) for d, m in flux)


def xirr(flux, bas=-0.9999, haut=10.0, tol=1e-10, max_iter=500):
    """flux : liste de (date, montant). Bissection robuste sur [bas, haut]."""
    flux = sorted(flux, key=lambda x: x[0])
    if not any(m < 0 for _, m in flux) or not any(m > 0 for _, m in flux):
        raise ValueError("il faut au moins un flux négatif et un flux positif")
    f_bas, f_haut = xnpv(bas, flux), xnpv(haut, flux)
    if f_bas * f_haut > 0:
        raise ValueError("pas de changement de signe : TRI introuvable dans l'intervalle")
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
    return (final / initial) ** (1 / annees) - 1


def _montant(txt):
    """Lit un montant au format français ou anglais (espaces insécables, 1.234,56 ou 1,234.56)."""
    t = txt.strip().replace("\u00a0", "").replace("\u202f", "").replace(" ", "").replace("€", "")
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
        for item in args.flux.split(","):
            d, m = item.rsplit(":", 1)
            flux.append((_parse_date(d), float(m)))
    if args.csv:
        with open(args.csv, encoding="utf-8") as f:
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
        flux = _lire_flux(args)
        t = xirr(flux)
        verse = -sum(m for _, m in flux if m < 0)
        recu = sum(m for _, m in flux if m > 0)
        print(f"{len(flux)} flux du {min(d for d, _ in flux)} au {max(d for d, _ in flux)}")
        print(f"Versé : {_eur(verse)} ; reçu ou valeur finale : {_eur(recu)} ; gain : {_eur(recu - verse)}")
        print(f"TRI annuel : {t * 100:.2f} %".replace(".", ","))
    else:
        print(f"Rendement annualisé : {annualise(args.initial, args.final, args.annees) * 100:.2f} %".replace(".", ","))
    return 0


if __name__ == "__main__":
    sys.exit(main())
