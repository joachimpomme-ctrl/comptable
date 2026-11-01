# Immobilier et crédit

Règles en vigueur et dates : `01-fraicheur.md`. Fiscalité (plus-values, LMNP, revenus fonciers, droits de mutation au détail) : `expert-comptable`.

## 1. Budget d'un achat de résidence principale

Coût total = prix + frais d'acquisition + travaux + frais de garantie et de dossier + déménagement et équipement.

- **Frais d'acquisition** (« frais de notaire ») : surtout des droits de mutation. Ordre de grandeur courant 7 à 8 % du prix dans l'ancien et 2 à 3 % dans le neuf (heuristique) ; chiffre exact avec le simulateur de notaires.fr et le taux du département (`01-fraicheur.md`, hausse possible jusqu'au 31/03/2028).
- **Garantie** : caution d'un organisme (une partie peut être restituée en fin de prêt), hypothèque conventionnelle ou hypothèque légale spéciale du prêteur de deniers (ex-privilège de prêteur de deniers, renommé au 01/01/2022). Demander le coût de chacune, mainlevée comprise en cas de revente.
- **Apport** : les banques demandent souvent qu'il couvre au moins les frais d'acquisition (pratique bancaire, variable).
- **Capacité** : `capacite.py` (taux d'effort HCSF, durée, assurance, reste à vivre).

## 2. Les règles d'octroi (HCSF)

- Taux d'effort : total des charges de crédit, assurance comprise, rapporté aux revenus nets avant impôt, au plus 35 %. Durée au plus 25 ans (27 avec différé dans certains cas). Une part de la production des banques peut déroger (détail dans `01-fraicheur.md`).
- Revenus locatifs : les banques en retiennent en général une fraction (souvent 70 %, pratique courante, à confirmer avec la banque).
- Le reste à vivre (revenus moins charges de crédit et charges fixes) pèse dans la décision de la banque au-delà du ratio.
- Le taux d'usure plafonne le TAEG : un dossier avec une assurance chère peut buter dessus.

## 3. Acheter avant de vendre, ou l'inverse

| Schéma | Avantage | Risque | Quand |
|---|---|---|---|
| Vendre d'abord | Prix de vente connu, pas de double charge | Logement temporaire, déménagement double | Marché lent ou incertain, budget tendu |
| Acheter d'abord avec prêt relais | On choisit le bien sans pression | Vente plus longue ou moins chère que prévu, double charge | Marché local liquide, bien à vendre facile, marge de sécurité sur le prix |
| Vente et achat coordonnés (promesse d'achat avec délai, condition suspensive de vente si le vendeur l'accepte) | Pas de relais | Négociation, calendrier serré | Vendeur souple |

**Prêt relais** (pratique bancaire, à confirmer) : avance d'une partie de la valeur estimée du bien à vendre (souvent 50 à 70 %, diminuée du capital restant dû du prêt en cours), durée 12 mois renouvelable une fois, intérêts seuls payés chaque mois ou capitalisés, remboursement à la vente.
- Tester le scénario défavorable avec `capacite.py achat-revente` : vente 10 % sous le prix espéré (le script vérifie que la vente couvre relais et capital restant dû) et 6 mois de portage de plus que prévu (coût affiché par durée).
- Règle HCSF depuis décembre 2023 (probable) : les intérêts d'un relais adossé à un crédit d'acquisition peuvent sortir du taux d'effort si le relais ne dépasse pas 80 % de la valeur du bien vendu. Faire confirmer par la banque le calcul retenu pendant la période de portage.

**Apport issu d'une vente** = prix net vendeur − capital restant dû − indemnités de remboursement anticipé (dues en principe en cas de simple vente ; exclues par la loi si la vente suit un changement de lieu d'activité professionnelle, le décès ou la cessation forcée d'activité de l'emprunteur ou de son conjoint, C. consom. art. L313-48 ; l'offre peut prévoir mieux) − frais de mainlevée et diagnostics. La plus-value sur la résidence principale est exonérée sous conditions (CGI art. 150 U, II, 1°, via `expert-comptable`).

**Prêt en cours à taux bas** : avant de le solder, lire l'offre de prêt pour une clause de transférabilité. Transférer un prêt ancien à taux bas sur le nouveau bien peut valoir plusieurs milliers d'euros quand les taux de marché sont plus hauts (`02-doctrine.md` 9.2). Clause rare et négociée, mais à vérifier.

## 4. Crédit : leviers et pièges

- **Taux** : comparer les offres par le TAEG et le coût total sur la durée, pas par le taux nominal seul. Un courtier inscrit à l'ORIAS (IOBSP) peut faire jouer la concurrence ; vérifier sa rémunération.
- **Assurance emprunteur** : souvent le second coût du crédit. Délégation possible dès l'offre, changement à tout moment (loi Lemoine). Comparer à garanties équivalentes. Quotités dans un couple : 100 % sur chaque tête protège le survivant mais coûte plus ; 50/50 coûte moins mais laisse la moitié du prêt au survivant.
- **Modulation et report d'échéances** : options gratuites souvent prévues par l'offre ; lire les conditions (délai depuis le début, nombre par an).
- **Remboursement anticipé** : `credit.py anticipation` compare le remboursement à un placement de même horizon (renseigner l'assurance : en mode durée, elle s'arrête avec le prêt). Plafond légal des indemnités : `credit.py ira`. Le contrat peut refuser un remboursement partiel d'au plus 10 % du capital initial, sauf s'il solde le prêt (C. consom. art. L313-47). Règle de fond : un remboursement équivaut à un placement sans risque au taux du prêt, mais l'argent remboursé ne revient pas. Avec un projet d'achat proche, garder la liquidité.
- **Renégociation ou rachat** : comparer le gain d'intérêts aux frais (indemnités, frais de dossier, nouvelle garantie, assurance). Heuristique ancienne : écart de taux d'environ 0,7 à 1 point, dans la première moitié du prêt ; faire le calcul plutôt qu'appliquer l'heuristique.

**Garde-fous de calendrier** (probable, à revérifier) : délai de réflexion de 10 jours avant d'accepter l'offre de prêt ; condition suspensive d'obtention du prêt dans le compromis ; délai de rétractation de 10 jours pour l'acquéreur d'un logement (CCH art. L271-1).

**Acheter à deux hors communauté** (PACS, concubinage, séparation de biens) : fixer dans l'acte des quotes-parts conformes au financement réel, prévoir une convention d'indivision, et selon le cas une clause de tontine ou une SCI. À voir chez le notaire avant de signer.

## 5. Louer ou acheter

- Méthode du coût d'usage (`02-doctrine.md` 8.1), calcul avec `louer_acheter.py`.
- Variables qui font basculer le résultat : durée de détention (les frais d'entrée et de sortie pèsent lourd sur moins de 7 à 10 ans, heuristique), évolution des prix (hypothèse, jamais certitude), rendement du placement de l'apport, rapport prix sur loyer de la ville.
- Les prix peuvent baisser plusieurs années de suite : la série longue de Friggit et les indices Notaires-INSEE montrent des baisses durables (années 1990 en France, par exemple).

## 6. Valoriser un bien

1. DVF : ventes réelles comparables (même rue ou quartier, surface et type proches, ventes récentes). Décalage de publication de plusieurs mois.
2. Indices et prix au mètre carré des notaires (immobilier.notaires.fr).
3. Estimations d'agences et de sites (rang 3) : utiles pour le marché du moment, souvent optimistes pour obtenir un mandat.
4. Donner une fourchette, pas un chiffre. Le prix de vente réel dépend du délai accepté.

## 7. Investissement locatif

- **Rendements** : brut = loyers annuels hors charges / prix d'achat (préciser si les frais d'acquisition sont inclus, les conventions varient) ; net = après charges non récupérables, taxe foncière, assurance PNO, gestion, entretien, vacance ; net-net = après impôt (`expert-comptable`). Le rendement net est souvent inférieur de 1,5 à 2,5 points au brut (heuristique, à calculer).
- **Cash-flow** : loyers − mensualité − charges − impôt. Un cash-flow négatif est un effort d'épargne forcé, à comparer à un placement financier de même effort.
- **Risques** : vacance, impayés, travaux de copropriété, règles énergétiques (calendrier DPE, `01-fraicheur.md`), encadrement des loyers, concentration et illiquidité.
- **Régimes** : location nue (micro-foncier ou réel, déficit foncier) ; meublée LMNP (micro-BIC ou réel avec amortissements, réintégration de tous les amortissements déduits à la revente, pour les cessions depuis le 15/02/2025, sauf résidences exclues par l'art. 150 VB, III) ; SCI. Tout chiffrage fiscal passe par `expert-comptable`.
- **Décence et DPE** : un logement G ne peut plus faire l'objet d'un nouveau bail ou d'un renouvellement depuis 2025, F en 2028, E en 2034, sous réserve de la réforme en cours. Le DPE se lit sur l'observatoire de l'ADEME ; depuis 2026, le nouveau coefficient de l'électricité peut faire gagner une classe à un logement chauffé à l'électricité (attestation gratuite).
- **Encadrement** : dans les zones concernées, le loyer de base ne dépasse pas le loyer de référence majoré de l'arrêté préfectoral, sauf complément de loyer justifié. Expérimentation à durée limitée, vérifier qu'elle est en vigueur.
- **Revendre un bien loué** : un logement occupé se vend en général moins cher qu'un logement libre ; congé pour vente aux dates et conditions de la loi de 1989 (location nue) ou du bail meublé.

## 8. SCPI et immobilier papier

Voir `08-alternatifs.md`.
