# FEW SHOTS — Agent IA Triple Fonction

**Usage :** Exemples de calibration pour Gemini. Injecter en contexte ou comme exemples d'entraînement.
**Format :** Question → Réponse idéale structurée (sourced, actionnables)
**Distribution :** 6 comptables · 7 financières · 12 patrimoniales · 3 fonctions
**Millésime :** les chiffres de ces exemples sont calibrés sur le millésime 2025 (ex. seuil micro-BNC 77 700 €, PASS 47 100 €). Pour les revenus 2026, consulter `referentiel_parametres.json` (micro-BNC 83 600 €, PASS 48 060 €).

---

## [FS-001] 📒 Comptable — ⬜ Simple

**Question :** J'ai acheté un bureau pour 420 € HT pour mon cabinet libéral. Je le comptabilise comment ?

*Contexte : Professionnel libéral BNC, déclaration contrôlée.*

**Réponse idéale :**

En dessous du seuil de 500 € HT, ce bureau est comptabilisé en **charge déductible immédiatement** (compte 6064 — Fournitures de bureau ou 6068 — Petit équipement). Aucune immobilisation, pas d'amortissement.

**Règle :** Biens de valeur unitaire ≤ 500 € HT → charge immédiatement déductible (bnc_011, M1).

Si ce bureau avait coûté 520 € HT, il aurait été obligatoirement immobilisé et amorti.

*Modules : M1 | Règles : bnc_013*

---

## [FS-002] 📒 Comptable — ⬜ Simple

**Question :** J'utilise un tableur Excel pour tenir ma comptabilité. Est-ce suffisant ?

*Contexte : Professionnel libéral avec comptabilité informatisée.*

**Réponse idéale :**

**Non.** Un tableur Excel ne satisfait pas à l'obligation de FEC (Fichier des Écritures Comptables). En cas de contrôle fiscal, toute comptabilité informatisée doit pouvoir produire un FEC conforme à la norme A47 A-1 du Livre des Procédures Fiscales.

**Sanction en cas de défaut :** 5 000 € par exercice contrôlé ou 10 % des droits rappelés si plus élevé.

**Recommandation :** Utiliser un logiciel comptable compatible FEC (EBP, Ciel, Sage, QuadraFact…).

Source : bnc_025, bnc_026 — M1

*Modules : M1 | Règles : bnc_025, bnc_026*

---

## [FS-003] 📒 Comptable — 🟨 Standard

**Question :** J'ai payé une facture par carte bancaire à débit différé le 18 novembre. Le débit réel sur mon compte est le 5 décembre. Quelle date je comptabilise ?

*Contexte : Professionnel libéral BNC, déclaration contrôlée.*

**Réponse idéale :**

La date à retenir est le **18 novembre** — date du paiement par carte bancaire — et non le 5 décembre (date du débit sur le relevé).

**Règle BNC :** Les dépenses sont comptabilisées à la date de **décaissement effectif**. Pour une carte bancaire à débit différé, c'est la date du paiement par carte qui fait foi, pas la date d'inscription sur le relevé bancaire.

Source : bnc_010 — M1

*Modules : M1 | Règles : bnc_010*

---

## [FS-004] 📒 Comptable — 🟨 Standard

**Question :** Mon téléphone est utilisé à 70 % pour mon activité professionnelle et 30 % à titre personnel. Comment je traite la facture de 80 € HT/mois ?

*Contexte : Professionnel libéral BNC.*

**Réponse idéale :**

Seule la **quote-part professionnelle** de 70 % est déductible, soit **56 € HT/mois** à comptabiliser en charges. Les 24 € restants (30 %) constituent une dépense personnelle non déductible.

**Règle :** Pour une dépense mixte, seule la part professionnelle est déductible. La part privée est réintégrée extra-comptablement ou passée en prélèvements personnels.

**Obligation :** Conserver le justificatif (facture mensuelle) et le document attestant la clé de répartition 70/30.

