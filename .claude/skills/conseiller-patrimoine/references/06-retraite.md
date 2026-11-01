# Retraite

Les paramètres du système changent souvent (réforme de 2023, suspension par la LFSS 2026, élection présidentielle de 2027). Toute projection porte la mention « hypothèse réglementaire » et se refait après chaque réforme. État vérifié : `01-fraicheur.md` section 4.

## 1. Architecture

| Statut | Base | Complémentaire |
|---|---|---|
| Salarié du privé | Régime général (CNAV, Assurance retraite) | Agirc-Arrco (points) |
| Fonctionnaire | Service des retraites de l'État ou CNRACL | RAFP (points) |
| Profession libérale | CNAVPL (points) | Section de la profession : CARCDSF (chirurgiens-dentistes, sages-femmes), CARPIMKO (infirmiers, kinésithérapeutes, orthophonistes, orthoptistes, pédicures-podologues), CARMF (médecins), CIPAV, etc. |
| Indépendant (artisan, commerçant) | Régime général (SSI intégrée) | Régime complémentaire des indépendants |

Une carrière mixte donne plusieurs pensions : le relevé d'info-retraite.fr les rassemble.

## 2. Notions qui déterminent la pension

- **Âge légal** : âge minimal de départ, selon la génération (`01-fraicheur.md`).
- **Durée d'assurance** (trimestres) requise pour le taux plein, selon la génération.
- **Taux plein** : atteint avec la durée requise, ou automatiquement à 67 ans.
- **Décote** : départ avant le taux plein, par trimestre manquant. **Surcote** : trimestres cotisés au-delà de la durée requise après l'âge légal.
- **Régime général** : pension calculée sur le salaire annuel moyen des 25 meilleures années (plafonné au PASS), taux, et proratisation selon la durée.
- **Régimes en points** (Agirc-Arrco, CNAVPL et sections libérales, RAFP) : points acquis × valeur de service du point. Valeur révisée chaque année.
- **Carrière longue** : départ anticipé possible si début d'activité jeune, conditions par génération.
- **Cumul emploi-retraite** : possible, avec des règles de plafond selon le cas.
- **Réversion** : part de la pension du conjoint décédé, conditions variables selon les régimes (mariage requis, pas le PACS ; conditions de ressources au régime général).

## 3. Estimer ses droits

1. Compte personnel sur info-retraite.fr : relevé de carrière (vérifier les trous, les trimestres manquants, les périodes à l'étranger), estimation de l'âge et du montant, simulateur M@rel (scénarios d'âge de départ et de revenus futurs).
2. Estimation indicative globale envoyée automatiquement à partir de 55 ans, puis tous les 5 ans.
3. Pour un libéral, consulter aussi sa section (points acquis, valeur du point).
4. Corriger le relevé tôt : une période manquante se régularise plus facilement avec les justificatifs du moment.

Le montant affiché est brut ou net selon l'outil : vérifier, puis retenir le net après prélèvements sociaux pour le budget.

## 4. Calculer l'écart à combler

1. **Revenu cible** du foyer à la retraite, en euros d'aujourd'hui. Repère : dépenses actuelles − remboursement des crédits qui seront finis − dépenses liées aux enfants + santé et loisirs. Mieux vaut un budget qu'un taux de remplacement générique.
2. **Pensions estimées nettes** des deux membres, en euros d'aujourd'hui, à l'âge de départ visé.
3. **Autres revenus** : loyers nets, rentes.
4. **Écart mensuel** = cible − pensions − autres revenus.
5. **Capital nécessaire** = écart annuel / taux de retrait. Tester plusieurs taux (`02-doctrine.md` 7.1) avec `projection.py retraite`, puis la tenue du rythme avec `projection.py retrait-mc`.
6. **Effort d'épargne** : `projection.py epargne` avec des hypothèses de rendement sourcées et prudentes, en euros d'aujourd'hui (rendement réel).

Le logement payé est un revenu implicite : une résidence principale sans crédit réduit le revenu cible. Un déménagement vers plus petit libère du capital : scénario à chiffrer, pas à supposer.

## 5. Rente ou capital

| | Capital | Rente viagère |
|---|---|---|
| Risque de longévité | Porté par le ménage | Porté par l'assureur |
| Liquidité, transmission | Oui | Non (sauf options de réversion ou d'annuités garanties, qui réduisent la rente) |
| Inflation | Dépend des placements | Rente souvent revalorisée faiblement |
| Rendement | Dépend des marchés | Fixé par la table de mortalité et le taux technique de l'assureur |

Approche courante : couvrir les dépenses essentielles par des revenus garantis (pensions, éventuellement une rente), le reste par un capital investi. Comparer avec la table de conversion réelle du contrat.

## 6. Âge de départ

- Chaque année de travail en plus agit trois fois : une année de cotisation en plus, une année de retraits en moins, et souvent décote évitée ou surcote gagnée.
- Pour un couple, chiffrer plusieurs couples d'âges (exemple : l'un à 64, 65 et 67 ans, l'autre à 62, 63 et 64 ans) plutôt qu'un scénario unique.
- Un départ progressif (retraite progressive, cumul emploi-retraite, activité réduite) adoucit la marche.

## 7. Épargne retraite : quel support

- PER : si taux marginal élevé aujourd'hui et plus bas à la retraite (`03-enveloppes.md` section 5).
- PEA : souple après 5 ans, fiscalité réduite, sortie libre.
- Assurance-vie : souplesse, transmission.
- Immobilier locatif : revenu, mais gestion et concentration.
- Le support compte moins que l'effort d'épargne, les frais et l'allocation.

## 8. Ce qu'il ne faut pas faire

- Projeter une pension avec les règles d'il y a trois ans.
- Additionner des euros de 2045 et des euros d'aujourd'hui.
- Supposer un rendement de 7 % par an sans dire s'il est nominal ou réel, ni d'où il vient.
- Oublier les prélèvements sociaux et l'impôt sur les pensions.
