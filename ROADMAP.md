# Feuille de route

Etat des lieux honnete de ce qui reste a faire, par ordre de valeur. Les contributions sont bienvenues sur chaque point — voir [CONTRIBUTING.md](CONTRIBUTING.md).

Derniere mise a jour : 2026-08-26.

---

## 1. Le chantier principal : sourcer puis faire valider les 391 regles

C'est la ou se joue la credibilite du corpus.

| Etape | Etat | Qui |
|-------|------|-----|
| Ancres legales verifiees (crosswalk) | **21 / 391 `sourced`** — 370 `a_verifier` | Sourcing IA par lots (verification de chaque regle contre Legifrance/BOFiP), module par module : M2 fiscalite liberale et M5 LMNP en priorite |
| Regles validees par un professionnel | **0 / 391** | Experts-comptables, fiscalistes, CGP, notaires — une issue par regle (`[VALIDATION]` / `[CORRECTION]`) |

Le sourcing IA etablit qu'une regle correspond au texte ; la validation professionnelle engage un nom sur son application. Les deux niveaux restent distincts et affiches.

## 2. Referentiel : cles a ajouter (mises en evidence par la passe du 2026-08-26)

- **PFU / prelevements sociaux sur les revenus du capital** : la LFSS 2026 porte la CSG a 10,6 % (total 18,6 %) sur la plupart des revenus du capital → clés `ps_revenus_capital` et `pfu_taux` (~31,4 % en 2026) a creer et sourcer. Aujourd'hui signale « hors referentiel, a sourcer » dans le moteur decisionnel.
- **CARMF (medecins)** : forfaits annuels a capturer sur carmf.fr (meme traitement que CARPIMKO).
- **Reforme CARPIMKO 2026** : confirmer la complementaire proportionnelle 8,70 % (0,5–3 PASS) et l'ASV sur le bulletin officiel, puis promouvoir.
- **Bareme kilometrique 2026** et **taux URSSAF 2026 detailles** : publies par arrete en debut d'annee — voir §4.
- Candidats suivants : plafonds PER (calcul complet), CEHR/CDHR, PEA, taux IS, abattement AV apres 70 ans (30 500 €) — cites dans le corpus sans cle de referentiel.

## 3. Corpus et tests

- **Etoffer la suite d'evaluation** (45 cas) : ajouter des cas sur les nouveautes 2026 (seuil micro-BNC 83 600 €, PS 17,2 % vs 18,6 %, CNAVPL 8,73 %, chambres d'hotes 2°) et des cas pieges proposes par les relecteurs (`[CAS DE TEST]`).
- **Elargir le corpus CGI** si l'usage le justifie (art. 787 B en detail, 199 sexdecies, 244 bis A...) — en restant dans le perimetre declare.
- **Few-shots** : ajouter 2-3 exemples calibres sur le millesime 2026.

## 4. Processus recurrent : la mise a jour de janvier

A chaque Loi de Finances / LFSS (checklist a derouler, idealement en fevrier apres publication) :

1. PASS, bareme IR, seuils micro, plafonds PER, baremes kilometriques, taux URSSAF (arretes + LF/LFSS).
2. Mettre a jour `knowledge/referentiel_parametres.json` (valeurs + `verifie_le` + `valable_jusqu_au`).
3. Repercuter dans le moteur decisionnel (module J), les baremes M13 et le README (table des millesimes).
4. Rejouer la suite d'evaluation, reconstruire le paquet (`python3 scripts/build_skill_package.py`), committer `dist/`.
5. Prevenir les utilisateurs du skill installe : ils doivent re-importer le zip (pas de mise a jour automatique).

## 5. Outillage communaute

- **Modeles d'issues GitHub** (`.github/ISSUE_TEMPLATE/`) pre-remplis pour `[VALIDATION]`, `[CORRECTION]`, `[REFERENTIEL]`, `[CAS DE TEST]`, `[BUG REPONSE]` — abaisse encore la barriere pour les non-techniciens.
- **Controles automatiques a chaque push** (GitHub Action) : JSON valides, comptes coherents (391/51/45/32) entre README, manifest et fichiers reels, absence de donnees personnelles, paquet `dist/` a jour.
- **Compteur de validation auto-genere** : script qui lit les statuts des regles et met a jour le tableau « Etat de validation » du README.
- **Releases GitHub versionnees** (ex. `v2026-08`) avec changelog, pour que les utilisateurs sachent quelle version de la base ils ont installee.

## 6. Diffusion

- Verifier que GitHub Pages est actif (Settings → Pages → main, racine) : [page de presentation](https://joachimpomme-ctrl.github.io/comptable/).
- Le cas echeant : article court de presentation, partage aux ordres/associations professionnelles interessees.

---

## Ce qui ne changera pas

- `validated` reste reserve aux professionnels identifies — jamais auto-attribue par une IA.
- Aucun chiffre sans source ; le referentiel prime sur les textes du corpus.
- Les limites restent affichees en premier (README, page, premiere reponse de l'agent).
