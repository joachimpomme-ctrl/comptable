# Agent IA Comptable & Patrimoine

Agent IA specialise en comptabilite, fiscalite des professions liberales, location meublee, gestion financiere et gestion de patrimoine. Fonctionne sur **Claude Code** (skill integre au depot), **Gemini Gems** et **ChatGPT Custom GPT**.

Le depot contient **deux skills Claude complementaires** : `assistant-fiscal-comptable` (regles fiscales et comptables, referentiel source) et `conseiller-patrimoine` (aide a la decision patrimoniale pour un usage personnel, sources de premiere main, calculs). Voir [Deux skills Claude](#deux-skills-claude).

**Page de presentation du projet :** [joachimpomme-ctrl.github.io/comptable](https://joachimpomme-ctrl.github.io/comptable/) — a partager pour presenter le projet en une page.

> ## ⚠️ A lire avant toute utilisation
>
> - **Outil d'aide a la recherche fonde sur des modeles d'IA** (Claude, Gemini, ChatGPT). Ses reponses peuvent etre fausses, incompletes ou perimees, meme quand elles citent une source.
> - **Ce n'est ni une consultation juridique ou fiscale, ni une mission d'expertise comptable, ni un conseil en investissement, en credit ou en assurance.** Exercees pour autrui de facon habituelle, et selon les cas remuneree, ces activites sont reservees a des professionnels habilites (avocats, experts-comptables, notaires, conseillers en investissements financiers, courtiers inscrits a l'ORIAS).
> - **Particuliers :** verifiez sur une source officielle (impots.gouv.fr, Legifrance, BOFiP) ou aupres d'un professionnel avant toute declaration ou decision.
> - **Professionnels :** les sorties sont des brouillons ; les utiliser aupres de vos clients engage votre responsabilite et vos obligations (secret professionnel, devoir de conseil, RGPD). Ne saisissez aucune donnee qui identifie un client. Si vous mettez l'agent a disposition de vos clients, dites-leur qu'ils echangent avec une IA (reglement (UE) 2024/1689, art. 50).
> - **Etat : 0 des 391 regles metier relue par un professionnel** ; les controles de sources ont ete faits par des agents d'IA. Les 38 parametres chiffres du referentiel citent chacun leur source officielle, leur URL et leur date de verification. Voir [Etat de validation du corpus](#etat-de-validation-du-corpus).
> - **Millesimes :** les chiffres verifies couvrent 2025 et 2026 (impot sur les revenus 2025) ; les baremes des revenus 2026 dependent de la LF 2027, non promulguee au 01/11/2026. Voir la [table des millesimes](#table-des-millesimes).

---

## Deux skills Claude

| Skill | Role | Paquet | Documentation |
|-------|------|--------|---------------|
| `assistant-fiscal-comptable` | Fiscalite, comptabilite BNC/BIC, LMNP, revenus fonciers, transmission : regles tracees, referentiel de 38 parametres sources, 63 articles CGI | [`dist/assistant-fiscal-comptable.zip`](dist/assistant-fiscal-comptable.zip) | Ce README |
| `conseiller-patrimoine` | Aide a la decision patrimoniale, usage personnel (pas un conseil en investissement) : ou placer, PEA, assurance-vie, PER, ETF et allocation, credit et capacite d'emprunt, achat-revente, louer ou acheter, retraite, protection du conjoint, charte d'investissement. Va chercher chaque chiffre volatil a sa source officielle et le date, calcule avec ses scripts | [`dist/conseiller-patrimoine.zip`](dist/conseiller-patrimoine.zip) | **[Guide complet : docs/conseiller-patrimoine.md](docs/conseiller-patrimoine.md)** |

Les deux se completent : le conseiller delegue toute question fiscale a `assistant-fiscal-comptable`. Installer les deux pour un usage patrimonial.

### En bref : le skill conseiller-patrimoine

- **Contradicteur, pas vendeur.** Pour chaque decision : au moins deux options plus le statu quo, pire cas chiffre, liquidite, reversibilite, cout complet, contre-argument ecrit, avis conditionnel avec niveau de confiance (sur / probable / hypothese).
- **Information de premiere main.** Carte des sources officielles par sujet (Legifrance, BOFiP, Banque de France, INSEE, HCSF, AMF, ACPR, ORIAS, REGAFI, DIC des emetteurs, fiches d'indices, DVF, info-retraite...). Aucun taux, plafond ou donnee de marche de memoire : valeur, date d'effet, date de consultation et lien.
- **Regles volatiles datees.** `references/01-fraicheur.md` liste l'etat verifie au 01/11/2026 (normes HCSF, calendrier DPE, encadrement des loyers, retraite, prelevements sociaux 2026, MiCA...) avec source, statut et date de reverification.
- **Doctrine referencee.** Une trentaine de resultats de recherche (diversification, couts, gestion active, facteurs, taux de retrait, comportement), chacun marque consensus, debattu ou heuristique ; references controlees par un agent d'IA, sans relecture humaine.
- **Six scripts de calcul testes** (32 tests) : credit et remboursement anticipe, capacite d'emprunt et pret relais, projections et Monte-Carlo, TRI, exposition et reequilibrage, louer ou acheter. Aucun rendement par defaut.
- **Relu par un second agent d'IA** le 01/11/2026 (13 erreurs corrigees avant publication), pas encore par un professionnel.
- **Partageable.** Aucune donnee personnelle. Sans fiche patrimoniale privee, il part d'un profil en dix questions.
- **Pas un conseil reglemente** (ni CIF, ni notaire) : une aide a la decision, a faire valider par le bon professionnel quand l'enjeu le justifie.

---

## A quoi ca sert (pour un professionnel)

Usages concrets en cabinet ou en pratique individuelle : **pre-qualification d'un dossier** (regime, seuils, options applicables), **brouillon de reponse sourcee** a verifier avant envoi, **checklists declaratives** (2035, 2042, 2044, 2048-IMM), **rappel des pieges** (ARD en LMNP, reintegration des amortissements depuis 2025, bascules micro/reel).

Trois questions de demonstration a copier-coller :

```
"Je suis medecin liberal en BNC, CA 150 000 EUR. Comparez micro-BNC et regime reel pour 2025."
"J'ai vendu un appartement detenu 12 ans, PV brute 80 000 EUR. Calcule ma plus-value imposable apres abattements."
"Quels sont les seuils micro-BIC pour un meuble de tourisme non classe, revenus 2025 declares 2026 ?"
```

Pour tester l'agent : `knowledge/08_evaluation_suite.md` contient 45 questions : 12 avec un resultat attendu detaille et chiffre (EV-029 a EV-040), 8 a criteres qualitatifs, 25 qui reprennent les exemples de calibrage fournis a l'agent (11 avec des chiffres attendus) : utiles pour le format, pas pour mesurer la qualite. Les cas EV-029 a EV-040 sont le meilleur point de depart pour un relecteur.

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
| M_CGI | 63 articles du Code General des Impots (texte legal, millesime 2026) |

---

## Etat de validation du corpus

**C'est ici qu'on a besoin de vous.** Le corpus est structure et trace, mais n'a pas encore ete relu par des professionnels du chiffre.

| Composant | Volume | Statut |
|-----------|--------|--------|
| Regles metier (`02_golden_rules_claude_first.md`) | 391 | **0 validee** — 391 `candidate_to_validate` |
| Referentiel de parametres chiffres (`referentiel_parametres.json`) | 38 cles | **38 `sourced`** : source officielle, URL et date pour chacune (passe du 2026-08-26, corrections et ajouts du 2026-11-01) |
| Articles CGI (`M_CGI_code_general_impots.md`) | 63 | Texte legal officiel integral (export Legifrance du 30/10/2026 pour les 30 articles reextraits le 2026-11-01) |
| Tracabilite regle → source (`07_rule_source_crosswalk.jsonl`) | 391 entrees | 358 ancres legales controlees par des agents d'IA (195 confirmees, 46 ancres rectifiees, 74 enonces nuances, 32 enonces corriges, 11 sans trace de verdict) ; 33 enonces de pratique ou de doctrine sans ancre legale (`a_verifier`). Passes du 05/06, du 26/08 et du 01/11/2026. Page du document d'origine : rapprochement automatique, probable |
| Cas de test (`08_evaluation_suite.md`) | 45 | 12 detailles et chiffres, 8 qualitatifs, 25 repris des exemples de calibrage |

**Vous etes expert-comptable, avocat fiscaliste, CGP, notaire ?** Une relecture benevole, par lots d'une vingtaine de regles, fait progresser le corpus pour tout le monde. Elle porte sur l'enonce au millesime indique et n'engage pas votre responsabilite professionnelle. Voir **[CONTRIBUTING.md](CONTRIBUTING.md)**.

**Ce qui reste a faire et ou aider :** voir la **[feuille de route (ROADMAP.md)](ROADMAP.md)** — relecture professionnelle des regles (le controle des ancres par IA couvre 358 regles sur 391), cles de referentiel a ajouter (CARMF, plafonds PER, deficit foncier majore), mise a jour annuelle de janvier, outillage communaute.

---

## Table des millesimes

| Parametre | 2025 | 2026 | Statut |
|-----------|------|------|--------|
| PASS | 47 100 € | **48 060 €** | `sourced` (arretes JO) |
| Seuil micro-BNC (CGI 102 ter) | 77 700 € | **83 600 €** (triennat 2026-2028) | `sourced` |
| Micro-BIC tourisme non classe (loi Le Meur) | 15 000 € / 30 % | 15 000 € / 30 % | `sourced` |
| Micro-BIC tourisme classe, chambres d'hotes, location meublee longue duree | 77 700 € / 50 % | **83 600 € / 50 %** (2026-2028) | `sourced` |
| Micro-BIC fourniture de logement (para-hotellerie, 1° de l'art. 50-0) | 188 700 € / 71 % | **203 100 € / 71 %** (2026-2028) | `sourced` |
| Seuil LMP / Seuil IFI / Deficit foncier | 23 000 € / 1,3 M€ / 10 700 € | inchanges | `sourced` |
| Deficit foncier majore (renovation energetique E/F/G vers A-D) | 21 400 € | 21 400 € jusqu'au 31/12/2027 | `sourced` |
| Bareme IR, premiere tranche (par part) | 11 497 € (revenus 2024) | **11 600 €** (revenus 2025) | `sourced` |
| PFU (IR 12,8 % + prelevements sociaux) | 30 % | **31,4 %** (revenus percus depuis le 01/01/2026) | `sourced` |
| Prelevements sociaux dividendes, interets (annee de perception) | 17,2 % | **18,6 %** | `sourced` |
| Prelevements sociaux location meublee non professionnelle (annee des revenus) | **18,6 %** (revenus 2025) | 18,6 % | `sourced` |
| PV immobiliere (IR + PS) | 19 % + 17,2 % | 19 % + **17,2 % maintenu** (LFSS 2026 : 18,6 % sur la plupart des autres revenus du capital, mais PV immo/fonciers/AV restent a 17,2 %) | `sourced` |
| Taux URSSAF PL (maladie jusqu'a 8,5 % a 3 PASS, CNAVPL T1 **8,73 %**, CSG-CRDS 9,7 %) | 2025 | 2026 | `sourced` pour les cles ; bareme detaille (fichier 04) probable |
| Bareme kilometrique | revenus 2025 : bareme de 2023 reconduit | revenus 2026 : PLF 2027 en discussion | `sourced` |
| CARPIMKO : invalidite-deces / complementaire | 1 022 € / forfait 2 312 € + 3 % | 1 022 € / **8,70 %** (0,5 a 3 PASS) | `sourced` (bulletin CARPIMKO avril 2026) |
| CARMF (medecins) | non reporte | base 8,73 % + 1,87 %, complementaire 11,80 % jusqu'a 3,5 PASS | probable (hors referentiel, a verifier sur carmf.fr) |

Source de verite : `knowledge/referentiel_parametres.json` (chaque cle porte sa source officielle, son URL et sa date de verification). **En cas d'ecart entre un texte du corpus et le referentiel, le referentiel prime.** Prochaine mise a jour attendue : janvier (apres la Loi de Finances).

---

## Ce que l'agent ne fait pas

- **Pas de conseil** au sens reglementaire — uniquement des projets d'analyse a faire valider par un professionnel.
- **Pas de teledeclaration.** La version Gemini peut lire et ecrire dans votre Google Drive si vous activez ces outils ; le skill conseiller-patrimoine peut lire un connecteur bancaire si vous en avez un. Ne saisissez aucune donnee qui identifie un client (nom, adresse, numero fiscal, IBAN) : travaillez sur des cas anonymises. Securite et signalement : [SECURITY.md](SECURITY.md).
- **Pas de veille automatique** : la base fige a sa date de mise a jour ; les baremes changent a chaque Loi de Finances.
- **Hors scope** (refus explicite) : fiscalite crypto-actifs, TVA intracommunautaire, fiscalite internationale, contentieux LPF.
- Sur ChatGPT : pas d'integration Google Drive (archivage manuel uniquement).

---

## Structure du depot

```
README.md                               <- Ce fichier
CONTRIBUTING.md                         <- Workflow de validation des regles
ROADMAP.md                              <- Feuille de route : ce qui reste a faire
CHANGELOG.md                            <- Journal des versions (2026.11.3)
NOTICE.md                               <- Origine des contenus, licences, editeur
GUIDE_INSTALLATION.html                 <- Guide detaille (ouvrir dans un navigateur)
.claude/skills/assistant-fiscal-comptable/
  SKILL.md                              <- Skill Claude Code (auto-charge dans ce depot)
  scripts/lookup.py                     <- Extraction ciblee : regles, articles CGI, referentiel
  evals/evals.json                      <- Cas de test du skill
.claude/skills/conseiller-patrimoine/
  SKILL.md                              <- Skill conseil patrimonial (auto-charge dans ce depot)
  references/                           <- 11 fichiers : sources, fraicheur, doctrine, enveloppes, ETF,
                                           immobilier et credit, retraite, protection, alternatifs,
                                           garde-fous, methode et gabarits
  scripts/                              <- 6 scripts de calcul + tests/test_calculs.py (32 tests)
  evals/                                <- 7 cas d'evaluation (format claude plugin eval)
docs/
  conseiller-patrimoine.md              <- Guide complet du skill conseiller-patrimoine
dist/
  assistant-fiscal-comptable.zip / .skill         <- Paquet autonome assistant-fiscal-comptable
  conseiller-patrimoine.zip / .skill    <- Paquet autonome conseiller-patrimoine
.github/workflows/tests.yml             <- Tests automatiques a chaque push
gemini/
  00_INSTRUCTIONS_GEMINI.md             <- System prompt Gemini (avec archivage Drive)
chatgpt/
  00_INSTRUCTIONS_CHATGPT.md            <- System prompt ChatGPT (sans Drive)
knowledge/
  referentiel_parametres.json           <- SOURCE DE VERITE des chiffres (38 cles, sources + millesimes)
  01_decision_engine.md                 <- Moteur decisionnel IF/THEN (10 modules)
  02_golden_rules_claude_first.md       <- 391 regles curatees
  03_few_shots.md                       <- 25 exemples calibres
  04_formules_et_risques.md             <- Formules + risques + baremes M13
  05_agent_governance.md                <- Playbooks + risk matrix
  06_golden_checklists.md               <- Checklists par domaine
  07_rule_source_crosswalk.jsonl        <- Tracabilite regles -> sources PDF
  08_evaluation_suite.md                <- 45 cas de test
  09_agent_manifest.json                <- Metadonnees corpus
  M_CGI_code_general_impots.md          <- 63 articles CGI — texte legal (millesime 2026)
  chatgpt_only/                         <- Fichiers supplementaires ChatGPT uniquement
    10_documents.json                   <- Inventaire documents sources
    M_CGI_code_general_impots.jsonl     <- Version JSONL du CGI (doublon du MD)
scripts/
  archivage_analyses.gs                 <- Script Apps Script (archivage Drive)
  build_skill_package.py                <- Fabrique les paquets dist/ des deux skills
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

Ouvrir le depot dans [Claude Code](https://claude.com/claude-code) : les deux skills sont charges. Le skill `conseiller-patrimoine` (`.claude/skills/conseiller-patrimoine/`) se declenche sur toute demande d'avis ou d'arbitrage patrimonial. Le skill `assistant-fiscal-comptable` (`.claude/skills/assistant-fiscal-comptable/`) se declenche automatiquement sur toute question fiscale, comptable ou patrimoniale. Il consulte la base `knowledge/` dans l'ordre prescrit, cite ses sources avec millesime et statut de validation, et utilise un script de lookup pour extraire regles, articles CGI et parametres chiffres sans charger les gros fichiers.

```
Exemples : "Mon client kine a encaisse 80 000 EUR en 2026, peut-il rester au micro-BNC ?"
           "Calcule la PV de cession d'un LMNP au reel, amortissements deduits 40 000 EUR."
```

**Sans cloner le depot — paquet pret a l'emploi :** telecharger [`dist/assistant-fiscal-comptable.zip`](dist/assistant-fiscal-comptable.zip) (environ 360 Ko, base de connaissances embarquee), activer l'execution de code dans claude.ai puis importer le zip dans **Settings** > **Capabilities** > **Skills** > **Upload skill**. Les skills demandent une offre Pro, Max, Team ou Enterprise (aide Claude, « Using Skills in Claude »). Un skill importe est prive a votre compte ; dans Claude Code, cloner le depot suffit. **Ancien nom : `expert-comptable`** : si vous aviez importe `expert-comptable.zip`, supprimez ce skill avant d'importer le nouveau. Le paquet se regenere avec `python3 scripts/build_skill_package.py` apres chaque mise a jour du corpus.

**Skill conseiller-patrimoine :** meme procedure avec [`dist/conseiller-patrimoine.zip`](dist/conseiller-patrimoine.zip), en plus d'`assistant-fiscal-comptable`. Activer la recherche web dans Claude : le skill lit les sources officielles en ligne. Mode d'emploi detaille, exemples et maintenance : [docs/conseiller-patrimoine.md](docs/conseiller-patrimoine.md). Les deux paquets se regenerent ensemble avec `python3 scripts/build_skill_package.py` (ou un seul : `python3 scripts/build_skill_package.py conseiller-patrimoine`). Pas de mise a jour automatique : reimporter le zip a chaque nouvelle version.

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
| 5 | `referentiel_parametres.json` | **Source de verite des chiffres** (38 cles sourcees) |
| 6 | `05_agent_governance.md` | Playbooks + deontologie |
| 7 | `06_golden_checklists.md` | Checklists par domaine |
| 8 | `07_rule_source_crosswalk.jsonl` | Tracabilite regles -> sources |
| 9 | `08_evaluation_suite.md` | Cas de test de reference |
| 10 | `M_CGI_code_general_impots.md` | 63 articles CGI — texte legal (millesime 2026) |

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

-- Conseil patrimonial (skill conseiller-patrimoine) --
"J'ai 60 000 EUR disponibles sur mon PEE. On veut acheter
 un appartement d'ici deux ans. Je mets tout sur mon PEA ?"
"Combien peut-on emprunter sur 25 ans avec 7 000 EUR de revenus nets,
 650 EUR de credit locatif et 800 EUR de loyers ?"
"Mon PEA est a 100 % sur un ETF monde. Comment ajouter de l'Europe et
 des emergents sans rien vendre ?"
"Un proche me conseille une SCPI a 6 %. J'y mets 30 000 EUR ?"

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

- **Textes legaux** : 63 articles CGI (texte officiel, millesime 2026), references BOFiP et Legifrance dans le referentiel de parametres (`source_url` par cle).
- **Regles metier** : reformulees a partir de 10 documents, dont un guide fiscal des professions liberales diffuse par Banque Populaire (edition 04/2025, 217 regles sur 391 ; identification probable d'apres le nom du fichier), des guides prives sur la location meublee, la comptabilite liberale et la gestion de patrimoine, un support de formation en gestion de patrimoine et le recueil des normes comptables de l'ANC. **Ces documents ne font pas autorite : seule l'ancre legale citee (CGI, BOFiP, PCG) fait foi.** Ils ne sont pas redistribues ; inventaire dans `knowledge/chatgpt_only/10_documents.json`, details dans [NOTICE.md](NOTICE.md). La page citee au crosswalk vient d'un rapprochement automatique (page probable).
- **Chiffres** : chaque valeur du referentiel porte sa source officielle, son URL et sa date de verification. Les autres chiffres du corpus (exemples, baremes de cotisations) n'ont pas tous ce niveau de tracabilite.
- **Outils** : corpus constitue et controle avec des outils d'IA (Claude, Codex).

---

## Limites

- Les baremes (IR, PASS, seuils micro) changent a chaque Loi de Finances. Verifiez les millesimes (voir [table](#table-des-millesimes)).
- Aucune regle metier n'est encore validee par un professionnel — voir [Etat de validation](#etat-de-validation-du-corpus).
- Hors scope : fiscalite crypto, TVA intracommunautaire, fiscalite internationale, contentieux LPF.
- La base doit etre mise a jour en janvier de chaque annee.
- `conseiller-patrimoine` : aide a la decision, pas un conseil en investissement reglemente (CIF). Ses regles volatiles sont datees du 01/11/2026 et se reverifient avant toute decision ; ses projections dependent d'hypotheses fournies par l'utilisateur. Revue prevue en janvier et en juillet.
- Sur ChatGPT : pas d'integration Google Drive, archivage manuel uniquement.

---

## Licence

Contenu propre au depot : Creative Commons Attribution - Pas d'utilisation commerciale 4.0 International (texte integral dans [LICENSE](LICENSE)). Ce n'est pas une licence « open source » au sens de l'OSI. Les textes du CGI sont reutilises sous Licence Ouverte (Legifrance, DILA) et ne sont pas soumis a la clause non commerciale ; les documents d'origine des regles restent la propriete de leurs auteurs. Details, editeur et contact : [NOTICE.md](NOTICE.md). Rien dans ce depot ne constitue un conseil professionnel.
