#!/usr/bin/env python3
"""Compare ou met a jour les articles du corpus M_CGI a partir d'un export PDF Legifrance du CGI.

Etapes :
  1. Telecharger l'export PDF du CGI sur Legifrance (LEGITEXT000006069577).
  2. pdftotext -raw export.pdf cgi.txt        (le mode -raw garde les tirets de fin de ligne)
  3. python3 scripts/extraire_articles_cgi.py cgi.txt                  -> etat de chaque article du corpus
     python3 scripts/extraire_articles_cgi.py cgi.txt --remplacer 150-VB 39 ...
                                                                        -> remplace le texte de ces articles
     (dans le MD et dans le JSONL ChatGPT ; mettre a jour ensuite l'en-tete de source du MD)

Etats : IDENTIQUE (memes mots et chiffres, dans le meme ordre), IDENTIQUE HORS ESPACES (seuls des espaces
different, par exemple un mot accole a la cellule voisine dans l'export), COUPE (le corpus n'a que le debut
du texte), DIFFERENT (a relire : modification du texte), ABSENT DE L'EXPORT. La comparaison ignore les retours
a la ligne, les espaces multiples et la mise en tableau Markdown du corpus (caracteres | et lignes |---|).
La colonne jsonl verifie que le JSONL ChatGPT porte exactement le meme texte que le MD.

Les tableaux (art. 194, 293 B, 669, 777, 977, 1609 nonies G) sont mal restitues par pdftotext et ont ete
mis en tableau a la main dans le corpus : --remplacer refuse ces articles (les refaire a la main, puis
relancer la comparaison). Chaque article porte la ligne « **Version du texte :** » et le JSONL le champ
version_texte : les mettre a jour avec la date du nouvel export.
"""
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
MD = RACINE / "knowledge" / "M_CGI_code_general_impots.md"
JSONL = RACINE / "knowledge" / "chatgpt_only" / "M_CGI_code_general_impots.jsonl"

LABEL = re.compile(r"^(Livre|Première|Deuxième|Troisième|Quatrième|Cinquième|Titre|Chapitre|Section|Sous-section|"
                   r"Paragraphe|Sous-paragraphe|\d*[IVXL]+|\d+°|[A-Z]|\d+|[a-z])\b[^:]{0,40} : \S.*$")
FOOT = re.compile(r"^Code général des impôts, CGI\. - Dernière modification .*$")

def parse(raw):
    lines = raw.split("\n")
    out = []
    i = 0
    while i < len(lines):
        l = lines[i]
        if FOOT.match(l.strip()):
            i += 1
            continue
        if l.startswith("\x0c"):
            l = l[1:]
            if l.strip() == "Code général des impôts":
                i += 1
                while i < len(lines) and (LABEL.match(lines[i].strip()) or not lines[i].strip()):
                    i += 1
                continue
        out.append(l)
        i += 1
    text = "\n".join(out)
    arts = {}
    pos = [(m.start(), m.group(1)) for m in re.finditer(r"^Article (\S.*?)\s*$", text, re.M)]
    for k, (start, num) in enumerate(pos):
        end = pos[k + 1][0] if k + 1 < len(pos) else len(text)
        body = text[start:end].split("\n")
        body = [b.rstrip() for b in body if b.strip()]
        while body and LABEL.match(body[-1].strip()):
            body.pop()
        # fil d'Ariane avant l'article suivant (titres parfois coupes sur deux lignes)
        for j in range(len(body) - 1, max(len(body) - 14, 0), -1):
            if re.match(r"^Livre (premier|[IVX]+|deuxième|troisième|quatrième) : ", body[j]):
                body = body[:j]
                break
        if num not in arts:
            arts[num] = "\n".join(body)
    return arts


SEPARATEUR = re.compile(r"^\|(?:\s*:?-{3,}:?\s*\|)+\s*$", re.M)


def _norm(s):
    """Espaces et retours a la ligne reduits ; mise en tableau Markdown (| et lignes |---|) ignoree."""
    return re.sub(r"\s+", " ", SEPARATEUR.sub("", s).replace("|", " ")).strip()


def blocs_corpus(md):
    return re.findall(r"^## Article (.+?) \u2014.*?\n```\n(.*?)\n```", md, re.S | re.M)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    arts = parse(open(sys.argv[1], encoding="utf-8").read())
    md = MD.read_text(encoding="utf-8")
    if "--remplacer" not in sys.argv:
        jsonl = {}
        for ligne in JSONL.read_text(encoding="utf-8").splitlines():
            if ligne.strip():
                e = json.loads(ligne)
                jsonl[e["article"].replace("CGI Art. ", "").strip()] = e.get("texte_complet")
        blocs = blocs_corpus(md)
        for num, ancien in blocs:
            num = num.strip()
            neuf = arts.get(num)
            if neuf is None:
                etat = "ABSENT DE L'EXPORT"
            elif _norm(ancien) == _norm(neuf):
                etat = "IDENTIQUE"
            elif _norm(ancien).replace(" ", "") == _norm(neuf).replace(" ", ""):
                etat = "IDENTIQUE HORS ESPACES"
            elif _norm(neuf).startswith(_norm(ancien)[:-40]):
                etat = "COUPE"
            else:
                etat = "DIFFERENT"
            j = "ok" if jsonl.get(num) == ancien else ("ABSENT" if num not in jsonl else "ECART")
            print(f"{num:18} {etat:22} corpus={len(ancien):6} export={len(neuf or ''):6} jsonl={j}")
        orphelins = sorted(set(jsonl) - {n.strip() for n, _ in blocs})
        if orphelins:
            print("Articles du JSONL absents du MD : " + ", ".join(orphelins))
        print(f"{len(blocs)} articles dans le MD, {len(jsonl)} dans le JSONL.")
        return 0
    cibles = [a.replace("-", " ") if not re.match(r"^\d+-\d", a) else a for a in sys.argv[sys.argv.index("--remplacer") + 1:]]
    for num in cibles:
        pat = re.compile(r"(^## Article " + re.escape(num) + r" \u2014.*?\n```\n)(.*?)(\n```)", re.S | re.M)
        m = pat.search(md)
        if not m or num not in arts:
            sys.exit(f"Article {num} introuvable dans le corpus ou dans l'export.")
        if SEPARATEUR.search(m.group(2)):
            sys.exit(f"Article {num} : tableau mis en forme dans le corpus, a remplacer a la main.")
        md = md[:m.start(2)] + arts[num] + md[m.end(2):]
    MD.write_text(md, encoding="utf-8")
    lignes = []
    for ligne in JSONL.read_text(encoding="utf-8").splitlines(keepends=True):
        if ligne.strip():
            e = json.loads(ligne)
            num = e["article"].replace("CGI Art. ", "").strip()
            if num in cibles:
                e["texte_complet"] = arts[num]
                ligne = json.dumps(e, ensure_ascii=False) + "\n"
        lignes.append(ligne)
    JSONL.write_text("".join(lignes), encoding="utf-8")
    print(f"{len(cibles)} article(s) remplace(s). Mettre a jour l'en-tete de source du MD.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
