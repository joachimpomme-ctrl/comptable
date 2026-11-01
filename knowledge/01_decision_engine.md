# MOTEUR DÉCISIONNEL GLOBAL
## Knowledge Base Comptable · Financière · Patrimoniale

**Version :** 1.0 — 2026-05-11
**Portée :** Tous modules M1-M8 (BNC, fiscalité PL, PCG, location meublée, patrimoine, CGP, bases compta)
**Format :** IF / ALORS / SINON / EFFET / ATTENTION
**Usage agent IA :** Ce moteur sert de raisonnement structuré avant toute réponse. L'agent parcourt les arbres concernés, identifie le cas, puis cite la règle source (id JSONL).

---

## MODULE A — RÉGIME D'IMPOSITION BNC (Professions libérales)

### A1 — Choix du régime BNC

- **SEUIL** micro-BNC : 77 700 € pour les revenus 2025 (triennat 2023-2025) ; **83 600 €** pour les revenus 2026-2028 [referentiel: seuil_micro_bnc]
- **SI** CA annuel HT ≤ seuil micro-BNC du millésime
  - **ALORS** régime micro-BNC possible
  - **EFFET** abattement forfaitaire 34 % sur recettes → revenu imposable = CA × 66 %
  - **DÉCLARATIONS** 2042 C PRO uniquement
  - **MAIS** cotisations PER non déductibles du revenu catégoriel BNC (seulement du revenu global)
- **SI** CA annuel HT > seuil micro-BNC **OU** option pour le réel exercée
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
  - **STRATÉGIE** utiliser d'abord le plafond BNC (art. 154 bis : 15 % supplémentaires sur la fraction du bénéfice comprise entre 1 et 8 PASS) avant le plafond global, ce qui préserve les plafonds du revenu global reportables ; la déduction ne réduit pas l'assiette des cotisations sociales (versements réintégrés, CSS art. L131-6) ; effet sur le RFR à vérifier (CGI art. 1417, IV)
- **SI** professionnel libéral au micro-BNC
  - **ALORS** cotisations PER NON déductibles du revenu catégoriel
  - **MAIS** déductibles du revenu global uniquement
- **SI** versement volontaire PER avec renonciation à la déduction
  - **ALORS** choix irrévocable au moment du versement
- **ATTENTION LF 2026** versements effectués à 70 ans ou plus : non déductibles depuis le 01/01/2026 (LF 2026, art. 9) ; fraction non utilisée du plafond du revenu global reportable sur les cinq années suivantes pour les plafonds de 2026 et suivants, sur trois ans pour les plafonds antérieurs (LF 2026, art. 10, non rétroactif ; BOFiP ACTU-2026-00106 du 10/08/2026) : en 2026, seuls les reliquats de 2023 à 2025 s'ajoutent au plafond de l'année ; voir GFPL-168
- **SEUIL** PASS 2025 = 47 100 € ; PASS 2026 = 48 060 € [referentiel: PASS]
- **SOURCE** GFPL-165 à GFPL-174, M2

### A3 — TVA des professions libérales

- **SI** profession médicale/paramédicale, transports sanitaires, assurance/courtage, certaines formations agréées
  - **ALORS** hors champ TVA → pas de déclaration
