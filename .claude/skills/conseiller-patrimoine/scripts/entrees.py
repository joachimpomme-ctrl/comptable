#!/usr/bin/env python3
"""Contrôle des paramètres saisis en ligne de commande, commun aux scripts.

Chaque fonction sert de `type=` à argparse. Une saisie invalide produit un
message en français, sans trace Python : argparse affiche l'usage et le
message, puis sort avec le code 2.

Conventions des scripts : montants en euros, taux en % (3.5 pour 3,5 %),
parts et quotités en fraction (0.70 pour 70 %).
"""

import argparse
import math
import re

# 300,000 ou 1.234 : séparateur de milliers ou décimale ? Trop risqué pour deviner.
AMBIGU = re.compile(r"-?[1-9]\d{0,2}([.,]\d{3})+")


def nombre(txt):
    """Nombre fini ; accepte la virgule décimale et les espaces (1 234,5).
    Refuse les écritures ambiguës comme 300,000 ou 1.234."""
    brut = str(txt).strip().replace("\u00a0", "").replace("\u202f", "").replace(" ", "")
    if AMBIGU.fullmatch(brut):
        raise argparse.ArgumentTypeError(
            f"« {txt} » est ambigu (séparateur de milliers ou décimale ?) : écrire 300000, ou 300.5 pour une décimale")
    t = brut.replace(",", ".")
    try:
        x = float(t)
    except ValueError:
        raise argparse.ArgumentTypeError(f"« {txt} » n'est pas un nombre")
    if math.isnan(x) or math.isinf(x):
        raise argparse.ArgumentTypeError(f"« {txt} » n'est pas un nombre fini")
    return x


def montant(txt):
    """Montant positif ou nul."""
    x = nombre(txt)
    if x < 0:
        raise argparse.ArgumentTypeError(f"montant négatif ({txt}) : saisir une valeur positive ou nulle")
    return x


def montant_positif(txt):
    """Montant strictement positif."""
    x = nombre(txt)
    if x <= 0:
        raise argparse.ArgumentTypeError(f"montant nul ou négatif ({txt}) : saisir une valeur strictement positive")
    return x


def fraction(txt):
    """Part entre 0 et 1. Refuse 70 pour 0.70, l'erreur de saisie la plus fréquente."""
    x = nombre(txt)
    if 1 < x <= 100:
        raise argparse.ArgumentTypeError(
            f"{txt} ressemble à un pourcentage : ce paramètre attend une fraction entre 0 et 1 "
            f"(par exemple {x / 100:g} pour {x:g} %)")
    if not 0 <= x <= 1:
        raise argparse.ArgumentTypeError(f"{txt} : ce paramètre attend une fraction entre 0 et 1")
    return x


def pct_borne(bas, haut, libelle="taux"):
    """Pourcentage compris entre bas et haut inclus."""
    def _type(txt):
        x = nombre(txt)
        if not bas <= x <= haut:
            raise argparse.ArgumentTypeError(
                f"{libelle} de {txt} % hors de la plage admise ({bas:g} à {haut:g} %) : vérifier l'unité "
                f"(les taux se saisissent en %, 3.5 pour 3,5 %)")
        return x
    return _type


def rendement(txt):
    """Rendement ou variation annuelle en %, strictement supérieur à -100 %."""
    x = nombre(txt)
    if x <= -100:
        raise argparse.ArgumentTypeError(f"rendement de {txt} % : il doit être supérieur à -100 %")
    if x > 100:
        raise argparse.ArgumentTypeError(
            f"rendement de {txt} % par an : valeur hors de toute hypothèse raisonnable, vérifier l'unité (en %)")
    return x


def duree_annees(bas, haut):
    """Durée en années (décimales admises) comprise entre bas et haut."""
    def _type(txt):
        x = nombre(txt)
        if not bas <= x <= haut:
            raise argparse.ArgumentTypeError(f"durée de {txt} an(s) hors de la plage admise ({bas:.2g} à {haut:g} ans)")
        return x
    return _type


def entier_min(minimum):
    """Entier supérieur ou égal à minimum."""
    def _type(txt):
        try:
            x = int(str(txt).strip())
        except ValueError:
            raise argparse.ArgumentTypeError(f"« {txt} » n'est pas un nombre entier")
        if x < minimum:
            raise argparse.ArgumentTypeError(f"{txt} : il faut un entier supérieur ou égal à {minimum}")
        return x
    return _type


def liste(convertir):
    """Liste séparée par des points-virgules ou des virgules (1;3;5 ou 1,3,5), chaque élément contrôlé.
    Avec des virgules comme séparateur, saisir les décimales avec un point (3.5)."""
    def _type(txt):
        sep = ";" if ";" in txt else ","
        morceaux = [m for m in txt.split(sep) if m.strip()]
        if not morceaux:
            raise argparse.ArgumentTypeError("liste vide")
        return [convertir(m) for m in morceaux]
    return _type


# Plages usuelles, larges, qui arrêtent surtout les erreurs d'unité.
taux_pret = pct_borne(0, 20, "taux du prêt")
taux_assurance = pct_borne(0, 5, "taux d'assurance")
pct_frais = pct_borne(0, 30, "pourcentage de frais")
pct_0_100 = pct_borne(0, 100, "pourcentage")
