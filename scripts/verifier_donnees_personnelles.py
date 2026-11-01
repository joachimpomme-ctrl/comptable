#!/usr/bin/env python3
"""Contrôle de sécurité : aucune donnée personnelle ni secret dans le dépôt.

Vérifie :
1. les fichiers suivis par git (hors archives binaires) : adresses e-mail,
   identifiants de type Google Drive, IBAN, numéros de carte, numéros de
   téléphone français, clés d'API et jetons courants ;
2. les auteurs et committers de tout l'historique : seules les adresses
   anonymes (noreply) sont admises.

Usage : python3 scripts/verifier_donnees_personnelles.py
Code retour 1 si un problème est trouvé. Lancé par la CI à chaque push.
Ne jamais ajouter ici une liste de noms ou d'adresses réelles : elle serait publiée.
"""

import re
import subprocess
import sys

EMAILS_ADMIS = re.compile(
    r"^(noreply@anthropic\.com|noreply@github\.com|[0-9]+\+[A-Za-z0-9-]+@users\.noreply\.github\.com"
    r"|[A-Za-z0-9._-]+@(example\.(com|org|fr)|exemple\.fr))$",
    re.I,
)
EXTENSIONS_IGNOREES = (".zip", ".skill", ".png", ".jpg", ".jpeg", ".pdf", ".ico")
CE_FICHIER = "scripts/verifier_donnees_personnelles.py"

MOTIFS = {
    "adresse e-mail": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "identifiant Google Drive": re.compile(r"\b[0-9A-Za-z_-]{28,44}\b"),
    "IBAN": re.compile(r"\bFR\d{2}[ ]?(?:\d{4}[ ]?){5}\d{3}\b"),
    "numéro de carte": re.compile(r"\b(?:\d{4}[ -]?){3}\d{4}\b"),
    "téléphone français": re.compile(r"(?<![\d.,])(?:\+33[ .]?|0)[67](?:[ .]?\d{2}){4}(?![\d.,])"),
    "clé d'API ou jeton": re.compile(
        r"\b(?:sk-[A-Za-z0-9_-]{20,}|sk-ant-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}"
        r"|AIza[0-9A-Za-z_-]{35}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,})\b"
    ),
}


def ressemble_a_un_id_drive(s):
    """Un identifiant Drive mélange majuscules, minuscules et chiffres, sans mot lisible."""
    if s.startswith(("sha256", "LEGIARTI", "JORFTEXT", "JORFARTI")) or s.count("-") > 2 or s.count("_") > 2:
        return False
    if re.search(r"[A-Za-z]{6,}", s) and re.search(r"[a-z]{6,}", s):
        return False  # contient un mot lisible : nom de fichier ou identifiant de règle
    return bool(re.search(r"[A-Z]", s) and re.search(r"[a-z]", s) and re.search(r"\d", s)) and not re.fullmatch(
        r"[0-9a-f]{28,44}", s
    )


def luhn(num):
    chiffres = [int(c) for c in re.sub(r"\D", "", num)][::-1]
    total = sum(c if i % 2 == 0 else (c * 2 - 9 if c * 2 > 9 else c * 2) for i, c in enumerate(chiffres))
    return total % 10 == 0


def fichiers_suivis():
    sortie = subprocess.run(["git", "ls-files", "-z"], capture_output=True, check=True).stdout
    return [f for f in sortie.decode("utf-8").split("\0") if f and not f.endswith(EXTENSIONS_IGNOREES) and f != CE_FICHIER]


def controler_fichiers():
    problemes = []
    for chemin in fichiers_suivis():
        try:
            texte = open(chemin, encoding="utf-8").read()
        except (UnicodeDecodeError, FileNotFoundError):
            continue
        for num, ligne in enumerate(texte.splitlines(), start=1):
            for nom, motif in MOTIFS.items():
                for m in motif.finditer(ligne):
                    v = m.group(0)
                    if nom == "adresse e-mail" and EMAILS_ADMIS.match(v):
                        continue
                    if nom == "identifiant Google Drive" and not ressemble_a_un_id_drive(v):
                        continue
                    if nom == "numéro de carte" and not luhn(v):
                        continue
                    problemes.append(f"{chemin}:{num} : {nom} ({v[:6]}...)")
    return problemes


def controler_historique():
    sortie = subprocess.run(["git", "log", "--all", "--format=%ae%n%ce"], capture_output=True, text=True, check=True).stdout
    adresses = {a.strip() for a in sortie.splitlines() if a.strip()}
    return [f"historique git : adresse non anonyme ({a.split('@')[0][:3]}...@{a.split('@')[-1]})"
            for a in sorted(adresses) if not EMAILS_ADMIS.match(a)]


def main():
    problemes = controler_fichiers() + controler_historique()
    if problemes:
        print("Données personnelles ou secrets possibles :")
        for p in problemes:
            print("  - " + p)
        print("Corriger avant de fusionner. Pour l'historique : adresse noreply GitHub (voir SECURITY.md).")
        return 1
    print("OK : aucune donnée personnelle ni secret détecté (fichiers suivis et auteurs de l'historique).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
