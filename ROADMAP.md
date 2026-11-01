# Feuille de route

Etat des lieux honnete de ce qui reste a faire, par ordre de valeur. Les contributions sont bienvenues sur chaque point — voir [CONTRIBUTING.md](CONTRIBUTING.md).

Derniere mise a jour : 2026-08-26.

---

## 1. Le chantier principal : sourcer puis faire valider les 391 regles

C'est la ou se joue la credibilite du corpus.

| Etape | Etat | Qui |
|-------|------|-----|
| Ancres legales verifiees (crosswalk) | **379 / 391 `sourced`** — CHANTIER TERMINE le 2026-08-26 (373 regles verifiees en 2 passes : 15 corrigees, 90 precisees, 41 ancres precisees). Les 12 restantes sont des enonces de pratique/doctrine sans texte officiel verifiable | Re-verification annuelle lors de la mise a jour de janvier ; validation professionnelle par issues |
| Regles validees par un professionnel | **0 / 391** | Experts-comptables, fiscalistes, CGP, notaires — une issue par regle (`[VALIDATION]` / `[CORRECTION]`) |

Le sourcing IA etablit qu'une regle correspond au texte ; la validation professionnelle engage un nom sur son application. Les deux niveaux restent distincts et affiches.

## 2. Referentiel : cles a ajouter (mises en evidence par la passe du 2026-08-26)

- **Fait le 2026-11-01** : cles `pfu_taux_global`, `ps_produits_placement`, `ps_revenus_patrimoine`, `ps_revenus_fonciers_av_epargne_logement` (LFSS 2026) ; seuils micro-BIC 2026 corriges.
- **Fait le 2026-11-01 (lot 2)** : CARPIMKO (`carpimko_invalidite_deces_forfait`, `carpimko_complementaire_taux`, bulletin d'avril 2026), `deficit_foncier_plafond_renovation_energetique` ; baremes REF-002 a REF-006 refaits.
- **CARMF (medecins)** : taux 2026 repris de Weblex (probable) dans REF-003, a confirmer sur carmf.fr puis a passer en cles.
- **Bareme kilometrique 2026** et **taux URSSAF 2026 detailles** : publies par arrete en debut d'annee — voir §4.
- Candidats suivants : plafonds PER (calcul complet), CEHR/CDHR, PEA, taux IS, abattement AV apres 70 ans (30 500 €) — cites dans le corpus sans cle de referentiel.

## 3. Corpus et tests

- **Etoffer la suite d'evaluation** (45 cas) : ajouter des cas sur les nouveautes 2026 (seuil micro-BNC 83 600 €, PS 17,2 % vs 18,6 %, CNAVPL 8,73 %, chambres d'hotes 2°) et des cas pieges proposes par les relecteurs (`[CAS DE TEST]`).
- **Corpus CGI** : 12 articles ajoutes le 2026-11-01 (50-0, 150 VC, 200 A, 219, 223 sexies, 224, 293 B, 757 B, 790 A bis, 968, 977, 1609 nonies G). Suivants possibles : 790 E et 790 F (donations entre epoux et partenaires), 199 sexdecies, 244 bis A. Outil : `scripts/extraire_articles_cgi.py` sur un export PDF Legifrance.
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
- **Controles automatiques a chaque push** (GitHub Action) : JSON valides, comptes coherents (391/63/45/38), aucun article CGI coupe, tests du script de lookup entre README, manifest et fichiers reels, absence de donnees personnelles, paquet `dist/` a jour.
- **Compteur de validation auto-genere** : script qui lit les statuts des regles et met a jour le tableau « Etat de validation » du README.
- **Releases GitHub versionnees** (ex. `v2026-08`) avec changelog, pour que les utilisateurs sachent quelle version de la base ils ont installee.

## 6. Diffusion

- Verifier que GitHub Pages est actif (Settings → Pages → main, racine) : [page de presentation](https://joachimpomme-ctrl.github.io/comptable/).
- Le cas echeant : article court de presentation, partage aux ordres/associations professionnelles interessees.

---

## 7. Skill conseiller-patrimoine

Premiere version publiee le 2026-11-01 (guide : [docs/conseiller-patrimoine.md](docs/conseiller-patrimoine.md)).

| Chantier | Etat |
|----------|------|
| Regles volatiles verifiees et datees (`references/01-fraicheur.md`) | Fait au 2026-11-01 ; reverifier en janvier et juillet |
| Relecture independante par un agent | Faite le 2026-11-01 : 13 erreurs corrigees |
| Relecture par des professionnels (CGP, CIF, notaires, courtiers) | **A faire** : priorite sur `01-fraicheur.md`, `03-enveloppes.md`, `05-immobilier-credit.md`, `07-protection-transmission.md` |
| Executer les 7 cas d'evaluation avec et sans skill (`claude plugin eval`) | **A faire** |
| Echeances a suivre | Encadrement des loyers (vote de l'Assemblee annonce le 19/11/2026) ; projet de loi logement (DPE) ; decrets du statut du bailleur prive ; mesures retraite apres 2027 |
| Lignes « probables » a confirmer sur le texte officiel | Prelevements sociaux 2026 (location meublee), assouplissements HCSF de decembre 2023, PER 2026, frais du PEA |
| Enrichissements possibles | Module investissement locatif detaille (rentabilite, fiscalite via expert-comptable), suivi de performance du portefeuille, gabarit de charte en document partageable |

---

## Ce qui ne changera pas

- `validated` reste reserve aux professionnels identifies — jamais auto-attribue par une IA.
- Aucun chiffre sans source ; le referentiel prime sur les textes du corpus.
- Les limites restent affichees en premier (README, page, premiere reponse de l'agent).
