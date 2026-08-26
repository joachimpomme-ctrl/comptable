# Golden Checklists

Checklists opérationnelles et workflows détaillés pour l'agent Gem.

## Domain Workflows (protocoles de raisonnement)

**Comptable:** Qualifier l'opération + régime (BNC/BIC/société/LM). Identifier la logique : trésorerie ou engagement. Classer : charge / immobilisation / produit / provision / amortissement / dette. Vérifier les pièces justificatives. Citer règle + source. Sortie minimale : traitement, justification, pièce à conserver, source, validation expert-comptable si ambigu.

**Fiscal:** Identifier l'année fiscale + régime. Vérifier seuils et conditions. Lister obligations déclaratives. Séparer fiscalité/comptabilité. Mentionner les exceptions. Citer les sources. Conclure prudemment. Ne jamais répondre sans millésime ou sans signaler son absence.

**LMNP/LMP:** Qualifier — meublé/nu, tourisme classé/non classé, LMNP ou LMP, micro-BIC ou réel. Traiter charges + amortissements (CGI art. 39-C). Vérifier déficits, TVA/parahôtellerie, CFE/cotisations. Alerter sur la plus-value à la sortie (réintégration amortissements déduits depuis 2025). Toujours distinguer : revenus 2024 déclarés 2025 / revenus 2025 déclarés 2026 / longue durée / meublé tourisme classé / non classé.

**Gestion financière:** Identifier l'objectif (trésorerie / rentabilité / BFR / CAF / point mort / financement). Lister les données nécessaires. Utiliser les formules de `04_formules_et_risques.md`. Calculer si données disponibles. Interpréter + proposer des actions. Citer les sources. Ne jamais conclure sur un seul ratio.

**Patrimoine:** Identifier la situation familiale + actifs/passifs/revenus/horizon/objectifs. Identifier le régime matrimonial/enfants/succession/protection. Analyser immobilier/AV/retraite/fiscalité/liquidité. Proposer des scénarios, pas des prescriptions. Lister risques + validations. Toujours distinguer : protection conjoint / transmission enfants / optimisation fiscale / liquidité / réversibilité.

## Comptabilité générale et PCG
- Qualifier l'opération : Nature, date, montant, tiers, justificatif.
- Identifier le traitement comptable : Comptes, bilan/compte de résultat, immobilisation ou charge.
- Vérifier la source PCG ou document corpus : Citer document et page.
- Contrôler les pièces : Facture, contrat, relevé, procès-verbal, calcul.
- Signaler les zones à revue : Norme, estimation, provision, amortissement, clôture.

## Fiscalité professionnelle BNC/BIC
- Identifier activité et régime : BNC/BIC, micro/réel, déclaration contrôlée, année.
- Vérifier seuils et millésime : Ne jamais appliquer un seuil sans date.
- Lister obligations : Déclarations, TVA, CFE, liasse, justificatifs.
- Séparer comptable et fiscal : Traitement comptable distinct de l'effet fiscal.
- Marquer validation : Expert-comptable/fiscaliste requis pour décision.

## Location meublée LMNP/LMP
- Qualifier location et statut : LMNP/LMP, meublé classique, tourisme, chambre d'hôtes.
- Comparer micro-BIC/réel : Recettes, abattement, charges réelles, amortissements, déficits.
- Contrôler TVA et parahôtellerie : Services fournis et conditions.
- Analyser plus-value : Statut, durée, régime applicable, date.
- Produire recommandation prudente : Options sourcées, pas de prescription sans validation.

## Gestion financière
- Définir l'objectif financier : Trésorerie, rentabilité, BFR, CAF, financement, seuil.
- Collecter les données : Chiffre d'affaires, charges, échéances, stocks, créances, dettes.
- Calculer les indicateurs : Formules sourcées, hypothèses explicites.
- Interpréter : Tendance, risque, marge de sécurité, leviers.
- Lister actions possibles : Impact, délai, risques.

## Gestion de patrimoine
- Établir le diagnostic : Famille, objectifs, actifs, passifs, revenus, horizon, risque.
- Cartographier les enveloppes : Immobilier, assurance-vie, retraite, liquidités, entreprise.
- Analyser transmission/protection : Donation, succession, régime matrimonial, bénéficiaires.
- Construire des scénarios : Bénéfices, risques, fiscalité, liquidité, réversibilité.
- Encadrer le conseil : Validation CGP/notaire/avocat selon sujet.

## Conformité et déontologie
- Identifier le niveau de risque : Fiscal, juridique, patrimonial, normatif.
- Exiger sources : Document et page.
- Afficher les limites : Hypothèses, millésime, incertitudes.
- Refuser si nécessaire : Pas de source, conflit, données manquantes.
- Tracer la réponse : Sources, date, statut candidat ou validé.

## Déclarations fiscales — Checklists et erreurs fréquentes

### Formulaire 2042 — IR général

**Qui :** tous contribuables personnes physiques. **Quand :** mai-juin N+1.

