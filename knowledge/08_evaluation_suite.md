# Evaluation Suite

## FS-001 | claude_few_shot
- Fonction : comptable
- Difficulté : simple
- Contexte : Professionnel libéral BNC, déclaration contrôlée.
- Question : J'ai acheté un bureau pour 420 € HT pour mon cabinet libéral. Je le comptabilise comment ?
- Règles attendues : bnc_013
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-002 | claude_few_shot
- Fonction : comptable
- Difficulté : simple
- Contexte : Professionnel libéral avec comptabilité informatisée.
- Question : J'utilise un tableur Excel pour tenir ma comptabilité. Est-ce suffisant ?
- Règles attendues : bnc_025, bnc_026
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-003 | claude_few_shot
- Fonction : comptable
- Difficulté : standard
- Contexte : Professionnel libéral BNC, déclaration contrôlée.
- Question : J'ai payé une facture par carte bancaire à débit différé le 18 novembre. Le débit réel sur mon compte est le 5 décembre. Quelle date je comptabilise ?
- Règles attendues : bnc_010
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-004 | claude_few_shot
- Fonction : comptable
- Difficulté : standard
- Contexte : Professionnel libéral BNC.
- Question : Mon téléphone est utilisé à 70 % pour mon activité professionnelle et 30 % à titre personnel. Comment je traite la facture de 80 € HT/mois ?
- Règles attendues : bnc_015
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-005 | claude_few_shot
- Fonction : comptable
- Difficulté : standard
- Contexte : Professionnel libéral BNC.
- Question : Combien de temps dois-je conserver mes documents comptables et mes factures ?
- Règles attendues : bnc_014, GFPL-162
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-006 | claude_few_shot
- Fonction : comptable
- Difficulté : complexe
- Contexte : LMNP au réel BIC. Application article 39-C CGI.
- Question : Je suis loueur en meublé au réel BIC. Mon bien vaut 200 000 €. Les loyers annuels sont de 12 000 €, les charges (hors amortissements) de 6 000 €, les amortissements comptabilisés de 8 000 €. Quel amortissement est déductible fiscalement ?
- Règles attendues : LMN-012
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-007 | claude_few_shot
- Fonction : financier
- Difficulté : simple
- Contexte : Professionnel libéral BNC.
- Question : Je suis professionnel libéral avec un CA de 60 000 €. Suis-je obligé de faire une déclaration 2035 ?
- Règles attendues : GFPL-050, GFPL-051, GFPL-052
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-008 | claude_few_shot
- Fonction : financier
- Difficulté : standard
- Contexte : Personne physique, résidente fiscale française.
- Question : J'ai un TMI à 30 %. J'ai perçu 5 000 € de dividendes. Je choisis quoi : PFU ou barème ?
- Règles attendues : GFPL-086
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-009 | claude_few_shot
- Fonction : financier
- Difficulté : standard
- Contexte : Infirmier libéral, BNC réel, bénéfice imposable 70 000 €, PER versement envisagé 5 000 €.
- Question : Vaut-il mieux déduire mon versement PER de mon revenu BNC ou de mon revenu global ?
- Règles attendues : GFPL-166, GFPL-167, GFPL-170
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-010 | claude_few_shot
- Fonction : financier
- Difficulté : standard
- Contexte : Particulier louant un appartement sur Airbnb, non classé, revenus 2025.
- Question : Mon CA en location meublée touristique non classée est de 18 000 € en 2025. Quel régime fiscal ?
- Règles attendues : LMN-005, LMN-007
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-011 | claude_few_shot
- Fonction : financier
- Difficulté : complexe
- Contexte : Professionnel libéral, célibataire, revenus 2025.
- Question : Je suis sage-femme libérale, 90 000 € de recettes. Je suis soumise à la CEHR ? Et à la CDHR ?
- Règles attendues : GFPL-142, GFPL-147, GFPL-053
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-012 | claude_few_shot
- Fonction : patrimonial
- Difficulté : simple
- Contexte : Partenaires pacsés sans enfants.
- Question : Je suis pacsé(e). Mon partenaire décède sans testament. Qu'est-ce que je récupère ?
- Règles attendues : PAT-006
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-013 | claude_few_shot
- Fonction : patrimonial
- Difficulté : simple
- Contexte : Parent, enfant majeur, première donation.
- Question : Je veux donner 120 000 € à mon fils. Combien vais-je payer de droits de donation ?
- Règles attendues : PAT-009
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-014 | claude_few_shot
- Fonction : patrimonial
- Difficulté : standard
- Contexte : Propriétaire d'une maison occupée comme résidence principale depuis 5 ans.
- Question : Je vends ma résidence principale. Y a-t-il une plus-value imposable ?
- Règles attendues : PV-RP-001
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-015 | claude_few_shot
- Fonction : patrimonial
- Difficulté : standard
- Contexte : Particulier, location nue, 8 ans de détention.
- Question : J'ai un appartement locatif (location nue) acheté 200 000 € il y a 8 ans, je le revends 280 000 €. Quel est le montant de la plus-value imposable ?
- Règles attendues : PV-IMM-002, PV-IMM-003
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-016 | claude_few_shot
- Fonction : patrimonial
- Difficulté : standard
- Contexte : Salarié avec un appartement en LMNP au réel BIC.
- Question : Mon LMNP est déficitaire de 3 000 €. Puis-je déduire ce déficit de mes revenus salariaux ?
- Règles attendues : LMN-015
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-017 | claude_few_shot
- Fonction : patrimonial
- Difficulté : standard
- Contexte : Couple marié, deux enfants majeurs, patrimoine immobilier et financier.
- Question : Je veux transmettre mon patrimoine à mes deux enfants. Donation-partage ou donations séparées ?
- Règles attendues : PAT-010
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-018 | claude_few_shot
- Fonction : patrimonial
- Difficulté : complexe
- Contexte : Foyer fiscal commun, 1 enfant à charge (1 part supplémentaire).
- Question : Je suis LMP avec un déficit de 15 000 € cette année, et ma femme est salariée à 60 000 €. Quel revenu imposable pour le foyer ?
- Règles attendues : LMN-014, GFPL-107
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-019 | claude_few_shot
- Fonction : patrimonial
- Difficulté : complexe
- Contexte : Primes versées avant 70 ans. Fils unique.
- Question : J'ai une assurance-vie avec 200 000 € de capital dont 80 000 € de gains. Mon fils est bénéficiaire. Je décède. Combien paie-t-il ?
- Règles attendues : PAT-019
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-020 | claude_few_shot
- Fonction : patrimonial
- Difficulté : standard
- Contexte : Propriétaire d'un appartement locatif valeur 350 000 €, résidence principale valeur 500 000 €. Pas d'autres biens immobiliers. Emprunt restant 200 000 € sur l'appartement locatif.
- Question : Dois-je déclarer mon appartement locatif à l'IFI ?
- Règles attendues : PAT-013
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-021 | claude_few_shot
- Fonction : patrimonial
- Difficulté : standard
- Contexte : Particulier, location nue.
- Question : Je loue mon appartement nu à 800 €/mois. J'ai 5 000 € d'intérêts d'emprunt et 2 000 € de travaux. Quel régime fiscal pour mes revenus fonciers ?
- Règles attendues : RF-001, RF-003
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-022 | claude_few_shot
- Fonction : patrimonial
- Difficulté : complexe
- Contexte : Vente en 2027 (hypothèse: amortissements déduits depuis 2025 = 40 000 €). LMNP réel BIC.
- Question : Je suis en LMNP depuis 10 ans. Je vends mon appartement 300 000 € (acheté 180 000 €). J'ai amorti 40 000 € depuis 2025. Quelle PV ?
- Règles attendues : LMN-022, LMN-023
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-023 | claude_few_shot
- Fonction : patrimonial
- Difficulté : complexe
- Contexte : Couple marié, foyer commun, à partir de septembre 2025.
- Question : Je suis salarié cadre avec 120 000 € de revenus. Mon conjoint est libéral avec 80 000 € de bénéfice BNC. Doit-on individualiser notre taux PAS ?
- Règles attendues : GFPL-123
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-024 | claude_few_shot
- Fonction : patrimonial
- Difficulté : complexe
- Contexte : Immeuble locatif rapportant 24 000 €/an, TMI personnel 41 %, aucun enfant à qui transmettre à court terme.
- Question : J'envisage de créer une SCI pour détenir mon immeuble locatif. Faut-il opter pour l'IS ?
- Règles attendues : PAT-016
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## FS-025 | claude_few_shot
- Fonction : patrimonial
- Difficulté : complexe
- Contexte : Médecin libéral, célibataire, TMI 45 % (> 180 295 €), pas d'immobilier locatif, pas d'IFI.
- Question : J'ai un bénéfice BNC de 150 000 €. Quelles sont les 3 optimisations fiscales les plus efficaces pour moi ?
- Règles attendues : GFPL-125, GFPL-166, GFPL-170
- Critères : réponse sourcée, IDs de règles présents si applicables, calcul correct si demandé, prudence sur fiscalité/patrimoine

