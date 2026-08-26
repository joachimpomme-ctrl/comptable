# Contribuer — Validation des regles par des professionnels

Ce depot a besoin de relecteurs du chiffre : **experts-comptables, fiscalistes, CGP, notaires, avocats fiscalistes**. Les 391 regles metier sont en statut `candidate_to_validate` : structurees et tracees, mais non validees. Chaque validation (ou correction) augmente la fiabilite du corpus pour tout le monde.

Aucune connaissance de Git n'est necessaire pour contribuer : **une issue GitHub suffit.**

---

## Valider ou contester une regle (le coeur du besoin)

1. Ouvrir une **issue GitHub** ([Issues > New issue](../../issues/new)) — **une issue par regle**.
2. Titre : `[VALIDATION] <id de la regle>` ou `[CORRECTION] <id de la regle>` — ex. `[VALIDATION] GFPL-050`, `[CORRECTION] LMN-011`.
3. Corps de l'issue (modele a copier) :

```
Regle : <id> (fichier knowledge/02_golden_rules_claude_first.md)
Verdict : VALIDE / VALIDE AVEC RESERVE / ERRONEE
Motif / correction proposee :
  <texte corrige de la regle si erronee, ou reserve precisee>
Source d'appui : <CGI art. X / BOFiP BOI-XXX / jurisprudence / doctrine>
Millesime verifie : <ex. revenus 2025>
Valideur : <Nom, qualite — ex. Jean D., expert-comptable> 
Date : <AAAA-MM-JJ>
```

4. Ce qui se passe ensuite (par le mainteneur, ou par vous en pull request si vous etes a l'aise avec Git) :
   - **VALIDE** → la regle passe `candidate_to_validate` → `validated` dans `02_golden_rules_claude_first.md`, avec ajout de deux lignes :
     `- Valide par : <Nom, qualite>` et `- Valide le : <date>` ;
   - **ERRONEE** → le texte de la regle est corrige, la source d'appui est ajoutee a l'ancre, puis la regle passe `validated` ;
   - le tableau « Etat de validation du corpus » du README est mis a jour (compteur X/391).

### Regles du jeu

- Une validation engage son auteur sur **le fond de la regle a la date et au millesime indiques** — pas sur les millesimes futurs.
- Toute validation **doit citer une source d'appui verifiable** (CGI, BOFiP, jurisprudence, doctrine administrative). « De memoire » ne suffit pas — c'est la meme exigence que celle imposee a l'agent.
- En cas de desaccord entre deux professionnels sur une meme regle, la regle reste `candidate_to_validate` avec un lien vers la discussion, jusqu'a arbitrage source.

---

## Autres contributions bienvenues

- **Chiffres du referentiel** (`knowledge/referentiel_parametres.json`) : signaler une valeur perimee ou proposer le sourcing d'une cle `candidate_to_validate` (CARMF, CARPIMKO, taux TNS...) — issue `[REFERENTIEL] <cle>` avec la source officielle (URL Legifrance, JO, urssaf.fr...).
- **Mise a jour annuelle** (janvier, apres la Loi de Finances) : PASS, baremes IR, taux URSSAF, bareme kilometrique — issue `[MILLESIME AAAA]`.
- **Cas de test** (`knowledge/08_evaluation_suite.md`) : proposer un cas reel anonymise avec la reponse attendue sourcee — issue `[CAS DE TEST]`.
- **Erreur constatee en utilisant l'agent** : issue `[BUG REPONSE]` avec la question posee, la reponse obtenue et ce qui est faux (et la source qui le montre).

---

## Ce que ce depot n'accepte pas

- Des regles ou chiffres **sans source verifiable**.
- Des donnees personnelles ou des cas clients non anonymises.
- Les PDF sources sous droits d'auteur (guides fiscaux commerciaux) — on cite le document et la page, on ne redistribue pas le fichier.

---

## Licence des contributions

En contribuant, vous acceptez que votre contribution soit diffusee sous la licence du depot (CC BY-NC 4.0). Les validations sont creditees nominativement (nom + qualite) dans les regles validees.