- **SI** autres professions libérales (architecture, conseil, expertise comptable, juridique, artistique)
  - **ALORS** soumises à TVA
  - **SI** CA < 37 500 € (seuil de base) ET CA N-1 < 37 500 €
    - **ALORS** franchise en base — mention obligatoire: "TVA non applicable — art. 293 B du CGI"
  - **SI** CA entre 37 500 € et 41 250 € en N avec CA N-1 < 37 500 €
    - **ALORS** franchise applicable jusqu'au 31/12/N; assujettissement au 01/01/N+1
  - **SI** CA > 41 250 € en cours d'année
    - **ALORS** fin de la franchise pour les opérations réalisées à compter de la date du dépassement (CGI art. 293 B, II)
  - **ATTENTION** la réforme du seuil unique à 25 000 € a été abandonnée : seuils 2026 inchangés (85 000 / 93 500 € ventes et hébergement ; 37 500 / 41 250 € services ; avocats et auteurs 50 000 / 55 000 € et 35 000 / 38 500 €, art. 293 B, texte du 30/10/2026)
  - **SI** hors franchise ET CA ≤ plafond du régime simplifié (CIBS art. L162-4 : 254 000 € pour les services jusqu'en 2025 ; 286 000 € pour 2026-2028, probable) ET TVA annuelle < 15 000 €
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
- **REVENUS 2026 (triennat 2026-2028)** seuil du 2° porté à **83 600 €** / 50 % pour la location longue durée, les meublés de tourisme classés et les chambres d'hôtes [referentiel: seuil_micro_bic_classe/2026] ; 1° (fourniture de logement, para-hôtellerie) 203 100 € / 71 % [referentiel: seuil_micro_bic_ventes_fourniture_logement/2026] ; meublés non classés : 15 000 € / 30 %, non actualisé ; plafonds du réel simplifié portés à 945 000 € et 286 000 € (probable : source secondaire citant le BOFiP du 19/08/2026)
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
  - **CALCUL (cessions depuis le 15/02/2025)** PV = Prix vente − (Prix acquisition − TOTALITÉ des amortissements déduits pendant la location au titre de l'art. 39 C, y compris ceux déduits avant 2025) (CGI art. 150 VB, III, créé par la LF 2025 art. 84 ; RM Mette n° 10097, JOAN 24/03/2026)
  - **CALCUL (cessions avant le 15/02/2025)** PV = Prix vente − Prix acquisition (amortissements ignorés)
  - **EXCEPTIONS** (pas de réintégration) : résidences pour étudiants, pour jeunes de moins de 30 ans en formation et pour personnes de plus de 65 ans (CCH L631-12 et L631-13) ; établissements des 6° et 7° du I de l'art. L312-1 CASF ; résidences services agréées ; accueil familial salarié ; unités de soins de longue durée
  - **PRIX D'ACQUISITION** majoré des frais réels ou du forfait de 7,5 % (sans condition de durée) et des travaux réels ou du forfait de 15 % (cession plus de 5 ans après l'acquisition) ; articulation des forfaits avec la réintégration : à confirmer au BOFiP
  - **LF 2026** l'art. 150 VB, III minore aussi le prix d'acquisition des amortissements du statut du bailleur privé (art. 31, I, 1° i et j)
  - **ABATTEMENTS IR:** 0 % (0–5 ans), 6 %/an (6–21 ans), 4 % (22ème), exonération IR > 22 ans
  - **ABATTEMENTS PS:** 0 % (0–5 ans), 1,65 %/an (6–21 ans), 1,6 % (22ème), 9 %/an (23–30 ans), exonération PS > 30 ans
  - **TAUX** 19 % IR + 17,2 % PS, taux maintenu en 2026 (sur base après abattements) [referentiel: pv_immo_taux_prelevements_sociaux] ; taxe supplémentaire si la PV nette imposable à l'IR dépasse 50 000 € [referentiel: pv_immo_surtaxe_seuil]
- **SOURCE** LMN-022, LMN-023, M5

### B6 — Plus-values LMP (régime professionnel)

- **SI** cession sous statut LMP
  - **ALORS** PV professionnelle = Prix vente − VNC (valeur d'origine − amortissements DÉDUITS, hors ARD)
  - **SI** bien détenu < 2 ans → PV court terme (IR barème progressif)
  - **SI** bien détenu > 2 ans → PV CT dans la limite des amortissements déduits + PV LT au-delà (12,8 % IR + PS : 17,2 % jusqu'aux revenus 2024 ; pour les revenus 2025 et suivants, taux à vérifier, 18,6 % probable [referentiel: ps_revenus_patrimoine])
  - **EXONÉRATIONS possibles** (activité ≥ 5 ans):
    - Art. 151 septies: totale si recettes moy. < 90 000 € ; partielle jusqu'à 126 000 € (la catégorie à 250 000 € exclut expressément la location de locaux d'habitation meublés, art. 151 septies, II, 1° a ; voir LMN-025)
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
    - **ALORS** fin de la franchise pour les opérations réalisées à compter de la date du dépassement (CGI art. 293 B, II)
- **SOURCE** LMN-016, LMN-017, M5

### B8 — Cotisations sociales en location meublée

- **SI** recettes de courte durée ≤ 23 000 € ET statut LMNP
  - **ALORS** pas de cotisations sociales ; prélèvements sociaux de **18,6 %** sur le résultat BIC à compter de l'imposition des revenus 2025 (LFSS 2026, art. 12), 17,2 % pour les revenus 2024 et antérieurs [referentiel: ps_revenus_patrimoine]
- **SI** recettes courte durée > 23 000 € OU statut LMP
  - **ALORS** affiliation SSI obligatoire
  - **ABATTEMENTS** 60 % (courte durée standard) ou 87 % (tourisme classé) sur les recettes
  - **ATTENTION** confier la gestion à une agence ne dispense pas d'affiliation au-delà du seuil (voir LMN-020) ; seule alternative prévue : l'option pour le régime général lors de l'affiliation (CSS L311-3, 35°)
- **SOURCE** LMN-020, LMN-021, M5

### B9 - Location NUE : statut du bailleur privé (LF 2026, CGI art. 31, I, 1°, i et j)

- **SI** logement situé dans un immeuble collectif, loué nu en résidence principale, acquis neuf ou en VEFA (i), ou acquis avec des travaux concourant à la production d'un immeuble neuf (art. 257, I, 2, 2°) ou des travaux d'amélioration d'au moins 30 % du prix répondant aux critères d'une réhabilitation lourde (j)
  - **ALORS** option pour un amortissement déductible des revenus fonciers, sur le prix hors foncier (foncier forfaitaire de 20 %)
  - **TAUX** neuf : 3,5 % (location intermédiaire), 4,5 % (sociale), 5,5 % (très sociale) ; ancien : 3 %, 3,5 %, 4 %
  - **PLAFOND** 8 000 € par an et par foyer pour l'ensemble des amortissements i et j, majoré de 2 000 € ou 4 000 € si au moins 50 % des revenus bruts des logements amortis viennent de la location sociale ou très sociale
  - **CONDITIONS** engagement de location de 9 ans minimum, plafonds de loyer et de ressources, option irrévocable exercée avec la déclaration de l'année d'achèvement ou d'acquisition ; locataire hors foyer fiscal et hors parents ou alliés jusqu'au 2e degré ; pas de déduction si la propriété est démembrée ; en société non soumise à l'IS, conservation des parts pendant la période de location
  - **DATES** acquisitions (ou dépôts de permis de construire pour un logement que le contribuable fait construire, i) réalisées entre le lendemain de la publication de la loi n° 2026-103 du 19/02/2026 et le 31/12/2028 (texte de l'art. 31), soit du 21/02/2026 au 31/12/2028, la date retenue étant celle de la signature de l'acte notarié (service-public F39735, vérifiée le 21/07/2026)
  - **RUPTURE** d'un engagement : le revenu foncier de l'année est majoré des amortissements déduits, imposés selon un système de quotient (sauf invalidité, licenciement ou décès)
  - **ATTENTION** à la revente, le prix d'acquisition est minoré des amortissements déduits (CGI art. 150 VB, III) ; micro-foncier exclu pour tout le foyer (CGI art. 32, 2, c) ; imputation sur le revenu global d'un déficit créé par l'amortissement : à vérifier (rien dans l'art. 156 au 30/10/2026)
- **SOURCE** RF-006 ; CGI art. 31, I, 1°, i et j, art. 32 et 150 VB, texte du 30/10/2026 ; cas de test EV-042

---

## MODULE C — IMPÔT SUR LE REVENU ET PRÉLÈVEMENTS SOCIAUX

### C1 — Barème IR des revenus 2025 (déclarés en 2026)

| Tranche (par part) | TMI |
|---|---|
| ≤ 11 600 € | 0 % |
| 11 601 € à 29 579 € | 11 % |
| 29 580 € à 84 577 € | 30 % |
| 84 578 € à 181 917 € | 41 % |
| > 181 917 € | 45 % |

- **SOURCE DES CHIFFRES** CGI art. 197 en vigueur (LF 2026) [referentiel: bareme_ir_seuil_tranche_11pct/2026, _30pct, _41pct, _45pct]
- **REVENUS 2024 (déclarés en 2025)** 11 497 / 29 315 / 83 823 / 180 294 € ; quotient familial plafonné à 1 791 € par demi-part
- **REVENUS 2026** barème fixé par la LF 2027, non promulguée au 01/11/2026 : ne pas l'anticiper
- **QUOTIENT FAMILIAL** avantage plafonné à 1 807 € par demi-part (revenus 2025)
- **DÉCLARATION AUTOMATIQUE** possible si revenus intégralement déclarés par tiers (mais nécessaire pour PFU→barème ou crédits d'impôt)
- **SOURCE** GFPL-105 à GFPL-115, M2

### C2 — PFU (Flat Tax) vs barème progressif sur revenus financiers

- **SI** dividendes, intérêts, PV mobilières, gains assurance-vie
  - **ALORS** PFU par défaut : 12,8 % IR + PS. Dividendes et intérêts, selon l'année de perception : **31,4 %** depuis le 01/01/2026 (PS 18,6 %), 30 % en 2025 (PS 17,2 %) [referentiel: pfu_taux_global]. Plus-values mobilières, selon l'année de réalisation : 31,4 % dès celles de 2025 (PS 18,6 %, probable) [referentiel: ps_revenus_patrimoine/2025]. Assurance-vie, PEL et CEL : PS maintenus à 17,2 %
  - **OPTION** barème progressif possible (option globale sur tous les revenus financiers de l'année)
  - **FORME** option expresse, exercée lors du dépôt de la déclaration et au plus tard à la date limite de déclaration (CGI art. 200 A, 2, texte du 30/10/2026 : le mot « irrévocable » n'y figure plus)
  - **RÉVOCABILITÉ** pour les revenus 2026 (déclarés en 2027) et suivants, le contribuable peut renoncer à l'option dans le délai de réclamation ou en cours de contrôle (service-public F34913, vérifiée le 15/04/2026 ; impots.gouv.fr « Les revenus mobiliers », modifiée le 08/04/2026 : « À compter de 2026, le caractère irrévocable de cette option a été supprimé ») ; changement issu de la LF 2026 (probable : les pages officielles lues ne citent pas l'article de loi) ; revenus 2025 et antérieurs : renonciation non prévue par ces sources (à vérifier)
  - **ATTENTION** l'option distincte pour les plus-values sur actifs numériques reste « expresse et irrévocable » (CGI art. 200 C, texte du 30/10/2026)
  - **SI** option barème + dividendes → abattement 40 % sur les dividendes
  - **SI** TMI ≤ 11 % → option barème avantageuse
  - **SI** TMI ≥ 30 % → PFU généralement plus avantageux
- **SOURCE** CGI art. 200 A, 1 et 2, et art. 200 C (texte du 30/10/2026) ; service-public F34913

### C3 — Prélèvements sociaux (2025 et 2026)

| Assiette | CSG | CRDS | Prélèvement solidarité | TOTAL |
|---|---|---|---|---|
| Revenus fonciers, PV immobilières, assurance-vie, PEL/CEL/PEP | 9,2 % | 0,5 % | 7,5 % | **17,2 %** en 2025 et 2026 [referentiel: ps_revenus_fonciers_av_epargne_logement] |
| Produits de placement (dividendes, intérêts, gains de PEA), selon l'année de perception | 9,2 % puis 10,6 % | 0,5 % | 7,5 % | **17,2 %** en 2025 ; **18,6 %** depuis le 01/01/2026 [referentiel: ps_produits_placement] |
| Autres revenus du patrimoine (LMNP, certaines PV mobilières), selon l'année des revenus | 9,2 % puis 10,6 % | 0,5 % | 7,5 % | **17,2 %** revenus 2024 ; **18,6 %** dès les revenus 2025 [referentiel: ps_revenus_patrimoine] |
| Revenus d'activité (BNC, salaires) | 9,2 % | 0,5 % | — | **9,7 %** |

- **ATTENTION** jamais de taux unique : le taux dépend de la catégorie de revenu et de l'année (perception pour les placements, revenus pour le patrimoine). Gains de PEA : taux historiques possibles pour les gains acquis avant 2018. LMP : cotisations sociales, pas ces taux.
- **SOURCE** GFPL-155 à GFPL-159, M2 ; LFSS 2026 (loi n° 2025-1403, art. 12) ; service-public F2329

### C4 — CEHR (Contribution Exceptionnelle sur les Hauts Revenus)

- **SI** RFR > 250 000 € (célibataire) OU > 500 000 € (imposition commune)
  - **ALORS** CEHR due
  - **BARÈME célibataire** 3 % de 250 001 € à 500 000 € / 4 % au-delà
  - **BARÈME couple** 3 % de 500 001 € à 1 000 000 € / 4 % au-delà
- **SOURCE** GFPL-142 à GFPL-145, M2

### C5 — CDHR (Contribution Différentielle sur les Hauts Revenus, CGI art. 224)

- **DURÉE** créée pour les revenus 2025 (LF 2025), prorogée par la LF 2026 jusqu'à l'imposition des revenus de l'année au titre de laquelle le déficit du budget général passe sous 3 % du PIB (BOFiP BOI-IR-CDHR, § 10, publié le 30/06/2026 ; voir GFPL-146)

- **SI** RFR retraité > 250 000 € (célibataire) OU > 500 000 € (couple)
  **ET** IR + CEHR < 20 % du RFR retraité
  - **ALORS** CDHR = 20 % × RFR retraité − (IR + CEHR)
  - **ACOMPTE** 95 % du montant estimé à verser entre le 1er et le 15 décembre de l'année des revenus
  - **PÉNALITÉ** 20 % si défaut/retard ou acompte insuffisant de > 20 %
- **SOURCE** GFPL-146 à GFPL-154, M2

---

## MODULE D — PLUS-VALUES PROFESSIONNELLES (BNC)

### D1 — Qualification CT vs LT

- **SI** élément amortissable détenu < 2 ans → PV court terme
- **SI** élément amortissable détenu > 2 ans → PV CT dans la limite des amortissements déduits + PV LT au-delà
- **SI** élément NON amortissable détenu > 2 ans → PV long terme
- **PV CT** intégrée au résultat imposable (barème IR); étalement possible sur 3 ans (option)
- **PV LT** 12,8 % IR + PS : 30 % jusqu'aux revenus 2024 ; 31,4 % probable dès les revenus 2025 (PS 18,6 %, LFSS 2026, une seule source) [referentiel: ps_revenus_patrimoine]
- **SOURCE** GFPL-082 à GFPL-094, M2

### D2 — Exonérations (activité ≥ 5 ans)

- **Art. 151 septies** (exonération recettes):
  - **SI** recettes moy. (prestations de services) < 90 000 € → exonération TOTALE (IR + PS)
  - **SI** recettes moy. entre 90 000 € et 126 000 € → exonération PARTIELLE et dégressive
- **Art. 151 septies A** (départ à la retraite):
  - **SI** cessation de fonctions + retraite dans les 24 mois avant ou après la cession
  - **ALORS** exonération IR sur PV CT + LT ; prélèvements sociaux maintenus (taux : voir D1)
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
- **PACS** aucun droit successoral légal → testament nécessaire pour protéger le partenaire ; seul droit légal : jouissance gratuite du logement et du mobilier pendant un an (C. civ. art. 515-6, al. 3, renvoyant à l'art. 763)
- **SOURCE** PAT-006, M6

### F4 — Abattements fiscaux donations (15 ans glissants)

| Lien | Abattement |
|---|---|
| Parent → enfant | 100 000 € par parent et par enfant |
| Grand-parent → petit-enfant | 31 865 € |
| Arrière-grand-parent → arrière-petit-enfant | 5 310 € |
| Don en numéraire (donateur < 80 ans, donataire majeur) | + 31 865 € supplémentaire |
| Enfant handicapé (abattement spécifique supplémentaire) | + 159 325 € (soit 259 325 € total par parent) |
| Don de sommes d'argent affecté sous 6 mois à l'achat d'un logement neuf ou en VEFA, ou à des travaux de rénovation énergétique de la résidence principale (CGI art. 790 A bis) | Exonération jusqu'à 100 000 € par donateur et 300 000 € par donataire, pour les dons versés du 15/02/2025 au **31/12/2026** ; conservation du logement 5 ans |

- **RECONSTITUTION** tous les 15 ans → possibilité de renouveler les abattements
- **SOURCE** PAT-009, M6

### F5 — Assurance-vie : fiscalité des rachats et transmission

**RACHATS (gains):**
- **SI** contrat < 8 ans → PFU 12,8 % + PS 17,2 % sur les gains
- **SI** contrat ≥ 8 ans ET primes versées non remboursées (tous contrats) ≤ 150 000 €
  - **ALORS** 7,5 % + PS 17,2 % après abattement annuel de 4 600 € (seul) ou 9 200 € (couple)
- **SI** contrat ≥ 8 ans ET primes > 150 000 € → 7,5 % sur la fraction des gains égale à gains × 150 000 / primes, 12,8 % sur le reste (CGI art. 200 A, 1, B, 2°), PS 17,2 %

**TRANSMISSION AU DÉCÈS:**
- **SI** bénéficiaire = conjoint/partenaire PACS → EXONÉRATION TOTALE
- **SI** primes versées avant 70 ans → abattement 152 500 € par bénéficiaire, puis 20 % sur la part taxable jusqu'à 700 000 € (soit jusqu'à 852 500 € de capital), 31,25 % au-delà (CGI art. 990 I)
- **ATTENTION** au dénouement par décès, les prélèvements sociaux (17,2 %) restent dus sur les gains qui n'y ont pas encore été soumis, notamment en unités de compte (probable)
- **SI** primes versées après 70 ans → abattement global 30 500 € (partagé entre tous bénéficiaires); droits de succession sur l'excédent
- **SOURCE** PAT-018, PAT-019, M6

### F6 — PEA vs Compte-titres ordinaire (CTO) vs Assurance-vie

| Critère | PEA | CTO | Assurance-vie |
|---|---|---|---|
| Plafond versements | 150 000 € | Illimité | Illimité |
| Universel d'actifs | Actions UE + OPCVM UE | Tous actifs | Fonds €, UC (OPCVM, SCPI...) |
| Fiscalité gains < 5 ans | PFU + clôture | PFU | 12,8 % + PS 17,2 % = 30 % |
| Fiscalité gains > 5 ans | Exonération IR + PS | PFU | 12,8 % + PS 17,2 % = 30 % (< 8 ans) |
| Fiscalité gains > 8 ans | Exonération IR + PS | PFU | 7,5 % + PS 17,2 % (primes ≤ 150 K€) |
| Transmission au décès | Clôture (PV soumises à PS) | Succession ordinaire | Hors succession (152 500 €/bénéf.) |
| Liquidité | Retrait avant 5 ans = clôture | Libre | Libre (rachat partiel) |

- **TAUX** PFU 30 % pour les revenus perçus en 2025, **31,4 %** depuis le 01/01/2026 [referentiel: pfu_taux_global] ; PS sur les gains de PEA : 18,6 % depuis 2026 (probable) [referentiel: ps_produits_placement] ; assurance-vie : PS maintenus à 17,2 %
- **STRATÉGIE** PEA en priorité pour actions européennes long terme; assurance-vie pour transmission hors succession et liquidité; CTO pour diversification internationale ou produits non éligibles PEA
- **SOURCE** PAT-022, PAT-023, M6

### F7 — SCI : IR vs IS

- **SI** SCI soumise à l'IR (régime par défaut)
  - **ALORS** revenus = fonciers pour les associés; PV immobilières = régime particuliers avec abattements durée de détention; charges déductibles (intérêts, réparations, taxe foncière)
  - **AVANTAGE** abattement durée de détention sur PV (exo IR après 22 ans, PS après 30 ans)
- **SI** SCI option pour l'IS
  - **ALORS** résultat soumis à IS 25 % (taux réduit 15 % < 42 500 €); amortissement du bien possible; dividendes soumis au PFU (30 % jusqu'en 2025, 31,4 % depuis le 01/01/2026) [referentiel: pfu_taux_global]
  - **ATTENTION** option IS révocable seulement jusqu'au 5e exercice suivant celui de l'option (CGI art. 239, 1, depuis la LF 2019), définitive ensuite ; plus d'abattement pour durée de détention : la société paie l'IS sur la PV de cession de l'immeuble ; la cession des parts par l'associé relève des PV mobilières
- **SI** SCI fait de la location meublée → soumise à l'IS de PLEIN DROIT (activité commerciale)
- **SI** SCI héberge la résidence principale des associés → perd abattement IFI 30 % et droit au logement du conjoint survivant
- **COMPTABILITÉ** obligatoire si SCI: soumise à TVA, à IS, > 2 des 3 seuils (bilan 1 550 000 €, CA 3 100 000 €, 50 salariés)
- **SOURCE** PAT-016, PAT-017, M6

### F8 — IFI : assiette, seuil et réductions

- **SEUIL** IFI dû si valeur nette du patrimoine immobilier > 1 300 000 € (CGI art. 964, inchangé en 2026) [referentiel: seuil_ifi]
- **RÉDUCTIONS ET EXONÉRATIONS:**
  - SIIC: actifs immobiliers EXCLUS de l'assiette (si détention < 5 % du capital)
  - Nue-propriété: valeur de la PP n'entre pas dans l'assiette du nu-propriétaire pendant l'usufruit
  - Bois et forêts: exonération 75 % (engagement 30 ans d'exploitation + certificat gestion durable)
  - Dons à organismes d'intérêt général: réduction IFI = 75 % des versements, plafond 50 000 €/an
  - Donation temporaire d'usufruit: sort le bien de l'assiette IFI du donateur (à justifier par un besoin réel)
- **DÉCOTE** patrimoine net taxable P entre 1 300 000 € et 1 400 000 € : IFI réduit de 17 500 € − 1,25 % × P (CGI art. 977, 2). Exemple : P = 1 350 000 € → barème 2 850 €, décote 625 €, IFI 2 225 €
- **DÉMEMBREMENT** l'usufruitier déclare la pleine propriété (CGI art. 968), sauf exceptions de cet article
- **PLAFONNEMENT** IFI + IR ≤ 75 % des revenus de l'année précédente
- **SOURCE** PAT-013, PAT-014, IFI-002, M6

### F9 - Pacte Dutreil (CGI art. 787 B)

- **EFFET** exonération de droits de mutation à titre gratuit à hauteur de 75 % de la valeur des titres transmis (donation ou succession)
- **CONDITIONS** engagement collectif de conservation d'au moins 2 ans en cours au jour de la transmission (ou réputé acquis) ; engagement individuel de chaque héritier ou donataire de **6 ans** à compter de la fin de l'engagement collectif ; activité principale ou fonction de direction exercée par l'un des signataires ou bénéficiaires pendant l'engagement collectif et les 3 ans qui suivent la transmission
- **DATES** 6 ans pour les transmissions (donations ou décès) depuis le 21/02/2026, 4 ans pour les transmissions antérieures (loi n° 2026-103, art. 8 ; BOFiP ACTU-2026-00114 du 10/08/2026)
- **AUCUNE CONDITION DE PARENTÉ** : le bénéficiaire n'a pas à être un descendant
- **EXCLUSIONS (LF 2026, transmissions depuis le 21/02/2026)** la fraction de valeur des titres qui représente des biens non affectés exclusivement à l'activité pendant au moins 3 ans avant la transmission et jusqu'à la fin de l'engagement individuel : chasse, pêche, véhicules de tourisme, yachts, bateaux de plaisance, aéronefs, bijoux, métaux précieux, objets d'art, de collection ou d'antiquité, chevaux de course ou de concours, vins et alcools, logements et résidences
- **CUMUL** donation en pleine propriété par un donateur de moins de 70 ans : réduction de 50 % des droits (CGI art. 790, I)
- **RUPTURE** droits exonérés exigibles avec intérêt de retard (CGI art. 1840 G ter, I) ; exceptions et détail : 04 RISK-008
- **ATTENTION** montage à faire valider par un notaire ou un avocat fiscaliste
- **SOURCE** TRM-003, RISK-008 ; CGI art. 787 B, 790 et 1840 G ter, texte du 30/10/2026 ; cas de test EV-041

### F10 - Taxe sur les holdings patrimoniales (CGI art. 235 ter C)

- **SI** société soumise à l'IS (de plein droit ou sur option), ou société étrangère équivalente, qui remplit à la clôture de l'exercice les trois conditions suivantes :
  - valeur vénale de l'ensemble de ses actifs ≥ 5 000 000 € ;
  - une personne physique détient au moins 50 % des droits de vote ou des droits financiers, ou y exerce en fait le pouvoir de décision (le conjoint, le partenaire de PACS, le concubin, les ascendants, les descendants et les frères et sœurs comptent comme une seule personne) ;
  - revenus passifs (dividendes, intérêts, redevances, droits d'auteur, loyers, produits de cession des biens qui les génèrent) > 50 % des produits d'exploitation et financiers de l'exercice
  - **ALORS** taxe de **20 %** sur la valeur vénale, à la clôture, des actifs suivants : biens affectés à la chasse ou à la pêche ; véhicules non affectés à une activité professionnelle, véhicules de tourisme, yachts, bateaux de plaisance, aéronefs ; bijoux et métaux précieux ; chevaux de course ou de concours ; vins et alcools ; logements dont la personne physique se réserve la jouissance (occupés gratuitement ou pour un loyer inférieur au prix du marché, ou loués fictivement), diminués de certaines dettes d'acquisition
  - **SAUF** la part de ces actifs affectée à une activité industrielle, commerciale, artisanale, agricole ou libérale (de la société, d'une société liée ou de la personne physique, dans les conditions de l'art. 975)
  - **EFFETS** taxe non déductible de l'IS ; société étrangère : taxe due par les personnes physiques domiciliées en France, sur leur déclaration de revenus, sauf si elles justifient que le choix du siège n'a pas pour but principal de contourner la loi fiscale française
- **ATTENTION** taxe créée par la LF 2026 (rapport d'information du Sénat n° 760 du 17/06/2026) ; premiers exercices concernés : à vérifier, aucune source officielle lue sur la date d'application ; ne pas confondre avec les exclusions du Pacte Dutreil (F9), dont la liste est proche ; à faire valider par un avocat fiscaliste
- **SOURCE** CGI art. 235 ter C, texte du 30/10/2026 ; pas de règle dédiée dans le corpus

---

## MODULE G — ÉPARGNE RETRAITE (PER)

### G1 — Choix de la déduction PER

- **SI** professionnel libéral au réel BNC
  - **ALORS** déduction possible du revenu catégoriel BNC (charge de l'année de paiement) ET/OU du revenu global
  - **STRATÉGIE** utiliser d'abord le plafond BNC (art. 154 bis) : il ajoute 15 % du bénéfice compris entre 1 et 8 PASS et préserve les plafonds du revenu global reportables. Il ne réduit ni les cotisations sociales (versements réintégrés dans l'assiette des TNS, CSS art. L131-6) ni l'IFI (qui ne dépend pas du RFR ; seul son plafonnement dépend des revenus)
- **SI** salarié
  - **ALORS** déduction du revenu global uniquement (plafond : 10 % des revenus d'activité de N-1 nets de frais, dans la limite de 8 PASS de N-1, minimum 10 % du PASS de N-1)
- **SI** option de ne PAS déduire les versements
  - **ALORS** choix irrévocable au moment du versement; sortie capital: plus-values soumises au PFU uniquement
- **SEUIL** PASS 2025 = 47 100 € ; PASS 2026 = 48 060 € [referentiel: PASS]
- **PLAFOND SALARIÉ (versements 2026)** au minimum 4 710 € [referentiel: per_plafond_salarie_plancher/2026], au maximum 37 680 € [referentiel: per_plafond_salarie_max/2026], diminué de l'épargne retraite professionnelle déjà déduite ; le plafond personnel figure sur l'avis d'impôt
- **PLAFOND TNS (art. 154 bis, II, 1°)** 10 % du bénéfice imposable dans la limite de 8 PASS, plus 15 % de la fraction comprise entre 1 et 8 PASS ; minimum 10 % du PASS. Exemple revenus 2025 : bénéfice 95 000 € → 9 500 + 15 % × (95 000 − 47 100) = 16 685 €
- **ATTENTION LF 2026** versements effectués à 70 ans ou plus : non déductibles depuis le 01/01/2026 (LF 2026, art. 9) ; fraction non utilisée du plafond du revenu global reportable sur les cinq années suivantes pour les plafonds de 2026 et suivants, sur trois ans pour les plafonds antérieurs (LF 2026, art. 10, non rétroactif ; BOFiP ACTU-2026-00106 du 10/08/2026) : en 2026, seuls les reliquats de 2023 à 2025 s'ajoutent au plafond de l'année ; voir GFPL-168
- **SORTIE** en rente ou en capital au choix (sauf compartiment cotisations obligatoires = rente uniquement)
- **SOURCE** GFPL-165 à GFPL-174 (M2), PAT-020, PAT-021 (M6)

### G2 — Fiscalité de sortie du PER (compartiment versements volontaires)

| Option | Sortie en rente | Sortie en capital |
|---|---|---|
| Déduction à l'entrée (option 1) | IR régime rentes à titre gratuit (abattement 10 %) + PS | Partie capital: barème IR / Plus-values: PFU |
| Pas de déduction à l'entrée (option 2) | IR régime rentes à titre onéreux (fraction selon âge) + PS | Plus-values uniquement: PFU |

- **TAUX** PFU 30 % pour les sorties de 2025, 31,4 % depuis le 01/01/2026 [referentiel: pfu_taux_global] ; PS de 18,6 % sur les gains et les rentes depuis le 01/01/2026 (probable : questions-réponses BOSS citées par Weblex le 20/07/2026) [referentiel: ps_produits_placement]

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
| Don organismes détresse/Fondation patrimoine | 75 % puis 66 % | Plafond 2 000 € pour 75 % (CGI art. 200, 1 ter en vigueur ; 1 000 € auparavant, dons depuis le 14/10/2025 selon la LF 2026, probable) | 20 % du revenu imposable |
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
  - **ALORS** donation-partage : effet civil (biens évalués au jour de la donation pour l'imputation et le calcul de la réserve, sous les conditions de l'art. 1078 C. civ. ; pas de rapport) ; effet fiscal identique à une donation simple (donations de moins de 15 ans rappelées pour leur valeur au jour de l'acte, CGI art. 784)
- **SI** objectif favoriser une personne hors famille ou faire un legs
  - **ALORS** testament (utilisation de la quotité disponible)
- **SI** objectif transmettre un capital important hors succession
  - **ALORS** assurance-vie (abattement 152 500 €/bénéficiaire pour primes < 70 ans; exonération totale pour conjoint/PACS)
- **SOURCE** PAT-009, PAT-010, PAT-018, PAT-019, M6

---

## MODULE I — CONSEIL EN GESTION DE PATRIMOINE (Méthode)

> Méthode générale de collecte des faits. Elle ne repose sur aucune règle du corpus et ne fixe aucun chiffre. Les règles applicables se trouvent dans les branches citées, qui reposent sur des textes.

### I1 - Faits à réunir avant une préconisation patrimoniale

1. **Situation juridique** mode de conjugalité, enfants (communs ou non), modes de détention des biens (pleine propriété, démembrement, indivision, SCI) : branches F1, F2, F3, F7
2. **Situation patrimoniale** actifs (immobilier, financiers, assurance-vie, professionnels) et dettes : branches B, F6, F8, F10
3. **Retraite et prévoyance** épargne retraite en cours, âge des versements, contrats d'assurance-vie et âge des primes : branches F5, G1, G2
4. **Situation fiscale** année des revenus, TMI, RFR, IFI, prélèvements sociaux, niches déjà utilisées : branches C1 à C5, F8, H1
5. **Situation financière** capacité d'épargne = revenus − dépenses courantes − impôts − frais financiers − primes d'assurance (identité comptable, sans source normative)

- **SI** un de ces faits manque et change la règle applicable
  - **ALORS** le demander ou poser l'hypothèse explicitement avant de répondre
- **SOURCE** aucune règle source : méthode générale

### I2 - Objectif exprimé : branches à parcourir

| Objectif | Branches |
|---|---|
| Protéger le conjoint ou le partenaire | F1, F2, F3, F5 |
| Transmettre aux enfants de son vivant | F4, H3, F9 si entreprise |
| Préparer la retraite | G1, G2 |
| Réduire l'IR ou l'IFI | C1 à C5, F8, H1, H2 |
| Investir en immobilier locatif | B1 à B9, F7 |
| Détenir des actifs via une société | F7, F10 |

- **SOURCE** aucune règle source : table d'orientation vers les branches du moteur

---

## MODULE J — SEUILS ET RÉFÉRENCES 2025-2026

> Source de vérité : `referentiel_parametres.json` (clé + millésime). En cas d'écart avec un texte du corpus, le référentiel prime.

| Paramètre | Valeur 2025 | Valeur 2026 |
|---|---|---|
| PASS (Plafond Annuel Sécurité Sociale) | 47 100 € | **48 060 €** [referentiel: PASS] |
| Seuil micro-BNC | 77 700 € | **83 600 €** (triennat 2026-2028) [referentiel: seuil_micro_bnc] |
| Seuil micro-BIC (location meublée longue durée, chambres d'hôtes) | 77 700 € | **83 600 €** (triennat 2026-2028) [referentiel: seuil_micro_bic_classe] |
| Seuil micro-BIC (tourisme NON classé) | 15 000 € | 15 000 € [referentiel: seuil_micro_bic_tourisme_non_classe] |
| Seuil micro-BIC (tourisme CLASSÉ) | 77 700 € | **83 600 €** (triennat 2026-2028) [referentiel: seuil_micro_bic_classe] |
| Seuil micro-BIC (fourniture de logement, para-hôtellerie, 1° de l'art. 50-0) | 188 700 € | **203 100 €** [referentiel: seuil_micro_bic_ventes_fourniture_logement] |
| Seuil LMP (recettes location) | 23 000 € | 23 000 € [referentiel: seuil_lmp_recettes] |
| Seuil IFI | 1 300 000 € | 1 300 000 € [referentiel: seuil_ifi] |
| Seuil CEHR (célibataire) | 250 000 € RFR | 250 000 € (CGI art. 223 sexies, texte du CGI au 30/10/2026) |
| Seuil CEHR (couple) | 500 000 € RFR | 500 000 € (CGI art. 223 sexies, texte du CGI au 30/10/2026) |
| Seuil CDHR (célibataire / couple) | 250 000 € / 500 000 € RFR retraité | 250 000 € / 500 000 € (CGI art. 224, texte du CGI au 30/10/2026) ; CDHR prorogée par la LF 2026 (BOFiP BOI-IR-CDHR, § 10) |
| Plafond PEA | 150 000 € ; plafond commun PEA + PEA-PME de 225 000 € (probable : à lire comme un total, pas comme 150 000 + 225 000) | à vérifier (Code monétaire et financier, hors corpus) |
| Abattement assurance-vie (avant 70 ans) | 152 500 € / bénéficiaire | 152 500 € [referentiel: abattement_av_avant_70] |
| Abattement assurance-vie (après 70 ans) | 30 500 € global | 30 500 € (CGI art. 757 B, texte du CGI au 30/10/2026) |
| Abattement donation parent/enfant | 100 000 € / parent / enfant (15 ans) | 100 000 € [referentiel: abattement_donation_parent_enfant] |
| Taux IS normal | 25 % | 25 % (CGI art. 219, texte du CGI au 30/10/2026) |
| Taux IS réduit (bénéfice ≤ 42 500 €, PME, CA ≤ 10 M€) | 15 % | 15 % (CGI art. 219, texte du CGI au 30/10/2026) |
| Plafond majoré du déficit foncier (rénovation énergétique E/F/G vers A-D) | 21 400 € | 21 400 € jusqu'au 31/12/2027 [referentiel: deficit_foncier_plafond_renovation_energetique] |
| Barème IR, première tranche (par part) | 11 497 € (revenus 2024) | 11 600 € (revenus 2025) [referentiel: bareme_ir_seuil_tranche_11pct/2026] |
| PFU (Flat Tax) | 30 % (12,8 % IR + 17,2 % PS) | **31,4 %** (12,8 % + PS 18,6 %), revenus perçus depuis le 01/01/2026 [referentiel: pfu_taux_global] |
| Prélèvements sociaux — PV immobilières, revenus fonciers, assurance-vie | 17,2 % | **17,2 % maintenu** (CSS art. L136-8, IV) [referentiel: ps_revenus_fonciers_av_epargne_logement] |
| Prélèvements sociaux, dividendes et intérêts (année de perception) | 17,2 % | **18,6 %** (CSG portée à 10,6 %, LFSS 2026 art. 12) [referentiel: ps_produits_placement] |
| Prélèvements sociaux, LMNP et certaines PV mobilières (année des revenus) | **18,6 %** (revenus 2025) | **18,6 %** [referentiel: ps_revenus_patrimoine] |

---

*Dernière mise à jour : 2026-11-01 (lot 1 de l'audit : prélèvements sociaux et PFU 2026, micro-BIC 2026, LMNP, PER ; lot 2 : statut du bailleur privé (B9), Pacte Dutreil (F9) ; lot 3 : option pour le barème (C2), taxe sur les holdings patrimoniales (F10), module I réécrit sans renvoi aux règles CGP retirées). Sources : M1 à M8, éditions 2022-2025 ; referentiel_parametres.json pour les millésimes 2026 ; texte du CGI au 30/10/2026*
