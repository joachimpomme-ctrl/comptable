# Agent IA Comptable & Patrimoine

Agent IA specialise en comptabilite, fiscalite des professions liberales, location meublee, gestion financiere et gestion de patrimoine. Fonctionne sur **Gemini Gems** et **ChatGPT Custom GPT**.

> **Avertissement :** Cet agent ne remplace pas un professionnel. Toutes les regles sont des candidats a valider (`candidate_to_validate`). Ne prenez jamais de decision fiscale ou patrimoniale importante sur la seule base de ses reponses.

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
| FORM | 7 formules de calcul + 8 risques critiques |
| M_CGI | 44 articles du Code General des Impots (texte legal, millesime 2026) |

---

## Structure du depot

```
README.md                               <- Ce fichier
GUIDE_INSTALLATION.html                 <- Guide detaille (ouvrir dans un navigateur)
gemini/
  00_INSTRUCTIONS_GEMINI.md             <- System prompt Gemini (avec archivage Drive)
chatgpt/
  00_INSTRUCTIONS_CHATGPT.md            <- System prompt ChatGPT (sans Drive)
knowledge/
  01_decision_engine.md                 <- Moteur decisionnel IF/THEN (10 modules)
  02_golden_rules_claude_first.md       <- 359 regles curatees
  03_few_shots.md                       <- 27 exemples calibres
  04_formules_et_risques.md             <- Formules + risques critiques
  05_agent_governance.md                <- Playbooks + risk matrix
  06_golden_checklists.md               <- Checklists par domaine
  07_rule_source_crosswalk.jsonl        <- Tracabilite regles -> sources PDF
  08_evaluation_suite.md                <- 28 cas de test
  09_agent_manifest.json                <- Metadonnees corpus
  M_CGI_code_general_impots.md          <- 44 articles CGI — texte legal (millesime 2026)
  chatgpt_only/                         <- Fichiers supplementaires ChatGPT uniquement
    10_documents.json                   <- Inventaire documents sources
    M_CGI_code_general_impots.jsonl     <- Version JSONL du CGI (doublon du MD)
scripts/
  archivage_analyses.gs                 <- Script Apps Script (archivage Drive)
```

---

## Installation rapide

### Gemini Gems

> Gemini est limite a **10 fichiers** de connaissances. Uploader uniquement les fichiers listes ci-dessous.

1. Ouvrir [gemini.google.com](https://gemini.google.com) > **Mes Gems** > **Nouveau Gem**
2. Copier le contenu de `gemini/00_INSTRUCTIONS_GEMINI.md` dans le champ **Instructions**
3. Remplacer les 2 occurrences de `[VOTRE_FOLDER_ID_DRIVE]` par l'ID de votre dossier Google Drive
4. Uploader ces **10 fichiers** dans **Connaissances** :

| # | Fichier | Pourquoi |
|---|---------|----------|
| 1 | `01_decision_engine.md` | Moteur IF/THEN — coeur du raisonnement |
| 2 | `02_golden_rules_claude_first.md` | 359 regles curatees |
| 3 | `03_few_shots.md` | Calibrage du style de reponse |
| 4 | `04_formules_et_risques.md` | Formules de calcul + risques |
| 5 | `05_agent_governance.md` | Playbooks + deontologie |
| 6 | `06_golden_checklists.md` | Checklists par domaine |
| 7 | `07_rule_source_crosswalk.jsonl` | Tracabilite regles -> sources |
| 8 | `08_evaluation_suite.md` | Cas de test de reference |
| 9 | `M_CGI_code_general_impots.md` | 44 articles CGI — texte legal |
| 10 | `09_agent_manifest.json` | Metadonnees corpus |

> Les fichiers du sous-dossier `knowledge/chatgpt_only/` sont exclus de Gemini (hors limite 10 fichiers).
> Sur **ChatGPT** (sans limite stricte), uploader les 12 fichiers.

5. Activer les outils **Google Drive**, **Google Docs**, **Google Sheets**

### ChatGPT Custom GPT

1. Ouvrir [chatgpt.com](https://chatgpt.com) > **Explorer les GPTs** > **+ Creer** > onglet **Configurer**
2. Copier le contenu de `chatgpt/00_INSTRUCTIONS_CHATGPT.md` dans le champ **Instructions**
3. Uploader les **12 fichiers** du dossier `knowledge/` dans **Base de connaissances**
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
"Quels sont les seuils du regime micro-BNC en 2025 ?"
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
- **Regles applicables** — IDs de regles + statut de validation
- **Application / calcul** — raisonnement etape par etape
- **Points de vigilance** — exceptions, millesimes, risques
- **Sources** — documents et pages de reference
- **Validation requise** — quel professionnel consulter

---

## Limites

- Les baremes (IR, PASS, seuils micro) changent a chaque Loi de Finances. Verifiez les millesimes.
- Hors scope : fiscalite crypto, TVA intracommunautaire, fiscalite internationale.
- La base doit etre mise a jour en janvier de chaque annee.
- Sur ChatGPT : pas d'integration Google Drive, archivage manuel uniquement.

---

## Licence

Ce projet est partage a des fins pedagogiques et d'usage personnel.
Les regles metier sont extraites de sources publiques (guides fiscaux, BOFiP, CGI).
Elles ne constituent pas un conseil professionnel.
