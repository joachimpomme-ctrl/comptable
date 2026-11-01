#!/usr/bin/env python3
"""Contrôles de cohérence du corpus, lancés par la CI à chaque push et pull request.

1. Chaque renvoi « [referentiel: cle] » ou « [referentiel: cle/AAAA] » du corpus,
   des skills et des instructions vise une clé qui existe (et un millésime présent).
2. Les comptes du manifeste correspondent aux fichiers (règles, articles CGI,
   clés du référentiel, questions de test).
3. Un montant écrit juste avant un renvoi (« 83 600 € [referentiel: seuil_micro_bnc/2026] »)
   est égal à la valeur de la clé pour ce millésime.
4. Le fichier de traçabilité et les règles d'or concordent : mêmes identifiants,
   même ancre, un verdict pour chaque ancre « sourced », plus aucun énoncé
   marqué « INVALIDÉ ».
5. Le rappel de première réponse (skill Claude, instructions Gemini et ChatGPT)
   annonce la version, le nombre de règles et de paramètres du manifeste ; les
   instructions courtes de ChatGPT tiennent dans le champ Instructions (8 000 caractères).
6. Aucun paramètre du référentiel n'a dépassé sa date « valable_jusqu_au ».
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
# Montant écrit juste avant un renvoi : « 3 844,80 € [referentiel: …] », « 18,6 % [referentiel: …] ».
# Les deux lookbehind empêchent de lire la fin d'un nombre (« 844,80 » dans « 3 844,80 »).
MONTANT_PUIS_RENVOI = re.compile(
    r"(?<![\d,.])(?<!\d[ \u00a0\u202f])(\d{1,3}(?:[ \u00a0\u202f]\d{3})+(?:,\d+)?|\d+(?:,\d+)?)"
    r"\s*(€|EUR|%)\s*\(?\s*`?\[referentiel: ([^\]]+)\]")
FICHIERS_RENVOIS = sorted(
    [p for p in K.glob("*.md")]
    + list((RACINE / ".claude" / "skills").glob("*/SKILL.md"))
    + list((RACINE / ".claude" / "skills").glob("*/references/*.md"))
    + [RACINE / "gemini" / "00_INSTRUCTIONS_GEMINI.md", RACINE / "chatgpt" / "00_INSTRUCTIONS_CHATGPT.md",
       RACINE / "chatgpt" / "00_INSTRUCTIONS_CHATGPT_COURT.md"]
)
FICHIERS_RAPPEL = [RACINE / ".claude" / "skills" / "assistant-fiscal-comptable" / "SKILL.md",
                   RACINE / "gemini" / "00_INSTRUCTIONS_GEMINI.md",
                   RACINE / "chatgpt" / "00_INSTRUCTIONS_CHATGPT.md",
                   RACINE / "chatgpt" / "00_INSTRUCTIONS_CHATGPT_COURT.md"]
RAPPEL = re.compile(r"Corpus (\d{4}\.\d+\.\d+) : (\d+) r[eè]gles non relues .*?, (\d+) param[eè]tres")
LIMITE_INSTRUCTIONS_CHATGPT = 8000


def controler_renvois(params):
    problemes = []
    for f in FICHIERS_RENVOIS:
        if not f.exists():
            continue
        for num, ligne in enumerate(f.read_text(encoding="utf-8").splitlines(), start=1):
            for m in RENVOI.finditer(ligne):
                precedente = ""
                for morceau in m.group(1).split(","):
                    for ref in morceau.split(" / "):
                        ref = ref.strip()
                        cle, _, annee = ref.partition("/")
                        cle = cle.strip()
                        if cle.endswith("*"):
                            continue  # famille de clés (bareme_ir_seuil_tranche_*)
                        if cle.startswith("_"):
                            # Suffixe abrégé : « bareme_ir_seuil_tranche_11pct/2026, _30pct » vise
                            # bareme_ir_seuil_tranche_30pct, avec le millésime de la clé précédente.
                            if not precedente:
                                problemes.append(f"{f.relative_to(RACINE)}:{num} : suffixe « {cle} » sans clé complète avant lui")
                                continue
                            cle = precedente.rsplit("_", 1)[0] + cle
                        else:
                            precedente = cle
                        if cle not in params:
                            problemes.append(f"{f.relative_to(RACINE)}:{num} : clé inconnue « {cle} »")
                        elif annee and annee.strip().isdigit() and annee.strip() not in params[cle]["valeurs"]:
                            problemes.append(f"{f.relative_to(RACINE)}:{num} : millésime {annee} absent pour « {cle} »")
    return problemes


def controler_valeurs(params):
    problemes = []
    for f in FICHIERS_RENVOIS:
        if not f.exists():
            continue
        for num, ligne in enumerate(f.read_text(encoding="utf-8").splitlines(), start=1):
            for m in MONTANT_PUIS_RENVOI.finditer(ligne):
                ref = re.split(r",| / ", m.group(3))[0].strip()
                cle, _, annee = ref.partition("/")
                cle, annee = cle.strip(), annee.strip()
                if cle not in params or (annee and annee not in params[cle]["valeurs"]):
                    continue
                en_pct = params[cle].get("unite", "").startswith("pourc")
                if (m.group(2) == "%") != en_pct:
                    continue
                ecrit = float(re.sub(r"[ \u00a0\u202f]", "", m.group(1)).replace(",", "."))
                # Sans millésime, le montant doit égaler l'une des valeurs de la clé.
                attendus = ([float(params[cle]["valeurs"][annee])] if annee
                            else [float(v) for v in params[cle]["valeurs"].values() if v is not None])
                if attendus and all(abs(ecrit - a) > 1e-6 for a in attendus):
                    cible = f"{cle}/{annee}" if annee else cle
                    valeurs = ", ".join(f"{a:g}" for a in attendus)
                    problemes.append(f"{f.relative_to(RACINE)}:{num} : {m.group(1)} {m.group(2)} écrit, "
                                     f"« {cible} » vaut {valeurs}")
    return problemes


def ancre_a_verifier(r):
    """Ligne « Ancre » attendue pour une entrée a_verifier : le statut, la piste éventuelle, puis la note."""
    piste = (r.get("legal_anchor") or "").strip()
    texte = "a_verifier" if piste in ("", "a_verifier") else f"a_verifier (piste : {piste})"
    note = (r.get("anchor_note") or "").strip().rstrip(".")
    return f"{texte} ; {note}" if note else texte


def controler_tracabilite():
    regles = (K / "02_golden_rules_claude_first.md").read_text(encoding="utf-8")
    ancres = {}
    for bloc in re.split(r"(?m)^### ", regles)[1:]:
        rid = bloc.split(" | ")[0].strip()
        m = re.search(r"(?m)^- Ancre : (.*)$", bloc)
        ancres[rid] = m.group(1).strip() if m else None
    lignes = [json.loads(l) for l in (K / "07_rule_source_crosswalk.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    cw = {r["source_rule_id"]: r for r in lignes}
    problemes = []
    if len(cw) != len(lignes):
        problemes.append("crosswalk : identifiants en double")
    for rid in sorted(set(ancres) - set(cw)):
        problemes.append(f"règle {rid} absente du crosswalk")
    for rid in sorted(set(cw) - set(ancres)):
        problemes.append(f"crosswalk : {rid} ne correspond à aucune règle")
    for rid, r in cw.items():
        if r.get("anchor_status") not in ("sourced", "a_verifier"):
            problemes.append(f"crosswalk : {rid} a un statut inconnu « {r.get('anchor_status')} »")
            continue
        if r["anchor_status"] == "sourced":
            if not any(isinstance(r.get(k), dict) and r[k].get("verdict") for k in r if k.startswith(("verification_", "revision_"))):
                problemes.append(f"crosswalk : {rid} est sourced sans verdict")
            if rid in ancres and ancres[rid] != r["legal_anchor"].strip():
                problemes.append(f"règle {rid} : ancre différente du crosswalk")
        elif rid in ancres and ancres[rid] != ancre_a_verifier(r):
            problemes.append(f"règle {rid} : la ligne Ancre ne reprend pas le crosswalk (a_verifier, piste, note)")
    if re.search(r"INVALID", regles):
        problemes.append("règles d'or : un énoncé porte encore la mention INVALIDÉ")
    return problemes


def controler_comptes(params):
    man = json.loads((K / "09_agent_manifest.json").read_text(encoding="utf-8"))
    stats = man.get("statistics", {})
    regles = len(re.findall(r"^### ", (K / "02_golden_rules_claude_first.md").read_text(encoding="utf-8"), re.M))
    articles = len(re.findall(r"^## Article ", (K / "M_CGI_code_general_impots.md").read_text(encoding="utf-8"), re.M))
    # Cas de test : titres « ## FS-… », « ## EV-… », « ## advanced_… », « ## golden_… » (pas les titres de section).
    tests = len(re.findall(r"^## (?:FS-|EV-|advanced_|golden_)", (K / "08_evaluation_suite.md").read_text(encoding="utf-8"), re.M))
    reels = {"golden_rules": regles, "cgi_articles": articles, "referentiel_parametres_keys": len(params),
             "evaluation_test_cases": tests}
    problemes = [f"manifeste : {k} = {stats.get(k)} mais {v} dans les fichiers" for k, v in reels.items() if stats.get(k) != v]
    return problemes


def controler_rappels(params):
    man = json.loads((K / "09_agent_manifest.json").read_text(encoding="utf-8"))
    regles = len(re.findall(r"^### ", (K / "02_golden_rules_claude_first.md").read_text(encoding="utf-8"), re.M))
    attendu = (man.get("version"), str(regles), str(len(params)))
    problemes = []
    for f in FICHIERS_RAPPEL:
        texte = f.read_text(encoding="utf-8")
        trouves = RAPPEL.findall(texte)
        nom = f.relative_to(RACINE)
        if not trouves:
            problemes.append(f"{nom} : rappel de première réponse introuvable")
        for t in trouves:
            if t != attendu:
                problemes.append(f"{nom} : le rappel annonce {t[0]}, {t[1]} règles, {t[2]} paramètres ; "
                                 f"attendu {attendu[0]}, {attendu[1]}, {attendu[2]}")
    court = RACINE / "chatgpt" / "00_INSTRUCTIONS_CHATGPT_COURT.md"
    n = len(court.read_text(encoding="utf-8"))
    if n > LIMITE_INSTRUCTIONS_CHATGPT:
        problemes.append(f"{court.relative_to(RACINE)} : {n} caractères, plus que le champ Instructions "
                         f"({LIMITE_INSTRUCTIONS_CHATGPT})")
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
    problemes = (controler_renvois(params) + controler_valeurs(params) + controler_tracabilite()
                 + controler_comptes(params) + controler_rappels(params) + controler_validite(params))
    if problemes:
        print("Problèmes de cohérence du corpus :")
        for p in problemes:
            print("  - " + p)
        return 1
    print(f"OK : renvois et montants cités, traçabilité des règles, comptes du manifeste, rappels et validité des "
          f"{len(params)} paramètres.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
