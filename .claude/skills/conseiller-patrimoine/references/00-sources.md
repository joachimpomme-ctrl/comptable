# Carte des sources de première main

Dernière revue : 01/11/2026. Les adresses de domaine sont sûres. Les chemins internes des sites changent souvent : partir du domaine et de la rubrique nommée, ou d'une recherche ciblée (`site:domaine mot-clé`).

## 1. Hiérarchie

| Rang | Ce que c'est | Exemples | Statut d'un chiffre lu là |
|---|---|---|---|
| 1 | Le texte ou le producteur de la donnée | Légifrance, Journal officiel, BOFiP, décisions HCSF, AMF, ACPR, BCE ; INSEE, Banque de France, Eurostat ; DIC, prospectus, rapport annuel et conditions générales d'un produit ; document d'enregistrement universel d'une société | Sûr, avec date |
| 2 | Vulgarisation publique ou institutionnelle | service-public.gouv.fr, impots.gouv.fr, info-retraite.fr, ANIL, Assurance Banque Épargne Info Service, lafinancepourtous.com (IEFP), espace épargnants de l'AMF, France Assureurs | Sûr si daté et cohérent avec le rang 1, probable sinon |
| 3 | Presse spécialisée, professionnels, bases de données privées | Les Échos, L'AGEFI, Investir, Le Revenu, MoneyVox, courtiers, justETF, Quantalys, Morningstar | Probable si deux sources indépendantes concordent, hypothèse sinon |
| 4 | Le reste | Forums, réseaux sociaux, vidéos, sorties d'IA, pages commerciales sans référence | Jamais une source de chiffre |

Un chiffre de rang 3 sert à localiser le rang 1. Un comparateur peut avoir un TER ou une éligibilité PEA périmés : l'émetteur confirme.

## 2. Droit et fiscalité

| Besoin | Source | Remarque |
|---|---|---|
| Texte en vigueur (codes, lois, décrets, arrêtés) | legifrance.gouv.fr | Lire la mention « Version en vigueur depuis le ». Un article peut avoir une version future déjà publiée. |
| Doctrine fiscale | bofip.impots.gouv.fr | Opposable à l'administration. Date de publication en tête de chaque document. |
| Barèmes, simulateurs, formulaires | impots.gouv.fr | Simulateur officiel de l'impôt sur le revenu. |
| Lois en discussion | senat.fr (dossiers législatifs, « la loi en clair »), assemblee-nationale.fr | Adopté par une chambre ne veut pas dire en vigueur : attendre la promulgation au Journal officiel. |
| Fiche pratique | service-public.gouv.fr (ancien service-public.fr) | Mention « Vérifié le » en bas de fiche. |
| Fiscalité appliquée au foyer | Skill `assistant-fiscal-comptable` | Son référentiel porte millésime et source. |

## 3. Taux, crédit, épargne réglementée, macroéconomie

