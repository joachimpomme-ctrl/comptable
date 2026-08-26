#!/usr/bin/env python3
"""Construit le paquet autonome du skill Claude « expert-comptable ».

Le skill du depot (.claude/skills/expert-comptable/) lit la base knowledge/
a la racine du depot : il fonctionne pour qui a clone le repo. Ce script
fabrique la variante AUTONOME, installable dans un profil Claude sans cloner
le depot : la base de connaissances y est embarquee dans references/.

Usage :
    python3 scripts/build_skill_package.py

Produit :
    dist/expert-comptable.skill   (archive zip — carte « Save skill » dans Claude Code)
    dist/expert-comptable.zip     (meme contenu — upload claude.ai > Settings > Capabilities)

A relancer apres toute mise a jour de knowledge/ ou du SKILL.md (mise a jour
annuelle de janvier notamment), puis committer dist/.
"""
import shutil
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL_SRC = REPO / ".claude" / "skills" / "expert-comptable"
KNOWLEDGE = REPO / "knowledge"
BUILD = REPO / "dist" / "_build" / "expert-comptable"
DIST = REPO / "dist"

# knowledge/chatgpt_only/ est exclu : doublon JSONL du CGI et inventaire de
# pipeline, inutiles dans le paquet et couteux en taille.
KNOWLEDGE_FILES = sorted(p for p in KNOWLEDGE.iterdir() if p.is_file())


def main():
    if not (SKILL_SRC / "SKILL.md").exists():
        sys.exit(f"SKILL.md introuvable dans {SKILL_SRC}")

    if BUILD.parent.exists():
        shutil.rmtree(BUILD.parent)
    (BUILD / "scripts").mkdir(parents=True)
    (BUILD / "references").mkdir()

    # SKILL.md : les chemins knowledge/ deviennent references/ (embarques),
    # et le script de lookup s'appelle depuis le dossier du skill.
    text = (SKILL_SRC / "SKILL.md").read_text(encoding="utf-8")
    text = text.replace(".claude/skills/expert-comptable/scripts/lookup.py", "scripts/lookup.py")
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
    (BUILD / "SKILL.md").write_text(text, encoding="utf-8")

    # lookup.py est identique : il cherche references/ puis knowledge/.
    shutil.copy2(SKILL_SRC / "scripts" / "lookup.py", BUILD / "scripts" / "lookup.py")

    for f in KNOWLEDGE_FILES:
        shutil.copy2(f, BUILD / "references" / f.name)

    DIST.mkdir(exist_ok=True)
    for out_name in ("expert-comptable.skill", "expert-comptable.zip"):
        out = DIST / out_name
        if out.exists():
            out.unlink()
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for p in sorted(BUILD.rglob("*")):
                if p.is_file():
                    z.write(p, p.relative_to(BUILD.parent))
        print(f"OK {out.relative_to(REPO)} ({out.stat().st_size / 1024:.0f} Ko)")

    shutil.rmtree(BUILD.parent)
    print(f"Contenu : SKILL.md + scripts/lookup.py + {len(KNOWLEDGE_FILES)} fichiers references/")


if __name__ == "__main__":
    main()
