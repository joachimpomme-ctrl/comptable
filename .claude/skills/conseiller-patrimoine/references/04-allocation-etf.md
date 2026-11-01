# Allocation, ETF, rééquilibrage

## 1. Construire une allocation en cinq étapes

1. **Une poche par objectif.** Chaque objectif a un montant, une date et une priorité (la charte les fixe). Règle d'horizon : moins de 5 ans, pas d'actions ; 5 à 8 ans, part d'actions limitée et décroissante ; plus de 8 ans, actions diversifiées (heuristique, `SKILL.md` section 5).
2. **Capacité de risque**, objective : stabilité et cyclicité des revenus, matelas, dettes, patrimoine immobilier, horizon. Un revenu de fonctionnaire ou de profession de santé est plus stable qu'un revenu de startup ou de commission.
3. **Tolérance au risque**, subjective : demander ce que la personne a fait lors des dernières baisses fortes, et formuler la perte en euros avec un pire cas réaliste (l'indice mondial a perdu environ 57 % en dollars de 2007 à 2009) : « ta poche long terme vaut 200 000 €, elle tombe à 90 000 € en dix-huit mois : que fais-tu ? ». Une réponse « je vends » fixe le plafond d'actions plus sûrement qu'un questionnaire.
4. **Allocation neutre** : actions mondiales pondérées par les capitalisations pour le long terme ; supports sans risque actions pour le court terme. Tout écart à la neutralité (pays, secteur, style, petites capitalisations) est un pari à justifier par écrit.
5. **Écrire les règles** dans la charte : poids cibles, bandes de tolérance, rééquilibrage, ce qu'on fait dans une baisse de 30 %.

## 2. Exposition géographique

- Indices de référence : MSCI ACWI ou FTSE All-World (pays développés et émergents), MSCI World (développés seulement), MSCI Emerging Markets, MSCI Europe ou STOXX Europe 600.
- Les poids par pays changent : les lire sur la fiche mensuelle de l'éditeur, datée. Le poids des États-Unis dans les indices mondiaux est élevé ; c'est l'état du marché, pas une erreur. Le réduire par une surpondération Europe ou émergents est un choix actif, défendable (diversification des devises et des valorisations, concentration de quelques grandes sociétés américaines) et discutable (sous-performance possible pendant longtemps).
- Calcul d'exposition par transparence : `allocation.py`, avec les poids par zone de chaque fonds tirés de sa fiche et datés.
- Exemple de lecture : un portefeuille 80 % MSCI World, 10 % Europe, 10 % émergents a une part d'États-Unis égale à 0,8 fois le poids américain du MSCI World, une part d'Europe égale à 0,8 fois le poids européen du World plus 10 %, etc. Faire le calcul avec les poids du jour, pas de mémoire.

## 3. Choisir un ETF

Critères dans l'ordre :

1. **L'indice** : ce qu'il contient (pays, taille, nombre de titres, méthode de pondération). Deux ETF « monde » peuvent suivre des indices différents.
2. **L'enveloppe** : éligibilité PEA (DIC ou liste de l'émetteur), sinon compte-titres ou assurance-vie (liste des supports du contrat).
3. **Les frais** : frais courants (TER) dans le DIC ; mieux, l'écart de suivi réel (tracking difference) sur plusieurs années, dans le rapport annuel ou la fiche de l'émetteur.
4. **La taille et l'ancienneté** : un encours faible expose à une fermeture (liquidation, fiscalement pénible hors enveloppe). Seuil courant de prudence : quelques centaines de millions d'euros d'encours (heuristique).
5. **La réplication** : physique (détient les titres, peut prêter ses titres) ou synthétique (contrat d'échange). Les deux sont encadrées par la réglementation OPCVM. En PEA, l'exposition hors Europe passe par la réplication synthétique.
6. **Capitalisation ou distribution** : dans un PEA ou une assurance-vie, la capitalisation évite de gérer des dividendes ; sur compte-titres, elle reporte l'imposition à la vente.
7. **La devise** : la devise de cotation ne change rien au risque de change, qui dépend des actifs détenus. Une part couverte en euros (« hedged ») réduit le risque de change, avec un coût lié au différentiel de taux.
8. **La liquidité en bourse** : fourchette achat-vente sur Euronext, éviter les premières et dernières minutes de séance.
9. **La domiciliation** (Irlande, Luxembourg, France) : effet sur la retenue à la source des dividendes étrangers pour les fonds physiques ; détail technique, secondaire par rapport aux frais et à l'indice.

Toujours identifier l'ETF par son ISIN, lire le DIC chez l'émetteur et dater les chiffres. Un comparateur (justETF) aide à lister les candidats.

## 4. Poche sans risque actions

| Support | Liquidité | Risque | Usage |
|---|---|---|---|
| Livrets réglementés | Immédiate | Aucun en capital | Matelas, projets courts, dans la limite des plafonds |
| Fonds en euros | Rachat sous quelques jours | Garantie de l'assureur selon contrat | Projet à 1 à 8 ans, poche « maison », part sans risque d'un horizon de 5 à 8 ans |
| Fonds monétaire, ETF monétaire | Quelques jours | Très faible, pas de garantie | Attente, complément des livrets |
| Compte à terme | À l'échéance | Aucun en capital | Montant et date connus |
| Obligations d'État ou fonds obligataires à échéance (fonds datés) | Variable | Taux et crédit ; faible si détention jusqu'à l'échéance | Projet daté, rendement connu à l'avance si détenu à l'échéance |
| Fonds obligataires sans échéance | Quotidienne | Perd de la valeur quand les taux montent (sensibilité) | Diversification d'un portefeuille long |

Règle : la durée des obligations (sensibilité) ne dépasse pas l'horizon du besoin.

## 5. Rééquilibrage

- **Par les flux d'abord** : diriger chaque versement vers la ligne la plus sous-pondérée. Aucun frais de vente, aucun impôt. `allocation.py` calcule la répartition.
- **Revue annuelle** (janvier dans la charte) : si une ligne sort de sa bande, arbitrer.
- **Bandes de tolérance** : par exemple ±5 points absolus pour une ligne cible supérieure à 20 %, ±25 % relatifs pour une petite ligne (règle dite 5/25, heuristique).
- **Dans un PEA ou une assurance-vie**, arbitrer ne déclenche pas d'impôt ; sur compte-titres, si.
- Après une forte baisse, le rééquilibrage fait acheter des actions : c'est voulu, et c'est là que la règle écrite sert.

## 6. Investir une grosse somme (déblocage, héritage, vente)

1. Séparer d'abord ce qui sert un projet daté (poche courte) de ce qui est long terme.
2. Pour la part long terme : l'investissement immédiat gagne le plus souvent (`02-doctrine.md` 5.3). Si la crainte du regret risque de bloquer, fixer un calendrier d'étalement par écrit (par exemple 6 à 12 versements mensuels égaux), et ne plus le modifier selon l'actualité.
3. Respecter les plafonds d'enveloppe : un PEA reçoit au plus son plafond de versement restant ; le reste va en assurance-vie ou compte-titres.
4. Noter la décision dans le journal, avec le contre-argument.

## 7. Gestion pilotée, robo-conseillers, fonds profilés

- Utile si elle évite des erreurs de comportement. Comparer le coût total (frais du contrat, frais de gestion pilotée, frais des fonds) à un ETF mondial en gestion libre.
- Lire l'allocation réelle du profil choisi, pas seulement son nom.

## 8. Signaux d'alerte sur une allocation

- Plus de 10 % du patrimoine financier sur une seule société (employeur compris).
- Argent d'un projet à moins de 5 ans investi en actions.
- Plus de trois ou quatre fonds qui se recouvrent (plusieurs fonds « monde » et « USA » ensemble).
- Frais totaux supérieurs à 1 % par an sur la poche actions sans raison démontrée.
- Une allocation qu'aucun des deux membres du couple ne sait expliquer en deux phrases.
