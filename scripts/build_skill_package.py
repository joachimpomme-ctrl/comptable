#!/usr/bin/env python3
"""Construit les paquets autonomes des skills Claude du depot.

Deux skills sont versionnes dans .claude/skills/ :

- assistant-fiscal-comptable (anciennement expert-comptable) : lit la base knowledge/ a la racine du depot. Le paquet
  autonome embarque cette base dans references/ et adapte les chemins du
  SKILL.md.
- conseiller-patrimoine : deja autonome (SKILL.md, references/, scripts/).
  Le paquet reprend le dossier tel quel, sans evals/ ni caches Python.

Usage :
    python3 scripts/build_skill_package.py                        # les deux
    python3 scripts/build_skill_package.py assistant-fiscal-comptable  # un seul
    python3 scripts/build_skill_package.py conseiller-patrimoine

Produit, pour chaque skill :
    dist/<skill>.skill   (archive zip : carte « Save skill » dans Claude Code)
    dist/<skill>.zip     (meme contenu : upload claude.ai > Settings > Capabilities)

A relancer apres toute mise a jour d'un skill ou de knowledge/ (mise a jour
annuelle de janvier notamment), puis committer dist/.
"""
import shutil
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS = REPO / ".claude" / "skills"
KNOWLEDGE = REPO / "knowledge"
DIST = REPO / "dist"
BUILD_ROOT = DIST / "_build"

# Exclus de tout paquet : tests d'evaluation (servent au developpement) et caches.
EXCLUS = {"evals", "__pycache__", ".pytest_cache", ".DS_Store"}


def _zipper(build_dir, nom):
    DIST.mkdir(exist_ok=True)
    for out_name in (f"{nom}.skill", f"{nom}.zip"):
        out = DIST / out_name
        if out.exists():
            out.unlink()
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for p in sorted(build_dir.rglob("*")):
                if p.is_file():
                    z.write(p, p.relative_to(build_dir.parent))
        print(f"OK {out.relative_to(REPO)} ({out.stat().st_size / 1024:.0f} Ko)")


def build_assistant_fiscal_comptable():
    src = SKILLS / "assistant-fiscal-comptable"
    build = BUILD_ROOT / "assistant-fiscal-comptable"
    if not (src / "SKILL.md").exists():
        sys.exit(f"SKILL.md introuvable dans {src}")
    (build / "scripts").mkdir(parents=True)
    (build / "references").mkdir()

    # knowledge/chatgpt_only/ est exclu : doublon JSONL du CGI et inventaire de
    # pipeline, inutiles dans le paquet et couteux en taille.
    knowledge_files = sorted(p for p in KNOWLEDGE.iterdir() if p.is_file())

    # SKILL.md : les chemins knowledge/ deviennent references/ (embarques),
    # et le script de lookup s'appelle depuis le dossier du skill.
    text = (src / "SKILL.md").read_text(encoding="utf-8")
    text = text.replace(".claude/skills/assistant-fiscal-comptable/scripts/lookup.py", "scripts/lookup.py")
    text = text.replace("knowledge/", "references/")
    text = text.replace("adossé à la base de connaissances references/ de ce dépôt",
                        "adossé à sa base de connaissances embarquée (references/)")
    text = text.replace("dossier `references/` de ce dépôt", "dossier `references/` de ce skill")
    text = text.replace(
        "Base de connaissances : dossier `references/` à la racine du dépôt.",
        "Base de connaissances : dossier `references/` embarqué dans ce skill.")
    text = text.replace(
        "Tous les fichiers sont dans `references/` à la racine du dépôt.",
        "Tous les fichiers sont dans `references/` de ce skill.")
    (build / "SKILL.md").write_text(text, encoding="utf-8")

    # lookup.py est identique : il cherche references/ puis knowledge/.
    shutil.copy2(src / "scripts" / "lookup.py", build / "scripts" / "lookup.py")
    for f in knowledge_files:
        shutil.copy2(f, build / "references" / f.name)

    _zipper(build, "assistant-fiscal-comptable")
    print(f"Contenu : SKILL.md + scripts/lookup.py + {len(knowledge_files)} fichiers references/")


def build_conseiller_patrimoine():
    src = SKILLS / "conseiller-patrimoine"
    build = BUILD_ROOT / "conseiller-patrimoine"
    if not (src / "SKILL.md").exists():
        sys.exit(f"SKILL.md introuvable dans {src}")
    shutil.copytree(src, build, ignore=lambda d, noms: [n for n in noms if n in EXCLUS or n.endswith(".pyc")])
    n_ref = len(list((build / "references").glob("*.md")))
    n_scripts = len(list((build / "scripts").glob("*.py")))
    _zipper(build, "conseiller-patrimoine")
    print(f"Contenu : SKILL.md + {n_ref} fichiers references/ + {n_scripts} scripts (+ tests)")


CIBLES = {
    "assistant-fiscal-comptable": build_assistant_fiscal_comptable,
    "conseiller-patrimoine": build_conseiller_patrimoine,
}


def main(argv):
    noms = argv or list(CIBLES)
    inconnus = [n for n in noms if n not in CIBLES]
    if inconnus:
        sys.exit(f"Skill inconnu : {', '.join(inconnus)} (choix : {', '.join(CIBLES)})")
    if BUILD_ROOT.exists():
        shutil.rmtree(BUILD_ROOT)
    try:
        for n in noms:
            CIBLES[n]()
    finally:
        if BUILD_ROOT.exists():
            shutil.rmtree(BUILD_ROOT)


if __name__ == "__main__":
    main(sys.argv[1:])
