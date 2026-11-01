# Journal des versions

Versions calendaires : année.mois.numéro. Chaque version reconstruit les paquets `dist/` : réimporter les zips après une mise à jour.

## 2026.11.5 (01/11/2026)

- Lot 3 de l'audit, corpus fiscal. Les énoncés reconnus faux sont réécrits : 50 règles portent une ligne « Révision » (44 énoncés faux, 6 barèmes mis à jour) ; plus aucune mention « INVALIDÉ », « ERRONÉ » ni « Correction » empilée.
- 378 règles (391 avant) : 14 règles pédagogiques reprises d'un support de formation (M7) retirées ; nouvelle règle RF-006 (statut du bailleur privé, CGI art. 31).
- Traçabilité : chaque ancre `sourced` porte un verdict (358) ; 20 énoncés restent `a_verifier`. La ligne « Ancre » des règles est régénérée depuis le crosswalk, qui fait foi.
- Moteur et risques : option pour l'IS d'une SCI (art. 239), Pacte Dutreil (engagement individuel de 6 ans), option pour le barème, taxe sur les holdings patrimoniales (branche F10), module I sans renvoi aux règles retirées.
- CGI : 73 articles (10 ajoutés, dont 32, 39 C, 150 V, 239, 790 E) ; tableaux des articles 194, 777, 669, 293 B, 977 et 1609 nonies G ; Markdown et JSONL identiques.
- Référentiel : 40 paramètres, dont le plancher et le maximum du plafond PER des salariés ; base du millésime indiquée pour chaque clé.
- Suite d'évaluation : 47 cas (EV-041 Pacte Dutreil, EV-042 bailleur privé).
- Instructions Gemini et ChatGPT alignées sur le skill Claude. ChatGPT : le champ Instructions est limité à 8 000 caractères ; coller `chatgpt/00_INSTRUCTIONS_CHATGPT_COURT.md` et charger le fichier complet en connaissance.
- CI, lancée à chaque push : montant écrit juste avant un renvoi au référentiel comparé à la clé, suffixes de clés abrégés validés, concordance règles et traçabilité (ancres et verdicts), rappel de première réponse cohérent sur les trois plateformes (version, règles, paramètres), nombre exact de cas de test, paquets `dist/` identiques aux sources (zips reproductibles).
- À faire : réimporter `assistant-fiscal-comptable.zip` ; recharger les fichiers de `knowledge/` et les instructions sur Gemini et ChatGPT.

## 2026.11.4 (01/11/2026)

- Skill `conseiller-patrimoine`, version 2026-11-01 (2) : lot 4 de l'audit. Budget à la signature quand on achète avant de vendre avec un relais, alerte de quotité HCSF corrigée, assurance en remboursement total, même fonds dans deux enveloppes, contrôle des saisies (`scripts/entrees.py`) ; 58 tests.
- Règles du conseiller revérifiées sur les sources officielles : prélèvements sociaux, PER, PEE, PEA, HCSF, retraite, garantie des dépôts, don familial (fin le 31/12/2026), crypto-actifs, séparation, meublé de tourisme.
- 12 cas d'évaluation, dont une partie contrôle des valeurs. Corpus fiscal inchangé (2026.11.3) : réimporter seulement `conseiller-patrimoine.zip`.

## 2026.11.3 (01/11/2026)

- Skill `expert-comptable` renommé `assistant-fiscal-comptable` (le titre d'expert-comptable est réservé aux inscrits à l'Ordre). Supprimer l'ancien skill avant d'importer le nouveau zip.
- Promesses publiques corrigées : contrôles faits par des agents d'IA, décompte exact des ancres (358 contrôlées, 33 sans ancre légale), suite d'évaluation décrite telle qu'elle est, origine des règles, prérequis d'installation.
- Licence : texte intégral de CC BY-NC 4.0 ; `NOTICE.md` (contenus de tiers, éditeur).
- Avertissement commun (IA, absence de conseil, particuliers, professionnels) dans les documents et les instructions des trois plateformes.
- Traçabilité : inventaire des documents réduit aux originaux, marqueurs de pipeline retirés, libellés de documents corrigés.
- CI : contrôle des renvois `[referentiel: ...]`, des comptes et de la validité des paramètres.

## 2026.11.2 (01/11/2026)

- Lot 2 de l'audit : barème IR des revenus 2025, IFI, Dutreil, TVA, déficit foncier, assurance-vie, cotisations des indépendants, statut du bailleur privé ; 12 articles CGI ajoutés (63) ; 38 paramètres.

## 2026.11.1 (01/11/2026)

- Lot 1 de l'audit : prélèvements sociaux et PFU 2026, micro-BIC 2026, LMNP, plus-values immobilières, PER ; outil de recherche réparé ; texte intégral des articles CGI coupés.

## 2026.11.0 (01/11/2026)

- Sécurité : historique réécrit sans données personnelles, contrôle automatique des données personnelles, CI durcie, script d'archivage restreint, `SECURITY.md`.
