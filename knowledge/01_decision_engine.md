# MOTEUR DÉCISIONNEL GLOBAL
## Knowledge Base Comptable · Financière · Patrimoniale

**Version :** 1.0 — 2026-05-11
**Portée :** Tous modules M1-M8 (BNC, fiscalité PL, PCG, location meublée, patrimoine, CGP, bases compta)
**Format :** IF / ALORS / SINON / EFFET / ATTENTION
**Usage agent IA :** Ce moteur sert de raisonnement structuré avant toute réponse. L'agent parcourt les arbres concernés, identifie le cas, puis cite la règle source (id JSONL).

---

## MODULE A — RÉGIME D'IMPOSITION BNC (Professions libérales)

### A1 — Choix du régime BNC

- **SI** CA annuel HT ≤ 77 700 €
  - **ALORS** régime micro-BNC possible
  - **EFFET** abattement forfaitaire 34 % sur recettes → revenu imposable = CA × 66 %
  - **DÉCLARATIONS** 2042 C PRO uniquement
  - **MAIS** cotisations PER non déductibles du revenu catégoriel BNC (seulement du revenu global)
- **SI** CA annuel HT > 77 700 € **OU** option pour le réel exercée
  - **ALORS** déclaration contrôlée obligatoire
  - **EFFET** déduction des charges réelles + amortissements éventuels
  - **DÉCLARATIONS** 2035 + 2035 A/B + 2042 C PRO
  - **OPTION** exercée avant la date limite de déclaration des revenus N-1; valable 1 an, tacite reconduction
- **SI** contribuable en micro-BNC souhaite basculer au réel
  - **ALORS** option avant la date limite de dépôt de la déclaration des revenus de l'année précédente (mai/juin)
- **SOURCE** GFPL-049 à GFPL-056, M2

### A2 — PER et professionnel libéral BNC

