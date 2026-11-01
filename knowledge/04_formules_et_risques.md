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

### [FORM-002] Calcul PV LMNP (cessions depuis le 15/02/2025)

**Formule :**
PV brute LMNP (cessions depuis le 15/02/2025, CGI art. 150 VB, III) = Prix cession − (Prix acquisition majoré − TOTALITÉ des amortissements déduits pendant la location au titre de l'art. 39 C, quelle que soit leur date). Prix acquisition majoré (art. 150 VB, II) : + frais d'acquisition réels OU forfait de 7,5 % du prix d'acquisition (sans condition de durée) ; + travaux réels non déjà déduits OU forfait de 15 % si la cession intervient plus de 5 ans après l'acquisition (articulation des forfaits avec la minoration : à confirmer au BOFiP). PV nette imposable IR = PV brute × (1 − Abattement IR durée détention). PV nette imposable PS = PV brute × (1 − Abattement PS durée détention). IR = PV nette IR × 19 %. PS = PV nette PS × 17,2 % (taux maintenu en 2026 pour les plus-values immobilières). Taxe supplémentaire = barème par paliers sur la PV nette imposable à l'IR si elle dépasse 50 000 € (CGI art. 1609 nonies G).

*Corrigé le 2026-11-01 (audit) : date d'effet, totalité des amortissements, forfait de 7,5 % sans condition de durée, exceptions.*

**Paramètres :**
- `seuil_taxe_supplementaire` : 50000

**Taux :**
- `IR_pct` : 19
- `PS_pct` : 17.2

**Exceptions :**
- Cessions avant le 15/02/2025 : PV brute = Prix cession − Prix acquisition (amortissements non réintégrés)
- Pas de réintégration pour les logements situés dans : résidences pour étudiants, jeunes de moins de 30 ans en formation ou personnes de plus de 65 ans (CCH L631-12 et L631-13) ; établissements des 6° et 7° du I de l'art. L312-1 CASF ; résidences services agréées ; accueil familial salarié ; établissements de soins de longue durée
- LF 2026 : la minoration vise aussi les amortissements du statut du bailleur privé (art. 31, I, 1° i et j)

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
Ordre d'imputation : le revenu foncier brut s'impute d'abord sur les intérêts d'emprunt, puis sur les autres charges. Déficit imputable sur le revenu global = MIN(limite, déficit provenant des charges autres que les intérêts). Limite = 10 700 € [referentiel: deficit_foncier_plafond_standard], rehaussée du montant des dépenses de rénovation énergétique faisant passer le bien de E, F ou G à A, B, C ou D au plus tard le 31/12/2027, sans dépasser 21 400 € [referentiel: deficit_foncier_plafond_renovation_energetique]. Déficit provenant des intérêts et excédent au-delà de la limite : reportables sur les revenus fonciers des 10 années suivantes. Exemple : recettes 12 000 €, intérêts 4 000 €, travaux 25 000 € → 12 000 − 4 000 = 8 000 € ; 8 000 − 25 000 = −17 000 € ; 10 700 € imputables sur le revenu global, 6 300 € reportables.

*Corrigé le 2026-11-01 (audit) : ordre d'imputation, majoration non automatique, prorogation jusqu'au 31/12/2027 (CGI art. 156, I-3°, texte du 30/10/2026).*

Rappel : Déficit total année = Revenus locatifs nets bruts − Charges déductibles. Charges déductibles = intérêts emprunt + travaux entretien/réparation + taxe foncière + assurances + frais gestion + provisions copropriété.

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
RISQUE : une SCI qui donne un bien en location meublée exerce une activité commerciale. Elle devient passible de l'IS de plein droit (CGI art. 206, 2). Ce n'est pas une option : il n'y a donc rien à révoquer. Tolérance administrative : la société civile reste hors IS tant que ses recettes commerciales hors taxes ne dépassent pas 10 % de ses recettes totales hors taxes (BOFiP BOI-IS-CHAMP-10-30, § 320 et 330, version du 04/07/2018 lue le 01/11/2026 ; la location meublée y est traitée comme une activité commerciale, § 240 à 250).

À distinguer de l'option volontaire pour l'IS (CGI art. 239, 1). Elle n'est pas irrévocable d'emblée. La société peut y renoncer jusqu'au 5e exercice qui suit celui de l'option. La renonciation est notifiée avant la fin du mois qui précède la date limite de versement du premier acompte d'IS de l'exercice visé. Sans renonciation dans ce délai, l'option devient irrévocable. Après une renonciation, la société ne peut plus opter à nouveau pour l'IS.

Dans les deux cas, tant que la SCI est à l'IS : la cession de l'immeuble par la société ne bénéficie pas de l'abattement pour durée de détention ; les dividendes sont imposés au PFU (double imposition IS puis PFU). Piège fréquent lors de la mise en location meublée d'un bien détenu en SCI à l'IR.

*Corrigé le 2026-11-01 (audit) : le corps présentait l'IS comme une option « IRRÉVOCABLE ». Texte des art. 206 et 239 du CGI vérifié au 30/10/2026.*

**Conséquence :** Double imposition : IS (15 % jusqu'à 42 500 € de bénéfice, 25 % au-delà) puis PFU sur les dividendes (31,4 % s'ils sont perçus depuis le 01/01/2026, 30 % en 2025) [referentiel: pfu_taux_global] ; perte de l'abattement pour durée de détention

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
RISQUE: Option IS d'une SCI (devenue définitive après le 5e exercice qui la suit, art. 239) → perte de l'abattement pour durée de détention sur les PV immobilières (abattement qui exonère après 22 ans d'IR et 30 ans de PS). La cession de l'immeuble par la société est imposée à l'IS quel que soit le nombre d'années de détention, sur une valeur nette diminuée des amortissements. La cession des parts par l'associé relève, elle, des plus-values mobilières (PFU). Erreur fréquente lors d'une structuration patrimoniale à long terme.

*Corrigé le 2026-11-01 (audit) : option révocable pendant 5 exercices ; distinction cession de l'immeuble et cession des parts.*

**Conséquence :** PV imposée à l'IS au lieu de l'exonération totale possible après 22-30 ans

*Source: Guide patrimoine CV Finance 2022, Immobilier/SCI*

---

### [RISK-005] ⚠️ Risques IFI

**Risque :**
RISQUE: Donation temporaire d'usufruit à un enfant rattaché au foyer fiscal des parents pour réduire l'IFI → inopposable à l'administration fiscale. Le bien reste dans l'assiette IFI du donateur si les enfants sont rattachés au foyer fiscal (leurs biens/revenus sont agrégés dans le foyer fiscal des parents). Nécessite que les enfants soient DÉTACHÉS du foyer fiscal pour que la donation temporaire d'usufruit sorte le bien de l'assiette IFI.

**Conséquence :** IFI non réduit si enfant rattaché au foyer fiscal

*Source: Guide patrimoine CV Finance 2022, Immobilier/IFI*

---

### [RISK-006] ⚠️ Risques PV LMNP (cessions depuis le 15/02/2025)

**Risque :**
RISQUE: LMNP au réel depuis de nombreuses années. Pour toute cession depuis le 15/02/2025, la TOTALITÉ des amortissements déduits pendant la location (art. 39 C), y compris ceux déduits avant 2025, minore le prix d'acquisition (CGI art. 150 VB, III). Un investisseur qui a beaucoup amorti verra sa PV imposable augmenter d'autant. Impact d'autant plus fort si le bien est vendu peu après la mise en location (peu ou pas d'abattement pour durée de détention). Exceptions : résidences pour étudiants, jeunes en formation ou personnes âgées, établissements médico-sociaux, résidences services agréées, accueil familial salarié, soins de longue durée (voir FORM-002).

*Corrigé le 2026-11-01 (audit) : la version précédente limitait à tort la réintégration aux amortissements déduits depuis 2025.*

**Conséquence :** PV LMNP plus élevée qu'avant la réforme → impôt plus important à la revente

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
RISQUE : non-respect d'un engagement de conservation du Pacte Dutreil (CGI art. 787 B). L'exonération de 75 % est remise en cause. Les droits exonérés deviennent exigibles, majorés de l'intérêt de retard (art. 1727), dans le mois qui suit la rupture (CGI art. 1840 G ter, I).

Règles du texte en vigueur au 30/10/2026 (art. 787 B) :
- **Engagement collectif (a, b) :** au moins 2 ans, en cours au jour de la transmission. Il porte sur au moins 17 % des droits financiers et 34 % des droits de vote (10 % et 20 % si les titres sont cotés). Ces seuils sont à respecter pendant toute sa durée. Il est réputé acquis si une personne, seule ou avec son conjoint, partenaire de PACS ou concubin, détient depuis 2 ans des titres qui atteignent ces seuils, et si l'un d'eux exerce depuis 2 ans dans la société son activité principale ou, si la société est à l'IS, une fonction de direction. Après un décès sans engagement, les héritiers peuvent le conclure dans les 6 mois.
- **Engagement individuel (c) :** chaque héritier, donataire ou légataire conserve les titres **6 ans** à compter de la fin de l'engagement collectif. Durée de 6 ans pour les transmissions depuis le 21/02/2026, 4 ans auparavant (loi n° 2026-103, art. 8 ; BOFiP ACTU-2026-00114 du 10/08/2026).
- **Direction (d) :** un signataire ou un bénéficiaire exerce son activité principale (société de personnes) ou une fonction de direction (société à l'IS) pendant l'engagement collectif et les 3 ans qui suivent la transmission.
- **Biens exclus (3e alinéa) :** l'exonération ne porte pas sur la fraction de valeur des titres qui représente certains actifs non affectés exclusivement à l'activité, pendant au moins 3 ans avant la transmission (ou depuis leur acquisition) et jusqu'à la fin de l'engagement individuel : biens affectés à la chasse ou à la pêche ; véhicules de tourisme, yachts, bateaux de plaisance, aéronefs ; bijoux, métaux précieux, objets d'art, de collection ou d'antiquité (sauf régime de l'art. 238 bis AB) ; chevaux de course ou de concours ; vins et alcools ; logements et résidences. Même règle pour ces actifs détenus par une société contrôlée. Transmissions depuis le 21/02/2026 (même BOFiP).
- **Activité :** la société doit avoir une activité industrielle, commerciale, artisanale, agricole ou libérale. La gestion de son propre patrimoine mobilier ou immobilier en est exclue. Les titres ne doivent pas être inscrits sur un compte PME innovation (d bis).
- **Aucune condition de parenté** pour bénéficier de l'exonération.
- **Exceptions qui préservent l'exonération :** cession ou donation entre signataires pendant l'engagement collectif (b, 1) ; maintien pour les autres signataires si l'un d'eux cède, sous conditions (e bis) ; remise en cause limitée aux seuls titres cédés ou donnés par un bénéficiaire à un autre signataire (e ter) ; donation des titres par le bénéficiaire à ses descendants qui poursuivent l'engagement individuel (i) ; apport à une holding sous conditions (f) ; fusion, scission ou augmentation de capital (g, h) ; annulation des titres pour pertes ou liquidation judiciaire (g, h).
- **Entreprise individuelle (art. 787 C) :** conservation de l'ensemble des biens affectés à l'exploitation pendant 6 ans à compter de la transmission (texte au 30/10/2026 ; durée antérieure de 4 ans probable, date d'application à vérifier : voir TRM-003) ; un bénéficiaire poursuit l'exploitation pendant 3 ans.
- **Cumul :** réduction de 50 % des droits pour une donation en pleine propriété par un donateur de moins de 70 ans (art. 790).

**Conséquence :** Paiement des droits sur la part exonérée (75 % de la valeur), majorés de l'intérêt de retard (art. 1840 G ter et 1727)

*Corrigé le 2026-11-01 (audit) : durées, biens exclus et conséquence lus dans les art. 787 B, 787 C, 790 et 1840 G ter du CGI (texte du 30/10/2026). L'ancienne version annonçait des « pénalités » que le texte ne prévoit pas.*

*Source: Guide fiscal PL 2025 Banque Populaire, VI Transmission ; CGI art. 787 B, 787 C, 790, 1840 G ter (texte du 30/10/2026) ; BOFiP ACTU-2026-00114 et BOI-ENR-DMTG-10-20-40-10 (10/08/2026)*

---

## BARÈMES DE RÉFÉRENCE (Module M13 — millésimes 2025-2026)

> **Statut au 2026-11-01 :** PASS 2025-2026 et CARPIMKO `sourced` (arrêtés, bulletin de la caisse) ; taux URSSAF 2026 et CARMF 2026 probables (fiches URSSAF reprises par Weblex) ; réforme de l'assiette sociale intégrée (décret n° 2024-688) ; barème kilométrique des revenus 2025 identique à 2022-2024.  
> **Source de vérité des chiffres :** `referentiel_parametres.json` (clé + millésime). En cas d'écart avec un texte du corpus, le référentiel prime.  
> **Mise à jour :** janvier de chaque année (PASS, taux URSSAF, barèmes km publiés par arrêté).

### [REF-001] PASS 2025 et 2026

**PASS annuel 2025 : 47 100 € [referentiel: PASS/2025]** — PASS mensuel : 3 925 € | PASS journalier : 216 € (220 € en 2026)  
**PASS annuel 2026 : 48 060 € [referentiel: PASS/2026]** — PASS mensuel : 4 005 €

Utilisé pour : plafond PER (plancher de 10 % du PASS de l'année précédente : 4 710 € pour les versements de 2026 [referentiel: per_plafond_salarie_plancher/2026], 4 806 € pour ceux de 2027), Madelin, cotisations sociales des indépendants. Les seuils micro ne dépendent pas du PASS : ils sont actualisés tous les trois ans comme la première tranche du barème de l'IR (CGI art. 50-0 et 102 ter).

**Seuil micro-BNC associé (CGI art. 102 ter) : 77 700 € pour les revenus 2023-2025 ; 83 600 € pour les revenus 2026-2028 [referentiel: seuil_micro_bnc].**

*Source : Arrêté du 19/12/2024 (JO 29/12/2024) pour 2025 ; arrêté du 22/12/2025 (JO 23/12/2025) pour 2026*

---

### [REF-002] Cotisations URSSAF des professions libérales (2026)

Assiette : depuis la régularisation des revenus 2025 (avril 2026), assiette sociale unique égale au revenu professionnel abattu de 26 % (réforme de l'assiette, décret n° 2024-688). Les appels 2026 portent sur l'assiette sociale de 2025.

| Cotisation | Assiette | Taux 2026 |
|-----------|------|------|
| Maladie-maternité | Assiette sociale | 0 % sous 20 % du PASS (9 612 €), progressif jusqu'à 8,50 % à 3 PASS (144 180 €), 6,50 % sur la part au-delà [referentiel: tns_maladie_maternite_taux_max] |
| Maladie, praticiens et auxiliaires médicaux conventionnés (PAMC) | Revenus conventionnés | Même barème, pris en charge par l'Assurance maladie jusqu'à 8,40 points (reste à charge de l'ordre de 0,10 %) ; revenus hors convention : 3,25 % à 11,75 % |
| Indemnités journalières | 40 % du PASS minimum, 3 PASS maximum | 0,30 % (professions libérales réglementées, PAMC) ; artisans, commerçants et PL non réglementées : 0,50 % jusqu'à 5 PASS (probable) |
| Allocations familiales | Assiette sociale | 0 % sous 110 % du PASS (52 866 €), progressif jusqu'à 3,10 % à 140 % (67 284 €) |
| CSG-CRDS | Voir la note de la clé | 9,70 %, dont 6,80 % déductible [referentiel: tns_csg_crds_taux] |
| CURPS (professions de santé) | Revenu d'activité | 0,10 % (auxiliaires médicaux) à 0,50 % (médecins), plafonné à 240 € en 2026 |
| Formation professionnelle | PASS | 0,25 %, soit 120 € (0,34 % avec conjoint collaborateur) |
| Retraite de base, PL réglementée (CNAVPL), T1 | ≤ 1 PASS | 8,73 % (8,23 % jusqu'en 2024) [referentiel: tns_retraite_base_cnavpl_t1] |
| Retraite de base, PL réglementée (CNAVPL), T2 | 0 à 5 PASS, en plus de T1 | 1,87 % [referentiel: tns_retraite_base_cnavpl_t2] |
| Retraite de base, PL non réglementée (SSI) | ≤ 1 PASS / au-delà | 17,87 % / 0,72 % (depuis 2025, circulaire Cnav 2025-14) |

**Total charges sociales :** de l'ordre de 30 à 45 % selon le revenu et la caisse (ordre de grandeur, pas un taux).  
**Déduction 2035 :** cotisations EFFECTIVEMENT PAYÉES dans l'année (ligne BT), logique de trésorerie BNC.  
**Cotisations minimales :** dues même en cas de revenu nul ou déficitaire.

*Sources : CSS art. D621-2 ; URSSAF, fiche « Taux de cotisations 2026 - Praticien ou auxiliaire médical » (20/03/2026) reprise par Weblex le 21/04/2026 ; Weblex, médecins secteur 2, 04/05/2026 ; circulaire Cnav 2025-14. Corrigé le 2026-11-01 (audit) : l'ancienne version reprenait des taux d'avant la réforme 2025.*

---

### [REF-003] Cotisations CARMF (médecins), 2026

Cotisations **proportionnelles** pour l'essentiel (et non forfaitaires) :

| Poste | 2026 |
|-------|------|
| Retraite de base | 8,73 % jusqu'à 1 PASS (48 060 €) + 1,87 % jusqu'à 5 PASS (240 300 €), sur les revenus nets 2025 |
| Retraite complémentaire | 11,80 % jusqu'à 3,5 PASS (168 210 €) |
| ASV (secteur 2) | 5 751 € + 4 % du revenu conventionnel net 2025, plafonné à 5 PASS (secteur 1 : participation de l'Assurance maladie) |
| Invalidité-décès | 626 € (revenus < 1 PASS) à 1 010 € (> 3 PASS) |

> **Statut :** probable (Weblex du 04/05/2026 citant carmf.fr) : vérifier sur carmf.fr avant tout calcul.

---

### [REF-004] Cotisations CARPIMKO (auxiliaires médicaux), 2025 et 2026

Kinésithérapeutes, infirmiers, orthophonistes, pédicures-podologues, orthoptistes.

| Poste | 2025 | 2026 |
|-------|------|------|
| Retraite de base (CNAVPL, collectée par la CARPIMKO) | appels : 8,23 % jusqu'à 47 100 € + 1,87 % jusqu'à 235 500 € (base BNC N-1) | 8,73 % jusqu'à 48 060 € + 1,87 % jusqu'à 240 300 € (base assiette sociale N-1) |
| Retraite complémentaire | forfait de 2 312 € + 3 % entre 25 246 € et 231 840 € | forfait supprimé ; **8,70 %** entre 24 030 € et 144 180 € [referentiel: carpimko_complementaire_taux] |
| Invalidité-décès | 1 022 € | 1 022 € [referentiel: carpimko_invalidite_deces_forfait] |
| ASV (conventionnés, part de l'assuré) | 221 € + 0,16 % | 224 € + 0,16 % (Assurance maladie : 447 € + 0,24 %) |

> **Statut :** `sourced` (bulletin spécial CARPIMKO, assiette sociale, avril 2026). Corrigé le 2026-11-01 : la complémentaire 2025 n'était pas un « forfait par classe ».

---

### [REF-005] Barème kilométrique BNC — voitures (revenus 2022 à 2025)

*Source : arrêté du 27 mars 2023, barème reconduit pour les revenus 2023, 2024 et 2025 (brochure IR 2026). Identique au barème salarié (CGI art. 83). Revenus 2026 : un amendement au PLF 2027 prévoit une revalorisation, non définitive au 16/10/2026. Corrigé le 2026-11-01 : l'« arrêté du 2 février 2025 » cité auparavant n'a pas été trouvé.*

| Puissance fiscale | ≤ 5 000 km | 5 001–20 000 km | > 20 000 km |
|------------------|-----------|----------------|------------|
| 3 CV et moins | 0,529 €/km | (km × 0,316) + 1 065 | 0,370 €/km |
| 4 CV | 0,606 €/km | (km × 0,340) + 1 330 | 0,407 €/km |
| 5 CV | 0,636 €/km | (km × 0,357) + 1 395 | 0,427 €/km |
| 6 CV | 0,665 €/km | (km × 0,374) + 1 457 | 0,447 €/km |
| 7 CV et plus | 0,697 €/km | (km × 0,394) + 1 515 | 0,470 €/km |

**Exemple :** 5 CV, 9 000 km → (9 000 × 0,357) + 1 395 = **4 608 €** déductibles.

**Règles BNC :**
- Tenir un relevé kilométrique daté (date, trajet, client, km) — obligatoire en cas de contrôle.
- Choix annuel : barème **ou** frais réels (non irrévocable).
- Véhicule inscrit à l'actif du cabinet → frais réels uniquement, pas de barème.
- Véhicule 100 % électrique → majoration **+20 %** du barème (depuis 2023).

---

### [REF-006] ACRE : exonération de début d'activité (règles 2026)

- **Indépendant hors micro :** exonération partielle (25 %) des cotisations maladie, maternité, retraite de base, invalidité-décès et allocations familiales pendant 12 mois si le revenu professionnel ne dépasse pas 75 % du PASS (36 045 € en 2026) ; dégressive jusqu'au PASS (48 060 €) ; nulle au-delà.
- **Micro-entrepreneur :** taux minoré égal à 75 % du taux normal, jusqu'à la fin du 3e trimestre civil suivant le début d'activité.
- **Demande obligatoire** à l'URSSAF dans les 60 jours suivant le début d'activité ; réponse sous 30 jours, accord tacite à défaut. Pas d'ACRE si elle a été obtenue dans les 3 années précédentes.
- **Avant 2026 :** exonération totale sous 75 % du PASS (probable).
- **Attention :** ne couvre ni la CSG-CRDS ni la retraite complémentaire ; CARMF et CARPIMKO maintiennent leurs cotisations propres.
- *Sources : entreprendre.service-public.gouv.fr F11677 (vérifiée le 01/07/2026) ; Weblex, 18/02/2026. Corrigé le 2026-11-01 (audit).*

---

### [REF-007] Régularisation N-2 — Point de vigilance 2035

Les cotisations sont appelées sur les revenus **N-2** puis régularisées sur **N-1** après déclaration.  
Sur la 2035 : déduire les cotisations **effectivement payées** dans l'année civile, pas les cotisations dues.  
En phase de forte croissance : prévoir 1–2 ans de cotisations en décalage de trésorerie.

---