Source : bnc_015 — M1

*Modules : M1 | Règles : bnc_015*

---

## [FS-005] 📒 Comptable — 🟨 Standard

**Question :** Combien de temps dois-je conserver mes documents comptables et mes factures ?

*Contexte : Professionnel libéral BNC.*

**Réponse idéale :**

Deux délais s'appliquent :

- **6 ans** pour les documents fiscaux (délai de reprise de l'administration en règle générale)
- **10 ans** pour les livres, registres, et pièces comptables justificatives

En pratique : **conserver tout pendant 10 ans** pour couvrir les deux obligations.

⚠️ Le délai de reprise fiscale est porté à **10 ans** en cas de dissimulation volontaire ou fraude fiscale.

Source : bnc_014, GFPL-162 — M1, M2

*Modules : M1, M2 | Règles : bnc_014, GFPL-162*

---

## [FS-006] 📒 Comptable — 🟥 Complexe

**Question :** Je suis loueur en meublé au réel BIC. Mon bien vaut 200 000 €. Les loyers annuels sont de 12 000 €, les charges (hors amortissements) de 6 000 €, les amortissements comptabilisés de 8 000 €. Quel amortissement est déductible fiscalement ?

*Contexte : LMNP au réel BIC. Application article 39-C CGI.*

**Réponse idéale :**

**Application de l'article 39-C CGI :**

Amortissement déductible = Loyers acquis − Charges hors amortissements = 12 000 − 6 000 = **6 000 € maximum**

Amortissements comptabilisés = 8 000 €
Déductibles : 6 000 € / Différés : **2 000 € (ARD)**

**Résultat fiscal :** 12 000 − 6 000 (charges) − 6 000 (amortissements déductibles) = **0 € de bénéfice imposable** (neutre, pas de déficit).

**Les 2 000 € d'amortissements différés sont stockés** et déductibles lors d'un exercice futur bénéficiaire, dans la même limite (loyers − charges). Ils ne sont pas perdus, sauf vente du bien en LMNP.

Source : LMN-012 — M5

*Modules : M5 | Règles : LMN-012*

---

## [FS-007] 📈 Financier — ⬜ Simple

**Question :** Je suis professionnel libéral avec un CA de 60 000 €. Suis-je obligé de faire une déclaration 2035 ?

*Contexte : Professionnel libéral BNC.*

**Réponse idéale :**

**Non, pas obligatoirement.** Votre CA de 60 000 € est inférieur au seuil micro-BNC de **77 700 €** — vous pouvez donc bénéficier du régime **micro-BNC** (régime simplifié), qui ne nécessite pas de 2035.

En micro-BNC :
- Déclaration : 2042 C PRO uniquement
- Abattement forfaitaire de **34 %** sur le CA
- Revenu imposable = 60 000 × 66 % = **39 600 €**

Vous pouvez toutefois **opter pour la déclaration contrôlée** (2035) si vos charges réelles dépassent 34 % du CA — dans ce cas l'option doit être exercée avant la date limite de dépôt de la déclaration de revenus.

Source : GFPL-049 à GFPL-056 — M2

*Modules : M2 | Règles : GFPL-050, GFPL-051, GFPL-052*

---

## [FS-008] 📈 Financier — 🟨 Standard

**Question :** J'ai un TMI à 30 %. J'ai perçu 5 000 € de dividendes. Je choisis quoi : PFU ou barème ?

*Contexte : Personne physique, résidente fiscale française.*

**Réponse idéale :**

**Comparaison PFU vs barème à TMI 30 % :**

**Option PFU (flat tax) :**
5 000 € × 30 % (12,8 % IR + 17,2 % PS) = **1 500 €**

**Option barème progressif :**
Base imposable = 5 000 × 60 % (abattement 40 %) = 3 000 €
IR = 3 000 × 30 % = 900 €
PS = 5 000 × 17,2 % = 860 €
Total = **1 760 €**

→ **PFU plus avantageux à TMI 30 %** (1 500 € vs 1 760 €).

L'option barème devient intéressante uniquement si TMI ≤ 11 % (les dividendes sont alors imposés à 11 % + 17,2 % PS, soit 28,2 % < 30 %).

⚠️ L'option barème est **globale** : elle s'applique à tous les revenus financiers de l'année (pas uniquement aux dividendes).

Source : GFPL-086 (PFU), M2 — Module C2

*Modules : M2 | Règles : GFPL-086*

---

## [FS-009] 📈 Financier — 🟨 Standard

**Question :** Vaut-il mieux déduire mon versement PER de mon revenu BNC ou de mon revenu global ?

*Contexte : Infirmier libéral, BNC réel, bénéfice imposable 70 000 €, PER versement envisagé 5 000 €.*

**Réponse idéale :**

**Déduire du revenu BNC en priorité** — c'est systématiquement plus avantageux pour un TNS au réel.

**Pourquoi :**
1. La déduction du BNC réduit votre **revenu catégoriel net** → réduit le **RFR** (revenu fiscal de référence)
2. Un RFR plus bas réduit les cotisations sociales URSSAF/CARPIMKO calculées sur le bénéfice
3. La déduction du revenu global n'a pas cet effet sur les cotisations sociales

**Stratégie optimale :**
- Utiliser d'abord le **plafond de déduction du revenu professionnel** (BNC)
- Stocker les plafonds du revenu global des années antérieures non utilisés (récupérables 3 ans)
- Si plafond BNC épuisé → utiliser le plafond revenu global

Source : GFPL-165 à GFPL-170 — M2, Module G1

*Modules : M2 | Règles : GFPL-166, GFPL-167, GFPL-170*

---

## [FS-010] 📈 Financier — 🟨 Standard

**Question :** Mon CA en location meublée touristique non classée est de 18 000 € en 2025. Quel régime fiscal ?

*Contexte : Particulier louant un appartement sur Airbnb, non classé, revenus 2025.*

**Réponse idéale :**

Pour les **revenus 2025 déclarés en 2026**, le seuil micro-BIC pour un meublé de tourisme **NON classé** est de **15 000 €** avec un abattement de **30 %** (loi Le Meur 2024).

Votre CA de 18 000 € **dépasse ce seuil** → vous êtes obligatoirement au **régime réel BIC simplifié**.

**Conséquences :**
- Dépôt déclarations 2031 + 2033 + report sur 2042 C PRO
- Déduction des charges réelles (intérêts emprunt, taxe foncière, CFE, entretien, comptabilité)
- Amortissement du bien possible (méthode composants)
- FEC obligatoire si comptabilité informatisée

⚠️ Si vous aviez fait **classer** votre bien (1 à 5 étoiles), le seuil serait 77 700 € avec abattement 50 % → vous resteriez en micro-BIC.

Source : LMN-005, LMN-006, LMN-007 — M5

*Modules : M5 | Règles : LMN-005, LMN-007*

---

## [FS-011] 📈 Financier — 🟥 Complexe

**Question :** Je suis sage-femme libérale, 90 000 € de recettes. Je suis soumise à la CEHR ? Et à la CDHR ?

*Contexte : Professionnel libéral, célibataire, revenus 2025.*

**Réponse idéale :**

**CEHR :** Non. Le seuil de déclenchement est un **RFR > 250 000 €** (célibataire). Avec 90 000 € de recettes BNC, votre RFR sera nettement inférieur après charges et cotisations sociales déductibles.

**CDHR (revenus 2025 uniquement) :** Non plus, pour les mêmes raisons — seuil RFR retraité > 250 000 €.

**Votre situation fiscale probable :**
- Recettes 90 000 € → déclaration contrôlée (> 77 700 €)
- Bénéfice imposable ≈ 90 000 − charges réelles − cotisations sociales
- Tranche marginale d'imposition probable : 30 % (entre 29 316 € et 83 823 €)

⚠️ CEHR et CDHR concernent les contribuables à très hauts revenus. Pour une sage-femme libérale en début/milieu de carrière, ces contributions ne sont généralement pas applicables.

Source : GFPL-053, GFPL-142, GFPL-147 — M2

*Modules : M2 | Règles : GFPL-142, GFPL-147, GFPL-053*

---

## [FS-012] 🏠 Patrimonial — ⬜ Simple

**Question :** Je suis pacsé(e). Mon partenaire décède sans testament. Qu'est-ce que je récupère ?

*Contexte : Partenaires pacsés sans enfants.*

**Réponse idéale :**

**Rien**, légalement. Le PACS **n'attribue aucun droit successoral** à un partenaire de PACS. Sans testament, les biens du défunt reviennent à ses héritiers légaux (enfants, parents, frères et sœurs selon l'ordre légal).

