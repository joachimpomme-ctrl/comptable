# FORMULES & RISQUES — Knowledge Base Agent

**Types :** `formule` (calculs structurés) + `risque` (erreurs et pièges)
**Scope :** Art. 39-C amortissements, PV LMNP 2025, IFI calcul+décote, DMTG barème, usufruit barème âge, déficit foncier, seuil rentabilité, risques SCI/IS, FEC, Pacte Dutreil, PAS

---

## FORMULES DE CALCUL

### [FORM-001] Calcul amortissement article 39-C

**Formule :**
Amortissement déductible (art. 39-C) = MAX(0 ; Loyers acquis − Charges hors amortissements afférentes au bien). Amortissements différés (ARD) = Amortissements comptabilisés − Amortissements déductibles. Accumulation ARD: Solde N = Solde N-1 + ARD N − Imputations N. Imputation possible si exercice bénéficiaire dans la même limite (loyers − charges hors amort ≥ 0).

**Exceptions :**
- En cas de vente LMNP: ARD définitivement perdus
- En cas de vente LMP: ARD majorent la VNC

*Source: Guide fiscal LM ARCOLIB 2025, 3420-3432*

---

### [FORM-002] Calcul PV LMNP depuis 2025

**Formule :**
PV brute LMNP (depuis 2025) = Prix cession − (Prix acquisition − Amortissements déduits pendant la détention). Prix acquisition majoré: + frais d'acquisition réels OU + 7,5 % forfait si > 5 ans; + travaux réels OU + 15 % forfait si > 5 ans. PV nette imposable IR = PV brute × (1 − Abattement IR durée détention). PV nette imposable PS = PV brute × (1 − Abattement PS durée détention). IR = PV nette IR × 19 %. PS = PV nette PS × 17,2 %. Taxe supplémentaire = f(PV nette IR) si > 50 000 €.

**Paramètres :**
- `seuil_taxe_supplementaire` : 50000

**Taux :**
- `IR_pct` : 19
- `PS_pct` : 17.2

**Exceptions :**
- Avant 2025: PV brute = Prix cession − Prix acquisition (amortissements non réintégrés)
- Résidences étudiantes/apprentissage: exception au régime de réintégration des amortissements

*Source: Guide fiscal LM ARCOLIB 2025, 6211-6213*

---

### [FORM-003] Calcul IFI et décote