- **SI** professionnel libéral au réel BNC
  - **ALORS** cotisations PER déductibles du BNC (charge de l'année de paiement) ET mention sur la 2035
  - **ET** déductibles du revenu global jusqu'à épuisement du plafond global
  - **STRATÉGIE** utiliser d'abord le plafond BNC (réduit le RFR) avant le plafond global
- **SI** professionnel libéral au micro-BNC
  - **ALORS** cotisations PER NON déductibles du revenu catégoriel
  - **MAIS** déductibles du revenu global uniquement
- **SI** versement volontaire PER avec renonciation à la déduction
  - **ALORS** choix irrévocable au moment du versement
- **SEUIL** PASS 2025 = 47 100 € [referentiel: PASS/2025]
- **SOURCE** GFPL-165 à GFPL-174, M2

### A3 — TVA des professions libérales

- **SI** profession médicale/paramédicale, transports sanitaires, assurance/courtage, certaines formations agréées
  - **ALORS** hors champ TVA → pas de déclaration
- **SI** autres professions libérales (architecture, conseil, expertise comptable, juridique, artistique)
  - **ALORS** soumises à TVA
  - **SI** CA < 37 500 € (seuil de base) ET CA N-1 < 37 500 €
    - **ALORS** franchise en base — mention obligatoire: "TVA non applicable — art. 293 B du CGI"
    - **ATTENTION** réforme abaissement à 25 000 € suspendue jusqu'au 1er juin 2025
  - **SI** CA entre 37 500 € et 41 250 € en N avec CA N-1 < 37 500 €
    - **ALORS** franchise applicable jusqu'au 31/12/N; assujettissement au 01/01/N+1
  - **SI** CA > 41 250 € en cours d'année
    - **ALORS** assujettissement dès le 1er jour du mois de dépassement
  - **SI** CA entre 25 000 € et 254 000 € ET TVA annuelle < 15 000 €
    - **ALORS** régime réel simplifié (2 acomptes: juillet + décembre; déclaration annuelle 3517-S-SD)
  - **SI** CA > 254 000 € OU TVA annuelle > 15 000 €
    - **ALORS** régime réel normal (déclaration mensuelle CA3)
  - **SI** TVA annuelle < 4 000 €
    - **ALORS** option déclaration trimestrielle admise
- **SOURCE** GFPL-063 à GFPL-081, M2

---

## MODULE B — LOCATION MEUBLÉE (LMP / LMNP)

### B1 — Qualification LMP vs LMNP

- **SI** recettes annuelles foyer fiscal > 23 000 €
  **ET** ces recettes > revenus professionnels du foyer fiscal (T&S nets + BIC hors LM + BNC + BA + art. 62)
  - **ALORS** statut LMP (Loueur Meublé Professionnel)
  - **EFFETS** déficits imputables sur revenu global (illimité); PV régime professionnel; affiliation SSI
- **SINON** (l'une des 2 conditions non remplie)
  - **ALORS** statut LMNP (Loueur Meublé Non Professionnel)
  - **EFFETS** déficits reportables sur BIC LMNP uniquement (10 ans); PV régime particuliers
- **ATTENTION** appréciations à l'année civile; inscription RCS non requise depuis 01/01/2020
- **SOURCE** LMN-003, LMN-004, M5

### B2 — Régime fiscal micro-BIC vs réel (revenus 2025, déclarés 2026)

| Type de location | Micro-BIC si CA < | Abattement | Réel simplifié |
|---|---|---|---|
| Meublés tourisme CLASSÉS + chambres d'hôtes | 77 700 € | 50 % | 77 700 €–840 000 € |
| Meublés tourisme NON classés | 15 000 € | 30 % | > 15 000 € |
| Autres (résidence principale, EHPAD, etc.) | 77 700 € | 50 % | 77 700 €–254 000 € |
| Réel normal | — | — | > 840 000 € (classé) ou > 254 000 € (autres) |

- **SI** CA dépasse le seuil micro deux années de suite (N-2 et N-1)
  - **ALORS** basculement réel de plein droit
- **SI** micro-BIC
  - **ALORS** résultat toujours positif (pas de déficit), pas de liasse fiscale, RIOGA supprimée pour 2025
- **SI** réel BIC
  - **ALORS** déduction charges réelles + amortissements; FEC obligatoire si comptabilité informatisée
- **ATTENTION** revenus 2024 déclarés 2025: anciens seuils (188 700 €/71 % classés, 77 700 €/50 % non classés)
- **SOURCE** LMN-005, LMN-006, LMN-007, M5

### B3 — Amortissements et article 39-C CGI (réel BIC uniquement)

- **SI** bien loué en meublé au réel BIC
  - **ALORS** amortissement par composants obligatoire (terrain non amortissable)
  - **LIMITE** amortissement déductible ≤ Loyers acquis − Charges hors amortissements
  - **SI** résultat cette limite est dépassé
    - **ALORS** excédent d'amortissement = DIFFÉRÉ (non perdu), reportable sur bénéfices futurs
  - **SI** bien LMNP vendu avec ARD en stock
    - **ALORS** ARD définitivement perdus à la cession
  - **SI** bien LMP vendu avec ARD en stock
    - **ALORS** ARD majorent la VNC → réduisent la plus-value fiscale
- **SOURCE** LMN-011, LMN-012, M5

### B4 — Gestion des déficits

- **SI** statut LMP
  - **ALORS** déficit imputable sur revenu global SANS LIMITE; report global sur 6 ans si revenu global insuffisant
- **SI** statut LMNP
  - **ALORS** déficit reportable UNIQUEMENT sur BIC LMNP des 10 années suivantes
  - **ATTENTION** ne peut pas s'imputer sur salaires, BNC, BIC professionnels
- **SI** passage LMNP → LMP
  - **ALORS** déficits LMNP antérieurs ni imputables ni reportables en LMP
- **SOURCE** LMN-014, LMN-015, M5

### B5 — Plus-values LMNP (régime particuliers)

- **SI** cession sous statut LMNP (apprécié l'année de la cession)
  - **ALORS** régime PV des particuliers
  - **CALCUL (depuis 2025)** PV = Prix vente − (Prix acquisition − Amortissements déduits pendant la détention)
  - **CALCUL (avant 2025)** PV = Prix vente − Prix acquisition (amortissements ignorés)
  - **ABATTEMENTS IR:** 0 % (0–5 ans), 6 %/an (6–21 ans), 4 % (22ème), exonération IR > 22 ans
  - **ABATTEMENTS PS:** 0 % (0–5 ans), 1,65 %/an (6–21 ans), 1,6 % (22ème), 9 %/an (23–30 ans), exonération PS > 30 ans
  - **TAUX** 19 % IR + 17,2 % PS (sur base après abattements); taxe supplémentaire si PV > 50 000 €
- **SOURCE** LMN-022, LMN-023, M5

### B6 — Plus-values LMP (régime professionnel)

- **SI** cession sous statut LMP
  - **ALORS** PV professionnelle = Prix vente − VNC (valeur d'origine − amortissements DÉDUITS, hors ARD)
  - **SI** bien détenu < 2 ans → PV court terme (IR barème progressif)
  - **SI** bien détenu > 2 ans → PV CT dans la limite des amortissements déduits + PV LT au-delà (12,8 % + 17,2 % PS)
  - **EXONÉRATIONS possibles** (activité ≥ 5 ans):
    - Art. 151 septies: totale si recettes moy. < 90 000 € (250 000 € tourisme classé); partielle jusqu'à 126 000 €
    - Art. 151 septies B: abattement 10 %/an sur PV LT immo au-delà de 5 ans (exo totale à 15 ans)
    - Art. 238 quindecies: totale si cession < 500 000 € (hors immeubles); partielle jusqu'à 1 000 000 €
    - Art. 151 septies A: exonération totale si départ retraite dans 2 ans avant/après (hors immeubles)
- **SOURCE** LMN-024, LMN-025, M5

### B7 — TVA en location meublée

- **SI** location meublée standard (longue durée, saisonnière sans services)
  - **ALORS** EXONÉRÉE de TVA (art. 261-D-4° CGI)
- **SI** prestation para-hôtelière (durée < 30 nuits + ≥ 3 des 4 services: petit-déjeuner, nettoyage régulier, linge, accueil)
  - **ALORS** SOUMISE à TVA — taux 10 % hébergement / 20 % parking / 5,5 % EHPAD
  - **SI** CA < 85 000 € (seuil franchise depuis jan 2025)
    - **ALORS** franchise en base applicable
  - **SI** CA entre 85 000 € et 93 500 €
    - **ALORS** franchise applicable jusqu'à fin N; assujettissement au 01/01/N+1
  - **SI** CA > 93 500 €
    - **ALORS** déchéance franchise dès le 1er jour du mois de dépassement
- **SOURCE** LMN-016, LMN-017, M5

### B8 — Cotisations sociales en location meublée

- **SI** recettes de courte durée ≤ 23 000 € ET statut LMNP
  - **ALORS** prélèvements sociaux 17,2 % uniquement (pas de cotisations sociales)
- **SI** recettes courte durée > 23 000 € OU statut LMP
  - **ALORS** affiliation SSI obligatoire
  - **ABATTEMENTS** 60 % (courte durée standard) ou 87 % (tourisme classé) sur les recettes
  - **EXCEPTION** gestion déléguée à un professionnel de l'immobilier → PS uniquement même si > 23 000 €
- **SOURCE** LMN-020, LMN-021, M5

---

## MODULE C — IMPÔT SUR LE REVENU ET PRÉLÈVEMENTS SOCIAUX

### C1 — Barème IR 2024 (déclaré 2025)

| Tranche | TMI |
|---|---|
| ≤ 11 497 € | 0 % |
| 11 498 € – 29 315 € | 11 % |
| 29 316 € – 83 823 € | 30 % |
| 83 824 € – 180 294 € | 41 % |
| > 180 295 € | 45 % |

- **QUOTIENT FAMILIAL** avantage fiscal plafonné à 1 791 € par demi-part
- **DÉCLARATION AUTOMATIQUE** possible si revenus intégralement déclarés par tiers (mais nécessaire pour PFU→barème ou crédits d'impôt)
- **SOURCE** GFPL-105 à GFPL-115, M2

### C2 — PFU (Flat Tax) vs barème progressif sur revenus financiers

- **SI** dividendes, intérêts, PV mobilières, gains assurance-vie
  - **ALORS** PFU de 12,8 % + PS 17,2 % = 30 % par défaut
  - **OPTION** barème progressif possible (option globale sur tous les revenus financiers de l'année)
  - **SI** option barème + dividendes → abattement 40 % sur les dividendes
  - **SI** TMI ≤ 11 % → option barème avantageuse
  - **SI** TMI ≥ 30 % → PFU généralement plus avantageux

### C3 — Prélèvements sociaux 2025

| Assiette | CSG | CRDS | Prélèvement solidarité | TOTAL |
|---|---|---|---|---|
| Revenus du patrimoine (placements, loyers, PV) | 9,2 % | 0,5 % | 7,5 % | **17,2 %** |
| Revenus d'activité (BNC, salaires) | 9,2 % | 0,5 % | — | **9,7 %** |

- **SOURCE** GFPL-155 à GFPL-159, M2

### C4 — CEHR (Contribution Exceptionnelle sur les Hauts Revenus)

- **SI** RFR > 250 000 € (célibataire) OU > 500 000 € (imposition commune)
  - **ALORS** CEHR due
  - **BARÈME célibataire** 3 % de 250 001 € à 500 000 € / 4 % au-delà
  - **BARÈME couple** 3 % de 500 001 € à 1 000 000 € / 4 % au-delà
- **SOURCE** GFPL-142 à GFPL-145, M2

### C5 — CDHR (Contribution Différentielle sur les Hauts Revenus, revenus 2025 uniquement)

- **SI** RFR retraité > 250 000 € (célibataire) OU > 500 000 € (couple)
  **ET** IR + CEHR < 20 % du RFR retraité
  - **ALORS** CDHR = 20 % × RFR retraité − (IR + CEHR)
  - **ACOMPTE** 95 % du montant estimé à verser entre le 1er et le 15 décembre 2025
  - **PÉNALITÉ** 20 % si défaut/retard ou acompte insuffisant de > 20 %
- **SOURCE** GFPL-146 à GFPL-154, M2

---

## MODULE D — PLUS-VALUES PROFESSIONNELLES (BNC)

### D1 — Qualification CT vs LT

- **SI** élément amortissable détenu < 2 ans → PV court terme
- **SI** élément amortissable détenu > 2 ans → PV CT dans la limite des amortissements déduits + PV LT au-delà
- **SI** élément NON amortissable détenu > 2 ans → PV long terme
- **PV CT** intégrée au résultat imposable (barème IR); étalement possible sur 3 ans (option)
- **PV LT** 12,8 % IR + 17,2 % PS = 30 %
- **SOURCE** GFPL-082 à GFPL-094, M2

### D2 — Exonérations (activité ≥ 5 ans)

- **Art. 151 septies** (exonération recettes):
  - **SI** recettes moy. (prestations de services) < 90 000 € → exonération TOTALE (IR + PS)
  - **SI** recettes moy. entre 90 000 € et 126 000 € → exonération PARTIELLE et dégressive
- **Art. 151 septies A** (départ à la retraite):
  - **SI** cessation de fonctions + retraite dans les 24 mois avant ou après la cession
  - **ALORS** exonération IR sur PV CT + LT / PS 17,2 % maintenus
- **Art. 238 quindecies** (cession d'entreprise):
  - **SI** prix cession ≤ 500 000 € → exonération TOTALE (IR + PS)
  - **SI** prix entre 500 000 € et 1 000 000 € → exonération PARTIELLE
- **SOURCE** GFPL-095 à GFPL-104, M2

---

## MODULE E — COMPTABILITÉ BNC (Obligations et choix)

### E1 — Obligations comptables BNC (déclaration contrôlée)

- **DOCUMENTS OBLIGATOIRES** livre-journal recettes/dépenses + registre des immobilisations et amortissements
- **TENUE** chronologique, sans rature, sans blanc, justifiée par pièce
- **RECETTES** comptabilisées à l'ENCAISSEMENT (date de réception du chèque / inscription crédit / échéance traite)
- **DÉPENSES** comptabilisées au DÉCAISSEMENT (date remise chèque / paiement espèces / débit virement / carte bancaire)
- **SI** carte bancaire à débit différé → date du PAIEMENT par carte (non date du relevé)
- **SOURCE** bnc_004 à bnc_010, M1

### E2 — Déductibilité des dépenses BNC

- **CONDITION** dépense nécessitée par l'exercice de la profession ET exposée dans l'intérêt direct de l'exploitation
- **SI** dépense mixte (pro + perso) → déduire seulement la quote-part professionnelle
- **SI** frais kilométriques → barème fiscal (suivi précis km professionnels obligatoire)
- **SI** blanchissage à domicile → forfait calculable sur tarifs blanchisseurs (conserver le détail)
- **PIÈCES JUSTIFICATIVES** date + fournisseur + nature + montant + HT/TVA/TTC
- **CONSERVATION** 6 ans (fiscal) / 10 ans (comptable)
- **SOURCE** bnc_013 à bnc_017, M1

### E3 — FEC et comptabilité informatisée

- **SI** comptabilité informatisée → FEC obligatoire (norme A47 A-1 LPF)
- **ATTENTION** un simple tableur Excel ne satisfait PAS à cette exigence → utiliser un logiciel comptable FEC-compatible
- **SANCTION** 5 000 € ou 10 % des droits rappelés (si montant plus élevé) par exercice contrôlé
- **SOURCE** bnc_025, bnc_026, M1

### E4 — Immobilisations vs charges (BIC location meublée)

- **SI** montant unitaire ≤ 500 € HT → charge déductible immédiatement
- **SI** montant unitaire > 500 € HT → immobilisation obligatoire (amortissement)
- **EXCEPTION** premier achat de mobilier meublant → toujours immobilisation quel que soit le montant
- **FRAIS D'ACQUISITION** au choix: immobilisés (ajout au coût) OU déduits en charges — option irrévocable
- **SOURCE** LMN-008, LMN-009, M5

---

## MODULE F — PATRIMOINE ET TRANSMISSION

### F1 — Choix du régime matrimonial selon situation

| Situation | Régime recommandé | Raison |
|---|---|---|
| Professions libérale/commerciale/artisanale | Séparation de biens | Protection des dettes professionnelles |
| Enfants d'unions précédentes | Séparation de biens | Protection des héritiers |
| Couple sans risques professionnels | Communauté réduite aux acquêts | Solidarité + simplicité |
| Souhait maximiser protection conjoint | Communauté universelle + clause d'attribution intégrale | Transmission totale hors succession |

- **SI** changement de régime matrimonial → acte notarié (accord des enfants majeurs si après leur majorité)
- **SOURCE** PAT-001, PAT-002, PAT-003, M6

### F2 — Protection du conjoint survivant (outils par efficacité)

1. **Donation entre époux** (donation au dernier vivant): options conjoint survivant → 1/2 (1 enfant), 1/3 (2 enfants), 1/4 (3+ enfants) en PP; OU totalité usufruit; OU 1/4 PP + 3/4 usufruit
2. **Clause de préciput**: prélèvement d'un ou plusieurs biens de la communauté AVANT partage, sans entamer les droits successoraux
3. **Assurance-vie** (conjoint/partenaire PACS bénéficiaire): transmission HORS succession, EXONÉRATION TOTALE droits de succession
4. **Communauté universelle** avec clause d'attribution intégrale: radical mais possible (accord enfants majeurs requis)
- **SOURCE** PAT-004, PAT-005, M6

### F3 — Dévolution successorale légale (ordre de priorité)

- **SI** enfants présents → héritent de tout (excluent parents, frères/sœurs)
  - **SI** marié + enfants communs → conjoint: 1/4 PP OU totalité usufruit (au choix)
  - **SI** marié + enfants NON communs → conjoint: 1/4 PP seulement (pas de choix)
- **SI** pas d'enfants + marié → conjoint hérite (moitié si parents en vie)
- **SI** pas d'enfants + pas de conjoint → parents 50 %/50 % (+ frères/sœurs si présents)
- **PACS** aucun droit légal en succession → testament obligatoire pour protéger le partenaire
- **SOURCE** PAT-006, M6

### F4 — Abattements fiscaux donations (15 ans glissants)

| Lien | Abattement |
|---|---|
| Parent → enfant | 100 000 € par parent et par enfant |
| Grand-parent → petit-enfant | 31 865 € |
| Arrière-grand-parent → arrière-petit-enfant | 5 310 € |
| Don en numéraire (donateur < 80 ans, donataire majeur) | + 31 865 € supplémentaire |
| Enfant handicapé (abattement spécifique supplémentaire) | + 159 325 € (soit 259 325 € total par parent) |
| Don affecté création entreprise ou construction RP | Exonération 100 000 € |

- **RECONSTITUTION** tous les 15 ans → possibilité de renouveler les abattements
- **SOURCE** PAT-009, M6

### F5 — Assurance-vie : fiscalité des rachats et transmission

**RACHATS (gains):**
- **SI** contrat < 8 ans → PFU 12,8 % + PS 17,2 % sur les gains
- **SI** contrat ≥ 8 ans ET encours primes non rachetées < 150 000 €
  - **ALORS** PFU 7,5 % + PS 17,2 % + abattement annuel 4 600 € (seul) ou 9 200 € (couple)
- **SI** contrat ≥ 8 ans ET encours > 150 000 € → PFU 12,8 % + PS 17,2 %

**TRANSMISSION AU DÉCÈS:**
- **SI** bénéficiaire = conjoint/partenaire PACS → EXONÉRATION TOTALE
- **SI** primes versées avant 70 ans → abattement 152 500 € par bénéficiaire; 20 % de 152 501 € à 700 000 €; 31,25 % au-delà
- **SI** primes versées après 70 ans → abattement global 30 500 € (partagé entre tous bénéficiaires); droits de succession sur l'excédent
- **SOURCE** PAT-018, PAT-019, M6

### F6 — PEA vs Compte-titres ordinaire (CTO) vs Assurance-vie

| Critère | PEA | CTO | Assurance-vie |
|---|---|---|---|
| Plafond versements | 150 000 € | Illimité | Illimité |
| Universel d'actifs | Actions UE + OPCVM UE | Tous actifs | Fonds €, UC (OPCVM, SCPI...) |
| Fiscalité gains < 5 ans | PFU 30 % + clôture | PFU 30 % | PFU 30 % |
| Fiscalité gains > 5 ans | Exonération IR + PS 17,2 % | PFU 30 % | PFU 30 % (< 8 ans) |
| Fiscalité gains > 8 ans | Exonération IR + PS 17,2 % | PFU 30 % | 7,5 % + PS (si encours < 150K€) |
| Transmission au décès | Clôture (PV soumises à PS) | Succession ordinaire | Hors succession (152 500 €/bénéf.) |
| Liquidité | Retrait avant 5 ans = clôture | Libre | Libre (rachat partiel) |

- **STRATÉGIE** PEA en priorité pour actions européennes long terme; assurance-vie pour transmission hors succession et liquidité; CTO pour diversification internationale ou produits non éligibles PEA
- **SOURCE** PAT-022, PAT-023, M6

### F7 — SCI : IR vs IS

- **SI** SCI soumise à l'IR (régime par défaut)
  - **ALORS** revenus = fonciers pour les associés; PV immobilières = régime particuliers avec abattements durée de détention; charges déductibles (intérêts, réparations, taxe foncière)
  - **AVANTAGE** abattement durée de détention sur PV (exo IR après 22 ans, PS après 30 ans)
- **SI** SCI option pour l'IS
  - **ALORS** résultat soumis à IS 25 % (taux réduit 15 % < 42 500 €); amortissement du bien possible; dividendes soumis à PFU 30 %
  - **ATTENTION** option IS = IRRÉVOCABLE; perte de l'abattement durée de détention sur PV
- **SI** SCI fait de la location meublée → soumise à l'IS de PLEIN DROIT (activité commerciale)
- **SI** SCI héberge la résidence principale des associés → perd abattement IFI 30 % et droit au logement du conjoint survivant
- **COMPTABILITÉ** obligatoire si SCI: soumise à TVA, à IS, > 2 des 3 seuils (bilan 1 550 000 €, CA 3 100 000 €, 50 salariés)
- **SOURCE** PAT-016, PAT-017, M6

### F8 — IFI : assiette, seuil et réductions

- **SEUIL** IFI dû si valeur nette du patrimoine immobilier > 1 300 000 € (seuil 2025)
- **RÉDUCTIONS ET EXONÉRATIONS:**
  - SIIC: actifs immobiliers EXCLUS de l'assiette (si détention < 5 % du capital)
  - Nue-propriété: valeur de la PP n'entre pas dans l'assiette du nu-propriétaire pendant l'usufruit
  - Bois et forêts: exonération 75 % (engagement 30 ans d'exploitation + certificat gestion durable)
  - Dons à organismes d'intérêt général: réduction IFI = 75 % des versements, plafond 50 000 €/an
  - Donation temporaire d'usufruit: sort le bien de l'assiette IFI du donateur (à justifier par un besoin réel)
- **PLAFONNEMENT** IFI + IR ≤ 75 % des revenus de l'année précédente
- **SOURCE** PAT-013, PAT-014, M6

---

## MODULE G — ÉPARGNE RETRAITE (PER)

### G1 — Choix de la déduction PER

- **SI** professionnel libéral au réel BNC
  - **ALORS** déduction possible du revenu catégoriel BNC (charge de l'année de paiement) ET/OU du revenu global
  - **STRATÉGIE** utiliser d'abord le plafond BNC (réduit le RFR, donc aussi l'IFI et les cotisations sociales)
- **SI** salarié
  - **ALORS** déduction du revenu global uniquement (dans les plafonds: 10 % du salaire plafonné à 8 PASS)
- **SI** option de ne PAS déduire les versements
  - **ALORS** choix irrévocable au moment du versement; sortie capital: plus-values soumises au PFU uniquement
- **SEUIL** PASS 2025 = 47 100 € [referentiel: PASS/2025]
- **SORTIE** en rente ou en capital au choix (sauf compartiment cotisations obligatoires = rente uniquement)
- **SOURCE** GFPL-165 à GFPL-174 (M2), PAT-020, PAT-021 (M6)

### G2 — Fiscalité de sortie du PER (compartiment versements volontaires)

| Option | Sortie en rente | Sortie en capital |
|---|---|---|
| Déduction à l'entrée (option 1) | IR régime rentes à titre gratuit (abattement 10 %) + PS | Partie capital: barème IR / Plus-values: PFU 30 % |
| Pas de déduction à l'entrée (option 2) | IR régime rentes à titre onéreux (fraction selon âge) + PS | Plus-values uniquement: PFU 30 % |

- **RENTES À TITRE ONÉREUX** fraction imposable: 70 % (< 50 ans), 50 % (50–59 ans), 40 % (60–69 ans), 30 % (> 69 ans)
- **SOURCE** PAT-021, M6

---

## MODULE H — OPTIMISATION FISCALE GLOBALE

### H1 — Plafonnement des niches fiscales

- **PLAFOND GÉNÉRAL** 10 000 € par an et par foyer fiscal
- **PLAFOND SPÉCIFIQUE** 18 000 € pour Pinel Outre-Mer + SOFICA
- **HORS PLAFONNEMENT** Malraux, Monuments historiques, souscription au capital JEI/JEIR, dons, situations personnelles du contribuable
- **SOURCE** GFPL-139, GFPL-140, GFPL-141, M2

### H2 — Principaux dispositifs de réduction d'impôt 2025

| Dispositif | Taux | Conditions | Plafond |
|---|---|---|---|
| PME classique | 18 % | Investissement au capital PME | 9 000 € (seul) / 18 000 € (couple) |
| Sociétés foncières solidaires | 25 % | Investissement | 12 500 € / 25 000 € |
| JEI (Jeune Entreprise Innovante) | 30 % | R&D ≥ 20 % des charges | 22 500 € / 45 000 € |
| JEI R&D renforcée (≥ 30 % charges) | 50 % | R&D ≥ 30 % des charges | 25 000 € / 50 000 € |
| GFI (groupement forestier) | 18 % | Détention parts | 5 700 € / 11 400 € |
| Pinel (logement neuf, zones A/B1) — FERMÉ | 12/18/21 % | Engagement 6/9/12 ans | 300 000 € (5 500 €/m²) |
| Malraux (restauration historique) | 22 % ou 30 % | Zone concernée | 400 000 € (hors niches) |
| Censi-Bouvard (LMNP résidences services) — FERMÉ | 11 % sur 9 ans | Neuf uniquement | 300 000 €/an |
| Don organismes détresse/Fondation patrimoine | 75 % puis 66 % | Plafond 1 000 € pour 75 % | 20 % du revenu imposable |
| Réduction IFI (dons organismes intérêt général) | 75 % | Dons avant date dépôt déclaration | 50 000 €/an |

> **ATTENTION — Dispositifs FERMÉS aux nouvelles acquisitions :**
> - **Pinel :** fermé aux nouvelles acquisitions depuis le 01/01/2025 (seuls les investissements antérieurs continuent à produire leurs réductions). Ne pas présenter ce dispositif comme ouvert à de nouveaux investissements.
> - **Censi-Bouvard :** fermé aux nouvelles acquisitions depuis le 01/01/2023. Les réductions restent acquises pour les investissements signés avant cette date.

- **SOURCE** GFPL-125 à GFPL-141, PAT-015, M2, M6

### H3 — Transmission optimisée: donation vs succession

- **SI** objectif transmettre à ses enfants avant décès
  - **ALORS** donation (abattement 100 000 € par parent/enfant, renouvelable tous les 15 ans)
  - **STRATÉGIE** étaler les donations dans le temps pour maximiser l'utilisation des abattements
  - **DÉMEMBREMENT** donner la nue-propriété, garder l'usufruit (les loyers) → usufruit s'éteint au décès SANS droits de succession
- **SI** objectif transmettre en limitant les conflits entre héritiers
  - **ALORS** donation-partage (non rapportable, évaluée au jour de la donation, sécurisée)
- **SI** objectif favoriser une personne hors famille ou faire un legs
  - **ALORS** testament (utilisation de la quotité disponible)
- **SI** objectif transmettre un capital important hors succession
  - **ALORS** assurance-vie (abattement 152 500 €/bénéficiaire pour primes < 70 ans; exonération totale pour conjoint/PACS)
- **SOURCE** PAT-009, PAT-010, PAT-018, PAT-019, M6

---

## MODULE I — CONSEIL EN GESTION DE PATRIMOINE (Méthode)

### I1 — Audit patrimonial: 5 dimensions obligatoires

Avant toute préconisation, auditer systématiquement:

1. **D1 Situation juridique** Mode de conjugalité, composition familiale, modes de détention des biens (PP, démembrement, indivision, SCI)
2. **D2 Situation patrimoniale** Inventaire des actifs (immo, financiers, assurantiels, professionnels) et passifs (dettes)
3. **D3 Situation assurantielle/sociale** Couverture risques vie (décès, invalidité, dépendance), prévoyance, retraite attendue
4. **D4 Situation fiscale** IR (tranches effectives), IFI, prélèvements sociaux, niches fiscales utilisées
5. **D5 Situation financière** Capacité d'épargne = Revenus − Dépenses consommation − Impôts − Frais financiers − Primes assurance

- **SOURCE** CGP-004, CGP-006, M7

### I2 — Objectifs par étape du cycle de vie

| Étape | Priorités patrimoniales |
|---|---|
| Entrée dans la vie active | Choisir mode de conjugalité; premier achat RP; constitution capital |
| Développement familial | Capital + assurance-vie; protection conjoint (donation entre époux); début épargne retraite |
| Maturité professionnelle | Optimisation fiscale (IR, IFI); SCI; financement études enfants; fortifier retraite |
| Terme vie active / Retraite | Revenus complémentaires; liquidité du patrimoine; organiser transmission |
| Vie longue à la retraite | Couverture dépendance/santé; concilier revenus et transmission |

- **SOURCE** CGP-005, M7

---

## MODULE J — SEUILS ET RÉFÉRENCES 2025

| Paramètre | Valeur 2025 |
|---|---|
| PASS (Plafond Annuel Sécurité Sociale) | 47 100 € [referentiel: PASS/2025] |
| Seuil micro-BNC | 77 700 € [referentiel: seuil_micro_bnc/2025] |
| Seuil micro-BIC (autres locations meublées) | 77 700 € [referentiel: seuil_micro_bic_classe/2025] |
| Seuil micro-BIC (tourisme NON classé) | 15 000 € [referentiel: seuil_micro_bic_tourisme_non_classe/2025] |
| Seuil micro-BIC (tourisme CLASSÉ) | 77 700 € [referentiel: seuil_micro_bic_classe/2025] |
| Seuil LMP (recettes location) | 23 000 € [referentiel: seuil_lmp_recettes/2025] |
| Seuil IFI | 1 300 000 € [referentiel: seuil_ifi/2025] |
| Seuil CEHR (célibataire) | 250 000 € RFR |
| Seuil CEHR (couple) | 500 000 € RFR |
| Seuil CDHR (célibataire) | 250 000 € RFR |
| Plafond PEA | 150 000 € (+ 225 000 € PEA-PME) |
| Abattement assurance-vie (avant 70 ans) | 152 500 € / bénéficiaire [referentiel: abattement_av_avant_70/2025] |
| Abattement assurance-vie (après 70 ans) | 30 500 € global |
| Abattement donation parent/enfant | 100 000 € / parent / enfant (15 ans) [referentiel: abattement_donation_parent_enfant/2025] |
| Taux IS normal | 25 % |
| Taux IS réduit (bénéfice < 42 500 €, PME) | 15 % |
| PFU (Flat Tax) | 30 % (12,8 % IR + 17,2 % PS) |
| Prélèvements sociaux (revenus patrimoine) | 17,2 % |

---

*Dernière mise à jour : 2026-05-11 — Sources : M1 à M8, éditions 2022-2025*