**Ce qu'il faut faire pour être protégé(e) :**
1. Rédiger un **testament** en faveur de l'autre — permet de transmettre jusqu'à la quotité disponible (50 % en présence d'un enfant, etc.)
2. Souscrire une **assurance-vie** avec le partenaire comme bénéficiaire → transmission hors succession, exonération totale de droits

⚠️ Avantage fiscal: les partenaires PACS sont exonérés de droits de succession depuis la loi TEPA 2007 — mais encore faut-il avoir un testament pour que le partenaire hérite.

Source : PAT-006 — M6

*Modules : M6 | Règles : PAT-006*

---

## [FS-013] 🏠 Patrimonial — ⬜ Simple

**Question :** Je veux donner 120 000 € à mon fils. Combien vais-je payer de droits de donation ?

*Contexte : Parent, enfant majeur, première donation.*

**Réponse idéale :**

**Calcul des droits de donation :**

Abattement parent → enfant : **100 000 €** (renouvelable tous les 15 ans)
Base taxable : 120 000 − 100 000 = **20 000 €**

⚠️ Si vous ajoutez un **don en numéraire** (condition : vous avez moins de 80 ans, votre fils est majeur) : abattement supplémentaire de **31 865 €**
→ Dans ce cas, 120 000 € serait entièrement exonéré (100 000 + 31 865 > 120 000).

**Si la donation est uniquement un don manuel :**
Barème ligne directe sur 20 000 € :
- Jusqu'à 8 072 € : 5 % → 404 €
- De 8 073 € à 12 109 € : 10 % → 404 €
- De 12 110 € à 15 932 € : 15 % → 573 €
- De 15 933 € à 20 000 € : 20 % → 814 €
**Total droits ≈ 2 194 €**

Recommandation : structurer la donation en **don manuel en numéraire** pour cumuler les deux abattements (131 865 €) et éviter les droits.

Source : PAT-009 — M6, M10

*Modules : M6, M10 | Règles : PAT-009*

---

## [FS-014] 🏠 Patrimonial — 🟨 Standard

**Question :** Je vends ma résidence principale. Y a-t-il une plus-value imposable ?

*Contexte : Propriétaire d'une maison occupée comme résidence principale depuis 5 ans.*

**Réponse idéale :**

**Non — exonération totale.** La cession de la **résidence principale** est exonérée de toute plus-value immobilière (IR + prélèvements sociaux), sans condition de durée de détention.

**Condition unique :** Le bien doit constituer la **résidence habituelle et effective** du cédant au moment de la cession.

**Cas particuliers :**
- Si vous avez quitté le logement avant la vente : l'exonération est maintenue si le délai entre le départ et la vente est « normal » (généralement < 12 mois, apprécié au cas par cas par l'administration)
- Si le bien a été mis en location avant la vente : l'exonération est perdue (n'est plus la RP effective)

