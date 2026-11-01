#!/usr/bin/env python3
"""Contrôles de cohérence du corpus, lancés par la CI à chaque push.

1. Chaque renvoi « [referentiel: cle] » ou « [referentiel: cle/AAAA] » du corpus,
   des skills et des instructions vise une clé qui existe (et un millésime présent).
2. Les comptes du manifeste correspondent aux fichiers (règles, articles CGI,
   clés du référentiel, questions de test).
3. Aucun paramètre du référentiel n'a dépassé sa date « valable_jusqu_au ».
   Ce contrôle échoue volontairement après la date : il signale la mise à jour
   annuelle à faire (voir ROADMAP, section 4). Pour un correctif urgent sans la
   mise à jour annuelle : IGNORER_VALIDITE=1 python3 scripts/verifier_corpus.py

Usage : python3 scripts/verifier_corpus.py ; code retour 1 en cas de problème.
"""
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
K = RACINE / "knowledge"
RENVOI = re.compile(r"\[referentiel: ([^\]]+)\]")
FICHIERS_RENVOIS = sorted(
    [p for p in K.glob("*.md")]
    + list((RACINE / ".claude" / "skills").glob("*/SKILL.md"))
    + list((RACINE / ".claude" / "skills").glob("*/references/*.md"))
    + [RACINE / "gemini" / "00_INSTRUCTIONS_GEMINI.md", RACINE / "chatgpt" / "00_INSTRUCTIONS_CHATGPT.md"]
)


def controler_renvois(params):
    problemes = []
    for f in FICHIERS_RENVOIS:
        if not f.exists():
            continue
        for num, ligne in enumerate(f.read_text(encoding="utf-8").splitlines(), start=1):
            for m in RENVOI.finditer(ligne):
                for morceau in m.group(1).split(","):
                    for ref in morceau.split(" / "):
                        ref = ref.strip()
                        cle, _, annee = ref.partition("/")
                        cle = cle.strip()
                        if cle.endswith("*") or cle.startswith("_"):
                            continue  # familles de clés (bareme_ir_seuil_tranche_*) ou suffixes abrégés
                        if cle not in params:
                            problemes.append(f"{f.relative_to(RACINE)}:{num} : clé inconnue « {cle} »")
                        elif annee and annee.strip().isdigit() and annee.strip() not in params[cle]["valeurs"]:
                            problemes.append(f"{f.relative_to(RACINE)}:{num} : millésime {annee} absent pour « {cle} »")
    return problemes


def controler_comptes(params):
    man = json.loads((K / "09_agent_manifest.json").read_text(encoding="utf-8"))
    stats = man.get("statistics", {})
    regles = len(re.findall(r"^### ", (K / "02_golden_rules_claude_first.md").read_text(encoding="utf-8"), re.M))
    articles = len(re.findall(r"^## Article ", (K / "M_CGI_code_general_impots.md").read_text(encoding="utf-8"), re.M))
    tests = len(re.findall(r"^## ", (K / "08_evaluation_suite.md").read_text(encoding="utf-8"), re.M))
    reels = {"golden_rules": regles, "cgi_articles": articles, "referentiel_parametres_keys": len(params)}
    problemes = [f"manifeste : {k} = {stats.get(k)} mais {v} dans les fichiers" for k, v in reels.items() if stats.get(k) != v]
    if stats.get("evaluation_test_cases") is not None and tests < stats["evaluation_test_cases"]:
        problemes.append(f"manifeste : {stats['evaluation_test_cases']} cas de test annoncés, {tests} sections trouvées")
    return problemes


def controler_validite(params):
    if os.environ.get("IGNORER_VALIDITE") == "1":
        return []
    aujourd_hui = dt.date.today()
    return [f"référentiel : « {k} » valable jusqu'au {v['valable_jusqu_au']}, à revérifier (mise à jour annuelle)"
            for k, v in params.items()
            if v.get("valable_jusqu_au") and dt.date.fromisoformat(v["valable_jusqu_au"]) < aujourd_hui]


def main():
    params = json.loads((K / "referentiel_parametres.json").read_text(encoding="utf-8"))["parametres"]
    problemes = controler_renvois(params) + controler_comptes(params) + controler_validite(params)
    if problemes:
        print("Problèmes de cohérence du corpus :")
        for p in problemes:
            print("  - " + p)
        return 1
    print(f"OK : renvois au référentiel, comptes du manifeste et validité des {len(params)} paramètres.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
