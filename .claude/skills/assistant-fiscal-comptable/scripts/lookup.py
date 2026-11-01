#!/usr/bin/env python3
"""Lookup dans la base de connaissances knowledge/ du depot.

Usage (depuis n'importe quel dossier du depot) :
  python3 .claude/skills/assistant-fiscal-comptable/scripts/lookup.py referentiel PASS
  python3 .claude/skills/assistant-fiscal-comptable/scripts/lookup.py referentiel --list
  python3 .claude/skills/assistant-fiscal-comptable/scripts/lookup.py referentiel --search micro bic
  python3 .claude/skills/assistant-fiscal-comptable/scripts/lookup.py crosswalk bnc_001
  python3 .claude/skills/assistant-fiscal-comptable/scripts/lookup.py cgi "102 ter"
  python3 .claude/skills/assistant-fiscal-comptable/scripts/lookup.py regles LMN-025          (regle complete par identifiant)
  python3 .claude/skills/assistant-fiscal-comptable/scripts/lookup.py regles plus value       (recherche, 5 regles par page)
  python3 .claude/skills/assistant-fiscal-comptable/scripts/lookup.py regles plus value --page 2

Pourquoi ce script : 07_rule_source_crosswalk.jsonl (~820 Ko) et
02_golden_rules_claude_first.md (~290 Ko) ne doivent jamais etre charges
integralement en contexte. Ce script extrait uniquement l'entree demandee.

Les regles sont toujours affichees EN ENTIER : une Correction ou une
Precision n'est jamais coupee. Quand une regle porte la mention
"ENONCE INVALIDE", sa Correction prime sur l'enonce.

Le dossier knowledge/ est localise automatiquement en remontant depuis ce
script jusqu'a la racine du depot ; la variable d'environnement
COMPTABLE_KNOWLEDGE_DIR permet de forcer un autre emplacement.

Codes retour : 0 trouve, 1 introuvable, 2 usage incorrect.
"""
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

PAR_PAGE = 5

def _find_knowledge():
    env = os.environ.get("COMPTABLE_KNOWLEDGE_DIR")
    if env:
        p = Path(env)
        if (p / "referentiel_parametres.json").exists():
            return p
        sys.exit(f"COMPTABLE_KNOWLEDGE_DIR pointe sur '{env}' mais referentiel_parametres.json est introuvable.")
    here = Path(__file__).resolve()
    for parent in here.parents:
        for name in ("references", "knowledge"):
            cand = parent / name
            if (cand / "referentiel_parametres.json").exists():
                return cand
    sys.exit("Base de connaissances introuvable (ni references/ ni knowledge/ en remontant depuis le script). "
             "Definir COMPTABLE_KNOWLEDGE_DIR ou executer depuis le depot comptable.")


BASE = _find_knowledge()


def _norm(s):
    """Normalise un identifiant : casse, espaces, tirets et soulignes ignores."""
    return re.sub(r"[\s_\-]+", "", s or "").lower()


def _expire(v):
    lim = v.get("valable_jusqu_au")
    try:
        return lim and dt.date.fromisoformat(lim) < dt.date.today()
    except ValueError:
        return False


def referentiel(args):
    data = json.loads((BASE / "referentiel_parametres.json").read_text(encoding="utf-8"))
    params = data["parametres"]
    if not args:
        return _usage()
    if args[0] == "--list":
        for k, v in params.items():
            alerte = " [VALIDITE DEPASSEE]" if _expire(v) else ""
            print(f"{k} [{v.get('statut', '?')}]{alerte} : {v.get('libelle', '')}")
        print(f"\nmillesime_courant: {data.get('millesime_courant')}")
        return 0
    if args[0] == "--search":
        term = " ".join(args[1:]).lower()
        n = 0
        for k, v in params.items():
            hay = (k + " " + v.get("libelle", "") + " " + " ".join(v.get("alias", []))).lower()
            if all(t in hay for t in term.split()):
                print(f"{k} [{v.get('statut', '?')}] : {v.get('libelle', '')}")
                n += 1
        if not n:
            print(f"[DATA_NOT_FOUND_IN_KNOWLEDGE] aucune cle ne correspond a '{term}'.")
        return 0 if n else 1
    cle = args[0]
    if cle in params:
        v = params[cle]
        if _expire(v):
            print(f"ATTENTION : validite depassee ({v.get('valable_jusqu_au')}). "
                  f"Parametre non reverifie depuis le {v.get('verifie_le', '?')} : le controler sur la source citee "
                  f"et ne pas le presenter comme verifie.\n")
        print(json.dumps(v, ensure_ascii=False, indent=2))
        return 0
    print(f"[DATA_NOT_FOUND_IN_KNOWLEDGE] cle '{cle}' absente du referentiel.")
    proches = [k for k in params if _norm(cle) in _norm(k)]
    if proches:
        print("Cles proches : " + ", ".join(proches))
    return 1