⚠️ Cette exonération ne s'applique pas aux résidences secondaires ni aux biens locatifs — dans ces cas, les abattements pour durée de détention s'appliquent.

Source : M9 (PV-RP-001)

*Modules : M9 | Règles : PV-RP-001*

---

## [FS-015] 🏠 Patrimonial — 🟨 Standard

**Question :** J'ai un appartement locatif (location nue) acheté 200 000 € il y a 8 ans, je le revends 280 000 €. Quel est le montant de la plus-value imposable ?

*Contexte : Particulier, location nue, 8 ans de détention.*

**Réponse idéale :**

**Calcul de la plus-value nette imposable :**

PV brute = 280 000 − 200 000 = **80 000 €**

**Abattements pour durée de détention (8 ans) :**
- Pour l'IR : 0 % les 5 premières années + 6 %/an de la 6ème à la 21ème → 6 % × 3 ans = **18 %**
  → PV imposable IR = 80 000 × (100 % − 18 %) = **65 600 €**
- Pour les PS : 0 % les 5 premières années + 1,65 %/an de la 6ème à la 21ème → 1,65 % × 3 = **4,95 %**
  → PV imposable PS = 80 000 × (100 % − 4,95 %) = **76 040 €**

**Impôts :**
- IR = 65 600 × 19 % = **12 464 €**
- PS = 76 040 × 17,2 % = **13 079 €**
- **Total ≈ 25 543 €**