- [ ] Case 1AJ/1BJ : salaires (net imposable après abattement 10 %)
- [ ] Case 1AP/1BP : pensions et rentes
- [ ] Case 4BA : revenus fonciers nets régime réel (micro → case 4BE)
- [ ] Case 2DC/2TR : revenus capitaux mobiliers (dividendes, intérêts)
- [ ] Case 3VG : plus-values mobilières (renvoi 2074)
- [ ] Case 6RS/6RT/6RU : versements PER déductibles
- [ ] Case 7UF : dons associations (66 % réduction / 75 % aide aux personnes)
- [ ] Case 7DB : frais garde enfants (50 % crédit d'impôt)
- [ ] Quotient familial : parts, enfants à charge, garde alternée
- [ ] PAS : vérifier acompte tiers et solde

**Erreurs fréquentes :** oublier rachat AV partiel (→ 2042 C) — double comptage salaires + heures sup exonérées — oublier abattement 40 % dividendes option barème — ne pas reporter déficits fonciers antérieurs (10 700 €/an).

**Source CGI :** Art. 1 A, 13, 28-31, 150-0 A, 197 (M_CGI)

---

### Formulaire 2035 — BNC déclaration contrôlée

**Qui :** professions libérales CA > seuil micro-BNC (77 700 € revenus 2025 ; 83 600 € revenus 2026-2028 [referentiel: seuil_micro_bnc]) ou option réel. **Quand :** mai N+1.

- [ ] Ligne AA : encaissements TTC année civile (logique trésorerie)
- [ ] Ligne AB : honoraires rétrocédés (à déduire des recettes)
- [ ] Ligne AC : débours (remboursements frais avancés pour client)
- [ ] Ligne BV : loyer cabinet + charges locatives
- [ ] Ligne BT : cotisations sociales obligatoires payées (URSSAF, CARPIMKO/CARMF) + CSG déductible
- [ ] Ligne BU : cotisations Madelin / PER Madelin (dans plafond)
- [ ] Frais voiture : barème kilométrique (04_formules_et_risques.md REF-005) ou frais réels
- [ ] Amortissements : matériel médical 5-10 ans, mobilier 5-10 ans, informatique 3 ans
- [ ] TVA : exonéré si soins à la personne (CGI Art. 261) — sinon vérifier assujettissement
- [ ] CFE : base = recettes N-2, paiement décembre
- [ ] Résultat 2035 = recettes nettes − charges → reporter case 5QC/5RC sur 2042

**Erreurs fréquentes :** oublier cotisations sociales ligne BT — confondre date encaissement/facturation — ne pas amortir le matériel — dépasser plafond Madelin.

**Source CGI :** Art. 92-103, 154 bis (M_CGI) ; M1, M2

---

### Formulaire 2044 — Revenus fonciers régime réel

**Qui :** revenus fonciers bruts > 15 000 €/an ou option réel. **Quand :** joint à la 2042, mai N+1.

- [ ] Ligne 21 : loyers encaissés + charges récupérées
- [ ] Ligne 224 : frais gestion et administration
- [ ] Ligne 227 : primes d'assurance
- [ ] Lignes 229-230 : réparation, entretien, amélioration
- [ ] Ligne 231 : charges copropriété déductibles
- [ ] Ligne 250 : intérêts d'emprunt (déductibles sans limite en foncier)
- [ ] Ligne 251 : taxe foncière
- [ ] Déficit foncier : charges hors intérêts > recettes → imputable sur revenu global à 10 700 €/an ; surplus + intérêts reportables 10 ans sur foncier
- [ ] Location à des proches : vérifier loyer normal (risque requalification)
- [ ] SCI : reporter quote-part résultat sur 2044 S

**Erreurs fréquentes :** inclure travaux de construction (non déductibles) — confondre 10 700 € (revenu global) vs intérêts (foncier uniquement) — ne pas reporter déficits antérieurs.

**Source CGI :** Art. 14, 28-31, 156 (M_CGI) ; M9

---

### Formulaire 2048-IMM — Plus-values immobilières

**Qui :** vendeur d'un bien immo sauf résidence principale. **Quand :** lors de l'acte (notaire).

- [ ] Ligne 1 : prix de cession + charges assumées par l'acquéreur
- [ ] Ligne 2 : prix acquisition + frais (réels ou forfait 7,5 %) + travaux (réels ou forfait 15 % si > 5 ans)
- [ ] Abattements IR : 6 %/an de la 6e à la 21e année → exonération à 22 ans
- [ ] Abattements PS : 1,65 %/an (6-21 ans) + 1,60 % (22e) + 9 %/an (> 22 ans) → exonération à 30 ans
- [ ] Exonérations : résidence principale — cession < 15 000 € — 1ère cession RS si pas propriétaire RP depuis 4 ans — âge/invalidité — expropriation
- [ ] Taux : 19 % IR + 17,2 % PS = 36,2 % (hors exonérations)
- [ ] Surtaxe : +2 % à +6 % si PV nette > 50 000 €

**Source CGI :** Art. 150 U, 150 VB (M_CGI) ; M9

---

## Optimisation fiscale légale

### Règle générale

Utiliser les dispositifs légaux pour réduire l'impôt. **Licite :** abattements, régimes, déductions prévus par la loi. **Illicite :** abus de droit (Art. L64 LPF, pénalités Art. 1729 CGI), simulation, montages sans substance économique.

Pour toute stratégie : citer le dispositif légal exact + article CGI — vérifier éligibilité — chiffrer l'économie — signaler risques et contreparties — recommander validation fiscaliste/CGP.

### Leviers courants

| Dispositif | Économie | Conditions | Source |
|-----------|----------|------------|--------|
| PER | Versements déductibles × TMI | Plafond 10 % revenus N-1 (ou PASS), report 3 ans | CGI art. 163 quatervicies |
| Dons associations | Réduction 66 % (75 % aide aux personnes) | Don ≤ 20 % revenu imposable | CGI art. 200 |
| Déficit foncier | Imputation ≤ 10 700 €/an revenu global | Régime réel, travaux déductibles, location 3 ans | CGI art. 156 |
| Micro-BNC vs réel | Réel avantageux si charges > 34 % CA | CA ≤ 77 700 € (revenus 2025) / 83 600 € (revenus 2026-2028) pour micro | CGI art. 93, 102 ter |
| Quotient familial | Réduction TMI via demi-parts | Enfants à charge, invalidité, parent isolé | CGI art. 194-197 |
| Frais réels salariés | Déduction charges vs abattement 10 % | Si charges > 10 % salaire net | CGI art. 83 |
| PERCO/PEE | Abondement exonéré IR + PS (partiellement) | Dans plafonds légaux | M11 |

### Leviers avancés

| Dispositif | Mécanisme | Conditions et risques | Source |
|-----------|-----------|----------------------|--------|
| LMNP au réel | Amortissement bien → résultat fiscal nul/négatif | Nécessite compta, risque LMP si CA > 23 000 € | CGI art. 39 C, M5 |
| Démembrement | NP sortie du patrimoine taxable (IFI, succession) | Barème âge art. 669. Irréversible. | CGI art. 669, M6 |
| SCI à l'IR | Transparence fiscale, optimisation succession | Pas d'IS → PV pro impossibles | M6 |
| SCI à l'IS | Amortissement bien, capitalisation résultats | Double imposition sortie. Irréversible. | M6 |
| Pacte Dutreil | Abattement 75 % DMTG transmission entreprise | Engagement collectif + individuel conservation | CGI art. 787 B, M12 |
| Assurance-vie | Rachats allégés + transmission 152 500 €/bénéficiaire | Versements avant 70 ans, durée > 8 ans | CGI art. 125-0 A, 990 I |
| Donation-partage | Figer valeurs, abattement 100 000 € × enfant/15 ans | Irréversible. Notaire obligatoire. | CGI art. 779, 784 |

### Leviers profil libéral (BNC / TNS)

| Dispositif | Économie | Conditions | Source |
|-----------|----------|------------|--------|
| Madelin / PER Madelin | Déductibles BNC dans plafond (10 % + 25 % PASS) | Contrat éligible, cotisations régulières | CGI art. 154 bis |
| PER individuel TNS | Déduction revenu global + plafond majoré TNS | Revenu professionnel TNS | CGI art. 163 quatervicies |
| Option TVA | Récupérer TVA si activité partiellement taxée | Professions mixtes (ex. formations) | CGI art. 261 |
| Micro vs réel | Réel si charges + amortissements > 34 % CA | Analyse annuelle | CGI art. 93, 102 ter |
| SEL + SPFPL | Capitaliser bénéfices holding IS (15-25 % vs TMI 41-45 %) | Montage complexe, risque requalification | M7 |
| Véhicule / barème km | Barème BNC souvent plus avantageux | Tenir relevé kilométrique pro | M1, M2, REF-005 |

### Checklist optimisation annuelle (avant 31 décembre)

- [ ] Simuler économie PER selon TMI — maximiser si intérêt
- [ ] Maximiser dons si TMI élevée (66-75 % de réduction)
- [ ] Avancer ou décaler travaux déductibles selon exercice
- [ ] Comparer micro-BNC vs réel pour l'exercice en cours
- [ ] Vérifier abattements succession consommés (règle des 15 ans)
- [ ] Analyser opportunité donation avant fin d'année
- [ ] Vérifier plafonnement niches fiscales (max 10 000 €)
- [ ] Profils libéraux : maximiser Madelin/PER TNS avant 31/12

---

## Garde-fous transverses
- Règle fiscale obsolète : Toujours citer millésime et demander validation si décision.
- Confusion micro/réel : Comparer conditions, seuils, charges, amortissements et obligations.
- Conseil patrimonial définitif : Présenter scénarios et limites, validation CGP/notaire/avocat.
- Écriture comptable non sourcée : Exiger référence PCG/document corpus et pièces justificatives.
- Absence de page dans source Markdown/TXT : Citer le fichier et section/chunk, privilégier PDF paginé quand disponible.
- Surconfiance dans fiche candidate : Marquer `candidate` jusqu'à validation métier.