def crosswalk(args):
    if not args:
        return _usage()
    rule_id = _norm(" ".join(args))
    with open(BASE / "07_rule_source_crosswalk.jsonl", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            e = json.loads(line)
            if _norm(e.get("source_rule_id")) != rule_id:
                continue
            passes = sorted(k for k in e if k.startswith("verification_"))
            p1, p2 = e.get("page_start"), e.get("page_end")
            pages = f"{p1} a {p2}" if p1 is not None else "non renseignees"
            print(f"rule_id          : {e['source_rule_id']}")
            print(f"module           : {e.get('claude_module')}")
            print(f"ancre legale     : {e.get('legal_anchor')}")
            print(f"statut ancre     : {e.get('anchor_status')}")
            if e.get("anchor_note"):
                print(f"note ancre       : {e.get('anchor_note')}")
            print(f"verifiee le      : {e.get('anchor_verified_le') or e.get('anchor_verified_on') or 'non renseigne'}")
            # Passes de verification, de la plus recente a la plus ancienne : la premiere fait foi.
            for cle in reversed(passes):
                v = e[cle] or {}
                date = cle.replace("verification_", "").replace("_", "-")
                print(f"--- verification du {date}")
                if v.get("legal_anchor_precedente"):
                    print(f"ancre precedente : {v.get('legal_anchor_precedente')}")
                print(f"verdict          : {v.get('verdict', 'non renseigne')}")
                print(f"methode          : {v.get('methode', 'non renseignee')}")
                preuve = v.get("evidence") or v.get("preuve")
                if preuve:
                    print(f"preuve           : {preuve}")
            if not passes:
                print("verdict          : aucun (entree non repassee lors des verifications)")
            print(f"document source  : {e.get('source_document_label') or 'non renseigne'}")
            print(f"pages            : {pages} (rapprochement automatique, a confirmer)")
            return 0
    print(f"[DATA_NOT_FOUND_IN_KNOWLEDGE] regle '{' '.join(args)}' absente du crosswalk.")
    return 1


def cgi(args):
    """Extrait un article CGI par son numero (ex: '39', '150 VB', '102 ter')."""
    if not args:
        return _usage()
    article = " ".join(args).replace("Article", "").replace("art.", "").strip()
    text = (BASE / "M_CGI_code_general_impots.md").read_text(encoding="utf-8")
    sections = re.split(r"(?=^## Article )", text, flags=re.MULTILINE)
    for s in sections:
        m = re.match(r"## Article (.+?) —", s)
        if m and _norm(m.group(1)) == _norm(article):
            print(s.strip())
            return 0
    arts = re.findall(r"^## Article (.+?) —", text, re.MULTILINE)
    print(f"[DATA_NOT_FOUND_IN_KNOWLEDGE] Article {article} absent du corpus M_CGI ({len(arts)} articles).")
    print("Articles disponibles :", ", ".join(a.strip() for a in arts))
    return 1


def regles(args):
    """Regle complete par identifiant, ou recherche plein texte paginee (regles toujours entieres)."""
    page = 1
    if "--page" in args:
        i = args.index("--page")
        try:
            page = max(1, int(args[i + 1]))
        except (IndexError, ValueError):
            return _usage()
        args = args[:i] + args[i + 2:]
    if not args:
        return _usage()
    term = " ".join(args).strip()
    text = (BASE / "02_golden_rules_claude_first.md").read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"(?=^### )", text, flags=re.MULTILINE) if b.startswith("### ")]

    def ident(b):
        return b[4:].split("|")[0].strip()

    exact = [b for b in blocks if _norm(ident(b)) == _norm(term)]
    if exact:
        hits = exact
    else:
        mots = term.lower().split()
        hits = [b for b in blocks if all(m in b.lower() for m in mots)]
    if not hits:
        print(f"[DATA_NOT_FOUND_IN_KNOWLEDGE] aucune regle ne correspond a '{term}'.")
        return 1
    debut = (page - 1) * PAR_PAGE
    selection = hits if exact else hits[debut:debut + PAR_PAGE]
    if not exact:
        print(f"{len(hits)} regle(s) pour '{term}', page {page} sur {(len(hits) - 1) // PAR_PAGE + 1} :\n")
    for b in selection:
        if "INVALID" in b.upper():
            print("[ATTENTION : ENONCE INVALIDE. La Correction ci-dessous prime sur l'enonce.]")
        print(b.strip())
        print("-" * 60)
    if not exact and debut + PAR_PAGE < len(hits):
        print(f"Suite : ajouter --page {page + 1} (ou affiner la recherche).")
    return 0


def _usage():
    print(__doc__)
    return 2


COMMANDES = {"referentiel": referentiel, "crosswalk": crosswalk, "cgi": cgi, "regles": regles}

if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in COMMANDES:
        if len(sys.argv) >= 2 and sys.argv[1] not in COMMANDES:
            print(f"Commande inconnue : {sys.argv[1]}")
        sys.exit(_usage())
    try:
        sys.exit(COMMANDES[sys.argv[1]](sys.argv[2:]))
    except BrokenPipeError:
        sys.exit(0)