(Taxe supplémentaire si PV brute > 50 000 € : de 2 à 6 % sur la PV imposable IR → ici applicable sur 65 600 €, environ 2 % = 1 312 €)

⚠️ Ce calcul est effectué par le notaire lors de la vente. En pratique, il prélève l'impôt directement.

Source : M9 (PV-IMM-002, PV-IMM-003)

*Modules : M9 | Règles : PV-IMM-002, PV-IMM-003*

---

## [FS-016] 🏠 Patrimonial — 🟨 Standard

**Question :** Mon LMNP est déficitaire de 3 000 €. Puis-je déduire ce déficit de mes revenus salariaux ?

*Contexte : Salarié avec un appartement en LMNP au réel BIC.*

**Réponse idéale :**

**Non.** Le déficit LMNP (Loueur Meublé Non Professionnel) est **strictement cantonné** aux revenus de location meublée non professionnelle. Il ne peut pas s'imputer sur d'autres revenus (salaires, BNC, revenus fonciers, etc.).

**Ce que vous pouvez faire :**
- Reporter ce déficit de **3 000 €** sur les bénéfices LMNP des **10 années suivantes** (cases 5GA à 5GJ de la 2042 C PRO)

**Exception — si vous étiez LMP :** Les déficits LMP s'imputent sans limite sur le revenu global. Mais pour être LMP, vos recettes locatives doivent dépasser 23 000 € ET excéder vos revenus salariaux — ce qui est rare pour un salarié.

Source : LMN-015 — M5

*Modules : M5 | Règles : LMN-015*

---

## [FS-017] 🏠 Patrimonial — 🟨 Standard

**Question :** Je veux transmettre mon patrimoine à mes deux enfants. Donation-partage ou donations séparées ?

*Contexte : Couple marié, deux enfants majeurs, patrimoine immobilier et financier.*

**Réponse idéale :**

**La donation-partage est généralement préférable.** Voici pourquoi :

| Critère | Donation-partage | Donations séparées |
|---------|-----------------|--------------------|
| Rapport à la succession | Non rapportable | Rapportable (risque réévaluation) |
| Évaluation des biens | Figée au jour de la donation | Au jour du décès (peut avoir augmenté) |
| Équilibre entre enfants | Garanti au moment de la donation | Peut créer des tensions ultérieures |
| Abattements fiscaux | 100 000 €/parent/enfant (mêmes) | 100 000 €/parent/enfant |

**Avantage décisif :** Dans une donation-partage, les biens sont évalués au jour de la donation pour le calcul des droits de succession futurs — pas au jour du décès. Si l'immobilier s'apprécie, l'économie peut être substantielle.

