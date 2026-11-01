# Contribuer : relecture des regles par des professionnels

Ce depot a besoin de relecteurs : **experts-comptables, avocats fiscalistes, CGP, notaires**. Les 378 regles metier sont en statut `candidate_to_validate` : rattachees a leurs sources et controlees par des agents d'IA, mais relues par aucun professionnel.

Aucune connaissance de Git n'est necessaire : **une issue GitHub suffit** (modeles proposes a l'ouverture d'une issue).

---

## Relire un lot de regles (le coeur du besoin)

1. Choisir un lot d'une vingtaine de regles d'un meme theme. Par ou commencer : micro et reel (GFPL-049 a GFPL-060), LMNP (LMN-001 a LMN-025), plus-values immobilieres (PV-IMM-*), PER (GFPL-165 a GFPL-174). Les cas EV-029 a EV-040 de `knowledge/08_evaluation_suite.md` montrent ce que l'agent doit savoir faire.
2. Ouvrir une issue avec le modele **Relecture d'un lot** : titre `[RELECTURE] <theme ou identifiants>`.
3. Pour chaque regle : verdict (exacte / exacte avec reserve / erronee), correction proposee, source d'appui (CGI, BOFiP, jurisprudence), millesime verifie.
4. Indiquer votre qualite (profession) ; votre nom est facultatif. Tout ce qui est ecrit dans une issue reste public dans l'historique du depot.

### Ce qui se passe ensuite

- Le mainteneur verifie la qualite declaree dans un annuaire public (Ordre des experts-comptables, Conseil national des barreaux, notaires, ORIAS) et note « qualite verifiee le JJ/MM/AAAA ».
- Une regle passe `validated` apres **deux relectures concordantes** de relecteurs verifies. Elle recoit `validated_until` (fin du millesime relu) : une regle validee redevient a relire a chaque nouvelle loi de finances.
- Une regle jugee erronee est reecrite, avec la source d'appui ajoutee a l'ancre.
- En cas de desaccord, le mainteneur tranche sur la source la plus haute (texte, puis BOFiP, puis jurisprudence) et consigne la decision dans l'issue.

### Regles du jeu

- **La relecture est benevole, porte sur l'enonce a la date et au millesime indiques, et n'engage pas la responsabilite professionnelle du relecteur.**
- Toute relecture **cite une source d'appui verifiable**. « De memoire » ne suffit pas : c'est l'exigence imposee a l'agent.
- Les questions generales se posent dans une issue `[QUESTION]`.

---

## Autres contributions bienvenues

- **Chiffres du referentiel** (`knowledge/referentiel_parametres.json`) : signaler une valeur perimee ou proposer une cle manquante (CARMF, plafonds PER...) — issue `[REFERENTIEL] <cle>` avec la source officielle (URL Legifrance, JO, urssaf.fr...).
- **Mise a jour annuelle** (janvier, apres la Loi de Finances) : PASS, baremes IR, taux URSSAF, bareme kilometrique — issue `[MILLESIME AAAA]`.
- **Cas de test** (`knowledge/08_evaluation_suite.md`) : proposer un cas reel anonymise avec la reponse attendue sourcee — issue `[CAS DE TEST]`.
- **Erreur constatee en utilisant l'agent** : issue `[BUG REPONSE]` avec la question posee, la reponse obtenue et ce qui est faux (et la source qui le montre).

### Skill conseiller-patrimoine

- **Erreur de fond, regle perimee, garde-fou manquant** : issue `[CONSEILLER] <fichier ou sujet>` avec la source officielle qui le montre.
- **Regle volatile qui a change** (taux, plafond, norme, calendrier) : issue `[FRAICHEUR] <regle>` avec le nouveau texte, sa date d'effet et le lien. C'est la contribution la plus utile : `references/01-fraicheur.md` vieillit vite.
- **Cas de test** : issue `[CAS DE TEST] conseiller` avec une question reelle anonymisee et ce que la bonne reponse doit contenir.
- Relecteurs particulierement bienvenus : CGP, CIF, notaires, courtiers en credit. Voir le [guide du skill](docs/conseiller-patrimoine.md#13-signaler-une-erreur-contribuer).

---

## Ce que ce depot n'accepte pas

- Des regles ou chiffres **sans source verifiable**.
- Des donnees personnelles ou des cas clients non anonymises.
- Les PDF sources sous droits d'auteur (guides fiscaux commerciaux) — on cite le document et la page, on ne redistribue pas le fichier.

---

## Licence des contributions

En contribuant, vous acceptez que votre contribution soit diffusee sous la licence du depot (CC BY-NC 4.0, voir `NOTICE.md`). Les relectures sont creditees par la qualite du relecteur, et par son nom s'il le souhaite.
