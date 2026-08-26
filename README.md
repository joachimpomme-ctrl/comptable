# Agent IA Comptable & Patrimoine

Agent IA specialise en comptabilite, fiscalite des professions liberales, location meublee, gestion financiere et gestion de patrimoine. Fonctionne sur **Claude Code** (skill integre au depot), **Gemini Gems** et **ChatGPT Custom GPT**.

> ## ⚠️ A lire avant toute utilisation
>
> - **Les sorties de l'agent sont des projets de reponse a verifier — jamais un livrable client, jamais un conseil.** La consultation fiscale a titre habituel est une activite reglementee : cet outil est une aide a la recherche et a la pre-qualification, la responsabilite professionnelle reste celle du praticien.
> - **Etat de validation : 0 des 391 regles metier a ete validee par un professionnel** (statut `candidate_to_validate`). Seuls 24 parametres chiffres du referentiel sont verifies contre une source officielle. Voir [Etat de validation du corpus](#etat-de-validation-du-corpus).
> - **Millesimes :** les chiffres verifies couvrent 2025 et partiellement 2026 ; les baremes URSSAF/kilometrique restent au millesime 2025. Voir la [table des millesimes](#table-des-millesimes).

---

## A quoi ca sert (pour un professionnel)

Usages concrets en cabinet ou en pratique individuelle : **pre-qualification d'un dossier** (regime, seuils, options applicables), **brouillon de reponse sourcee** a verifier avant envoi, **checklists declaratives** (2035, 2042, 2044, 2048-IMM), **rappel des pieges** (ARD en LMNP, reintegration des amortissements depuis 2025, bascules micro/reel).

Trois questions de demonstration a copier-coller :

```
"Je suis medecin liberal en BNC, CA 150 000 EUR. Comparez micro-BNC et regime reel pour 2025."
"J'ai vendu un appartement detenu 12 ans, PV brute 80 000 EUR. Calcule ma plus-value imposable apres abattements."
"Quels sont les seuils micro-BIC pour un meuble de tourisme non classe, revenus 2025 declares 2026 ?"
```

Pour tester serieusement l'agent : `knowledge/08_evaluation_suite.md` contient **45 cas de test avec la reponse attendue ecrite** — le moyen le plus rapide pour un expert-comptable de juger la qualite des sorties.

---

## Domaines couverts

| Module | Domaine |
|--------|---------|
| M1 | Comptabilite BNC |
| M2 | Fiscalite professions liberales 2025 |
| M3 | Normes PCG 2025 |
| M5 / M5bis | Location meublee LMNP/LMP |
| M6 | Gestion patrimoniale (succession, donation, AV, PER, SCI) |
| M7 | Conseil en gestion de patrimoine (MIF2/DDA) |
| M8 | Bases comptables (BFR, CAF) |
| M9 | Revenus fonciers, plus-values immobilieres |
| M10 | Baremes DMTG, IFI |
| M11 | Epargne salariale (PEE, PERCOL, interessement) |
| M12 | Transmission, Pacte Dutreil, DPE, decote IFI |
| M13 | Baremes de reference : PASS, cotisations TNS, kilometrique (integre a `04_formules_et_risques.md`) |
| FORM | 7 formules de calcul + 8 risques critiques |
| M_CGI | 51 articles du Code General des Impots (texte legal, millesime 2026) |

---

## Etat de validation du corpus

**C'est ici qu'on a besoin de vous.** Le corpus est structure et trace, mais n'a pas encore ete relu par des professionnels du chiffre.

| Composant | Volume | Statut |
|-----------|--------|--------|
| Regles metier (`02_golden_rules_claude_first.md`) | 391 | **0 validee** — 391 `candidate_to_validate` |
| Referentiel de parametres chiffres (`referentiel_parametres.json`) | 32 cles | **24 `sourced`** (verifies contre source officielle, avec URL et date) · 8 `candidate_to_validate` |
| Articles CGI (`M_CGI_code_general_impots.md`) | 51 | Texte legal officiel (millesime 2026) |
| Tracabilite regle → source (`07_rule_source_crosswalk.jsonl`) | 391 entrees | Page et document source par regle |
| Cas de test (`08_evaluation_suite.md`) | 45 | Reponses attendues ecrites |

**Vous etes expert-comptable, fiscaliste, CGP, notaire ?** Chaque regle validee (ou corrigee) augmente la valeur du corpus pour tout le monde. Le workflow est simple : une issue GitHub par regle, passage `candidate_to_validate` → `validated` avec votre nom et la date. Voir **[CONTRIBUTING.md](CONTRIBUTING.md)**.

---

## Table des millesimes

| Parametre | 2025 | 2026 | Statut |
|-----------|------|------|--------|
| PASS | 47 100 € | **48 060 €** | `sourced` (arretes JO) |
| Seuil micro-BNC (CGI 102 ter) | 77 700 € | **83 600 €** (triennat 2026-2028) | `sourced` |
| Micro-BIC tourisme non classe (loi Le Meur) | 15 000 € / 30 % | 15 000 € / 30 % | `sourced` |
| Micro-BIC tourisme classe | 77 700 € / 50 % | 77 700 € / 50 % | `sourced` |
| Seuil LMP / Seuil IFI / Deficit foncier | 23 000 € / 1,3 M€ / 10 700 € | inchanges | `sourced` |
| PV immobiliere (IR + PS) | 19 % + 17,2 % | 19 % + 17,2 % | IR `sourced` · PS `candidate_to_validate` |
| Taux URSSAF PL, bareme kilometrique | millesime 2025 | **mise a jour 2026 en attente** | bareme km `sourced` 2025 · taux TNS `candidate_to_validate` |
| CARMF / CARPIMKO (forfaits) | indicatifs 2025 | a verifier sur carmf.fr / carpimko.fr | `candidate_to_validate` |

Source de verite : `knowledge/referentiel_parametres.json` (chaque cle porte sa source officielle, son URL et sa date de verification). **En cas d'ecart entre un texte du corpus et le referentiel, le referentiel prime.** Prochaine mise a jour attendue : janvier (apres la Loi de Finances).

---

## Ce que l'agent ne fait pas

- **Pas de conseil** au sens reglementaire — uniquement des projets d'analyse a faire valider par un professionnel.
- **Pas de teledeclaration** ni d'acces aux comptes, logiciels ou donnees reelles d'un client.
- **Pas de veille automatique** : la base fige a sa date de mise a jour ; les baremes changent a chaque Loi de Finances.
- **Hors scope** (refus explicite) : fiscalite crypto-actifs, TVA intracommunautaire, fiscalite internationale, contentieux LPF.
- Sur ChatGPT : pas d'integration Google Drive (archivage manuel uniquement).

---

## Structure du depot

```
README.md                               <- Ce fichier
CONTRIBUTING.md                         <- Workflow de validation des regles
GUIDE_INSTALLATION.html                 <- Guide detaille (ouvrir dans un navigateur)
.claude/skills/expert-comptable/
  SKILL.md                              <- Skill Claude Code (auto-charge dans ce depot)
  scripts/lookup.py                     <- Extraction ciblee : regles, articles CGI, referentiel
  evals/evals.json                      <- Cas de test du skill
gemini/
  00_INSTRUCTIONS_GEMINI.md             <- System prompt Gemini (avec archivage Drive)
chatgpt/
  00_INSTRUCTIONS_CHATGPT.md            <- System prompt ChatGPT (sans Drive)
knowledge/
  referentiel_parametres.json           <- SOURCE DE VERITE des chiffres (32 cles, sources + millesimes)
  01_decision_engine.md                 <- Moteur decisionnel IF/THEN (10 modules)
  02_golden_rules_claude_first.md       <- 391 regles curatees
  03_few_shots.md                       <- 25 exemples calibres
  04_formules_et_risques.md             <- Formules + risques + baremes M13
  05_agent_governance.md                <- Playbooks + risk matrix
  06_golden_checklists.md               <- Checklists par domaine
  07_rule_source_crosswalk.jsonl        <- Tracabilite regles -> sources PDF
  08_evaluation_suite.md                <- 45 cas de test
  09_agent_manifest.json                <- Metadonnees corpus
  M_CGI_code_general_impots.md          <- 51 articles CGI — texte legal (millesime 2026)
  chatgpt_only/                         <- Fichiers supplementaires ChatGPT uniquement
    10_documents.json                   <- Inventaire documents sources
    M_CGI_code_general_impots.jsonl     <- Version JSONL du CGI (doublon du MD)
scripts/
  archivage_analyses.gs                 <- Script Apps Script (archivage Drive)
```

---

## Installation rapide

### Claude Code (zero installation)

Le skill est versionne dans le depot : **il n'y a rien a installer**.

```bash
git clone https://github.com/joachimpomme-ctrl/comptable.git
cd comptable
claude
```

Ouvrir le depot dans [Claude Code](https://claude.com/claude-code) : le skill `expert-comptable` (`.claude/skills/expert-comptable/`) se declenche automatiquement sur toute question fiscale, comptable ou patrimoniale. Il consulte la base `knowledge/` dans l'ordre prescrit, cite ses sources avec millesime et statut de validation, et utilise un script de lookup pour extraire regles, articles CGI et parametres chiffres sans charger les gros fichiers.

```
Exemples : "Mon client kine a encaisse 80 000 EUR en 2026, peut-il rester au micro-BNC ?"
           "Calcule la PV de cession d'un LMNP au reel, amortissements deduits 40 000 EUR."
```

### Gemini Gems

> Gemini est limite a **10 fichiers** de connaissances. Uploader uniquement les fichiers listes ci-dessous.

1. Ouvrir [gemini.google.com](https://gemini.google.com) > **Mes Gems** > **Nouveau Gem**
2. Copier le contenu de `gemini/00_INSTRUCTIONS_GEMINI.md` dans le champ **Instructions**
3. Remplacer les 2 occurrences de `[VOTRE_FOLDER_ID_DRIVE]` par l'ID de votre dossier Google Drive
4. Uploader ces **10 fichiers** dans **Connaissances** :

| # | Fichier | Pourquoi |
|---|---------|----------|
| 1 | `01_decision_engine.md` | Moteur IF/THEN — coeur du raisonnement |
| 2 | `02_golden_rules_claude_first.md` | 391 regles curatees |
| 3 | `03_few_shots.md` | Calibrage du style de reponse |
| 4 | `04_formules_et_risques.md` | Formules de calcul + risques + baremes M13 |
| 5 | `referentiel_parametres.json` | **Source de verite des chiffres** (32 cles verifiees) |
| 6 | `05_agent_governance.md` | Playbooks + deontologie |
| 7 | `06_golden_checklists.md` | Checklists par domaine |
| 8 | `07_rule_source_crosswalk.jsonl` | Tracabilite regles -> sources |
| 9 | `08_evaluation_suite.md` | Cas de test de reference |
| 10 | `M_CGI_code_general_impots.md` | 51 articles CGI — texte legal (millesime 2026) |

> `09_agent_manifest.json` (metadonnees) et les fichiers de `knowledge/chatgpt_only/` sont exclus de Gemini (limite 10 fichiers) — le referentiel de parametres est prioritaire sur les metadonnees.

5. Activer les outils **Google Drive**, **Google Docs**, **Google Sheets**

### ChatGPT Custom GPT

1. Ouvrir [chatgpt.com](https://chatgpt.com) > **Explorer les GPTs** > **+ Creer** > onglet **Configurer**
2. Copier le contenu de `chatgpt/00_INSTRUCTIONS_CHATGPT.md` dans le champ **Instructions**
3. Uploader les **13 fichiers** de `knowledge/` (les 11 fichiers du dossier + les 2 fichiers de `chatgpt_only/`) dans **Base de connaissances**
4. Activer **Recherche dans la base de connaissances**

**Guide complet :** ouvrez `GUIDE_INSTALLATION.html` dans votre navigateur.

---

## Configuration de l'archivage (Gemini uniquement)

L'agent peut sauvegarder les analyses dans un dossier Google Drive sur demande explicite.

1. Creer un dossier dans Google Drive (ex. `Archive Analyses IA`)
2. Copier son ID depuis l'URL : `drive.google.com/drive/folders/**[ID]**`
3. Remplacer `[VOTRE_FOLDER_ID_DRIVE]` dans les instructions Gemini
4. Optionnel : deployer `scripts/archivage_analyses.gs` dans [Apps Script](https://script.google.com)

---

## Exemples d'utilisation

```
-- Fiscalite --
"Quels sont les seuils du regime micro-BNC en 2025 ? Et pour les revenus 2026 ?"
"Je suis medecin liberal en BNC, CA 150 000 EUR.
 Comparez micro-BNC et regime reel pour ma situation 2025."

-- Declarations --
"Aide-moi a remplir ma declaration 2035 : recettes 120 000 EUR,
 cotisations CARMF 18 000 EUR, loyer cabinet 12 000 EUR."
"Quelles cases renseigner sur la 2044 pour mon deficit foncier ?"
"J'ai vendu un appartement detenu 12 ans, PV brute 80 000 EUR.
 Calcule ma plus-value imposable apres abattements."

-- Optimisation fiscale --
"Quel est mon plafond PER pour 2025 si mes revenus 2024 sont 95 000 EUR ?"
"Quels leviers fiscaux pour reduire mon TMI de 41% en tant que liberal ?"
"Comparez SEL + SPFPL vs exercice individuel pour un chirurgien a 300 000 EUR de CA."

-- Patrimoine --
"Quelle strategie de transmission pour 800 000 EUR de patrimoine,
 2 enfants, TMI 41%, horizon 15 ans ?"

-- Archivage (Gemini uniquement) --
"Enregistre cette analyse dans un Google Doc."
```

---

## Format de reponse

L'agent structure toujours ses reponses :

- **Situation identifiee** — qualification du cas
- **Regles applicables** — ancre legale + millesime + statut de validation
- **Application / calcul** — raisonnement etape par etape, chiffres references au referentiel
- **Points de vigilance** — exceptions, millesimes, risques
- **Sources** — documents et pages de reference
- **Validation requise** — quel professionnel consulter

En debut de session, l'agent rappelle l'etat de validation du corpus (regles non validees, parametres verifies).

---

## Sources et tracabilite

- **Textes legaux** : 51 articles CGI (texte officiel, millesime 2026), references BOFiP et Legifrance dans le referentiel de parametres (`source_url` par cle).
- **Regles metier** : extraites de guides fiscaux professionnels et de sources publiques ; chaque regle est reliee a son document et sa page source via `07_rule_source_crosswalk.jsonl`. Les PDF sources ne sont pas redistribues dans ce depot (droits d'auteur) — l'inventaire complet est dans `knowledge/chatgpt_only/10_documents.json`.
- **Chiffres** : chaque valeur du referentiel porte sa source officielle, son URL et sa date de verification.

---

## Limites

- Les baremes (IR, PASS, seuils micro) changent a chaque Loi de Finances. Verifiez les millesimes (voir [table](#table-des-millesimes)).
- Aucune regle metier n'est encore validee par un professionnel — voir [Etat de validation](#etat-de-validation-du-corpus).
- Hors scope : fiscalite crypto, TVA intracommunautaire, fiscalite internationale, contentieux LPF.
- La base doit etre mise a jour en janvier de chaque annee.
- Sur ChatGPT : pas d'integration Google Drive, archivage manuel uniquement.

---

## Licence

Ce projet est partage a des fins pedagogiques et d'usage personnel (CC BY-NC 4.0).
Les regles metier sont extraites de sources publiques (guides fiscaux, BOFiP, CGI).
Elles ne constituent pas un conseil professionnel.
