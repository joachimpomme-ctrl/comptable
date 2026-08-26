#!/usr/bin/env python3
"""Lookup dans la base de connaissances knowledge/ du depot.

Usage (depuis n'importe quel dossier du depot) :
  python3 .claude/skills/expert-comptable/scripts/lookup.py referentiel PASS
  python3 .claude/skills/expert-comptable/scripts/lookup.py referentiel --list
  python3 .claude/skills/expert-comptable/scripts/lookup.py referentiel --search micro
  python3 .claude/skills/expert-comptable/scripts/lookup.py crosswalk bnc_001
  python3 .claude/skills/expert-comptable/scripts/lookup.py cgi "102 ter"
  python3 .claude/skills/expert-comptable/scripts/lookup.py regles amortissement

Pourquoi ce script : 07_rule_source_crosswalk.jsonl (~640 Ko) et
02_golden_rules_claude_first.md (~240 Ko) ne doivent jamais etre charges
integralement en contexte. Ce script extrait uniquement l'entree demandee.

Le dossier knowledge/ est localise automatiquement en remontant depuis ce
script jusqu'a la racine du depot ; la variable d'environnement
COMPTABLE_KNOWLEDGE_DIR permet de forcer un autre emplacement.
"""
import json
import os
import re
import sys
from pathlib import Path


def _find_knowledge():
    env = os.environ.get("COMPTABLE_KNOWLEDGE_DIR")
    if env:
        p = Path(env)
        if (p / "referentiel_parametres.json").exists():
            return p
        sys.exit(f"COMPTABLE_KNOWLEDGE_DIR pointe sur '{env}' mais referentiel_parametres.json est introuvable.")
    here = Path(__file__).resolve()
    for parent in here.parents:
        cand = parent / "knowledge"
        if (cand / "referentiel_parametres.json").exists():
            return cand
    sys.exit("Dossier knowledge/ introuvable en remontant depuis le script. "
             "Definir COMPTABLE_KNOWLEDGE_DIR ou executer depuis le depot comptable.")


BASE = _find_knowledge()


def referentiel(arg):
    data = json.loads((BASE / "referentiel_parametres.json").read_text(encoding="utf-8"))
    params = data["parametres"]
    if arg == "--list":
        for k, v in params.items():
            print(f"{k} [{v.get('statut','?')}] — {v.get('libelle','')}")
        print(f"\nmillesime_courant: {data.get('millesime_courant')}")
        return
    if arg == "--search":
        term = sys.argv[3].lower() if len(sys.argv) > 3 else ""
        for k, v in params.items():
            hay = (k + " " + v.get("libelle", "") + " " + " ".join(v.get("alias", []))).lower()
            if term in hay:
                print(f"{k} [{v.get('statut','?')}] — {v.get('libelle','')}")
        return
    if arg in params:
        print(json.dumps(params[arg], ensure_ascii=False, indent=2))
    else:
        print(f"[DATA_NOT_FOUND_IN_KNOWLEDGE] cle '{arg}' absente du referentiel.")
        print("Cles proches :")
        for k in params:
            if arg.lower() in k.lower():
                print(f"  {k}")


def crosswalk(rule_id):
    found = False
    with open(BASE / "07_rule_source_crosswalk.jsonl", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            e = json.loads(line)
            if e.get("source_rule_id") == rule_id:
                found = True
                print(f"rule_id        : {e['source_rule_id']}")
                print(f"module         : {e.get('claude_module')}")
                print(f"ancre legale   : {e.get('legal_anchor')}")
                print(f"statut ancre   : {e.get('anchor_status')}")
                print(f"document source: {e.get('source_document_label')}")
                print(f"pages          : {e.get('page_start')}–{e.get('page_end')}")
                break
    if not found:
        print(f"[DATA_NOT_FOUND_IN_KNOWLEDGE] regle '{rule_id}' absente du crosswalk.")


def cgi(article):
    """Extrait un article CGI par son numero (ex: '39', '150 VB', '102 ter')."""
    text = (BASE / "M_CGI_code_general_impots.md").read_text(encoding="utf-8")
    pattern = re.compile(
        r"^## Article " + re.escape(article) + r" — .*?(?=^## Article |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(text)
    if m:
        print(m.group(0).strip())
    else:
        print(f"[DATA_NOT_FOUND_IN_KNOWLEDGE] Article {article} absent du corpus M_CGI (51 articles).")
        arts = re.findall(r"^## (Article [^\n—]+)", text, re.MULTILINE)
        print("Articles disponibles :", ", ".join(a.replace("Article ", "").strip() for a in arts))


def regles(term):
    """Recherche plein texte dans 02_golden_rules (retourne les blocs de regles matchants)."""
    text = (BASE / "02_golden_rules_claude_first.md").read_text(encoding="utf-8")
    blocks = re.split(r"(?=^### )", text, flags=re.MULTILINE)
    hits = [b for b in blocks if term.lower() in b.lower() and b.startswith("### ")]
    if not hits:
        print(f"[DATA_NOT_FOUND_IN_KNOWLEDGE] aucun bloc de regle ne contient '{term}'.")
        return
    print(f"{len(hits)} regle(s) trouvee(s) pour '{term}' :\n")
    for b in hits[:15]:
        print(b.strip()[:1200])
        print("-" * 60)
    if len(hits) > 15:
        print(f"... {len(hits) - 15} autres resultats tronques. Affine le terme de recherche.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    cmd, arg = sys.argv[1], sys.argv[2]
    {"referentiel": referentiel, "crosswalk": crosswalk, "cgi": cgi, "regles": regles}.get(
        cmd, lambda a: print(f"Commande inconnue: {cmd}\n{__doc__}")
    )(arg)
