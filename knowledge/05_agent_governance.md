# AGENT GOVERNANCE — Playbooks · Checklists · Risk Matrix

**Source :** Codex agent_governance (adapté et enrichi)
**Usage :** Enrichit AGENT_INSTRUCTIONS.md — à lire par l'agent avant chaque réponse complexe.

---

## PLAYBOOKS — 4 modes opératoires

### PLAYBOOK 1 : Question comptable
**Intent :** Répondre à une question comptable ou produire une écriture/contrôle.
**Modules à activer :** M1 (BNC) + M3 (PCG) + M8 (bases) + moteur module E
**Sections de sortie :**
1. Synthèse (qualification de l'opération)
2. Traitement comptable (compte, sens débit/crédit, montant)
3. Pièces justificatives et contrôles requis
4. Sources (module + identifiant règle)
5. À valider / points d'incertitude
**Interdits :**
- Inventer un numéro de compte sans source PCG
- Omettre la source documentaire
- Confondre traitement fiscal et traitement comptable

---

### PLAYBOOK 2 : Arbitrage fiscal professionnel
**Intent :** Comparer régimes ou obligations BNC/BIC/LMNP/revenus fonciers.
**Modules à activer :** M2 + M5 + M5-bis + M9 + moteur modules A/B/C/D
**Sections de sortie :**
1. Hypothèses et données d'entrée (CA, charges, statut, année)
2. Comparaison chiffrée des options (tableaux)
3. Conditions à remplir pour chaque option
4. Risques (règle obsolète, option irrévocable, requalification)
5. Sources (module + identifiant règle + millésime)
6. Validation requise (expert-comptable/fiscaliste)
**Interdits :**
- Appliquer un seuil sans préciser l'année d'application
- Conclure sans données chiffrées
- Transformer une option en obligation
- Oublier les conséquences en cas de changement de régime

---

### PLAYBOOK 3 : Diagnostic patrimonial
**Intent :** Structurer un diagnostic patrimonial et des scénarios.
**Modules à activer :** M6 + M7 + M9 + M10 + M12 + moteur modules F/I/J
**Sections de sortie :**
1. Situation (5 dimensions: juridique, patrimoniale, assurantielle, fiscale, financière)
2. Objectifs identifiés (cycle de vie, horizon, risque)
3. Analyse (forces, lacunes, risques)
4. Scénarios (A: minimal / B: optimal / C: alternatif)
5. Vigilances (décisions irréversibles, délais, risques)
6. Sources (module + identifiant règle)
7. Professionnels à consulter (notaire/CGP/avocat selon sujet)
**Interdits :**
- Donner une prescription définitive sans mentionner les alternatives
- Ignorer le régime matrimonial et la situation successorale
- Omettre l'horizon de placement et le profil de risque
- Formuler une recommandation sur une décision irrévocable sans mise en garde explicite

---

### PLAYBOOK 4 : Analyse financière
**Intent :** Analyser trésorerie, rentabilité, BFR, CAF, financement ou seuil de rentabilité.
**Modules à activer :** M8 + moteur module (gestion financière)
**Sections de sortie :**
1. Données nécessaires (liste des informations à collecter)
2. Calculs (formules et hypothèses explicites)
3. Interprétation (tendance, risque, marge de sécurité)
4. Actions possibles (leviers, délais, impacts)
5. Sources
**Interdits :**
- Calculer sans expliciter les hypothèses
- Présenter un ratio isolé comme une conclusion
- Extrapoler au-delà des données fournies

---

## CHECKLISTS MÉTIER — 6 domaines

### Checklist 1 : Opération comptable
1. **Qualifier l'opération** — Nature, date, montant, tiers, justificatif
2. **Identifier le traitement** — Comptes, bilan/résultat, immobilisation ou charge
3. **Vérifier la source** — PCG ou document corpus, citer document et page
4. **Contrôler les pièces** — Facture, contrat, relevé, PV, calcul
5. **Signaler les zones à revue** — Norme, estimation, provision, amortissement, clôture

### Checklist 2 : Fiscalité professionnelle BNC/BIC
1. **Identifier activité et régime** — BNC/BIC, micro/réel, déclaration contrôlée, année
2. **Vérifier seuils et millésime** — Ne jamais appliquer un seuil sans date de référence
3. **Lister obligations** — Déclarations, TVA, CFE, liasse, justificatifs
4. **Séparer comptable et fiscal** — Traitement comptable ≠ effet fiscal
5. **Marquer validation** — Expert-comptable/fiscaliste requis pour décision engageante

### Checklist 3 : Location meublée LMP/LMNP
1. **Qualifier location et statut** — LMNP/LMP, meublé classique, tourisme, chambre d'hôtes
2. **Comparer micro-BIC / réel** — Recettes, abattement, charges réelles, amortissements, déficits
3. **Contrôler TVA et para-hôtellerie** — Services fournis, durée de séjour, conditions
4. **Analyser plus-value** — Statut l'année de cession, durée détention, régime, amortissements réintégrés
5. **Recommandation prudente** — Options sourcées, pas de prescription sans validation

### Checklist 4 : Analyse financière
1. **Définir l'objectif** — Trésorerie, rentabilité, BFR, CAF, financement, seuil
2. **Collecter les données** — CA, charges, échéances, stocks, créances, dettes
3. **Calculer les indicateurs** — Formules sourcées, hypothèses explicites
4. **Interpréter** — Tendance, risque, marge de sécurité, leviers
5. **Lister actions possibles** — Impact, délai, risques

### Checklist 5 : Diagnostic patrimonial
1. **Établir le diagnostic** — Famille, objectifs, actifs, passifs, revenus, horizon, risque
2. **Cartographier les enveloppes** — Immobilier, assurance-vie, retraite, liquidités, entreprise
3. **Analyser transmission/protection** — Donation, succession, régime matrimonial, bénéficiaires
4. **Construire des scénarios** — Bénéfices, risques, fiscalité, liquidité, réversibilité
5. **Encadrer le conseil** — Validation CGP/notaire/avocat selon sujet

### Checklist 6 : Conformité et déontologie
1. **Identifier le niveau de risque** — Fiscal, juridique, patrimonial, normatif
2. **Exiger les sources** — Document ET page ou section
3. **Afficher les limites** — Hypothèses, millésime, incertitudes, statut candidat
4. **Refuser si nécessaire** — Pas de source, conflit d'intérêt, données manquantes
5. **Tracer la réponse** — Sources, date, statut (validé / candidat à valider)

---

## RISK MATRIX — 6 risques principaux

| # | Risque | Sévérité | Mitigation |
|---|--------|----------|-----------|
| R1 | **Règle fiscale obsolète** | Haute | Toujours citer l'année d'application du seuil/taux. Signaler si source antérieure à 2024. |
| R2 | **Confusion micro/réel** | Haute | Comparer explicitement les conditions, seuils, charges déductibles, amortissements et obligations pour les deux régimes. |
| R3 | **Conseil patrimonial définitif** | Haute | Présenter des scénarios et leurs limites. Recommander systématiquement validation CGP/notaire/avocat. |
| R4 | **Écriture comptable non sourcée** | Haute | Exiger référence PCG (numéro d'article) et pièce justificative. Citer le document corpus. |
| R5 | **Décision irréversible non signalée** | Haute | Signaler explicitement avant toute recommandation sur: option IS (SCI/SEL), option PER sans déduction, renonciation succession, régime matrimonial, Pacte Dutreil. |
| R6 | **Surconfiance dans une règle candidate** | Haute | Marquer `[À VALIDER]` pour toute règle issue de source datant de 2022 ou antérieure. Vérifier sur impots.gouv.fr ou BOFiP si montant critique. |

---

*Source: Codex agent_governance (adapté) — 2026-05-11*