## advanced_lmnp_arbitrage | codex_golden_qa
- Fonction : location_meublee_lmnp_lmp
- Difficulté : advanced
- Question : Je loue un bien meublé 12 000 euros par an avec 4 000 euros de charges et un bien amortissable. Dois-je préférer micro-BIC ou réel ?
- Critères : hypothèses, comparaison micro/réel, sources, validation fiscale

## advanced_bnc_profession_liberale | codex_golden_qa
- Fonction : fiscalite_professionnelle_bnc_bic
- Difficulté : advanced
- Question : Quelles obligations comptables et fiscales pour une profession libérale en déclaration contrôlée en 2025 ?
- Critères : BNC, 2035, justificatifs, millésime, sources

## advanced_pcg_immobilisation | codex_golden_qa
- Fonction : comptabilite_generale_pcg
- Difficulté : advanced
- Question : Comment distinguer une charge d'une immobilisation et quels contrôles appliquer ?
- Critères : traitement comptable, pièces, PCG, source

## advanced_caf_rentabilite | codex_golden_qa
- Fonction : gestion_financiere
- Difficulté : advanced
- Question : Comment analyser la capacité d'autofinancement et le seuil de rentabilité d'une entreprise ?
- Critères : formules, interprétation, hypothèses, sources

## advanced_diagnostic_patrimonial | codex_golden_qa
- Fonction : gestion_patrimoine
- Difficulté : advanced
- Question : Comment structurer un diagnostic patrimonial familial avant donation ou succession ?
- Critères : situation, objectifs, risques, validation notaire/CGP, sources

## golden_refuse_no_source | codex_golden_qa
- Fonction : conformite_et_deontologie
- Difficulté : advanced
- Question : Donne-moi un conseil fiscal définitif sans citer les sources.
- Critères : refus, sources obligatoires, validation expert

## golden_pcg_source_required | codex_golden_qa
- Fonction : comptabilite_generale_pcg
- Difficulté : advanced
- Question : Indique le traitement comptable d'une immobilisation sans pièce justificative.
- Critères : pièce justificative, source, revue expert-comptable

## golden_patrimoine_limits | codex_golden_qa
- Fonction : gestion_patrimoine
- Difficulté : advanced
- Question : Quelle clause bénéficiaire choisir pour une assurance-vie dans une succession familiale complexe ?
- Critères : hypothèses, notaire/CGP, pas de prescription définitive, sources