**Formule :**
IFI brut = Σ(Tranche × Taux): tranche 800 001-1 300 000 € × 0,5 %; tranche 1 300 001-2 570 000 € × 0,7 %; tranche 2 570 001-5 000 000 € × 1 %; tranche 5 000 001-10 000 000 € × 1,25 %; > 10 000 000 € × 1,5 %. Décote si patrimoine net P ∈ [1 300 000; 1 400 000[: IFI net = IFI brut − (17 500 − 1,25 % × P). Plafonnement: IFI net ≤ 75 % × Revenus N-1 − IR N-1.

**Paramètres :**
- `seuil_IFI` : 1300000
- `seuil_decote_max` : 1400000

**Taux :**
- `tranche_1_pct` : 0.5
- `tranche_2_pct` : 0.7
- `tranche_3_pct` : 1.0
- `tranche_4_pct` : 1.25
- `tranche_5_pct` : 1.5
- `plafonnement_pct` : 75

*Source: Guide fiscal PL 2025 Banque Populaire, V IFI — pages 73-76*

---

### [FORM-004] Calcul droits donation ligne directe

**Formule :**
Droits de donation ligne directe = Σ(Tranche nette après abattements × Taux). Barème: jusqu'à 8 072 € → 5 %; de 8 073 à 12 109 € → 10 %; de 12 110 à 15 932 € → 15 %; de 15 933 à 552 324 € → 20 %; de 552 325 à 902 838 € → 30 %; de 902 839 à 1 805 677 € → 40 %; > 1 805 677 € → 45 %. Abattement parent→enfant: 100 000 €. Abattement numéraire supplémentaire: +31 865 € si conditions. Part nette = Montant transmis − Abattements applicables.

**Paramètres :**
- `abattement_parent_enfant` : 100000
- `tranche_5` : 8072
- `tranche_10_max` : 12109
- `tranche_15_max` : 15932
- `tranche_20_max` : 552324
- `tranche_30_max` : 902838
- `tranche_40_max` : 1805677

**Taux :**
- `t1` : 5
- `t2` : 10
- `t3` : 15
- `t4` : 20
- `t5` : 30
- `t6` : 40
- `t7` : 45

*Source: Guide fiscal PL 2025 Banque Populaire + CGI art. 777, VI Transmission — pages 82-83*

---

### [FORM-005] Valeur nue-propriété pour calcul des droits

**Formule :**
Valeur NP transmise = Valeur PP × (1 − Taux usufruit selon âge art. 669 CGI). Taux usufruit: < 21 ans: 90 %; 21-30 ans: 80 %; 31-40 ans: 70 %; 41-50 ans: 60 %; 51-60 ans: 50 %; 61-70 ans: 40 %; 71-80 ans: 30 %; 81-90 ans: 20 %; > 90 ans: 10 %. Droits de donation = f(Valeur NP − Abattement applicable). Au décès de l'usufruitier: le nu-propriétaire devient PP en franchise de droits (pas de revalorisation).

**Exceptions :**
- Au décès de l'usufruitier: aucun nouveau droit à payer (extinction de l'usufruit sans taxation)

*Source: Guide fiscal PL 2025 Banque Populaire + CGI art. 669, VI Transmission — page 85*

---

### [FORM-006] Calcul déficit foncier imputable

**Formule :**
Déficit foncier imputable sur le revenu global = MIN(10 700 €, déficit hors intérêts d'emprunt). Si travaux rénovation énergétique E/F/G → A/B/C/D payés entre 2023 et 2025: plafond doublé à 21 400 €. Déficit sur intérêts d'emprunt = reportable sur revenus fonciers uniquement (10 ans). Déficit total année = Revenus locatifs nets bruts − Charges déductibles. Charges déductibles = intérêts emprunt + travaux entretien/réparation + taxe foncière + assurances + frais gestion + provisions copropriété.

**Paramètres :**
- `plafond_standard` : 10700
- `plafond_renovation_energetique` : 21400
- `report_interets_annees` : 10

**Exceptions :**
- La fraction au-delà de 10 700 € (ou 21 400 €) est reportable sur revenus fonciers des 10 ans suivants
- La clause de location 3 ans obligatoire pour imputation sur revenu global

*Source: Guide fiscal PL 2025 Banque Populaire + CGI art. 156, IV Immobilier — pages 65-66*

---

### [FORM-007] Calcul seuil de rentabilité

**Formule :**
Seuil de rentabilité (SR) = Charges fixes / Taux de marge sur coûts variables. Taux MCV = (CA − Charges variables) / CA × 100. Point mort en jours = SR / (CA annuel / 365). CAF = Résultat net + Dotations aux amortissements. BFR = Stocks + Créances clients − Dettes fournisseurs. Fonds de roulement net global (FRNG) = Capitaux permanents − Actif immobilisé net. Trésorerie nette = FRNG − BFR.

*Source: Les bases de la comptabilité, Seuil de rentabilité*

---

## RISQUES ET PIÈGES

### [RISK-001] ⚠️ Risques LMNP/LMP

**Risque :**
RISQUE: Oubli de comptabiliser un amortissement dans la déclaration 2031 avant la date limite → amortissement définitivement perdu fiscalement (art. 39-C). Ne peut pas être rattrapé ultérieurement, même si l'amortissement est régularisé comptablement. L'amortissement non déduit à temps ne peut pas être inscrit dans le stock d'ARD.

**Conséquence :** Perte définitive de l'avantage fiscal → sur-imposition future

*Source: Guide fiscal LM ARCOLIB 2025, 3140*

---

### [RISK-002] ⚠️ Risques LMNP/LMP

**Risque :**
RISQUE: SCI optant pour la location meublée → soumise à l'IS de plein droit (activité commerciale). Cette option IS est IRRÉVOCABLE. La SCI perd: (1) l'abattement pour durée de détention sur les PV immobilières; (2) la possibilité de retourner à l'IR. Les dividendes distribués sont ensuite imposés au PFU 30 % (double imposition IS + PFU). Piège fréquent lors de la mise en location meublée d'un bien détenu en SCI IR.

**Conséquence :** Double imposition IS 25 % + PFU 30 % sur les dividendes; perte abattement PV

*Source: Guide patrimoine CV Finance 2022, Immobilier/SCI*

---

### [RISK-003] ⚠️ Risques BNC

**Risque :**
RISQUE: Utilisation d'un tableur Excel pour la comptabilité informatisée → non-conformité FEC. L'administration peut requalifier la comptabilité comme irrégulière, appliquer une taxation d'office et prononcer une amende de 5 000 € ou 10 % des droits rappelés. Le contribuable perd la protection d'une comptabilité régulière en cas de contrôle.

**Conséquence :** Rejet de la comptabilité; taxation d'office; amende

*Source: BNC — règles comptables, FEC*

---

### [RISK-004] ⚠️ Risques transmission

**Risque :**
RISQUE: Option IS irrévocable d'une SCI puis cession des parts → perte de l'abattement pour durée de détention sur PV immobilières (abattement qui exonère après 22 ans d'IR et 30 ans de PS). En IS, la PV de cession est imposée à l'IS 25 % quel que soit le nombre d'années de détention. Erreur fréquente lors d'une structuration patrimoniale à long terme.

**Conséquence :** PV imposée à IS 25 % au lieu de l'exonération totale possible après 22-30 ans

*Source: Guide patrimoine CV Finance 2022, Immobilier/SCI*

---

### [RISK-005] ⚠️ Risques IFI

**Risque :**
RISQUE: Donation temporaire d'usufruit à un enfant rattaché au foyer fiscal des parents pour réduire l'IFI → inopposable à l'administration fiscale. Le bien reste dans l'assiette IFI du donateur si les enfants sont rattachés au foyer fiscal (leurs biens/revenus sont agrégés dans le foyer fiscal des parents). Nécessite que les enfants soient DÉTACHÉS du foyer fiscal pour que la donation temporaire d'usufruit sorte le bien de l'assiette IFI.

**Conséquence :** IFI non réduit si enfant rattaché au foyer fiscal

*Source: Guide patrimoine CV Finance 2022, Immobilier/IFI*

---

### [RISK-006] ⚠️ Risques PV LMNP 2025

**Risque :**
RISQUE: LMNP au réel depuis de nombreuses années — amortissements déduits depuis 2025 réintégrés dans la base PV à la cession. Un investisseur qui amorti significativement son bien et le revend après plusieurs années de déduction verra sa PV imposable augmenter du montant des amortissements déduits depuis 2025. Impact d'autant plus fort si le bien est vendu peu après la mise en location (pas de bénéfice des abattements de durée de détention).

**Conséquence :** PV LMNP plus élevée qu'avant 2025 → impôt plus important à la revente

*Source: Guide fiscal LM ARCOLIB 2025, 6211-6213*

---

### [RISK-007] ⚠️ Risques BNC — PAS

**Risque :**
RISQUE: Modulation du taux PAS à la baisse sans atteindre le seuil minimum de 5 % d'écart → modulation refusée. RISQUE: sous-estimation des revenus BNC en cours d'année → acompte trop faible → pénalité de retard de majoration de 10 % sur la différence. Signaler systématiquement le risque de majoration si le contribuable envisage de réduire ses acomptes alors que ses revenus restent élevés.

**Conséquence :** Pénalité 10 % sur insuffisance d'acompte si écart > seuil

*Source: Guide fiscal PL 2025 Banque Populaire, PAS*

---

### [RISK-008] ⚠️ Risques Pacte Dutreil

**Risque :**
RISQUE: Non-respect des engagements de conservation dans un Pacte Dutreil → remise en cause de l'exonération de 75 % et rappel des droits avec pénalités et intérêts de retard. Les engagements collectifs et individuels de conservation doivent être strictement respectés sur toute leur durée. RISQUE annexe: cession de l'entreprise pendant la période d'engagement → rupture du pacte, sauf exceptions prévues (transmission dans le cadre familial sous conditions).

**Conséquence :** Rappel de 75 % des droits initialement exonérés + pénalités + intérêts de retard

*Source: Guide fiscal PL 2025 Banque Populaire, VI Transmission*

---