**Recommandation :** Faire appel à un notaire pour organiser la donation-partage, en pensant au démembrement (garder l'usufruit, donner la nue-propriété) pour réduire les droits.

Source : PAT-010 — M6

*Modules : M6 | Règles : PAT-010*

---

## [FS-018] 🏠 Patrimonial — 🟥 Complexe

**Question :** Je suis LMP avec un déficit de 15 000 € cette année, et ma femme est salariée à 60 000 €. Quel revenu imposable pour le foyer ?

*Contexte : Foyer fiscal commun, 1 enfant à charge (1 part supplémentaire).*

**Réponse idéale :**

**En LMP, le déficit s'impute sur le revenu global du foyer sans limitation.**

Calcul du revenu imposable :
- Salaires nets de Madame = 60 000 − 10 % (forfait frais pro, plafond 14 426 €) = **54 000 €** (ou frais réels si supérieurs)
- Déficit LMP = −15 000 €
- **Revenu imposable du foyer = 54 000 − 15 000 = 39 000 €**

Sur 2,5 parts (2 adultes + 1 enfant = 1/2 part supplémentaire) :
- Quotient = 39 000 / 2,5 = 15 600 €
- TMI = 11 % (tranche 11 498 € → 29 315 €)

⚠️ Aucun déficit n'est reportable en N+1 dans cet exemple (le déficit a été entièrement absorbé). Si les salaires de Madame avaient été insuffisants, le déficit global résiduel serait reportable sur **6 ans**.

Source : LMN-014 — M5

*Modules : M5, M2 | Règles : LMN-014, GFPL-107*

---

## [FS-019] 🏠 Patrimonial — 🟥 Complexe

**Question :** J'ai une assurance-vie avec 200 000 € de capital dont 80 000 € de gains. Mon fils est bénéficiaire. Je décède. Combien paie-t-il ?

*Contexte : Primes versées avant 70 ans. Fils unique.*

**Réponse idéale :**

**Fiscalité au décès (primes versées avant 70 ans) :**

Abattement : **152 500 €** par bénéficiaire

Capital transmis = 200 000 €
Abattement applicable = 152 500 €
Base taxable = 200 000 − 152 500 = **47 500 €**

Taxe à 20 % sur la tranche 152 501 € → 700 000 € = 47 500 × 20 % = **9 500 €**

**Votre fils paiera donc 9 500 €** sur les 200 000 € reçus — soit un taux effectif de **4,75 %**, bien plus avantageux que les droits de succession ordinaires.

**À titre de comparaison** : hors assurance-vie, une succession de 200 000 € à un enfant unique (après abattement de 100 000 €) donnerait :
- 100 000 € × barème ligne directe ≈ 20 000 € de droits

L'assurance-vie économise ici **~10 500 €** de droits.

Source : PAT-019 — M6

*Modules : M6 | Règles : PAT-019*

---

## [FS-020] 🏠 Patrimonial — 🟨 Standard

**Question :** Dois-je déclarer mon appartement locatif à l'IFI ?

*Contexte : Propriétaire d'un appartement locatif valeur 350 000 €, résidence principale valeur 500 000 €. Pas d'autres biens immobiliers. Emprunt restant 200 000 € sur l'appartement locatif.*

**Réponse idéale :**

**Calcul de l'assiette IFI :**

- Résidence principale : 500 000 € × 70 % (abattement de 30 %) = **350 000 €**
- Appartement locatif : 350 000 € (valeur de marché)
- Passif déductible : emprunt restant −200 000 €

Patrimoine net IFI = 350 000 + 350 000 − 200 000 = **500 000 €**

**Le seuil IFI est 1 300 000 € → Pas d'IFI à payer.**

Mais si votre patrimoine immobilier net dépassait 1 300 000 €, l'IFI serait calculé sur la valeur nette à partir de 800 000 € selon le barème progressif.

Source : PAT-013 — M6, M10

*Modules : M6, M10 | Règles : PAT-013*

---

## [FS-021] 🏠 Patrimonial — 🟨 Standard

**Question :** Je loue mon appartement nu à 800 €/mois. J'ai 5 000 € d'intérêts d'emprunt et 2 000 € de travaux. Quel régime fiscal pour mes revenus fonciers ?

*Contexte : Particulier, location nue.*

**Réponse idéale :**

**Revenus fonciers annuels = 800 × 12 = 9 600 €**
Seuil micro-foncier : 15 000 €
→ Vous pouvez être au **micro-foncier** (abattement 30 %) OU opter pour le **régime réel**.

**Comparaison :**

| Régime | Base imposable | Impôt (TMI 30 %) + PS | Total |
|--------|---------------|----------------------|-------|
| Micro-foncier (30 %) | 9 600 × 70 % = 6 720 € | 6 720 × 47,2 % | 3 172 € |
| Réel (intérêts + travaux) | 9 600 − 5 000 − 2 000 = 2 600 € | 2 600 × 47,2 % | 1 227 € |

→ **Le régime réel est 2,5× moins coûteux** dans ce cas (charges élevées).

⚠️ L'option pour le régime réel est valable **3 ans** (irrévocable pendant cette période). Elle est avantageuse ici car charges > 30 % des loyers.

Source : M9 (RF-001, RF-003)

*Modules : M9 | Règles : RF-001, RF-003*

---

## [FS-022] 🏠 Patrimonial — 🟥 Complexe

**Question :** Je suis en LMNP depuis 10 ans. Je vends mon appartement 300 000 € (acheté 180 000 €). J'ai amorti 40 000 € depuis 2025. Quelle PV ?

*Contexte : Vente en 2027 (hypothèse: amortissements déduits depuis 2025 = 40 000 €). LMNP réel BIC.*

**Réponse idéale :**

**Nouveau régime 2025 : les amortissements sont réintégrés dans le calcul de la PV LMNP.**

**PV brute = Prix vente − (Prix acquisition − Amortissements déduits)**
= 300 000 − (180 000 − 40 000)
= 300 000 − 140 000
= **160 000 €**

**Abattements pour 10 ans de détention :**
- IR : 6 %/an × 5 ans (6ème à 10ème année) = 30 % → base IR = 160 000 × 70 % = **112 000 €**
- PS : 1,65 %/an × 5 ans = 8,25 % → base PS = 160 000 × 91,75 % = **146 800 €**

**Impôts :**
- IR = 112 000 × 19 % = **21 280 €**
- PS = 146 800 × 17,2 % = **25 250 €**
- Taxe supplémentaire PV > 50 000 € : ~2 % × 112 000 = **2 240 €**
- **Total ≈ 48 770 €**

⚠️ Sans le nouveau régime 2025, la PV aurait été 300 000 − 180 000 = 120 000 € et les impôts ≈ 28 000 €. La réintégration des amortissements coûte ici ~20 000 € supplémentaires.

Source : LMN-022, LMN-023 — M5

*Modules : M5 | Règles : LMN-022, LMN-023*

---

## [FS-023] 🏠 Patrimonial — 🟥 Complexe

**Question :** Je suis salarié cadre avec 120 000 € de revenus. Mon conjoint est libéral avec 80 000 € de bénéfice BNC. Doit-on individualiser notre taux PAS ?

*Contexte : Couple marié, foyer commun, à partir de septembre 2025.*

**Réponse idéale :**

**À partir de septembre 2025, l'individualisation du taux PAS devient le principe par défaut pour les couples.**

**Fonctionnement :**
- Vos salaires (120 000 €) : taux individualisé calculé sur vos revenus propres
- BNC de votre conjoint (80 000 €) : acomptes prélevés calculés sur son revenu catégoriel BNC

**Intérêt de l'individualisation :**
Si vos revenus sont très différents, l'individualisation évite que l'un des conjoints finance l'impôt de l'autre par des retenues à la source excessives sur son salaire.

**Option possible :** Le couple peut demander le retour au taux du foyer fiscal (taux commun) — option à exercer auprès de l'administration.

⚠️ L'individualisation modifie les taux mais **pas le montant total d'impôt dû par le foyer** — c'est uniquement une répartition différente de qui paie quoi en cours d'année.

Source : GFPL-123 — M2

*Modules : M2 | Règles : GFPL-123*

---

## [FS-024] 🏠 Patrimonial — 🟥 Complexe

**Question :** J'envisage de créer une SCI pour détenir mon immeuble locatif. Faut-il opter pour l'IS ?

*Contexte : Immeuble locatif rapportant 24 000 €/an, TMI personnel 41 %, aucun enfant à qui transmettre à court terme.*

**Réponse idéale :**

**Réponse : à éviter sauf cas très spécifique.**

**SCI à l'IS — avantages :**
- Amortissement fiscal du bien (réduit le résultat imposable à l'IS)
- Taux IS 25 % (ou 15 % pour les 42 500 premiers € de bénéfice si PME)
- Déduction de tous les frais réels

**SCI à l'IS — inconvénients majeurs dans votre cas :**
1. **Option irrévocable** — impossible de revenir à l'IR
2. **Perte de l'abattement pour durée de détention sur les PV** (exo IR après 22 ans, PS après 30 ans) → en IS, la PV de cession est imposée à l'IS 25 %
3. **Dividendes imposés au PFU 30 %** lors de la distribution → double imposition (IS 25 % + PFU 30 %)
4. **Sans transmission à court terme**, l'intérêt de la SCI IR (démembrement + abattements donations) n'est pas pleinement exploité

**Recommandation :** SCI à l'**IR** — avantages fiscaux IFI (abattement si RP dans la SCI non recommandé), transmission via démembrement, abattements donations, exonération PV longue durée. Ou envisager le LMNP (location meublée) pour bénéficier des amortissements SANS les inconvénients de l'IS.

Source : PAT-016 — M6, Module F7

*Modules : M6 | Règles : PAT-016*

---

## [FS-025] 🏠 Patrimonial — 🟥 Complexe

**Question :** J'ai un bénéfice BNC de 150 000 €. Quelles sont les 3 optimisations fiscales les plus efficaces pour moi ?

*Contexte : Médecin libéral, célibataire, TMI 45 % (> 180 295 €), pas d'immobilier locatif, pas d'IFI.*

**Réponse idéale :**

À TMI 45 %, chaque euro de charge déductible économise 45 centimes d'IR + réduction des cotisations sociales sur le bénéfice.

**1. PER (Plan d'Épargne Retraite) — impact maximal**
Versement déductible du BNC dans la limite du plafond TNS. Sur 150 000 € de bénéfice :
Plafond ≈ 10 % × 150 000 + 15 % × (bénéfice entre 1 et 8 × PASS 47 100 €)
→ Plafond estimé ~32 000–38 000 € de versement déductible
Économie fiscale = ~38 000 × 45 % = **17 100 € d'IR économisé** + réduction des cotisations sociales

**2. Contrat Madelin / loi Madelin (remplacé par PER mais cotisations santé/prévoyance déductibles)**
Cotisations de santé complémentaire et de prévoyance souscrites dans le cadre professionnel sont déductibles du BNC.

**3. Dons aux organismes d'intérêt général**
Réduction d'impôt de **66 %** des dons dans la limite de 20 % du revenu imposable (ou 75 % jusqu'à 1 000 €/an pour organismes d'aide aux personnes en difficulté).
Exemple : 3 000 € de dons → réduction de 66 % = **1 980 €** d'IR en moins (hors niches fiscales)

⚠️ À ce niveau de revenus, vérifier si CEHR est applicable (RFR > 250 000 € → 3 % puis 4 % sur l'excédent).

Source : GFPL-125, GFPL-165, M2 — Module H2

*Modules : M2 | Règles : GFPL-125, GFPL-166, GFPL-170*

---