| Besoin | Source | Remarque |
|---|---|---|
| Taux des livrets réglementés (Livret A, LDDS, LEP) et du CEL | Taux fixé par le ministre : arrêté au Journal officiel, service-public.gouv.fr (fiche F2365), economie.gouv.fr, banque-france.fr après la décision | Révision normale au 1er février et au 1er août. Le communiqué de mi-janvier ou de mi-juillet de la Banque de France est une proposition, pas le taux fixé. |
| Taux du PEL | banque-france.fr, arrêté au Journal officiel | Taux des nouveaux plans calculé une fois par an par formule (Banque de France, début décembre), en vigueur en principe au 1er janvier ; figé à l'ouverture pour un plan donné. |
| Taux d'usure | banque-france.fr, avis au Journal officiel | Vérifier la date de l'avis et la catégorie (durée, montant). |
| Taux moyens des crédits à l'habitat | webstat.banque-france.fr (séries officielles), Observatoire Crédit Logement/CSA (rang 3, mensuel) | Le taux d'une offre réelle prime sur toute moyenne. |
| Normes d'octroi du crédit immobilier | economie.gouv.fr/hcsf (décisions, communiqués après chaque séance) | Page parfois illisible par l'outil : se rabattre sur deux articles datés citant la séance. |
| Taux directeurs, €STR | ecb.europa.eu | L'API de données de la BCE refuse les robots : lire les communiqués de politique monétaire. |
| Taux des emprunts d'État (OAT) | aft.gouv.fr (Agence France Trésor), banque-france.fr | |
| Inflation | insee.fr (indice des prix, publication mensuelle), Eurostat (IPCH) | |
| IRL, ICC, ILAT | insee.fr | Trimestriel. Le bail précise le trimestre de référence. |
| Revalorisation des fonds en euros | ACPR (étude annuelle sur la revalorisation des contrats d'assurance vie), France Assureurs, annonce de l'assureur pour son contrat | Le taux servi d'un contrat donné se lit chez l'assureur. |

## 4. Produits financiers

| Besoin | Source | Remarque |
|---|---|---|
| Identité d'un fonds ou d'un ETF | Code ISIN (12 caractères) | Raisonner par ISIN, jamais par nom commercial : un même nom couvre plusieurs parts et cotations. |
| DIC (KID PRIIPs), prospectus, rapport annuel, reporting mensuel | Site de la société de gestion, page du fonds, onglet documents ; base GECO de l'AMF (geco.amf-france.org) pour les fonds agréés en France | Le DIC donne frais, indicateur de risque (1 à 7), scénarios, durée recommandée. Le rapport annuel donne l'écart de suivi réel. |
| Éligibilité PEA d'un ETF | DIC, prospectus ou liste PEA de l'émetteur | Un comparateur peut se tromper : l'émetteur confirme. |
| Composition et performance d'un indice | Fiche mensuelle de l'éditeur : MSCI (msci.com, index factsheets), FTSE Russell, S&P Dow Jones Indices, STOXX | Poids par pays, secteurs, nombre de titres, performances annualisées. Dater la fiche. |
| Cours, volumes, fourchette | Euronext (live.euronext.com), autre place de cotation de la ligne | Un cours vaut pour sa date et son heure. |
| Frais de courtage et de tenue | Grille tarifaire du courtier ou de la banque | Rang 1 pour ses propres frais. |
| Société cotée | Document d'enregistrement universel et rapport annuel (site investisseurs), base des informations réglementées de l'AMF, filings.xbrl.org (ESEF), sec.gov/edgar (sociétés américaines) | |
| Épargne salariale et actionnariat salarié | Règlement du plan, reporting et DIC du FCPE, teneur de compte | Le règlement fixe les dates de disponibilité et les modalités de sortie. |

## 5. Autorisations et alertes (anti-arnaque)

| Vérification | Source |
|---|---|
| Listes noires et mises en garde | amf-france.org (rubrique listes noires), acpr.banque-france.fr (listes noires crédit, assurance, livrets, change) |
| Intermédiaire : CIF, courtier en crédit (IOBSP), intermédiaire en assurance | orias.fr |
| Banque, établissement de paiement ou de monnaie électronique agréé | regafi.fr |
| Prestataire de crypto-actifs agréé MiCA (PSCA, ou CASP) | Liste blanche de l'AMF (amf-france.org) et registre MiCA de l'ESMA (esma.europa.eu) : un prestataire agréé dans un autre État de l'UE et passeporté figure au registre ESMA |
| Garantie des dépôts, des titres et des contrats d'assurance-vie | garantiedesdepots.fr (FGDR), fgap.fr (FGAP), lafinancepourtous.com |
| Plateforme de financement participatif (PSFP) | amf-france.org, esma.europa.eu |
| Signalement, questions | abe-infoservice.fr (AMF, ACPR, Banque de France) |

## 6. Immobilier

| Besoin | Source | Remarque |
|---|---|---|
| Prix de transaction réels | DVF (app.dvf.etalab.gouv.fr), données notariales (immobilier.notaires.fr, indices Notaires-INSEE) | Comparer à surface, type, date et rue proches. DVF a un décalage de publication de plusieurs mois. |
| Série longue des prix et des loyers | Travaux de Jacques Friggit (IGEDD, ex-CGEDD), « prix immobilier, évolution 1200-20xx » | Rapport prix sur revenus, prix sur loyers. |
| Règles de location (bail, décence, DPE, encadrement, charges) | anil.org, service-public.gouv.fr, Légifrance (loi n° 89-462 du 6 juillet 1989) | L'ANIL et les ADIL donnent des fiches juridiques fiables et des consultations gratuites. |
| DPE d'un logement | Observatoire DPE de l'ADEME (numéro de DPE à 13 caractères) | Vérifier date et validité du diagnostic. |
| Encadrement des loyers | Arrêté préfectoral de loyers de référence, simulateur de la collectivité | Expérimentation à durée limitée : vérifier qu'elle est en vigueur (`01-fraicheur.md`). |
| Frais d'acquisition | Simulateur de notaires.fr ; taux des droits de mutation par département (impots.gouv.fr, DGFiP) | |
| PTZ et aides | service-public.gouv.fr, anil.org | Conditions révisées presque chaque année. |

## 7. Retraite

| Besoin | Source |
|---|---|
| Droits personnels, relevé de carrière, estimation, simulateur (M@rel) | info-retraite.fr (compte personnel) |
| Règles du régime général | lassuranceretraite.fr |
| Complémentaire des salariés du privé | agirc-arrco.fr |
| Libéraux | CNAVPL et la section de la profession (exemples : CARCDSF pour chirurgiens-dentistes et sages-femmes ; CARPIMKO pour infirmiers, kinésithérapeutes, orthophonistes, orthoptistes, pédicures-podologues ; CIPAV) |
| Projections et paramètres du système | cor-retraites.fr (rapport annuel du Conseil d'orientation des retraites) |

## 8. Données de long terme et recherche

| Besoin | Source |
|---|---|
| Rendements réels de long terme par pays et classe d'actifs | UBS Global Investment Returns Yearbook (Dimson, Marsh, Staunton), annuel |
| Rendement de toutes les classes d'actifs depuis 1870 | Jordà-Schularick-Taylor Macrohistory Database |
| Facteurs, séries américaines et internationales | Kenneth French Data Library (Dartmouth) |
| Rendements historiques américains, prime de risque implicite | Aswath Damodaran (pages.stern.nyu.edu/~adamodar) |
| CAPE et séries de Shiller | Site de Robert Shiller (Yale) |
| Gestion active contre indices | Rapports SPIVA (S&P Dow Jones Indices), Morningstar Active/Passive Barometer (Europe) |
| Écart entre rendement des fonds et rendement des investisseurs | Morningstar, étude « Mind the Gap » |

## 9. Données du foyer

- Skill `comptable-foyer` (fiche maître, registre) ou relevés fournis par l'utilisateur.
- Connecteur bancaire ou agrégateur s'il est disponible : citer la date de synchronisation.

## 10. Lire une page officielle avec l'outil

- Préférer la page HTML à un gros PDF. Pour un PDF, chercher d'abord la page de synthèse ou le communiqué.
- Relever à chaque fois : la valeur, la date d'effet, la date de publication ou « vérifié le », l'URL.
- Échec de lecture (robots, erreur, JavaScript) : le dire, essayer la source de rang 2 qui cite le texte, puis deux sources de rang 3 datées.
- Une donnée de marché (cours, valeur liquidative, encours, rendement) se cite avec sa date de valeur. Elle ne s'archive pas comme une vérité.
