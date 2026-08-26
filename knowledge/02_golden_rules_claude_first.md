# Golden Rules Claude-First

Règles curated issues du dossier Claude, normalisées par Codex et reliées aux chunks/sources Codex quand possible.

## comptabilite_generale_pcg

### bnc-pcg-001 | regle
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : Regl. ANC n2014-03 (PCG) art. 110-1 ; C. com. art. L.123-12 a L.123-28
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 26-27
- Règle : Les dispositions du règlement s’appliquent à toute personne physique ou morale soumise à l’obligation légale d’établir des comptes annuels comprenant le bilan, le compte de résultat et une annexe, sous réserve des dispositions spécifiques qui leur sont applicables.

### bnc-pcg-002 | regle
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : PCG (Regl. ANC 2014-03) art. 110-2 ; C. com. art. L.123-12
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 26-27
- Règle : Le bilan, le compte de résultat et l’annexe, qui forment un tout indissociable, sont établis à la clôture de l’exercice au vu des enregistrements comptables et de l’inventaire.

### bnc-pcg-003 | regle
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : PCG art. 112-2 (non-compensation) ; C. com. art. L.123-19
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 26-27
- Règle : Les éléments d’actif et de passif sont évalués séparément. Aucune compensation ne peut être opérée entre les postes d’actif et de passif.

### bnc-pcg-004 | regle
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : PCG art. 112-2 ; C. com. art. L.123-13
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 26-27
- Règle : Le compte de résultat récapitule les charges et les produits de l’exercice, sans qu’il soit tenu compte de leur date de paiement ou d’encaissement. Aucune compensation ne peut être opérée entre les postes de charges et de produits.

### bnc-pcg-005 | regle
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.123-14 (image fidele)
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 16-17
- Règle : Les comptes annuels doivent être réguliers, sincères et donner une image fidèle du patrimoine, de la situation financière et du résultat de l’entreprise.

### bnc-pcg-006 | regle
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : PCG art. 121-5 (permanence des methodes) ; C. com. art. L.123-17
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 17-18
- Règle : Sauf cas exceptionnels, les méthodes comptables retenues et la structure du bilan et du compte de résultat ne peuvent être modifiées d’un exercice à l’autre.
- Conditions : description et justification dans l’annexe en cas de modification

### bnc-pcg-007 | regle
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.123-20 (amortissements/provisions meme sans benefice)
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 18-19
- Règle : Même en cas d’absence ou d’insuffisance du bénéfice, il doit être procédé aux amortissements, dépréciations et provisions nécessaires.

### bnc-pcg-008 | derogation
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.123-25 (regime reel simplifie)
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 19-20
- Règle : Les personnes physiques placées sur option ou de plein droit sous le régime réel simplifié d’imposition peuvent n’enregistrer les créances et les dettes qu’à la clôture de l’exercice et ne pas établir d’annexe.
- Conditions : personnes physiques | régime réel simplifié d’imposition

### bnc-pcg-009 | derogation
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.123-25
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 19-20
- Règle : Les personnes physiques placées sur option ou de plein droit sous le régime réel simplifié d’imposition peuvent inscrire au compte de résultat, en fonction de leur date de paiement, les charges dont la périodicité n’excède pas un an.
- Conditions : personnes physiques | régime réel simplifié d’imposition | périodicité n’excédant pas un an
- Exceptions : achats

### bnc-pcg-010 | derogation
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.123-25 et L.123-28
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 25-26
- Règle : Les personnes mentionnées aux articles L. 123-25 et L. 123-28 peuvent procéder à l’enregistrement comptable des encaissements et des paiements en retenant la date de l’opération figurant sur le relevé bancaire.
- Conditions : personnes mentionnées aux articles L. 123-25 et L. 123-28

### bnc-pcg-011 | obligation
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : CGI art. 50-0 (micro-BIC) (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042159220/) ; C. com. art. L.123-28 (verifie le 2026-06-05)
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 20-20
- Règle : Les personnes physiques bénéficiant du régime défini à l’article 50-0 du CGI tiennent un livre mentionnant chronologiquement le montant et l’origine des recettes perçues au titre de leur activité professionnelle.
- Conditions : régime défini à l’article 50-0 du CGI

### bnc-pcg-012 | obligation
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : PCG art. 911-3 (documentation comptable) ; C. com. art. R.123-172
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 20-21
- Règle : Un document décrivant les procédures et l’organisation comptables est établi dès lors qu’il est nécessaire à la compréhension du système de traitement et à la réalisation des contrôles.
- Conditions : nécessaire à la compréhension du système de traitement et à la réalisation des contrôles

### bnc-pcg-013 | obligation
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.123-12 (livre-journal, grand-livre)
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 20-21
- Règle : Tout commerçant tient obligatoirement un livre-journal et un grand-livre.

### bnc-pcg-014 | obligation
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.123-12 al. 1
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 20-21
- Règle : Les mouvements affectant le patrimoine de l’entreprise sont enregistrés opération par opération et jour par jour pour le livre-journal.

### bnc-pcg-015 | obligation
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : PCG art. 921-3 (enregistrement) ; C. com. art. R.123-174
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 20-21
- Règle : Tout enregistrement comptable précise l’origine, le contenu et l’imputation de chaque donnée ainsi que les références de la pièce justificative qui l’appuie.

### bnc-pcg-016 | obligation
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.123-22 (conservation 10 ans)
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 19-20
- Règle : Les documents comptables et les pièces justificatives sont conservés pendant dix ans.

### bnc-pcg-017 | regle
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : PCG art. 213-1 et 213-3 (cout d'acquisition / valeur venale / cout de production)
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 18-19
- Règle : Les biens acquis à titre onéreux sont enregistrés à leur coût d’acquisition, les biens acquis à titre gratuit à leur valeur vénale et les biens produits à leur coût de production.

### bnc-pcg-018 | regle
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : PCG art. 213-8 (cout d'acquisition = prix d'achat + frais accessoires)
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 21-22
- Règle : Le coût d’acquisition est égal au prix d’achat majoré des frais accessoires nécessaires à la mise en état d’utilisation du bien.

### bnc-pcg-019 | obligation
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : PCG art. 214-1 et s. (plan d'amortissement) ; C. com. art. L.123-18
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 21-22
- Règle : Les éléments de l’actif immobilisé dont la durée d’utilisation est limitée sont amortis sur cette durée selon un plan d’amortissement.
- Conditions : durée d’utilisation limitée

### bnc-pcg-020 | obligation
- Module : M3
- Statut : `candidate_to_validate`
- Ancre : PCG art. 322-1 et s. (provisions pour risques et charges) ; C. com. art. L.123-20
- source_ingest : Recueil-NF-Janvier-2025.pdf, p. 22-23
- Règle : Les risques et charges, nettement précisés quant à leur objet, que des événements survenus ou en cours rendent probables, entraînent la constitution de provisions.
- Conditions : risques et charges nettement précisés | événements survenus ou en cours | probabilité

### BCG-001 | définition
- Module : M8
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 1-19
- Règle : La comptabilité générale est un système d'information chiffré à triple finalité: (1) moyen de preuve à l'égard des tiers; (2) base de calcul des impôts et taxes; (3) outil d'information pour les dirigeants (décisions) et les tiers (banques, fournisseurs, clients, actionnaires).

### BCG-002 | définition
- Module : M8
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 1-19
- Règle : Patrimoine = Avoirs (biens + créances) - Dettes. Ne pas confondre valeur du patrimoine (total actifs - dettes) avec solde du compte bancaire (trésorerie). Enrichissement = augmentation du patrimoine. Appauvrissement = diminution du patrimoine. Charges = éléments d'appauvrissement. Produits = éléments d'enrichissement.

### BCG-003 | définition
- Module : M8
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 1-19
- Règle : Bilan = photographie du patrimoine à une date donnée. Structure: ACTIF (gauche) = ce que possède l'entreprise; PASSIF (droite) = ce que doit l'entreprise. Le bilan donne une SITUATION à un INSTANT X (différent du compte de résultat qui couvre une période).

### BCG-004 | définition
- Module : M8
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 19-26
- Règle : Compte de résultat = explique l'enrichissement ou l'appauvrissement sur UN EXERCICE COMPTABLE (période entre 2 bilans ≈ 1 an). Bénéfice = Produits > Charges. Perte = Charges > Produits. Le résultat est AVANT impôt et HORS TAXE.

### BCG-005 | obligation
- Module : M8
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 19-26
- Règle : Obligations légales comptables: (1) conservation des documents comptables et pièces justificatives; (2) enregistrement périodique des mouvements affectant le patrimoine; (3) contrôle par inventaire au moins une fois par an; (4) établissement des comptes annuels (bilan + compte de résultat + annexe).

### BCG-006 | règle
- Module : M8
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 26-35
- Règle : Principe de la partie double: chaque écriture comptable est équilibrée → montant débit = montant crédit. Le journal enregistre les opérations chronologiquement par pièce justificative. Le grand livre reprend toutes les écritures par compte. La balance récapitule tous les comptes avec leurs soldes: Total débits = Total crédits.

### BCG-007 | règle
- Module : M8
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 35-40
- Règle : PCG 2018: chaque écriture doit s'appuyer sur une pièce justificative datée, établie sur support papier ou électronique fiable. Pour les comptabilités informatisées: procédure de validation interdisant toute modification ou suppression; procédure de clôture périodique pour figer la chronologie.

### BCG-008 | définition
- Module : M8
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 40-46
- Règle : Plan de trésorerie: tableau présentant tous les décaissements et encaissements prévus sur l'année, décomposé par mois (montants TTC). Solde trésorerie fin de mois = Solde début + Total encaissements TTC - Total décaissements TTC. Permet de prévoir les besoins de financement et de gérer la TVA.

### BCG-009 | définition
- Module : M8
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 46-52
- Règle : Besoin en fonds de roulement (BFR) = Stocks + Créances clients - Dettes fournisseurs. Représente le montant de financement nécessaire pour couvrir l'exploitation courante (délais de paiement clients vs fournisseurs + délais de stockage).

### BCG-010 | définition
- Module : M8
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 46-52
- Règle : Capacité d'autofinancement (CAF) = Bénéfice net après impôts + Dotations aux amortissements. Représente le surplus monétaire potentiel dégagé par l'activité. Utilisations: renforcement de la structure financière, investissements, remboursement d'emprunts, dividendes, valorisation des salariés.

### BCG-011 | règle
- Module : M8
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 52-55
- Règle : TVA collectée - TVA déductible = TVA à payer. La TVA est un impôt indirect: seul le consommateur final paie l'ensemble de la TVA. La TVA doit apparaître sur chaque facture. Montant HT (hors taxes) = base de calcul des prix et marges. TTC = HT × (1 + taux TVA).
- Taux : `{"taux_standard": 20}`

### BCG-012 | définition
- Module : M8
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 55-59
- Règle : Seuil de rentabilité (point mort) = Charges fixes / Taux de marge sur coûts variables. Taux MCV = (CA - Charges variables) / CA × 100. Charges fixes: loyer, assurance, charges sociales fixes. Charges variables: frais de déplacement VRP, commissions sur ventes. Au-delà du point mort: l'entreprise dégage des bénéfices.

### FORM-007 | formule
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : LES BASES DE LA COMPTABILITÉ.pdf, p. 55-59
- Règle : Seuil de rentabilité (SR) = Charges fixes / Taux de marge sur coûts variables. Taux MCV = (CA − Charges variables) / CA × 100. Point mort en jours = SR / (CA annuel / 365). CAF = Résultat net + Dotations aux amortissements. BFR = Stocks + Créances clients − Dettes fournisseurs. Fonds de roulement net global (FRNG) = Capitaux permanents − Actif immobilisé net. Trésorerie nette = FRNG − BFR.

## fiscalite_professionnelle_bnc_bic

### bnc_001 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 93 (BNC, recettes-depenses) et art. 96 (declaration controlee) ; BOI-BNC-BASE-20 (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046872511/) (verifie le 2026-06-05)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 8-9
- Règle : L'activité libérale relevant des BNC est soumise au régime de la déclaration contrôlée, fondé sur une logique recettes encaissées / dépenses payées, sauf option spécifique pour une comptabilité créances-dettes.

### bnc_002 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 99 (livre-journal et registre des immobilisations) ; BOI-BNC-DECLA-10-20
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 11-12
- Règle : Le professionnel doit tenir un livre-journal des recettes et des dépenses professionnelles et un registre des immobilisations et des amortissements.

### bnc_003 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 5-5
- Règle : Il est recommandé d'utiliser un compte bancaire exclusivement réservé à l'activité professionnelle afin de séparer les opérations privées et professionnelles.

### bnc_004 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 99 ; BOI-BNC-DECLA-10-20
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 11-12
- Règle : Le livre-journal doit être servi au jour le jour, par ordre de date, sans blancs, sans lacunes, sans ratures ni surcharges.

### bnc_005 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 99 ; BOI-BNC-DECLA-10-20-10
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 9-9
- Règle : Le livre-journal doit mentionner pour les recettes le détail des sommes reçues, l'identité du client, le mode de règlement et la nature des prestations fournies.

### bnc_006 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 99 ; BOI-BNC-DECLA-10-20-10 (secret professionnel)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 8-9
- Règle : L'identité complète du client peut être remplacée dans le livre-journal par une référence à un document annexe ou un fichier couvert par le secret professionnel, à condition de pouvoir fournir ces informations à l'administration sur demande.

### bnc_007 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 99 (livre-journal, mention du mode de reglement) ; BOI-BNC-DECLA-10-20-10
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 9-9
- Règle : Le mode d'encaissement ou de paiement doit être indiqué pour chaque opération : chèque, carte bancaire, espèces ou virement.

### bnc_008 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 93, 1 (recettes encaissees) ; BOI-BNC-BASE-20-10-10
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 17-18
- Règle : Le critère de prise en compte des recettes est l'encaissement. Les recettes doivent être comptabilisées à la date de réception du chèque, du paiement en espèces, de l'inscription au crédit du compte, de l'échéance pour une traite, de la libre disposition des fonds pour un compte courant ou de l'encaissement par le tiers.

### bnc_009 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 93, 1 (depenses payees) ; BOI-BNC-BASE-40-10
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 20-21
- Règle : Le critère de prise en compte des dépenses est le décaissement. Les dépenses doivent être enregistrées selon la date de remise du chèque ou du TIP, la date du paiement en espèces, la date d'inscription au débit du compte pour un virement, la date d'échéance pour une traite, la date de non libre disposition des fonds pour un compte courant, ou la date de paiement par carte.

### bnc_010 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 93, 1 ; BOI-BNC-BASE-40-10
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 20-21
- Règle : En cas de carte bancaire à débit différé, la dépense se comptabilise à la date du paiement par carte, et non à la date de l'inscription sur le relevé bancaire.

### bnc_011 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : LPF art. L.102 B (pieces justificatives) ; BOI-BNC-DECLA-10-20
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 14-15
- Règle : Tout enregistrement comptable doit être appuyé d'une pièce justificative, soit de base, soit récapitulative.

### bnc_012 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : LPF art. L.102 B (justificatifs) ; CGI art. 289, II (mentions des factures) ; BOI-BNC-DECLA-10-20
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 6-8
- Règle : Pour sécuriser la déductibilité, les pièces justificatives doivent comporter la date, l'identité et l'adresse de l'émetteur, l'identité et l'adresse du destinataire, le libellé de l'opération et la ventilation HT/TVA/TTC.

### bnc_013 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 93, 1 (depenses necessitees par l'exercice de la profession) ; BOI-BNC-BASE-40-10 (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046872511/) (verifie le 2026-06-05)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 6-8
- Règle : Pour être déductible, une dépense doit être nécessité par l'exercice de la profession, exposée dans l'intérêt direct de l'exploitation ou se rattacher à la gestion normale de l'activité.

### bnc_014 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : LPF art. L.102 B (conservation pieces) et L.169 (delai de reprise) ; C. com. art. L.123-22 (10 ans)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 15-16
- Règle : Les documents fiscaux doivent être conservés 6 ans et les livres, registres et pièces comptables justificatives 10 ans.

### bnc_015 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 93, 1 (quote-part professionnelle) ; BOI-BNC-BASE-40-60
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 5-5
- Règle : Seule la quote-part professionnelle d'une dépense mixte est déductible. La part privée doit être soit réintégrée extra-comptablement, soit passée en prélèvements personnels.

### bnc_016 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 93, 1 (frais professionnels) ; BOI-BNC-BASE-40-60 (frais mixtes evalues forfaitairement)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 22-23
- Règle : Les frais de blanchissage à domicile peuvent être évalués forfaitairement à partir des tarifs des blanchisseurs, à condition de conserver le détail du calcul.

### bnc_017 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : BOI-BAREME-000001 (bareme kilometrique) ; CGI art. 93 (frais de vehicule)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 22-23
- Règle : Les frais de voiture peuvent être évalués au barème kilométrique, sous réserve d'un suivi précis des kilomètres professionnels. Les dépenses réelles couvertes par ce barème et payées par le compte professionnel doivent alors être traitées en prélèvements personnels.

### bnc_018 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 23-25
- Règle : Les transferts entre comptes de trésorerie professionnels doivent être isolés dans une colonne 'virements internes'. Cette opération est purement financière et n'a aucune incidence sur le résultat.

### bnc_019 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 93 (deductibilite des interets, non du capital) ; BOI-BNC-BASE-40-60
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 18-20
- Règle : Le capital reçu au titre d'un emprunt professionnel constitue un mouvement patrimonial. Lors du remboursement, seule la part intérêts est fiscalement déductible ; la part capital ne l'est pas.

### bnc_020 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 5-5
- Règle : Le compte prélèvements personnels sert à enregistrer les retraits privés sur le compte professionnel, les dépenses privées payées avec ce compte et certaines dépenses couvertes par des forfaits.

### bnc_021 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 25-26
- Règle : Le compte apports personnels sert à enregistrer les mouvements de trésorerie privée vers la trésorerie professionnelle ou l'arrivée de sommes non imposables au titre des BNC sur le compte professionnel.

### bnc_022 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 25-26
- Règle : Lorsqu'un chèque déjà comptabilisé revient impayé, il faut soit annuler la recette en négatif dans le journal des recettes, soit enregistrer l'impayé dans le journal des dépenses.

### bnc_023 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 93, 1 et art. 99 (registre des immobilisations et amortissements) ; BOI-BNC-BASE-50
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 45-45
- Règle : Les acquisitions d'immobilisations ne sont pas déductibles immédiatement ; leur coût est étalé dans le temps par le biais de l'amortissement et elles doivent figurer au registre des immobilisations et des amortissements.

### bnc_024 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 99 (nomenclature et tenue du livre-journal/registre des immobilisations) ; BOI-BNC-DECLA-10-20
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 9-11
- Règle : La nomenclature comptable applicable comprend notamment les comptes financiers, les recettes professionnelles d'exploitation, les honoraires rétrocédés, les dépenses professionnelles d'exploitation, les recettes et dépenses patrimoniales, et les immobilisations/amortissements.

### bnc_025 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 99 ; LPF art. L.47 A I et art. A.47 A-1 (FEC)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 5-6
- Règle : Une comptabilité tenue informatiquement doit permettre la production d'un FEC conforme. L'usage d'un simple tableur ne permet pas de satisfaire à cette exigence.

### bnc_026 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 1729 D (amende defaut de FEC)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 5-6
- Règle : Le défaut de présentation du FEC est passible d'une amende de 5 000 euros par exercice ou année contrôlée, ou de 10 % des droits rappelés si ce montant est plus élevé.

### bnc_027 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : LPF art. A.47 A-1 (FEC) ; CGI art. 1729 D (amende defaut de FEC)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 6-8
- Règle : Avant la télétransmission de la déclaration 2035, les écritures doivent être validées et le FEC généré et sauvegardé. Les dates de validation doivent être antérieures ou concomitantes à la télétransmission.

### bnc_028 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : LPF art. L.13 G ; BOI-DJC-OA-20-10-20 (examen periodique de sincerite)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 5-6
- Règle : L'examen périodique de sincérité porte sur la déductibilité des dépenses, les amortissements et les réductions ou crédits d'impôt. Sa périodicité est de 6 ans si la comptabilité est tenue par un expert-comptable, sinon de 3 ans.

### bnc_029 | table
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : LPF art. L.13 G ; BOI-DJC-OA-20-10-20 (examen periodique de sincerite, nombre de pieces)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 6-8
- Règle : Nombre de pièces examinées dans l'EPS

### bnc_030 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 96 (declaration 2035) et art. 170 (2042) ; BOI-BNC-DECLA-20
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 8-9
- Règle : La sage-femme déclare le BNC issu de son activité via le formulaire 2035. Le revenu est ensuite reporté sur la déclaration du foyer fiscal via le formulaire 2042 C-PRO.

### bnc_031 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 158, 7 (majoration absence d'OGA, supprimee a compter de l'IR 2023) ; BOI-DJC-OA
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 8-9
- Règle : L'adhésion à une association de gestion agréée n'est pas obligatoire, mais le document indique qu'elle permet d'éviter une majoration de 25 % de l'impôt sur le revenu.

### bnc_032 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 93, 1 (depenses necessitees par l'exercice de la profession) ; BOI-BNC-BASE-40
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 6-8
- Règle : Les charges comprennent notamment le loyer, les charges sociales, les impôts, internet, le téléphone, le logiciel dossier patient, le logiciel de télétransmission, le secrétariat et la gestion des DASRI.

### bnc_033 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CSS art. L.131-6 (assiette des cotisations TNS) ; CGI art. 154 bis
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 56-57
- Règle : Les cotisations sociales comprennent notamment celles dues à l'URSSAF et à la CARCDSF. Elles sont calculées sur la base du revenu professionnel et peuvent être forfaitaires les premières années puis régularisées.

### bnc_034 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CGI art. 240 (declaration des honoraires DAS 2) ; CSS art. L.133-5-3 (DSN)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 14-15
- Règle : La DADS doit être remplie avant le 1er mai si le cabinet emploie des salariés. La DAS 2 doit être remplie en l'absence de salarié mais en présence d'honoraires versés, par exemple à une AGA ou au titre de rétrocessions. Le document mentionne ensuite la DSN.

### bnc_035 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 9-9
- Règle : Si la CPAM du lieu d'exercice n'a pas conclu d'accord avec l'URSSAF, la sage-femme doit aussi accomplir les formalités auprès de l'URSSAF au plus tard dans les 8 jours suivant le début de l'activité. Le CFE centralise ensuite les informations vers les organismes sociaux et fiscaux.

### bnc_036 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : CSS art. L.640-1 et art. L.642-1 (affiliation obligatoire au regime des professions liberales / CARCDSF)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 14-14
- Règle : Toute sage-femme inscrite à l'Ordre et commençant une activité libérale doit se déclarer obligatoirement à la CARCDSF dans un délai d'un mois.

### bnc_037 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : Loi n78-17 du 06/01/1978 (informatique et libertes) ; RGPD (UE) 2016/679, art. 9 (donnees de sante)
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 12-14
- Règle : Les fichiers patients contiennent des données sensibles. Le document indique qu'une déclaration CNIL n'est pas nécessaire pour des fichiers patients sécurisés, mais qu'une déclaration doit être faite avant la mise en place d'un système informatique destiné à sécuriser ces données.

### bnc_038 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 14-15
- Règle : Une sage-femme conventionnée peut rompre l'accord tacite avec la CPAM en l'informant par lettre recommandée avec avis de réception. La décision devient définitive un mois après réception du courrier.

### bnc_039 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 20-21
- Règle : La sage-femme non conventionnée fixe librement ses honoraires, doit en informer sa patientèle et relève selon le document d'un régime social différent pour sa propre protection sociale.

### bnc_040 | regle
- Module : M1
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Le_Plus-La_comptabilite_du_professionnel_liberal.pdf, p. 5-6
- Règle : Le non-respect des termes du conventionnement peut entraîner un examen par les instances paritaires et des sanctions telles qu'une suspension, une interdiction temporaire ou définitive d'exercer ou une amende administrative pouvant aller jusqu'à 3 000 euros.

### GFPL-001 | définition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 9-11
- Règle : Les professions libérales exercent une activité indépendante de prestations intellectuelles, techniques ou de soins.
- Ancre précisée (2026-08-26) : Loi n°2012-387 du 22/03/2012, art. 29 (définition légale des professions libérales)

### GFPL-002 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi n2022-1158 du 19/08/2022 (definition des professions liberales reglementees) ; CGI art. 92 (BNC)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 9-11
- Règle : Une profession libérale réglementée est régie par des règles de fonctionnement et d’organisation fixées par la loi ou un texte réglementaire.
- Ancre précisée (2026-08-26) : Ordonnance n° 2023-77 du 08/02/2023, art. 1er (ex-art. 29, loi n° 2012-387) ; CGI art. 92

### GFPL-003 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 9-11
- Règle : Le respect des règles de la profession est contrôlé par une instance professionnelle.
- Conditions : ordre professionnel, chambre professionnelle ou syndicat

### GFPL-004 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 9-11
- Règle : L’usage du titre est protégé.
- Ancre précisée (2026-08-26) : C. pénal art. 433-17 (usurpation de titre) ; fiche DGE « Les professions libérales réglementées »

### GFPL-005 | classification
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 9-11
- Règle : Les professions libérales réglementées sont organisées en trois familles : santé, juridique, technique/cadre de vie.
- Ancre précisée (2026-08-26) : Ordonnance n 2023-77 du 08/02/2023 relative a l'exercice en societe des professions liberales reglementees

### GFPL-006 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.526-22 (entreprise individuelle, profession liberale) ; ordonnance n2023-77 du 08/02/2023
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-11
- Règle : Une profession libérale peut être exercée en entreprise individuelle sous réserve des dispositions spécifiques applicables.

### GFPL-007 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.526-22 (entreprise individuelle : pas d'associe)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-11
- Règle : L’entreprise individuelle ne permet pas d’avoir un associé.

### GFPL-008 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.526-22 (entrepreneur individuel : decisions seules)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-11
- Règle : L’entrepreneur individuel prend seul les décisions concernant son entreprise.

### GFPL-009 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.526-22 (entreprise individuelle : pas de statuts a rediger)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 9-11
- Règle : L’entrepreneur individuel n’a pas besoin de rédiger des statuts.

### GFPL-010 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.526-22 (entreprise individuelle : pas de capital social)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-11
- Règle : L’entreprise individuelle n’exige pas d’apport minimal car elle n’a pas de capital.

### GFPL-011 | obligation
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 286 (declaration d'activite) ; C. com. art. R.123-1 et s. (guichet unique)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-11
- Règle : Pour créer une entreprise individuelle en profession libérale, il convient de procéder à l’immatriculation en ligne puis de déclarer l’activité à l’URSSAF.
- Précision (vérif. source officielle 2026-08-26) : Depuis le 01/01/2023, la formalite est unique : declaration de creation sur le guichet unique gere par l'INPI (C. com. art. L.123-33 et R.123-1 s.), qui transmet aux organismes dont l'URSSAF ; l'affiliation URSSAF est automatique, il n'y a plus de declaration separee a l'URSSAF ('Vous ne pouvez plus creer votre entreprise sur le site de l'Urssaf' - urssaf.fr).

### GFPL-012 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.526-22 et s. (statut unique entrepreneur individuel, loi 2022-172 du 14/02/2022)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 9-11
- Règle : Les entreprises individuelles créées depuis le 15 mai 2022 bénéficient du statut unique d’entreprise individuelle avec responsabilité limitée aux biens utiles à l’activité professionnelle.
- Précision (vérif. source officielle 2026-08-26) : Le statut unique (C. com. art. L.526-22 et s., loi 2022-172, en vigueur le 15/05/2022) ne bénéficie pas qu'aux EI « créées depuis le 15 mai 2022 » : il s'applique à tous les entrepreneurs individuels, la séparation des patrimoines ne jouant, pour les EI préexistantes, que pour les créances nées à compter du 15/05/2022.

### GFPL-013 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi 2022-172 du 14/02/2022 art. 6 (extinction de l'EIRL) ; ancien C. com. art. L.526-6
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 9-11
- Règle : Il n’est plus possible d’opter pour le statut d’EIRL depuis février 2022.

### GFPL-014 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi 2022-172 du 14/02/2022 art. 6 (maintien des EIRL existantes)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 9-11
- Règle : Les entrepreneurs ayant opté pour l’EIRL avant février 2022 conservent les caractéristiques protectrices de ce statut.

### GFPL-015 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Ordonnance n2023-77 du 08/02/2023 (exercice en societe des professions liberales reglementees)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-11
- Règle : Une profession libérale peut être exercée en société sous réserve des dispositions spécifiques applicables.

### GFPL-016 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : C. com. (formes sociales : EURL/SARL art. L.223-1, SA art. L.225-1, SAS art. L.227-1, SNC art. L.221-1)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-11
- Règle : En règle générale, les professions libérales non réglementées peuvent utiliser les formes classiques de société.
- Conditions : EURL, SARL, SA, SAS/SASU, SNC

### GFPL-017 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Ordonnance n2023-77 du 08/02/2023 (SEL, SCP, SPFPL, SPE) ; CGI art. 239 quater A (SCM) ; CSP art. L.4041-1 (SISA)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-11
- Règle : Les professions libérales réglementées peuvent notamment créer une SEL, une SCP, une SCM, une SPFPL ou une SISA.

### GFPL-018 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 239 quater A (SCM) ; loi n66-879 du 29/11/1966 art. 36 (objet de la SCM) ; BOI-BNC-SECT-70-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-13
- Règle : La SCM permet de mettre en commun des moyens sans faire disparaître l’indépendance et la clientèle de chaque associé.

### GFPL-019 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Ordonnance n2023-77 du 08/02/2023, livre V (SPFPL) ; ancien loi n90-1258 art. 31-1
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-13
- Règle : La SPFPL a pour objet la détention de titres de sociétés et ne permet pas en soi la réalisation de l’activité.

### GFPL-020 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CSP art. L.4041-1 et s. (SISA) ; loi n2011-940 du 10/08/2011 art. 1 (creation de la SISA)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-13
- Règle : La SISA permet à des professionnels de santé exerçant différentes professions de partager les rémunérations perçues pour l’exercice en commun.

### GFPL-021 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-13
- Règle : La location financière ne permet pas d’acquérir le matériel en fin de location, contrairement au crédit-bail.
- Ancre précisée (2026-08-26) : C. mon. fin. art. L.313-7 (crédit-bail : location avec possibilité d'acquisition)

### GFPL-022 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 11-13
- Règle : Le coût de la location financière est plus élevé que celui du crédit-bail.

### GFPL-023 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 13-14
- Règle : Le professionnel peut financer son matériel par un crédit, un crédit-bail ou une location financière.
- Ancre précisée (2026-08-26) : C. mon. fin. art. L.313-7 (credit-bail) ; location financiere : location sans option d'achat

### GFPL-024 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 13-14
- Règle : Les déductions fiscales du crédit classique et celles du crédit-bail ou de la location financière sont identiques sur la durée du financement.
- Conditions : déduction des intérêts et amortissements pour le crédit ; déduction des loyers puis amortissement de la valeur résiduelle éventuelle pour crédit-bail/location
- Précision (vérif. source officielle 2026-08-26) : Équivalence seulement globale, pas identité : les loyers de crédit-bail sont intégralement déductibles « sous réserve de la limitation prévue à l'article 39-4 du CGI » (BOI-BIC-BASE-60-20) et, en crédit-bail immobilier, la quote-part de loyer correspondant au terrain n'est pas déductible (CGI art. 239 sexies et s.) ; en crédit classique on déduit intérêts + amortissements, totaux proches mais non « identiques » dans tous les cas.

### GFPL-025 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 13-14
- Règle : Le crédit traditionnel procure des déductions plus importantes en début de période de remboursement, surtout avec un amortissement dégressif.

### GFPL-026 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 13-14
- Règle : Le crédit-bail et la location financière alignent le montant des déductions sur le montant des loyers annuels.
- Précision (vérif. source officielle 2026-08-26) : Les loyers de credit-bail et de location financiere sont en principe integralement deductibles (BOI-BIC-BASE-60-20 ; CGI art. 93, 1 pour les BNC), MAIS sous exceptions notables : plafonnement pour les vehicules de tourisme (CGI art. 39, 4 et 93, 1-2°) et quote-part du loyer se rapportant au terrain en credit-bail immobilier ; l'alignement pur sur les loyers annuels n'est donc pas systematique.

### GFPL-027 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 13-14
- Règle : Lorsque le bien financé est intégralement lié à l’activité professionnelle, il est possible de majorer le premier loyer du crédit-bail pour maximiser les charges déductibles.
- Précision (vérif. source officielle 2026-08-26) : Le premier loyer majoré d'un crédit-bail d'un bien affecté à l'activité est déductible l'année du paiement (BNC, comptabilité de caisse), mais la doctrine et la jurisprudence n'admettent la majoration que dans certaines limites (tolérance de l'ordre de 25-30 % de la valeur du bien, risque de remise en cause au-delà) — condition absente de l'énoncé.

### GFPL-028 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 8 (societes a l'IR) et art. 206 (assujettissement a l'IS)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 13-14
- Règle : Selon le statut juridique, les bénéfices sont soumis à l’impôt sur le revenu ou à l’impôt sur les sociétés.

### GFPL-029 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 206, 3 (option IS des societes de personnes) et art. 239
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 13-14
- Règle : Les structures relevant de plein droit de l’IR peuvent opter pour l’IS, et inversement selon les cas prévus.

### GFPL-030 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 239 quater A (la SCM n'entre pas dans le champ de l'IS) ; BOI-BNC-SECT-70-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 14-15
- Règle : La SCM ne peut pas être assujettie à l’impôt sur les sociétés.

### GFPL-031 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 206, 1 (SEL soumise a l'IS de plein droit) ; ordonnance n2023-77 du 08/02/2023
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 14-15
- Règle : La SEL est soumise de plein droit à l’IS dans les conditions de droit commun.
- Précision (vérif. source officielle 2026-08-26) : Exact pour les SELAFA, SELAS, SELCA et SELARL pluripersonnelles (CGI art. 206, 1 — sociétés de capitaux), mais la SELARL unipersonnelle dont l'associé unique est une personne physique relève de plein droit du régime des sociétés de personnes (IR, régime EURL, BOI-BNC-SECT-70-40), sauf option pour l'IS.

### GFPL-032 | exception
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 8 (EURL/SELARL unipersonnelle a l'IR) et art. 206, 3 (option IS)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 14-15
- Règle : La SELARL unipersonnelle dont l’associé unique est une personne physique est soumise de plein droit à l’IR avec possibilité d’option irrévocable pour l’IS sous conditions.
- Précision (vérif. source officielle 2026-08-26) : IR de plein droit exact (CGI art. 8) et option IS possible (CGI art. 239 ; art. 206, 3), mais depuis la LF 2019 (loi n° 2018-1317, art. 50) l'option n'est plus d'emblee irrevocable : renonciation possible jusqu'au 5e exercice suivant celui de l'option ; elle ne devient irrevocable qu'a defaut de renonciation dans ce delai (BOI-IS-CHAMP-20-20-30).

### GFPL-033 | exception
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 239 bis AB (option IR temporaire 5 ans pour societes de capitaux) ; BOI-IS-CHAMP-20-20-30
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 14-15
- Règle : Une SEL en début d’activité peut opter pour l’IR pendant 5 ans à partir de sa création sous conditions.
- Conditions : au moins 50 % du capital et des droits de vote détenus par des personnes physiques | au moins 34 % du capital et des droits de vote détenus directement ou indirectement par les dirigeants ou des membres de leur foyer fiscal | société de moins de 5 ans | activité principale industrielle, commerciale, artisanale, libérale ou agricole | moins de 50 salariés | CA annuel < 10 000 000 € | titres non admis aux négociations sur un marché d’instruments financiers

### GFPL-034 | obligation
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 223, 1 (declaration de resultat IS, formulaire 2065) ; BOI-IS-DECLA-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 14-15
- Règle : Si la structure est soumise à l’IS, le bénéfice net est déclaré via le formulaire 2065-SD.

### GFPL-035 | taux
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 219 (taux normal de l'IS) ; BOI-IS-LIQ-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 14-15
- Règle : Le taux normal de l’IS est de 25 % pour les exercices ouverts à compter du 1er janvier 2023.
- Taux : `"25 %"`
- Précision (vérif. source officielle 2026-08-26) : Le taux normal de 25 % (CGI art. 219, I) s'applique aux exercices ouverts a compter du 1er janvier 2022 (LF 2018 art. 84, trajectoire 28 % en 2020, 26,5 % en 2021, 25 % en 2022) - la date du 1er janvier 2023 citee est inexacte, meme si le taux de 25 % vaut bien pour 2023.

### GFPL-036 | taux réduit
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 219, I-b (taux reduit IS PME 15 %) ; BOI-IS-LIQ-20-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 15-16
- Règle : Des structures peuvent bénéficier d’un taux réduit d’IS de 15 % sur la fraction de bénéfices inférieure à 42 500 € sous conditions.
- Conditions : CA < 10 000 000 € | capital intégralement libéré | capital détenu à 75 % au moins directement ou indirectement par des personnes physiques
- Seuils : `{"tranche_benefice": 42500, "CA": 10000000}`
- Taux : `"15 %"`

### GFPL-037 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 239, 1 (renonciation a l'option IS, consequences de cessation) ; BOI-IS-CHAMP-20-20-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 15-16
- Règle : La révocation de l’option pour l’IS, possible jusqu’au 5e exercice suivant celui où elle a été exercée, est considérée comme une cessation d’activité avec ses conséquences fiscales.

### GFPL-038 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 92 (remuneration de l'associe de SEL imposee en BNC) ; BOI-BNC-CHAMP-10-30-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 16-17
- Règle : Pour les revenus perçus en 2024 et déclarés au printemps 2025, l’associé de SEL doit déclarer la rémunération liée à l’activité libérale dans la catégorie des BNC, sauf lien de subordination.

### GFPL-039 | historique
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 62 ; BOI-RSA-GER (regime SEL revenus 2023)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 15-16
- Règle : Pour les revenus perçus en 2023 et déclarés au printemps 2024, l’associé de SEL pouvait déclarer sa rémunération d’activité libérale soit en traitements et salaires / article 62, soit en BNC.

### GFPL-040 | historique
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 62 (regime SEL revenus 2022, regime transitoire)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 15-16
- Règle : Pour les revenus perçus en 2022 et déclarés au printemps 2023, l’associé de SEL déclarait sa rémunération d’activité libérale en traitements et salaires ou en rémunération de gérance article 62.
- Ancre précisée (2026-08-26) : BOFiP ACTU-2022-00159 (tolérance doctrinale, 05/01/2023) ; BOI-RES-BNC-000136 ; CGI art. 62

### GFPL-041 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 99 (obligations comptables BNC) ; BOI-BNC-DECLA-10-20 ; BOI-BNC-CHAMP-10-30-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 16-17
- Règle : Les associés de SEL imposables en BNC doivent tenir une comptabilité présentant le détail de leur rémunération et des frais engagés pour l’exercice de leur profession.

### GFPL-042 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 16-17
- Règle : L’assujettissement aux BNC n’oblige pas à l’ouverture d’un compte bancaire professionnel.
- Ancre précisée (2026-08-26) : CSS art. L.613-10 (compte dédié du micro-entrepreneur, CA > 10 000 € deux années consécutives)

### GFPL-043 | pratique
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 16-17
- Règle : En pratique, l’ouverture d’un compte professionnel peut simplifier la justification des écritures et des charges déduites des BNC.
- Conditions : cotisations versées à l’ordre | cotisations sociales | intérêts d’emprunt

### GFPL-044 | obligation
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-19
- Règle : Afin de pouvoir déclarer en mai-juin 2025 les revenus perçus en 2024, les associés de SEL doivent au préalable créer leur dossier professionnel en remplissant un questionnaire à déposer auprès du SIE dont dépend la SEL.
- Ancre précisée (2026-08-26) : Actualite impots.gouv.fr (communication DGFiP, demarche SIE des associes de SEL) ; BOI-RES-BNC-000136

### GFPL-045 | pratique
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-19
- Règle : Aucune date limite de dépôt du questionnaire SIE n’est précisée ; il est recommandé de le déposer le plus tôt possible.
- Précision (vérif. source officielle 2026-08-26) : Aucun délai légal codifié, mais le courrier accompagnant le questionnaire relatif à l'activité professionnelle (formulaire 751-SD) adressé par le SIE indique en pratique un délai de retour de 30 jours ; l'affirmation « aucune date limite n'est précisée » est donc trop absolue.

### GFPL-046 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 62 (gerant majoritaire SELARL / associe gerant SELCA) ; BOI-RSA-GER-10-30
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 16-17
- Règle : Pour un gérant majoritaire de SELARL ou un associé gérant de SELCA, la rémunération au titre des fonctions de dirigeant/gérant relève de l’article 62 du CGI.

### GFPL-047 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 80 ter (remuneration des dirigeants en traitements et salaires) ; BOI-RSA-GER-10-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 16-17
- Règle : Dans les autres cas, la rémunération au titre des fonctions de dirigeant/gérant relève des traitements et salaires.

### GFPL-048 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Ordonnance n2023-77 du 08/02/2023 (entree en vigueur 01/09/2024, mise en conformite des structures)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 15-16
- Règle : Les professions juridiques et judiciaires ne peuvent plus créer des sociétés de droit commun depuis le 1er septembre 2024 et les professionnels déjà en activité ont jusqu’au 31 août 2025 pour s’aligner sur le régime des SEL.

### GFPL-049 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 96 (declaration controlee) et art. 102 ter (micro-BNC) ; BOI-BNC-DECLA
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : Les BNC sont imposables selon deux régimes alternatifs : micro-BNC et déclaration contrôlée.

### GFPL-050 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 102 ter (seuil du micro-BNC) ; BOI-BNC-DECLA-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : Le micro-BNC s’applique si le chiffre d’affaires annuel hors taxe est inférieur au seuil de l'art. 102 ter : 77 700 € pour les revenus 2023-2025 ; 83 600 € pour les revenus 2026-2028.
- Seuils : `{"CA_HT_2025": 77700, "CA_HT_2026": 83600}` [referentiel: seuil_micro_bnc]

### GFPL-051 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 102 ter, 1 (abattement forfaitaire micro-BNC) ; BOI-BNC-DECLA-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : Le revenu imposable en micro-BNC est déterminé en appliquant un abattement forfaitaire de 34 % sur le chiffre d’affaires.
- Taux : `"34 %"`

### GFPL-052 | obligation
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 102 ter et art. 170 (declaration micro-BNC sur 2042 C PRO) ; BOI-BNC-DECLA-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : En micro-BNC, la déclaration fiscale est portée sur la 2042 C PRO rubrique « régime spécial BNC » et sur la 2042 ; une 2035 peut être éventuellement déposée.
- Précision (vérif. source officielle 2026-08-26) : CGI art. 102 ter, 2 : les contribuables au micro-BNC « portent directement sur la déclaration prévue à l'article 170 » (2042 / 2042 C PRO) le montant de leurs recettes — exact ; en revanche aucune 2035 n'est déposée en micro-BNC : le dépôt d'une 2035 vaut option pour la déclaration contrôlée (art. 102 ter, 5 renvoyant à l'art. 97) et donc sortie du régime spécial.

### GFPL-053 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 96 (declaration controlee, seuil et option) ; BOI-BNC-DECLA-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : La déclaration contrôlée s’applique si le chiffre d’affaires annuel hors taxe dépasse le seuil micro-BNC (77 700 € revenus 2023-2025 ; 83 600 € revenus 2026-2028) ou sur option du contribuable.
- Seuils : `{"CA_HT_2025": 77700, "CA_HT_2026": 83600}` [referentiel: seuil_micro_bnc]

### GFPL-054 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 93, 1 (benefice net BNC = recettes - depenses) ; BOI-BNC-BASE (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046872511/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : En déclaration contrôlée, le revenu imposable est déterminé en déduisant les charges réellement supportées du chiffre d’affaires.

### GFPL-055 | option
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 96, I (option pour la declaration controlee) ; BOI-BNC-DECLA-10-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : L’option pour la déclaration contrôlée peut être prise jusqu’à la date limite de déclaration des revenus en mai-juin de chaque année ; elle est valable un an et reconduite tacitement.
- Ancre précisée (2026-08-26) : CGI art. 102 ter, 5 (et art. 96, I pour le principe)

### GFPL-056 | obligation
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 97 (declaration de resultat 2035 en declaration controlee) ; BOI-BNC-DECLA-10-30
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : En déclaration contrôlée, le contribuable dépose la 2042 C PRO rubrique « régime déclaration contrôlée » et la déclaration de résultat BNC n° 2035 avec annexes 2035 A et B.

### GFPL-057 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 204 C (acompte de PAS preleve sur les BNC) ; BOI-IR-PAS-10-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : Pour les revenus imposables dans la catégorie des BNC, un acompte est prélevé directement sur le compte bancaire du contribuable.

### GFPL-058 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : Il ne faut pas confondre micro-BNC et micro-entreprise.
- Ancre précisée (2026-08-26) : CGI art. 102 ter ; CSS art. L.613-7 (régime micro-social)

### GFPL-059 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : La micro-entreprise est un régime unique et simplifié résultant de la fusion des régimes micro-social et micro-fiscal.

### GFPL-060 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 50-0 (micro-entreprise) et art. 102 ter (micro-BNC) ; CSS art. L.613-7
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : La micro-entreprise est accessible aux entrepreneurs individuels dont le CA annuel HT ne dépasse pas 77 700 €.
- Seuils : `{"CA_HT": 77700}`
- Précision (vérif. source officielle 2026-08-26) : Le seuil de 77 700 EUR (CGI art. 102 ter, 1 et art. 50-0, 1-2) ne vaut que pour les prestations de services et les BNC ; il est de 188 700 EUR pour les ventes et la fourniture de logement (art. 50-0, 1-1), et il est porte a 83 600 EUR pour les revenus 2026-2028 - l'enonce generalise un seuil qui n'est exact que pour les activites liberales et millesime 2023-2025.

### GFPL-061 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 102 ter, 1 (abattement forfaitaire 34 % BNC)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : La micro-entreprise permet un abattement forfaitaire de 34 % pour les activités libérales correspondant à des prestations de service non commerciales.
- Taux : `"34 %"`

### GFPL-062 | option
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 151-0 (versement liberatoire de l'IR du micro-entrepreneur) ; CSS art. L.613-7
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-17
- Règle : L’entrepreneur en micro-entreprise peut opter pour le versement libératoire de l’impôt sur le revenu, payé mensuellement ou trimestriellement en même temps que les cotisations et contributions sociales.

### GFPL-063 | exemple
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-19
- Règle : Sont citées comme professions libérales soumises à TVA : architectes, conseil, experts-comptables, activités artistiques, professions juridiques et sportives.
- Ancre précisée (2026-08-26) : CGI art. 256 et 256 A ; BOI-TVA-CHAMP-10-10-60-50

### GFPL-064 | exemple
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-19
- Règle : Sont citées comme professions libérales non soumises à TVA : activités médicales ou paramédicales et autres activités de santé, assurance/courtage, certaines activités d’enseignement/formation continue agréées, transports sanitaires.
- Ancre précisée (2026-08-26) : CGI art. 261, 4 (santé, transports sanitaires, enseignement/formation continue) ; CGI art. 261 C, 2° (assurance et courtage)

### GFPL-065 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 293 B (franchise en base de TVA) ; BOI-TVA-DECLA-40-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-19
- Règle : La franchise en base de TVA exonère les professionnels libéraux de la déclaration et du paiement de la TVA sur les prestations réalisées.

### GFPL-066 | seuil
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 293 B, I (seuils franchise en base, prestations de services)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-19
- Règle : Pour l’activité libérale hors avocat et artiste-auteur, les anciens seuils jusqu’au 28 février 2025 étaient de 37 500 € l’année civile précédente et 41 250 € l’année en cours.
- Seuils : `{"annee_precedente": 37500, "annee_en_cours": 41250}`
- Précision (vérif. source officielle 2026-08-26) : Les seuils 37 500 EUR (annee precedente) / 41 250 EUR (annee en cours) pour les prestations de services sont exacts (CGI art. 293 B issu de la LF 2024), mais le seuil unique de 25 000 EUR prevu au 1er mars 2025 (LF 2025 art. 32) a ete suspendu puis supprime par la loi n 2025-1044 du 3 novembre 2025 : ces seuils ne sont donc pas 'anciens', ils sont restes en vigueur toute l'annee 2025.

### GFPL-067 | seuil
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 293 B, III (seuils franchise avocats et auteurs)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-19
- Règle : Pour les avocats et artistes-auteurs, les anciens seuils jusqu’au 28 février 2025 étaient de 50 000 € l’année civile précédente et 55 000 € l’année en cours.
- Seuils : `{"annee_precedente": 50000, "annee_en_cours": 55000}`
- Précision (vérif. source officielle 2026-08-26) : Les montants sont exacts (CGI art. 293 B, I bis-A : plafond de 50 000 € de CA de l'année précédente, sortie en cours d'année au-delà de 55 000 €) mais les présenter comme « anciens seuils jusqu'au 28 février 2025 » est daté : l'abaissement à 25 000 € prévu par la LF 2025 au 1er mars 2025 a été suspendu, et le BOFiP consolidé au 01/07/2026 (BOI-TVA-DECLA-40-20) applique toujours 50 000/55 000 € aux avocats et auteurs.

### GFPL-068 | réforme
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi n2025-127 du 14/02/2025 (LF 2025) art. 32 (abaissement uniforme du seuil de franchise) ; CGI art. 293 B
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 17-19
- Règle : La loi de finances 2025 a prévu un abaissement uniforme des limites de franchise en base à 25 000 € l’année civile précédente et 27 500 € l’année en cours à compter du 1er mars 2025.
- Seuils : `{"annee_precedente": 25000, "annee_en_cours": 27500}`
- Précision (vérif. source officielle 2026-08-26) : La LF 2025 (art. 32) a bien prévu le seuil unique 25 000 € / 27 500 € au 1er mars 2025, mais son application a été suspendue (reports successifs, renvoi au PLF 2026) : la mesure n'a pas été appliquée et les seuils antérieurs (85 000 € / 37 500 €) sont restés en vigueur.

### GFPL-069 | suspension
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 19-20
- Règle : La réforme d’abaissement des seuils de franchise a été suspendue jusqu’au 1er juin 2025 le temps d’une concertation.
- Précision (vérif. source officielle 2026-08-26) : Exact au printemps 2025 : la reforme du seuil unique de franchise a 25 000 € (LF 2025) a bien ete suspendue jusqu'au 1er juin 2025 le temps d'une concertation, MAIS la suspension a ensuite ete prorogee jusqu'au 31 decembre 2025 (communique du 30/04/2025) et la reforme n'est finalement pas entree en vigueur (retour aux plafonds anterieurs).

### GFPL-070 | suspension
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 19-20
- Règle : Durant la suspension de la réforme, les micro-entreprises concernées ne sont pas tenues d’effectuer les nouvelles démarches déclaratives en matière de TVA.

### GFPL-071 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 19-20
- Règle : Les professions libérales sont soumises aux mêmes obligations que les autres redevables, notamment en matière de facturation et de tenue de comptabilité pour justifier le détail des opérations réalisées.
- Ancre précisée (2026-08-26) : CGI art. 286 et 289 ; BOI-TVA-DECLA-30

### GFPL-072 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 19-20
- Règle : Il existe également une obligation déclarative d’existence et d’identification.
- Ancre précisée (2026-08-26) : CGI art. 286, I-1 (declaration d'existence et d'identification dans les 15 jours)

### GFPL-073 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 266 et art. 267 (base d'imposition a la TVA) ; BOI-TVA-BASE
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 19-20
- Règle : L’assiette de la TVA est constituée de l’ensemble des honoraires perçus au titre des activités libérales, quelles que soient les modalités d’exécution et la forme juridique.

### GFPL-074 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 278 (taux normal de TVA 20 %) ; BOI-TVA-LIQ-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 19-20
- Règle : Le taux de droit commun de TVA est fixé à 20 %.
- Taux : `"20 %"`

### GFPL-075 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 271 (droit a deduction et remboursement du credit de TVA) ; BOI-TVA-DED-50-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 19-20
- Règle : Sur demande et sous réserve de certaines conditions, il est possible d’obtenir le remboursement du crédit de TVA correspondant à la TVA déductible non imputée.

### GFPL-076 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 302 septies A (regime simplifie d'imposition TVA) ; BOI-TVA-DECLA-20-20-30
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 19-20
- Règle : Le régime réel simplifié s’applique aux professionnels libéraux dont le CA annuel est compris entre 25 000 € et 254 000 € et dont la TVA exigible annuelle est inférieure à 15 000 €.
- Seuils : `{"CA_min": 25000, "CA_max": 254000, "TVA_exigible_max": 15000}`
- Précision (vérif. source officielle 2026-08-26) : Bornes hautes exactes (CA ≤ 254 000 € pour les prestations de services et TVA exigible N-1 < 15 000 €, CGI art. 302 septies A renvoyant au CIBS), mais la borne basse de 25 000 € correspond au seuil unique de franchise issu de la LF 2025, suspendu puis supprimé : la franchise en base applicable aux prestations de services reste 37 500 €, et le réel simplifié peut aussi s'appliquer sur option en dessous.

### GFPL-077 | obligation
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 302 septies A et art. 287, 3 (declaration annuelle 3517-S au RSI TVA) ; BOI-TVA-DECLA-20-20-30
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 19-20
- Règle : En régime réel simplifié, la déclaration annuelle est déposée via le formulaire 3517-S-SD.

### GFPL-078 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 287, 3 (acomptes semestriels de TVA au regime simplifie) ; BOI-TVA-DECLA-20-20-30
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 19-20
- Règle : En régime réel simplifié, la TVA est payée par deux acomptes semestriels en juillet et décembre.

### GFPL-079 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 302 septies A (regime reel normal au-dela des seuils RSI) ; BOI-TVA-DECLA-20-20-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 19-20
- Règle : Le régime réel normal s’applique si le CA annuel dépasse 254 000 € ou si la TVA exigible annuelle est supérieure à 15 000 €.
- Seuils : `{"CA": 254000, "TVA_exigible": 15000}`

### GFPL-080 | obligation
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 287, 2 (declaration mensuelle CA3 au reel normal) ; BOI-TVA-DECLA-20-20-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : Les professionnels au régime réel normal doivent déclarer chaque mois la TVA devenue exigible au cours du mois précédent ; le paiement est effectué en ligne.
- Précision (vérif. source officielle 2026-08-26) : Principe exact (CGI art. 287, 2 : dépôt mensuel de la CA3 au réel normal, télédéclaration et télépaiement), mais tolérance omise : dépôt par trimestre civil admis lorsque la taxe exigible annuellement est inférieure à 4 000 €.

### GFPL-081 | exception
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 287, 2 (declaration trimestrielle si TVA annuelle < 4 000 EUR) ; BOI-TVA-DECLA-20-20-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : Si le montant de TVA exigible annuellement est inférieur à 4 000 €, les déclarations peuvent être déposées par trimestre civil.
- Seuils : `{"TVA_exigible_annuelle": 4000}`

### GFPL-082 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 duodecies (regime des plus-values professionnelles) ; BOI-BIC-PVMV
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : Sauf exceptions, le régime de droit commun des plus-values professionnelles s’applique aux cessions d’éléments de l’actif immobilisé réalisées par les exploitants individuels et les sociétés relevant de l’IR, quelle que soit l’activité exercée.

### GFPL-083 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 38, 2 et art. 39 duodecies (constatation d'une plus-value : prix > VNC)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : Le cédant constate une plus-value lorsque le prix de cession est supérieur à la valeur nette comptable ou à la valeur d’origine.

### GFPL-084 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 38 sexies (valeur nette comptable = valeur d'acquisition - amortissements) ; BOI-BIC-PVMV-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : La valeur nette comptable correspond à la valeur d’acquisition diminuée du montant des amortissements déjà constatés.
- Ancre précisée (2026-08-26) : CGI art. 39 duodecies ; BOI-BIC-PVMV-20-10

### GFPL-085 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 151 nonies (cession de parts de societe de personnes a l'IR : PV professionnelle)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : La cession de titres d’une société soumise à l’IR relève des plus-values professionnelles.
- Précision (vérif. source officielle 2026-08-26) : CGI art. 151 nonies, I : les parts ne sont des actifs professionnels (PV professionnelle des art. 39 duodecies à 39 quindecies) que si l'associé « exerce son activité professionnelle » dans la société de personnes relevant des art. 8 et 8 ter ; pour l'associé non exerçant, la cession relève des PV des particuliers (art. 150-0 A) — condition manquante dans l'énoncé.

### GFPL-086 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150-0 A (PV de cession de valeurs mobilieres) et art. 200 A (PFU 12,8 %)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : La cession de titres d’une société soumise à l’IS relève des plus-values mobilières, taxées au PFU de 12,8 % ou au barème de l’IR.

### GFPL-087 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 duodecies, 2 (PV a court terme, bien amortissable < 2 ans)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : Pour un élément amortissable détenu moins de 2 ans, la plus-value est à court terme.

### GFPL-088 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 duodecies, 2 (qualification CT/LT bien amortissable > 2 ans)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : Pour un élément amortissable détenu plus de 2 ans, la plus-value est à court terme dans la limite de l’amortissement déduit puis à long terme au-delà.

### GFPL-089 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 duodecies (PV a long terme, bien non amortissable > 2 ans)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : Pour un élément non amortissable détenu plus de 2 ans, la plus-value est à long terme.

### GFPL-090 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 duodecies (constatation d'une moins-value : prix < VNC)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : Lorsque le prix de cession est inférieur à la valeur nette comptable ou à la valeur d’origine, le cédant constate une moins-value.

### GFPL-091 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 quaterdecies et art. 39 quindecies (compensation des PV/MV par nature)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : En général, les plus-values et moins-values de l’exercice se compensent entre elles selon leur nature, court terme ou long terme.

### GFPL-092 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 quaterdecies (PV nette a court terme imposee au taux de droit commun)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-21
- Règle : La plus-value à court terme, après imputation des moins-values à court terme, est intégrée aux revenus imposables dans les conditions et au taux de droit commun.

### GFPL-093 | option
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 quaterdecies, 1 (etalement de la PV nette a court terme sur 3 ans)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-21
- Règle : L’imposition de la plus-value à court terme peut être étalée à parts égales sur 3 ans.

### GFPL-094 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 quindecies (PV nette a long terme imposee a 12,8 % + 17,2 % PS)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-21
- Règle : La plus-value à long terme, après imputation des moins-values à long terme des 10 exercices précédents, est imposée à 12,8 % plus 17,2 % de prélèvements sociaux, soit 30 % au total.
- Taux : `"30 %"`

### GFPL-095 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 151 septies (exoneration PV pro selon recettes, activite >= 5 ans) ; BOI-BIC-PVMV-40-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-21
- Règle : L’exonération de l’article 151 septies CGI suppose une activité libérale exercée pendant 5 ans consécutivement et concerne les entreprises individuelles ou sociétés de personnes soumises à l’IR.
- Précision (vérif. source officielle 2026-08-26) : CGI art. 151 septies, I et II (corpus local) : exonération applicable aux activités « exercées à titre professionnel » (contribuables relevant de l'IR : EI et associés de sociétés de personnes) « à condition que l'activité ait été exercée pendant au moins cinq ans » — le texte n'exige pas 5 ans « consécutivement » : la doctrine admet le cumul des périodes d'exercice d'une même activité.

### GFPL-096 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 151 septies, II-1 (exoneration totale, recettes <= 90 000 EUR)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-21
- Règle : L’exonération est totale si les recettes de prestations de services n’excèdent pas 90 000 €.
- Seuils : `{"recettes": 90000}`

### GFPL-097 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 151 septies, II-1 (exoneration degressive entre 90 000 et 126 000 EUR)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-21
- Règle : L’exonération est partielle et dégressive si les recettes sont comprises entre 90 000 € et 126 000 €.
- Seuils : `{"recettes_min": 90000, "recettes_max": 126000}`

### GFPL-098 | effet
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 151 septies (exoneration applicable a l'IR et aux PS) ; BOI-BIC-PVMV-40-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-21
- Règle : L’exonération de l’article 151 septies s’applique à l’impôt sur le revenu et aux prélèvements sociaux.

### GFPL-099 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 151 septies A (exoneration PV pour depart a la retraite) ; BOI-BIC-PVMV-40-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-21
- Règle : L’exonération de l’article 151 septies A CGI suppose une activité exercée pendant 5 ans et que le cédant cesse toute fonction dans l’entreprise et fasse valoir ses droits à la retraite dans un délai de 24 mois avant ou après la cession.

### GFPL-100 | effet
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 151 septies A (exoneration IR maintenue, PS dus) ; BOI-BIC-PVMV-40-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-21
- Règle : L’exonération pour départ à la retraite s’applique à la totalité des plus-values à court et long terme, mais les prélèvements sociaux de 17,2 % restent dus.

### GFPL-101 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 238 quindecies (exoneration PV en fonction de la valeur de cession) ; BOI-BIC-PVMV-40-20-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-21
- Règle : L’exonération de l’article 238 quindecies CGI suppose une activité exercée pendant 5 ans et concerne les entreprises individuelles ou sociétés de personnes soumises à l’IR.
- Précision (vérif. source officielle 2026-08-26) : CGI art. 238 quindecies et BOI-BIC-PVMV-40-20-50 : la condition d'activité exercée pendant au moins 5 ans est exacte, mais le champ est plus large que l'énoncé — le dispositif bénéficie aussi aux sociétés soumises à l'IS répondant à la définition de PME (moins de 250 salariés, CA < 50 M€ ou bilan < 43 M€).

### GFPL-102 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 238 quindecies (exoneration totale, valeur <= 500 000 EUR)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-21
- Règle : L’exonération est totale si le prix de cession n’excède pas 500 000 €.
- Seuils : `{"prix_cession": 500000}`

### GFPL-103 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 238 quindecies (exoneration partielle entre 500 000 et 1 000 000 EUR)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 21-22
- Règle : L’exonération est partielle si le prix de cession est compris entre 500 000 € et 1 000 000 €.
- Seuils : `{"prix_cession_min": 500000, "prix_cession_max": 1000000}`

### GFPL-104 | effet
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 238 quindecies (exoneration applicable a l'IR et aux PS) ; BOI-BIC-PVMV-40-20-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-21
- Règle : L’exonération fondée sur le prix de cession s’applique à l’impôt sur le revenu et aux prélèvements sociaux.

### GFPL-105 | tranche
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 197, I-1 (bareme progressif de l'IR, tranche a 0 %) (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 22-23
- Règle : Jusqu’à 11 497 €, le taux marginal d’imposition est de 0 %.
- Seuils : `{"revenu_max": 11497}`
- Taux : `"0 %"`

### GFPL-106 | tranche
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 197, I-1 (bareme IR, tranche a 11 %) (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 22-23
- Règle : De 11 498 € à 29 315 €, le taux marginal d’imposition est de 11 %.
- Seuils : `{"revenu_min": 11498, "revenu_max": 29315}`
- Taux : `"11 %"`

### GFPL-107 | tranche
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 197, I-1 (bareme IR, tranche a 30 %) (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 22-23
- Règle : De 29 316 € à 83 823 €, le taux marginal d’imposition est de 30 %.
- Seuils : `{"revenu_min": 29316, "revenu_max": 83823}`
- Taux : `"30 %"`

### GFPL-108 | tranche
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 197, I-1 (bareme IR, tranche a 41 %) (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 22-23
- Règle : De 83 824 € à 180 294 €, le taux marginal d’imposition est de 41 %.
- Seuils : `{"revenu_min": 83824, "revenu_max": 180294}`
- Taux : `"41 %"`

### GFPL-109 | tranche
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 197, I-1 (bareme IR, tranche a 45 %) (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 22-23
- Règle : Au-delà de 180 295 €, le taux marginal d’imposition est de 45 %.
- Seuils : `{"revenu_min": 180295}`
- Taux : `"45 %"`

### GFPL-110 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 197, I-2 (plafonnement des effets du quotient familial) (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 22-23
- Règle : L’avantage fiscal attaché à chaque demi-part est plafonné à 1 791 €, soit 896 € par quart de part additionnelle.
- Seuils : `{"demi_part": 1791, "quart_part": 896}`

### GFPL-111 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 196 B (abattement pour rattachement d'un enfant majeur)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 22-23
- Règle : Le plafond de l’avantage lié au rattachement d’un enfant majeur est de 6 794 €.
- Seuils : `{"plafond": 6794}`
- Précision (vérif. source officielle 2026-08-26) : 6 794 € est le montant exact de l'abattement de l'art. 196 B pour l'imposition des revenus 2024 (BOI-IR-BASE-40), porte a 6 855 € pour les revenus 2025 ; en outre l'abattement ne vise que le rattachement d'enfants maries, pacses ou charges de famille (le rattachement d'un enfant majeur celibataire sans charge ouvre droit a une majoration de quotient familial, pas a l'abattement).

### GFPL-112 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 83, 3 (deduction forfaitaire de 10 % pour frais professionnels des salaries)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 22-23
- Règle : La déduction forfaitaire de 10 % pour frais professionnels des salariés est plafonnée à 14 426 € par déclarant avec un plancher de 504 €.
- Seuils : `{"plafond": 14426, "plancher": 504}`
- Taux : `"10 %"`
- Précision (vérif. source officielle 2026-08-26) : Valeurs exactes pour les revenus 2024 déclarés en 2025 (plafond 14 426 €, minimum 504 €) ; pour les revenus 2025 déclarés en 2026, le plafond est porté à 14 555 € et le minimum à 509 €.

### GFPL-113 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 158, 5-a (abattement de 10 % sur les pensions)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 22-23
- Règle : Le plafond de l’abattement de 10 % sur les pensions est de 4 399 € par foyer fiscal avec un plancher de 450 €.
- Seuils : `{"plafond": 4399, "plancher": 450}`
- Taux : `"10 %"`
- Précision (vérif. source officielle 2026-08-26) : Valeurs exactes pour les revenus 2024 déclarés en 2025 (plafond 4 399 € par foyer, minimum 450 €) ; pour les revenus 2025 déclarés en 2026, le plafond est porté à 4 439 € et le minimum à 454 € (impots.gouv.fr, pensions de retraite).

### GFPL-114 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 171 (declaration automatique des revenus) ; loi n2019-1479 du 28/12/2019 art. 155
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 21-22
- Règle : Depuis l’imposition des revenus 2019, certains contribuables dont les revenus sont intégralement déclarés par des tiers peuvent remplir leur obligation déclarative de manière automatique sans adresser de déclaration.

### GFPL-115 | exception
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 171 (declaration requise pour option bareme/PFU ou credits d'impot) ; art. 200 A, 2
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 21-22
- Règle : Même en cas d’éligibilité à la déclaration automatique, une déclaration de revenus doit être déposée pour opter pour le barème progressif au lieu du PFU ou pour bénéficier de réductions et/ou crédits d’impôt.

### GFPL-116 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 204 A (prelevement a la source de l'IR) ; BOI-IR-PAS
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 22-23
- Règle : Le prélèvement à la source permet un paiement de l’impôt dès la perception du revenu.

### GFPL-117 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 204 A, 2 (retenue a la source et acomptes)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 22-23
- Règle : Deux modes de prélèvement coexistent selon le type de revenus : prélèvement direct par le collecteur pour certains revenus et acomptes prélevés par l’administration fiscale pour d’autres revenus.

### GFPL-118 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 204 C (acomptes sur les revenus des independants/BNC)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 23-24
- Règle : Les revenus des travailleurs indépendants, y compris les BNC, donnent lieu à des acomptes prélevés sur le compte bancaire du contribuable chaque mois ou chaque trimestre.

### GFPL-119 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 204 D (revenus hors champ du PAS)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 23-24
- Règle : Les revenus de capitaux mobiliers, les plus-values mobilières et immobilières, ainsi que les gains de stock-options et d’attribution gratuite d’actions sont hors du champ du PAS.

### GFPL-120 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 204 J (modulation du prelevement en cas de changement de situation)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 23-24
- Règle : Le contribuable peut demander une modification de son taux en cas de changement de situation familiale ou de variation de ses revenus.

### GFPL-121 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 204 J, III (modulation a la baisse, ecart minimum) ; BOI-IR-PAS-20-30-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 23-24
- Règle : En cas de baisse des revenus, la modulation n’est possible que s’il existe une différence d’au moins 5 % entre le prélèvement avant et après modulation.
- Seuils : `{"ecart_min": 5}`

### GFPL-122 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 204 I (changement de situation familiale, delai de 60 jours)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 23-24
- Règle : Le changement de situation familiale doit être signalé dans un délai de 60 jours à compter de la survenance de l’événement.
- Seuils : `{"delai_jours": 60}`

### GFPL-123 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 204 E et art. 204 M (individualisation du taux du PAS)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 22-23
- Règle : Dès septembre 2025, pour les couples à déclaration commune, le taux de PAS sera individualisé par principe pour les revenus personnels de chaque conjoint ou partenaire ; sur option, le couple pourra demander le taux du foyer fiscal.

### GFPL-124 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 204 H, III (credits et reductions hors calcul du taux de PAS)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 23-24
- Règle : Le prélèvement à la source ne remet pas en cause les crédits et réductions d’impôt ; ils continuent d’être pris en compte dans le calcul de l’IR mais pas dans le calcul du taux de PAS.
- Ancre précisée (2026-08-26) : CGI art. 204 H, I (calcul du taux de droit commun)

### GFPL-125 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 200 (reduction d'impot pour dons, taux 75 %/66 %)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 4-4
- Règle : Les dons aux organismes d’aide aux personnes en difficulté et d’aide aux victimes de violences domestiques ouvrent droit à une réduction d’impôt de 75 % dans la limite de 1 000 € par an ; au-delà, le taux est de 66 % dans la limite globale de 20 % du revenu imposable.
- Seuils : `{"limite_75": 1000, "limite_globale_revenu_imposable": 20}`
- Taux : `"75 % puis 66 %"`
- Précision (vérif. source officielle 2026-08-26) : CGI art. 200, 1 ter : taux de 75 % pour les dons aux organismes d'aide aux personnes en difficulté et aux victimes de violence domestique, au-delà 66 % dans la limite de 20 % du revenu imposable — exact ; mais le plafond de 1 000 € (millésime 2025) a été porté à 2 000 € par la LF 2026 (promulguée le 19/02/2026) pour les dons effectués à compter du 14/10/2025.

### GFPL-126 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 200, 1 (dons Fondation du patrimoine) ; LF 2025 art. 16 (taux temporaire 75 %)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 4-4
- Règle : Les dons affectés à la collecte nationale pour le patrimoine religieux des petites communes (Fondation du patrimoine ; communes < 10 000 habitants, < 20 000 outre-mer) versés du 15 septembre 2023 au 31 décembre 2025 ouvrent droit à une réduction d'impôt de 75 % dans la limite de 1 000 € par an (LF 2024, art. 30) ; la LF 2025 (art. 16) a étendu le taux de 75 % aux dons aux fondations RUP œuvrant à la sauvegarde du patrimoine à compter du 15 février 2025. Au-delà du plafond, et hors dispositifs temporaires, régime de droit commun : 66 % dans la limite de 20 % du revenu imposable (CGI art. 200, 1).
- Vérification (2026-08-26) : énoncé antérieur ERRONÉ (il datait le 75 % du 15/02/2025 alors que la collecte patrimoine religieux en bénéficie depuis le 15/09/2023) — corrigé contre LF 2024 art. 30 et culture.gouv.fr.

### GFPL-127 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 199 terdecies-0 A (reduction d'impot souscription FCPI)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 4-7
- Règle : Le taux de la réduction d’impôt pour la souscription de parts de FCPI est augmenté à 25 % à compter d’une date fixée par décret.
- Taux : `"25 %"`
- Précision (vérif. source officielle 2026-08-26) : Énoncé exact au millésime 2025 (LF 2025, art. 12 et 14 : taux porté à 25 % pour les FCPI, applicable aux versements effectués à compter d'une date fixée par décret) mais daté : le décret n°2025-973 du 01/10/2025 a fixé cette date — le taux de 25 % s'applique aux versements effectués à compter du 28/09/2025.

### GFPL-128 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 199 terdecies-0 A, VI ter (reduction FIP recentree Corse et outre-mer)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 4-7
- Règle : La réduction d’impôt pour la souscription de parts de FIP est recentrée sur la Corse et l’outre-mer ; les investissements en métropole n’ouvrent plus droit à l’avantage fiscal.
- Ancre précisée (2026-08-26) : CGI art. 199 terdecies-0 A, VI ter (FIP Corse) et VI ter A (FIP outre-mer)

### GFPL-129 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 200 quater B (credit d'impot frais de garde des jeunes enfants)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 25-26
- Règle : Le crédit d’impôt pour la garde des jeunes enfants hors du domicile est égal à 50 % des dépenses retenues dans la limite de 3 500 € par an et par enfant, soit 1 750 € maximum.
- Seuils : `{"depenses": 3500, "credit_max": 1750}`
- Taux : `"50 %"`

### GFPL-130 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 199 decies H (DEFI foret, investissement forestier)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 25-26
- Règle : Le crédit d’impôt DEFI forêt-acquisition est de 25 % du prix d’acquisition des parts, retenu dans la limite de 6 250 € pour une personne seule ou 12 500 € pour un couple.
- Seuils : `{"personne_seule": 6250, "couple": 12500}`
- Taux : `"25 %"`
- Ancre précisée (2026-08-26) : CGI art. 200 quindecies ; BOI-IR-RICI-60-20-20

### GFPL-131 | effet
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 199 decies H (DEFI foret, plafond du credit selon situation familiale)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 25-26
- Règle : Le crédit d’impôt maximal DEFI forêt est de 1 563 € à 3 125 € selon la situation familiale.
- Seuils : `{"credit_min": 1563, "credit_max": 3125}`
- Ancre précisée (2026-08-26) : CGI art. 200 quindecies ; BOI-IR-RICI-60

### GFPL-132 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 199 terdecies-0 A (reduction IR-PME souscription au capital)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 26-27
- Règle : Pour les investissements réalisés à compter du 1er janvier 2025, la réduction d’impôt pour souscription au capital de PME dépend des caractéristiques de la PME.

### GFPL-133 | taux
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 199 terdecies-0 A (taux 18 % souscription PME)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 26-27
- Règle : Pour les autres PME, le taux de réduction est de 18 % avec une réduction maximale de 9 000 € ou 18 000 € selon la situation familiale.
- Seuils : `{"max_celibataire": 9000, "max_couple": 18000}`
- Taux : `"18 %"`

### GFPL-134 | taux
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 199 terdecies-0 AB (taux 25 % entreprises solidaires/foncieres solidaires)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 26-27
- Règle : Pour les sociétés foncières solidaires, le taux de réduction est de 25 % avec une réduction maximale de 12 500 € ou 25 000 € selon la situation familiale.
- Seuils : `{"max_celibataire": 12500, "max_couple": 25000}`
- Taux : `"25 %"`

### GFPL-135 | taux
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 199 terdecies-0 AB (ESUS logement social, taux 25 %)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 26-27
- Règle : Pour les foncières solidaires agréées ESUS (dont logement social), la réduction d'impôt est de 25 % des versements retenus dans la limite annuelle de 50 000 € (personne seule) ou 100 000 € (imposition commune), soit une réduction maximale de 12 500 € ou 25 000 € (CGI art. 199 terdecies-0 AB).
- Seuils : `{"plafond_versements_celibataire": 50000, "plafond_versements_couple": 100000, "reduction_max_celibataire": 12500, "reduction_max_couple": 25000}`
- Vérification (2026-08-26) : énoncé antérieur ERRONÉ (réduction max 9 000/18 000 €) — corrigé contre le texte de l'art. 199 terdecies-0 AB.
- Taux : `"25 %"`

### GFPL-136 | taux
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 199 terdecies-0 A bis (souscription JEI, taux 30 %)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 26-27
- Règle : Pour les JEI, le taux de réduction est de 30 % avec une réduction maximale de 22 500 € ou 45 000 € selon la situation familiale.
- Seuils : `{"max_celibataire": 22500, "max_couple": 45000}`
- Taux : `"30 %"`

### GFPL-137 | taux
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 199 terdecies-0 A bis (JEI a forte intensite de R&D, taux 50 %)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 26-27
- Règle : Pour les JEI réalisant des dépenses de recherche et développement représentant au moins 30 % de leurs charges, le taux de réduction est de 50 % avec une réduction maximale de 25 000 € ou 50 000 € selon la situation familiale.
- Seuils : `{"max_celibataire": 25000, "max_couple": 50000}`
- Taux : `"50 %"`
- Ancre précisée (2026-08-26) : CGI art. 199 terdecies-0 A ter (JEIR, taux 50 %)

### GFPL-138 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 44 sexies-0 A (definition de la jeune entreprise innovante)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 26-27
- Règle : Pour être qualifiée de JEI, la PME doit avoir été créée depuis moins de 8 ans, exercer une activité nouvelle, réaliser des dépenses de R&D représentant au moins 20 % de ses charges et avoir un capital détenu pour 50 % minimum par une personne physique, une autre JEI ou un établissement public de recherche et d’enseignement, etc.

### GFPL-139 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 200-0 A (plafonnement global des avantages fiscaux, 10 000 EUR)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 28-29
- Règle : Depuis 2009, le total de certains avantages fiscaux ne peut pas procurer une diminution d’impôt supérieure à 10 000 € par an et par foyer fiscal.
- Seuils : `{"plafond_general": 10000}`
- Précision (vérif. source officielle 2026-08-26) : CGI art. 200-0 A, 1 confirme le plafond de 10 000 € (18 000 € pour certains avantages outre-mer/Sofica), mais « depuis 2009 » est inexact : le plafonnement global institué par la LF 2009 s'appliquait initialement à 25 000 € + 10 % du revenu, puis a été abaissé par étapes ; le montant de 10 000 € ne s'applique que depuis l'imposition des revenus de 2013.

### GFPL-140 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 200-0 A, 1 (supplement de plafond de 8 000 EUR : Outre-mer, SOFICA)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 28-29
- Règle : Certains dispositifs bénéficient d’un supplément de plafond de 8 000 € par an et par foyer fiscal.
- Conditions : Outre-Mer | SOFICA
- Seuils : `{"supplement": 8000}`

### GFPL-141 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 200-0 A (avantages exclus du plafonnement global)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 28-29
- Règle : Les avantages fiscaux liés à la situation personnelle du contribuable ou à un objectif d’intérêt général sans contrepartie, ainsi que Malraux, Monuments historiques et la souscription au capital de JEI ou JEIR, ne sont pas soumis au plafonnement global des niches fiscales.

### GFPL-142 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 223 sexies (contribution exceptionnelle sur les hauts revenus, seuils)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 29-30
- Règle : La CEHR est due lorsque le revenu fiscal de référence excède 250 000 € pour un célibataire, veuf, séparé ou divorcé, ou 500 000 € pour des contribuables soumis à imposition commune.
- Seuils : `{"RFR_celibataire": 250000, "RFR_couple": 500000}`

### GFPL-143 | tranche
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 223 sexies (taux CEHR celibataire 3 %/4 %)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 29-30
- Règle : Pour un contribuable célibataire, veuf, séparé ou divorcé, le taux de CEHR est de 3 % de 250 001 € à 500 000 € et de 4 % au-delà de 500 000 €.

### GFPL-144 | tranche
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 223 sexies (taux CEHR couple 3 %/4 %)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 29-30
- Règle : Pour des contribuables mariés ou pacsés soumis à imposition commune, le taux de CEHR est de 3 % de 500 001 € à 1 000 000 € et de 4 % au-delà de 1 000 000 €.

### GFPL-145 | définition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 1417, IV (revenu fiscal de reference) ; art. 223 sexies
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 29-30
- Règle : Le revenu fiscal de référence utilisé pour la CEHR inclut le revenu net imposable, des revenus et plus-values imposés à taux forfaitaire, certains revenus soumis au prélèvement libératoire et certains revenus exonérés.

### GFPL-146 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi n2025-127 du 14/02/2025 (LF 2025) art. 10 (contribution differentielle sur les hauts revenus, CDHR, revenus 2025)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 29-30
- Règle : La CDHR s’applique temporairement, uniquement au titre des revenus de l’année 2025.
- Précision (vérif. source officielle 2026-08-26) : Exact au regard de la LF 2025 (art. 10 : CDHR au titre des seuls revenus 2025), mais énoncé daté : la loi de finances pour 2026 a prorogé la CDHR au-delà des revenus 2025 (imposition des revenus 2026).

### GFPL-147 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi n2025-127 du 14/02/2025 (LF 2025) art. 10 (CDHR, seuils de RFR 250 000/500 000 EUR)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 29-30
- Règle : La CDHR concerne les contribuables dont le revenu fiscal de référence excède 250 000 € pour un célibataire, veuf, séparé ou divorcé, ou 500 000 € pour une imposition commune.
- Seuils : `{"RFR_celibataire": 250000, "RFR_couple": 500000}`

### GFPL-148 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi n2025-127 du 14/02/2025 (LF 2025) art. 10 (CDHR, imposition minimale de 20 %)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-30
- Règle : La CDHR vise à assurer une imposition minimale de 20 % à l’impôt sur le revenu pour les contribuables ayant des revenus élevés.
- Taux : `"20 %"`

### GFPL-149 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi n2025-127 du 14/02/2025 (LF 2025) art. 10 (la CDHR s'ajoute a l'IR et a la CEHR)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-30
- Règle : La CDHR s’ajoute à l’impôt sur le revenu ainsi qu’à la CEHR.

### GFPL-150 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi n2025-127 du 14/02/2025 (LF 2025) art. 10 (mode de calcul de la CDHR)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-30
- Règle : La CDHR s’applique si l’imposition réelle du contribuable (IR + CEHR) est inférieure à 20 % de son revenu fiscal de référence retraité ; son montant correspond à 20 % du RFR retraité diminué de l’imposition réelle.

### GFPL-151 | condition
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi n2025-127 du 14/02/2025 (LF 2025) art. 10 (CDHR, domiciliation fiscale en France)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-30
- Règle : Seuls les contribuables domiciliés fiscalement en France sont concernés par la CDHR.

### GFPL-152 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi n2025-127 du 14/02/2025 (LF 2025) art. 10 (CDHR, mecanisme de decote)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-32
- Règle : Un mécanisme de décote est prévu lorsque le revenu fiscal de référence ajusté est inférieur ou égal à 330 000 € pour les célibataires, veufs, divorcés, et 660 000 € pour les contribuables soumis à imposition commune.
- Seuils : `{"celibataire": 330000, "couple": 660000}`

### GFPL-153 | obligation
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi n2025-127 du 14/02/2025 (LF 2025) art. 10 (CDHR, acompte de 95 %)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-32
- Règle : Le contribuable doit verser un acompte de CDHR entre le 1er décembre et le 15 décembre 2025, égal à 95 % du montant estimé de la contribution due jusqu’au 31 décembre 2025.
- Seuils : `{"acompte": 95}`

### GFPL-154 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Loi n2025-127 du 14/02/2025 (LF 2025) art. 10 (CDHR, penalite) ; CGI art. 1731
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-32
- Règle : Une pénalité de 20 % peut s’appliquer en cas de défaut ou retard de paiement de l’acompte, ou lorsque le montant versé est inférieur de 20 % à 95 % du montant de CDHR due.
- Taux : `"20 %"`

### GFPL-155 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CSS art. L.136-8 (CSG/CRDS sur revenus du patrimoine) ; CGI art. 1600-0 S (prelevement de solidarite)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-32
- Règle : Pour les revenus du patrimoine et les produits de placement, la CSG est de 9,2 %, la CRDS de 0,5 % et le prélèvement de solidarité de 7,5 %, soit un taux global de 17,2 %.
- Taux : `"17,2 %"`
- Précision (vérif. source officielle 2026-08-26) : Taux exacts millésime 2025 : CSG 9,2 % + CRDS 0,5 % + prélèvement de solidarité 7,5 % = 17,2 % (service-public.gouv.fr F2329) ; mais la LFSS pour 2026 porte la CSG sur les revenus du capital à 10,6 %, soit un taux global de 18,6 % applicable à compter de 2026 (placements dès le 01/01/2026).

### GFPL-156 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CSS art. L.136-8 (taux de CSG revenus d'activite et de remplacement)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-32
- Règle : Concernant les revenus d’activité et de remplacement, la CSG est de 9,2 % ; pour les pensions de retraite ou d’invalidité, elle est de 8,3 % avec des taux réduits possibles de 6,6 % ou 3,8 % selon le RFR.
- Précision (vérif. source officielle 2026-08-26) : CSS art. L.136-8 : le taux de 9,2 % ne concerne que les revenus d'activite ; les revenus de remplacement autres que les pensions (allocations chomage, IJSS) sont a 6,2 %, les pensions de retraite et d'invalidite a 8,3 % avec taux reduits de 6,6 % ou 3,8 % (voire exoneration) selon le RFR - la premiere partie de l'enonce assimile a tort les revenus de remplacement au taux de 9,2 %.

### GFPL-157 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : Ordonnance n96-50 du 24/01/1996 art. 19 (CRDS 0,5 %)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-32
- Règle : La CRDS sur les revenus d’activité et de remplacement est de 0,5 %.
- Taux : `"0,5 %"`

### GFPL-158 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CSS art. L.14-10-4 (CASA 0,3 % sur pensions)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-32
- Règle : La CASA est prélevée au taux de 0,3 % sur les pensions de retraite et d’invalidité.
- Taux : `"0,3 %"`
- Ancre précisée (2026-08-26) : CSS art. L.137-40 et L.137-41 (CASA)

### GFPL-159 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CSS art. L.131-2 (cotisation maladie 1 % sur pensions de retraite/invalidite)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-32
- Règle : La cotisation d’assurance maladie est prélevée au taux de 1 % sur les pensions de retraite et d’invalidité.
- Taux : `"1 %"`
- Précision (vérif. source officielle 2026-08-26) : La cotisation maladie de 1 % ne frappe pas toutes les pensions : elle s'applique, pour les pensionnes assujettis a la CSG au taux plein, aux seules pensions servies par un regime autre que le regime de base et ayant beneficie d'un financement de l'employeur (retraites complementaires type Agirc-Arrco) — urssaf.fr, revenus de remplacement ; les pensions de base des residents n'y sont pas soumises.

### GFPL-160 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : LPF art. L.10 et L.55 (controle et rectification des declarations)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 30-32
- Règle : Les déclarations de revenus peuvent être contrôlées et modifiées par l’administration fiscale dans le cadre d’un contrôle des déclarations.

### GFPL-161 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : LPF art. L.62 (droit a l'erreur / declaration rectificative) ; loi n2018-727 du 10/08/2018
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 32-34
- Règle : Le contribuable peut demander à rectifier sa déclaration s’il aperçoit une erreur ou s’il a oublié de déclarer un élément.

### GFPL-162 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : LPF art. L.169 (delai de reprise de droit commun : 3 ans)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 32-34
- Règle : Le délai de reprise / prescription expire le 31 décembre de la 3e année qui suit l’année pour laquelle l’imposition est due en principe.

### GFPL-163 | exception
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : LPF art. L.169 (delai de reprise porte a 10 ans : activites occultes, fraude)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 32-34
- Règle : Le délai de reprise / prescription est porté à 10 ans dans certains cas, notamment dissimulations volontaires, fraudes fiscales ou fausse domiciliation à l’étranger.
- Précision (vérif. source officielle 2026-08-26) : LPF art. L.169 : le délai de reprise est bien porté à la fin de la dixième année en cas d'activité occulte (ou illicite), de manquement aux obligations déclaratives sur les avoirs détenus à l'étranger et de fausse domiciliation fiscale à l'étranger ; en revanche la « fraude fiscale » en général n'emporte pas à elle seule le délai décennal — l'énumération de la règle est trop large sur ce point.

### GFPL-164 | effet
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : LPF art. L.169 (prescription : imposition definitive a l'expiration du delai)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 32-34
- Règle : Au-delà du délai de reprise, la déclaration et l’imposition sont définitives.

### GFPL-165 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CSS art. D.242-17 (revalorisation annuelle du PASS) ; arrete du 19/12/2024 (PASS 2025) ; voir referentiel cle PASS
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 4-4
- Règle : Le PASS 2025 est fixé à 47 100 € et le PASS 2026 à 48 060 € (arrêté du 22/12/2025) ; il sert notamment à la limite de déduction des versements sur les placements d’épargne retraite.
- Seuils : `{"PASS_2025": 47100, "PASS_2026": 48060}` [referentiel: PASS]

### GFPL-166 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 163 quatervicies (deductibilite des versements PER) ; C. mon. fin. art. L.224-2
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 49-50
- Règle : Les versements volontaires sur un PER sont déductibles du revenu global pour tous ou du revenu catégoriel pour les seuls TNS ; il est possible de renoncer à la déduction au moment du versement.

### GFPL-167 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 163 quatervicies, I-2 (plafond annuel de deduction PER)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 45-45
- Règle : La déduction des versements volontaires sur un PER est plafonnée annuellement.

### GFPL-168 | pratique
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 163 quatervicies, I-2 (report du plafond de deduction sur 3 ans)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 45-45
- Règle : Si le professionnel libéral n’a pas utilisé le plafond de déduction du revenu global de l’année 2022, il doit choisir en priorité cette déduction car elle n’est utilisable que pendant 3 ans.

### GFPL-169 | pratique
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 154 bis (deduction des cotisations PER du benefice professionnel TNS)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 45-45
- Règle : S’il a déjà consommé les plafonds de déduction du revenu global de l’année 2022, il doit choisir en priorité le plafond de déduction du revenu professionnel pour stocker les plafonds de revenu global, disposer d’un plafond supplémentaire de 15 % du bénéfice imposable compris entre 1 et 8 PASS et réduire son RFR.

### GFPL-170 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 154 bis (deduction des cotisations PER du BNC au reel) ; BOI-BNC-BASE-40-60
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 45-45
- Règle : Les cotisations PER des indépendants sont déductibles de leur BNC au titre des charges de l’année de leur paiement et doivent être indiquées dans la déclaration n° 2035 au réel BNC.

### GFPL-171 | micro-BNC
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 163 quatervicies (micro-BNC : deduction PER du revenu global uniquement)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 45-45
- Règle : Au régime micro-BNC, l’indépendant ne peut pas déduire les cotisations PER de son revenu catégoriel ; il peut uniquement les déduire de son revenu global.

### GFPL-172 | option
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : CGI art. 163 quatervicies, I-1 (renonciation irrevocable a la deduction) ; C. mon. fin. art. L.224-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 45-45
- Règle : Le souscripteur peut choisir de ne pas déduire de son revenu le versement volontaire sur le PER ; ce choix est irrévocable et doit être exprimé au moment du versement.

### GFPL-173 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : C. mon. fin. art. L.224-40 (transfert de produits d'epargne retraite, pas de nouvelle deduction)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 45-45
- Règle : Le transfert de produits d’épargne retraite sur un nouveau PER individuel n’ouvre pas droit à une nouvelle déduction fiscale.

### GFPL-174 | règle
- Module : M2
- Statut : `candidate_to_validate`
- Ancre : C. mon. fin. art. L.224-28 (interdiction du PER pour les mineurs depuis le 01/01/2024, LF 2024)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 45-45
- Règle : Depuis le 1er janvier 2024, il est interdit pour les enfants mineurs d’ouvrir un PER individuel ou d’effectuer des versements volontaires sur un PER ouvert avant cette date.

## gestion_financiere

### ES-001 | définition
- Module : M11
- Statut : `candidate_to_validate`
- Ancre : C. trav. art. L.3311-1 et L.3314-1 et s. (interessement) ; CSS art. L.137-15 (forfait social)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 48-49
- Règle : L'intéressement est un dispositif facultatif liant les salariés aux résultats ou performances de leur entreprise. Accord obligatoire (3 ans, renouvelable). Bénéficiaires: tous les salariés (avec éventuelle ancienneté ≤ 3 mois). Plafond individuel: 20 % du total des salaires bruts annuels du bénéficiaire (dans la limite de 75 % du PASS soit 35 325 € en 2025). Fiscalité: exonéré d'impôt sur le revenu si placé sur un plan d'épargne (PEE, PER) dans les 15 jours; soumis à l'IR si versé en espèces. Dans tous les cas: exonération de cotisations sociales (sauf CSG/CRDS).
- Seuils : `{"plafond_pct_salaires": 20, "plafond_pct_PASS": 75, "plafond_euros_2025": 35325}`
- Exceptions : Soumis à CSG/CRDS quelle que soit l'utilisation

### ES-002 | définition
- Module : M11
- Statut : `candidate_to_validate`
- Ancre : C. trav. art. L.3322-1 et s. (participation, seuil 50 salaries) et art. L.3324-1 (formule legale RSP)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 53-54
- Règle : La participation est un dispositif légal OBLIGATOIRE pour les entreprises de 50 salariés et plus (effectif dépassé pendant 12 mois consécutifs ou non sur 3 ans). Formule légale: RSP = (1/2) × (Bénéfice net fiscal − 5 % des capitaux propres) × (Salaires / Valeur ajoutée). Les sommes sont BLOQUÉES 5 ans (sauf cas de déblocage anticipé). Fiscalité: exonéré d'IR si maintenu bloqué; soumis à l'IR si déblocage. Cotisations sociales: exonéré (sauf CSG/CRDS).
- Conditions : entreprise ≥ 50 salariés
- Seuils : `{"seuil_salaries": 50, "blocage_ans": 5, "formule_taux_capitaux_propres_pct": 5}`
- Exceptions : Cas de déblocage anticipé: mariage, PACS, naissance 3ème enfant, divorce, invalidité, décès, cessation contrat, création d'entreprise, acquisition RP

### ES-003 | définition
- Module : M11
- Statut : `candidate_to_validate`
- Ancre : C. trav. art. L.3332-1 et s. (plan d'epargne entreprise, PEE) ; CGI art. 81, 18 (exoneration)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 45-46
- Règle : Le PEE est un système collectif d'épargne à moyen terme permettant aux salariés de se constituer un portefeuille de valeurs mobilières avec l'aide de l'entreprise. Alimentation: versements volontaires du salarié (plafond: 25 % de la rémunération annuelle brute), intéressement, participation, abondement employeur. Abondement employeur: exonéré d'IR et de cotisations sociales (hors CSG/CRDS) dans la limite de 3 fois le versement salarié et 8 % du PASS (3 768 € en 2025). Indisponibilité: 5 ans (sauf déblocage anticipé). Fiscalité à la sortie: exonération IR sur les gains; PS 17,2 % dus.
- Seuils : `{"versement_max_pct_salaire": 25, "abondement_max_pct_versement": 300, "abondement_max_pct_PASS": 8, "abondement_max_euros_2025": 3768, "indisponibilite_ans": 5}`
- Taux : `{"PS_sortie_pct": 17.2}`
- Exceptions : Cas de déblocage anticipé similaires à la participation | Abondement majoré possible pour les PEE investis en titres de l'entreprise

### ES-004 | définition
- Module : M11
- Statut : `candidate_to_validate`
- Ancre : C. mon. fin. art. L.224-13 a L.224-26 (PER collectif, PERCOL, loi PACTE 2019-486) ; C. trav. art. L.3334-1
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 58-58
- Règle : Le PERCO (ancien) est remplacé par le PER Collectif (PERCOL) depuis la loi PACTE 2019. Le PERCOL fonctionne comme le PEE mais avec une épargne bloquée jusqu'à la retraite (sauf déblocage anticipé dont l'achat de la résidence principale). Les sommes investies peuvent bénéficier de l'abondement employeur (mêmes plafonds que PEE majorés: jusqu'à 16 % du PASS soit 7 536 € en 2025). Fiscalité à la sortie en capital: exonération IR sur les capitaux épargne salariale, PS 17,2 % sur les gains. Les anciens PERCO peuvent toujours être alimentés et ont vocation à être transformés en PERCOL.
- Seuils : `{"abondement_max_pct_PASS": 16, "abondement_max_euros_2025": 7536}`
- Taux : `{"PS_sortie_pct": 17.2}`
- Exceptions : Déblocage anticipé pour achat RP possible (contrairement au PERCO classique) | PERCO existants: non souscription de nouveaux depuis oct 2020 mais alimentation possible

### ES-005 | règle
- Module : M11
- Statut : `candidate_to_validate`
- Ancre : C. mon. fin. art. L.224-40 (transferts vers le PER, non imposables)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 58-58
- Règle : Les droits accumulés sur un PERCO, un Article 83 ou un contrat Madelin peuvent être transférés vers un PER individuel. Le transfert n'est pas imposable. Les compartiments conservent leur nature fiscale d'origine (épargne salariale reste dans le 2ème compartiment du PER → sortie capital exonérée d'IR). L'ancien PEE peut être transféré vers un PERCOL mais pas directement vers un PER individuel. Intérêt du transfert: regroupement et simplification, accès au large choix de supports d'investissement du PER individuel.
- Exceptions : PEE → transfert vers PERCOL uniquement (pas vers PER individuel directement) | Délai de blocage du PEE redémarre à zéro en cas de transfert vers PERCOL

### ES-006 | règle
- Module : M11
- Statut : `candidate_to_validate`
- Ancre : C. trav. art. L.3315-2 (interessement affecte a un plan, exoneration IR) ; C. mon. fin. art. L.224-40 (transferts)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 46-48
- Règle : Stratégies d'optimisation: (1) Placer l'intéressement sur le PEE ou PERCOL dans les 15 jours → exonération IR immédiate; (2) Maximiser l'abondement employeur (chaque euro d'abondement est exonéré d'IR et de cotisations); (3) Utiliser le PEE comme épargne intermédiaire (5 ans) avant le PER (retraite); (4) Transférer les droits PERCO vers PER individuel pour profiter d'une gestion plus large; (5) En cas de déblocage anticipé (acquisition RP), le montant est exonéré d'IR mais soumis aux PS 17,2 % sur les gains.

### FORM-003 | formule
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 977 (bareme IFI), art. 977-II (decote) et art. 979 (plafonnement IFI)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 76-78
- Règle : IFI brut = Σ(Tranche × Taux): tranche 800 001-1 300 000 € × 0,5 %; tranche 1 300 001-2 570 000 € × 0,7 %; tranche 2 570 001-5 000 000 € × 1 %; tranche 5 000 001-10 000 000 € × 1,25 %; > 10 000 000 € × 1,5 %. Décote si patrimoine net P ∈ [1 300 000; 1 400 000[: IFI net = IFI brut − (17 500 − 1,25 % × P). Plafonnement: IFI net ≤ 75 % × Revenus N-1 − IR N-1.
- Conditions : patrimoine net IFI > 1 300 000 €
- Seuils : `{"seuil_IFI": 1300000, "seuil_decote_max": 1400000}`
- Taux : `{"tranche_1_pct": 0.5, "tranche_2_pct": 0.7, "tranche_3_pct": 1.0, "tranche_4_pct": 1.25, "tranche_5_pct": 1.5, "plafonnement_pct": 75}`

### FORM-004 | formule
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 777 (bareme DMTG ligne directe), art. 779 (abattement 100 000 EUR) et art. 790 G (don familial de sommes d'argent) (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030061736/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 81-83
- Règle : Droits de donation ligne directe = Σ(Tranche nette après abattements × Taux). Barème: jusqu'à 8 072 € → 5 %; de 8 073 à 12 109 € → 10 %; de 12 110 à 15 932 € → 15 %; de 15 933 à 552 324 € → 20 %; de 552 325 à 902 838 € → 30 %; de 902 839 à 1 805 677 € → 40 %; > 1 805 677 € → 45 %. Abattement parent→enfant: 100 000 €. Abattement numéraire supplémentaire: +31 865 € si conditions. Part nette = Montant transmis − Abattements applicables.
- Conditions : ligne directe: parents, enfants, petits-enfants, arrière-petits-enfants
- Seuils : `{"abattement_parent_enfant": 100000, "tranche_5": 8072, "tranche_10_max": 12109, "tranche_15_max": 15932, "tranche_20_max": 552324, "tranche_30_max": 902838, "tranche_40_max": 1805677}`
- Taux : `{"t1": 5, "t2": 10, "t3": 15, "t4": 20, "t5": 30, "t6": 40, "t7": 45}`

### FORM-005 | formule
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 669 (bareme de l'usufruit selon l'age) ; art. 777 (DMTG) (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006310173/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 84-85
- Règle : Valeur NP transmise = Valeur PP × (1 − Taux usufruit selon âge art. 669 CGI). Taux usufruit: < 21 ans: 90 %; 21-30 ans: 80 %; 31-40 ans: 70 %; 41-50 ans: 60 %; 51-60 ans: 50 %; 61-70 ans: 40 %; 71-80 ans: 30 %; 81-90 ans: 20 %; > 90 ans: 10 %. Droits de donation = f(Valeur NP − Abattement applicable). Au décès de l'usufruitier: le nu-propriétaire devient PP en franchise de droits (pas de revalorisation).
- Conditions : donation avec réserve d'usufruit | âge de l'usufruitier au jour de la donation
- Exceptions : Au décès de l'usufruitier: aucun nouveau droit à payer (extinction de l'usufruit sans taxation)

### FORM-006 | formule
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 156, I-3 (imputation du deficit foncier sur le revenu global, plafond et doublement renovation energetique) ; BOI-RFPI-BASE-30-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 65-66
- Règle : Déficit foncier imputable sur le revenu global = MIN(10 700 €, déficit hors intérêts d'emprunt). Si travaux rénovation énergétique E/F/G → A/B/C/D payés entre 2023 et 2025: plafond doublé à 21 400 €. Déficit sur intérêts d'emprunt = reportable sur revenus fonciers uniquement (10 ans). Déficit total année = Revenus locatifs nets bruts − Charges déductibles. Charges déductibles = intérêts emprunt + travaux entretien/réparation + taxe foncière + assurances + frais gestion + provisions copropriété.
- Conditions : régime réel foncier
- Seuils : `{"plafond_standard": 10700, "plafond_renovation_energetique": 21400, "report_interets_annees": 10}`
- Exceptions : La fraction au-delà de 10 700 € (ou 21 400 €) est reportable sur revenus fonciers des 10 ans suivants | La clause de location 3 ans obligatoire pour imputation sur revenu global

### RISK-003 | risque
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : LPF art. A.47 A-1 (FEC) ; CGI art. 1729 D (amende)
- source_ingest : _GUIDE DU LOUEUR EN MEUBLES FINAL.pdf, p. 21-22
- Règle : RISQUE: Utilisation d'un tableur Excel pour la comptabilité informatisée → non-conformité FEC. L'administration peut requalifier la comptabilité comme irrégulière, appliquer une taxation d'office et prononcer une amende de 5 000 € ou 10 % des droits rappelés. Le contribuable perd la protection d'une comptabilité régulière en cas de contrôle.
- Conditions : comptabilité informatisée
- Seuils : `{"amende_FEC": 5000}`

### RISK-005 | risque
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 968 (usufruit impose en valeur PP) et art. 964 (foyer fiscal IFI) ; LPF art. L.64 (abus de droit)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 16-16
- Règle : RISQUE: Donation temporaire d'usufruit à un enfant rattaché au foyer fiscal des parents pour réduire l'IFI → inopposable à l'administration fiscale. Le bien reste dans l'assiette IFI du donateur si les enfants sont rattachés au foyer fiscal (leurs biens/revenus sont agrégés dans le foyer fiscal des parents). Nécessite que les enfants soient DÉTACHÉS du foyer fiscal pour que la donation temporaire d'usufruit sorte le bien de l'assiette IFI.

### RISK-006 | risque
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150 VB, II (reintegration des amortissements LMNP a la PV, LDF 2025 art. 84) ; BOI-RFPI-PVI
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 69-70
- Règle : RISQUE: LMNP au réel depuis de nombreuses années — amortissements déduits depuis 2025 réintégrés dans la base PV à la cession. Un investisseur qui amorti significativement son bien et le revend après plusieurs années de déduction verra sa PV imposable augmenter du montant des amortissements déduits depuis 2025. Impact d'autant plus fort si le bien est vendu peu après la mise en location (pas de bénéfice des abattements de durée de détention).
- Exceptions : Résidences étudiantes/apprentissage: exception | Plus de 22 ans de détention: exonération IR (les amortissements réintégrés restent soumis aux PS)

### RISK-007 | risque
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 1729 G (majoration 10 % en cas d'insuffisance des acomptes PAS) ; art. 204 J (modulation a la baisse) ; BOI-IR-PAS
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 23-24
- Règle : RISQUE: Modulation du taux PAS à la baisse sans atteindre le seuil minimum de 5 % d'écart → modulation refusée. RISQUE: sous-estimation des revenus BNC en cours d'année → acompte trop faible → pénalité de retard de majoration de 10 % sur la différence. Signaler systématiquement le risque de majoration si le contribuable envisage de réduire ses acomptes alors que ses revenus restent élevés.
- Seuils : `{"ecart_minimum_modulation_pct": 5}`
- Taux : `{"penalite_sous_estimation_pct": 10}`

## gestion_patrimoine

### PAT-001 | définition
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. civ. art. 1400 a 1491 (communaute reduite aux acquets) ; art. 757 (droits du conjoint)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 6-7
- Règle : Communauté réduite aux acquêts (régime légal par défaut): biens propres = acquis avant mariage ou reçus par donation/succession; biens communs = acquis pendant le mariage. Chacun peut gérer seul les biens communs sauf actes importants (vente, hypothèque, donation). En cas de décès: conjoint reçoit 50% du commun + 1/4 en PP ou 100% en usufruit sur la succession (si enfants communs).
- Exceptions : Présence d'enfants non communs: conjoint reçoit seulement 1/4 en PP

### PAT-002 | définition
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. civ. art. 1536 a 1543 (separation de biens)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 7-8
- Règle : Séparation de biens: chaque époux gère seul ses biens personnels; pour les biens acquis en commun → indivision. Avantage: protection du patrimoine de chaque époux des dettes de l'autre (sauf dettes solidaires dont fiscales). Recommandé pour professions artisanales/commerciales/libérales ou présence d'enfants d'unions précédentes.

### PAT-003 | définition
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. civ. art. 1569 a 1581 (participation aux acquets)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 6-6
- Règle : Participation aux acquêts: fonctionne comme séparation de biens pendant le mariage; à la dissolution → fonctionne comme communauté (enrichissement de chacun partagé en valeur). Calcul: créance de participation = (patrimoine final - patrimoine originaire)/2. Seul l'enrichissement est partagé, pas les dettes.

### PAT-004 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. civ. art. 1397 (changement de regime) ; art. 1094-1 (donation entre epoux) ; CGI art. 990 I
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 8-8
- Règle : Outils de protection du conjoint par ordre d'efficacité: (1) Modification du régime matrimonial (communauté universelle avec clause d'attribution intégrale); (2) Donation entre époux (donation au dernier vivant): augmente les droits du survivant; options: 1/2, 1/3 ou 1/4 en PP selon nb d'enfants, ou totalité en usufruit, ou 1/4 PP + 3/4 usufruit; (3) Assurance-vie avec conjoint bénéficiaire: transmission hors succession, exonération totale de droits de succession.

### PAT-005 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. civ. art. 1515 (clause de preciput) ; art. 1094-1 (cantonnement)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 8-8
- Règle : Clause de préciput: permet au conjoint survivant de prélever un ou plusieurs biens de la communauté AVANT le partage de la succession, sans entamer ses droits successoraux. Cantonnement: le conjoint survivant peut limiter ses droits à une partie des biens qu'il doit recevoir → les biens non pris reviennent aux autres héritiers (sans droits de donation pour eux).
- Conditions : Dans un contrat de mariage ou donation entre époux

### PAT-006 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. civ. art. 734 a 740 (devolution legale) et art. 757 a 757-3 (conjoint)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 17-18
- Règle : Ordre de dévolution légale: (1) enfants/petits-enfants (excluent tous les autres); (2) si marié+enfants: conjoint reçoit 1/4 PP ou totalité usufruit (option); si marié sans enfants: conjoint hérite selon présence des parents; (3) si pas d'enfants ni conjoint: parents 50% chacun; frères et sœurs reçoivent la moitié si parents en vie, sinon la totalité. PACS: aucun droit successoral légal → testament obligatoire.
- Exceptions : Enfants non communs: conjoint reçoit seulement 1/4 en PP (pas de choix)

### PAT-007 | obligation
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 641 (declaration de succession) ; art. 746 (droit de partage) ; C. civ. art. 815 et s.
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 20-20
- Règle : Processus: (1) identification héritiers par le notaire; (2) évaluation du patrimoine (actif - passif); (3) dévolution successorale; (4) déclaration de succession à l'administration fiscale dans les 6 mois après le décès; (5) partage des biens (amiable ou judiciaire). Droit de partage: 2,5% de la valeur nette de l'actif partagé.
- Seuils : `{"delai_declaration_mois": 6}`
- Taux : `{"droit_partage_pct": 2.5}`

### PAT-008 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. civ. art. 967 a 1001 (testaments) ; art. 912 a 917 (reserve hereditaire)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 23-23
- Règle : Testament olographe: entièrement écrit à la main, daté, signé. Gratuit, simple, mais risque de nullité ou perte. Testament authentique: reçu par notaire en présence de 2 témoins ou 2ème notaire; coût ~120 € HT; conservé au fichier central. Réserve héréditaire = part minimale réservée aux enfants; quotité disponible = part dont on peut disposer librement.
- Seuils : `{"cout_testament_authentique_HT": 120}`
- Exceptions : Testament révocable à tout moment par le testateur

### PAT-009 | seuil
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 779 (abattement parent/enfant) et art. 790 G (don numeraire) ; art. 784 (delai 15 ans)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 26-26
- Règle : Abattements fiscaux sur donations (reconstitution tous les 15 ans): parents vers enfants: 100 000 € par parent et par enfant; grands-parents vers petits-enfants: 31 865 €; arrière-grands-parents vers arrière-petits-enfants: 5 310 €. Abattement supplémentaire don en numéraire: 31 865 € (donateur < 80 ans, donataire majeur). Don affecté à création d'entreprise ou construction résidence principale: exonération 100 000 €.
- Seuils : `{"abattement_parent_enfant": 100000, "abattement_grands_parents": 31865, "abattement_arriere_grands_parents": 5310, "abattement_don_numeraire": 31865, "exoneration_creation_entreprise": 100000, "delai_reconstitution_ans": 15}`
- Exceptions : Enfant handicapé: abattement supplémentaire de 159 325 € (soit 259 325 € total par parent)

### PAT-010 | définition
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. civ. art. 843 et s. (rapport) ; art. 1075 (donation-partage) ; CGI art. 669 (demembrement)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 24-24
- Règle : Formes de donation: (1) Donation en avancement de part: pour héritiers réservataires (enfants/petits-enfants), rapportable à la succession; (2) Donation hors part: pour toute personne, pas rapportable; (3) Donation-partage: donne ET partage de son vivant, non rapportable, évaluée au jour de la donation; (4) Démembrement de propriété: donateur garde l'usufruit, enfants reçoivent la nue-propriété → à son décès, usufruit s'éteint, enfants deviennent PP SANS droits de succession.

### PAT-011 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 757 (don manuel) ; C. civ. art. 852 (present d'usage)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 26-26
- Règle : Don manuel: transmission de biens mobiliers (argent, objets, titres) de la main à la main, sans formalisme. Déclaré par le donataire → droits de donation + abattements applicables. Présent d'usage (cadeau circonstanciel de valeur modique vs patrimoine du donateur): non soumis aux droits de donation, non rapportable à la succession.
- Exceptions : Présent d'usage: pas de droits, non rapportable

### PAT-012 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. civ. art. 805 (renonciation) ; art. 754 (representation) ; CGI art. 785
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 22-22
- Règle : Un enfant peut renoncer à sa part de succession pour que ses propres enfants (petits-enfants du défunt) héritent à sa place (saut de génération). Délai de renonciation: 4 mois après le décès. Les héritiers venant en représentation se partagent l'abattement fiscal et le tarif du renonçant. Formulaire Cerfa n°15828*05 au greffe du tribunal judiciaire.
- Seuils : `{"delai_renonciation_mois": 4}`
- Exceptions : Renonciation est un acte irrévocable et total (pas possible de renoncer partiellement)

### PAT-013 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 965 a 976 (assiette IFI) ; art. 976 (bois et forets) ; art. 978 (dons) ; art. 979 (plafonnement)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 40-40
- Règle : Stratégies de réduction d'IFI: (1) SIIC (sociétés foncières cotées): actifs immobiliers exclus de l'assiette IFI si détention < 5% du capital; (2) Nue-propriété: bien en démembrement → valeur de la pleine propriété n'est pas dans l'assiette IFI du nu-propriétaire jusqu'à l'extinction de l'usufruit; (3) Bois et forêts: exonération 75% si engagement d'exploitation 30 ans + certificat de gestion durable; (4) Dons à organismes d'intérêt général: réduction IFI de 75% dans la limite de 50 000 €/an; (5) Plafonnement IFI: IFI + IR ≤ 75% des revenus de N-1.
- Seuils : `{"exoneration_bois_forets_pct": 75, "don_reduction_IFI_pct": 75, "don_IFI_plafond": 50000}`
- Taux : `{"plafonnement_IFI_revenus_pct": 75}`
- Exceptions : SIIC: exclusion uniquement si détention < 5% du capital directement ou indirectement | SCPI et OPCI: inclus dans l'assiette IFI (contrairement aux SIIC)

### PAT-014 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 968 (usufruit impose en valeur PP) et art. 669 (bareme usufruit) ; LPF art. L.64 (abus de droit) (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006310173/) (verifie le 2026-06-05)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 41-42
- Règle : Donation temporaire d'usufruit: transfert temporaire (généralement 5-10 ans) de l'usufruit à un enfant majeur détaché du foyer fiscal. Effets: (A) le donateur ne déclare plus le bien à l'IFI pendant la période; (B) l'enfant perçoit les loyers. Risques: droits de mutation à titre gratuit lors de la donation; peut être remise en cause par l'administration si pas de réel besoin du bénéficiaire (abus de droit).
- Conditions : enfant majeur détaché du foyer fiscal du donateur | justification d'un réel besoin (obligation alimentaire)
- Exceptions : Si les enfants sont rattachés au foyer fiscal des parents: valeur PP doit être déclarée par les usufruitiers

### PAT-015 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Péremption : Pinel : fermé aux nouvelles acquisitions depuis le 01/01/2025 (seuls les investissements antérieurs continuent à produire leurs réductions). Censi-Bouvard : fermé aux nouvelles acquisitions depuis le 01/01/2023.
- Ancre : CGI art. 199 novovicies (Pinel/Denormandie), art. 199 sexvicies (Censi-Bouvard) et art. 199 tervicies (Malraux)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 66-66
- Règle : Dispositifs de défiscalisation immobilière locative: Pinel (logement neuf/assimilé, zones A/A bis/B1): taux 12%/18%/21% selon engagement 6/9/12 ans, plafond 300 000 € et 5 500 €/m², plafonds loyers et ressources locataires; Denormandie (logements anciens réhabilités, communes ciblées): mêmes modalités que Pinel, travaux ≥ 25% coût total; Censi-Bouvard (LMNP résidences services): 11% sur 9 ans, plafond 300 000 €/an; Malraux (restauration patrimoine historique): 22% ou 30% selon zone, plafond 400 000 €, engagement 9 ans.
- Seuils : `{"Pinel_plafond_prix": 300000, "Pinel_plafond_m2": 5500, "CensiBourvard_plafond": 300000, "Malraux_plafond": 400000}`
- Taux : `{"Pinel_6ans": 12, "Pinel_9ans": 18, "Pinel_12ans": 21, "CensiBouvard": 11, "Malraux_zone_1": 22, "Malraux_zone_2": 30}`
- Exceptions : Malraux hors plafonnement niches fiscales

### PAT-016 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 8 (SCI a l'IR) et art. 206, 2 (IS de plein droit si location meublee) ; C. civ. art. 1832 et s.
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 43-44
- Règle : Intérêts de la SCI: (1) facilite transmission via donation de parts (démembrement possible: parents gardent usufruit+loyers, enfants nue-propriété → PP sans droits de succession au décès); (2) protection des locaux professionnels de la faillite de l'entreprise; (3) responsabilité des associés: indéfinie mais divisible (chacun à hauteur de ses parts). SCI soumise à IS de plein droit si elle fait de la location meublée (activité commerciale → IS obligatoire). Option IS irrévocable: perd l'abattement durée détention PV immobilières.
- Seuils : `{"obligation_comptabilite_bilan": 1550000, "obligation_comptabilite_CA": 3100000, "obligation_comptabilite_salaries": 50}`
- Exceptions : SCI résidence principale: perd abattement IFI 30% et droit au logement du conjoint survivant

### PAT-017 | obligation
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. com. art. L.612-1 (seuils comptabilite) ; CGI art. 206 ; BOI-BIC-DECLA
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 48-48
- Règle : Comptabilité obligatoire pour SCI: assujettie à TVA; soumise à IS; construction-vente ou placement collectif; taille importante (≥ 2 des 3 seuils: 1 550 000 € bilan, 3 100 000 € CA, 50 salariés); statuts imposant cette formalité. Pour les autres SCI (IR): pas d'obligation légale mais comptabilité de trésorerie fortement recommandée. Une SCI sans vie sociale (pas d'AG annuelle, pas de comptes) risque d'être requalifiée en société fictive.
- Seuils : `{"bilan_seuil": 1550000, "CA_seuil": 3100000, "salaries_seuil": 50}`

### PAT-018 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 125-0 A (fiscalite de l'assurance-vie) ; CSS art. L.136-7 (PS)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 50-51
- Règle : Fiscalité des gains (intérêts + PV) à la sortie par rachat: versements avant 27/09/2017: PFL 35%/15%/7,5% selon durée (0-4/4-8/>8 ans) ou barème IR + PS; versements depuis 27/09/2017: PFU 12,8% + PS (encours < 150 000 €) ou 7,5% + PS si contrat > 8 ans et encours < 150 000 € (sinon 12,8%). Après 8 ans: abattement annuel 4 600 € (personne seule) ou 9 200 € (couple). PS: 17,2%.
- Seuils : `{"abattement_personne_seule": 4600, "abattement_couple": 9200, "seuil_taux_7_5": 150000}`
- Taux : `{"PFU_standard": 12.8, "PFU_plus8ans_moins150k": 7.5, "PS": 17.2}`
- Exceptions : Option pour le barème progressif IR possible lors de la déclaration de revenus

### PAT-019 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 990 I (assurance-vie hors succession) et art. 757 B (primes apres 70 ans) (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047288653/) (verifie le 2026-06-05)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 50-51
- Règle : Transmission hors succession: bénéficiaires librement désignés dans la clause. Fiscalité: conjoint/partenaire PACS bénéficiaire → EXONÉRATION TOTALE de droits. Autres bénéficiaires: abattement de 152 500 € par bénéficiaire sur primes versées avant 70 ans; taxe 20% de 152 501 € à 700 000 €; taxe 31,25% au-delà de 700 000 €. Primes versées après 70 ans: abattement global de 30 500 € (partagé entre tous les bénéficiaires) puis droits de succession sur l'excédent.
- Seuils : `{"abattement_avant_70ans": 152500, "seuil_taxe_20_pct": 700000, "abattement_apres_70ans": 30500}`
- Taux : `{"taxe_tranche_1": 20, "taxe_tranche_2": 31.25}`

### PAT-020 | définition
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. mon. fin. art. L.224-1 a L.224-8 (PER, loi PACTE 2019-486 du 22/05/2019)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 58-58
- Règle : Plan d'épargne retraite (PER, loi PACTE mai 2019): 3 compartiments: (1) versements volontaires (libres, déductibles ou non du revenu); (2) épargne salariale transférée (intéressement, participation, abondement, CET); (3) cotisations obligatoires (sortie uniquement en rente). Remplace: Perp, Madelin, Perco, art. 83 (impossibles à souscrire depuis oct 2020; transfert possible sur PER). Déblocage anticipé possible: décès conjoint, invalidité, achat résidence principale.

### PAT-021 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 163 quatervicies (deduction PER) ; art. 158, 5 (rentes) ; C. mon. fin. art. L.224-1
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 58-59
- Règle : Compartiment versements volontaires: OPTION A (déduction à l'entrée) → sortie en rente: IR régime rentes viagères à titre gratuit (abattement 10%) + PS; sortie en capital: partie capital au barème IR + PV au PFU 30%. OPTION B (pas de déduction) → sortie en rente: IR régime rentes à titre onéreux (fraction imposable selon âge: 70%/<50 ans, 50%/50-59 ans, 40%/60-69 ans, 30%/>69 ans) + PS; sortie en capital: PV uniquement au PFU. Compartiment épargne salariale: exonération IR sur le capital en sortie; PV soumises aux PS 17,2%.
- Taux : `{"PFU": 30, "PS": 17.2}`

### PAT-022 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. mon. fin. art. L.221-30 a L.221-32 (PEA) ; CGI art. 157, 5 bis
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 62-62
- Règle : PEA: 1 seul par personne physique majeure domiciliée en France. Plafond de versement: 150 000 € (hors gains). Valeurs éligibles: actions cotées européennes, parts de SARL, OPCVM/Sicav avec ≥75% actions européennes. Exclus: obligations, dérivés, SCI, titres démembrés. Retrait avant 5 ans: clôture automatique du PEA. Service de règlement différé: uniquement sur compte-titres ordinaire.
- Conditions : personne physique majeure | domicile fiscal France
- Seuils : `{"plafond_versement": 150000}`
- Exceptions : PEA-PME: plafond complémentaire de 225 000 € | PEA jeunes: pour 18-25 ans encore rattachés

### PAT-023 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150-0 A et 157, 5 bis (fiscalite PEA) ; CSS art. L.136-7
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 63-64
- Règle : PEA fiscalité: retrait avant 5 ans: PFU 12,8% sur les gains (ou barème IR sur option) + PS 17,2%. Retrait après 5 ans: gains exonérés d'IR + PS 17,2%. Sortie en rente viagère après 8 ans: exonération totale d'IR sur la rente; fraction déterminée selon âge soumise aux PS. Compte-titres ordinaire: dividendes et PV soumis au PFU 12,8% + PS 17,2% (ou barème IR option); dividendes avec option barème: abattement 40% sur les dividendes.
- Taux : `{"PFU": 12.8, "PS": 17.2, "abattement_dividendes_bareme": 40}`

### PAT-024 | définition
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. mon. fin. art. L.214-114 a L.214-118 (SCPI) ; CGI art. 965, 2 (parts de SCPI dans l'assiette IFI)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 56-57
- Règle : SCPI (sociétés civiles de placement immobilier): sociétés qui acquièrent et gèrent des biens immobiliers et redistribuent les loyers aux porteurs de parts. Revenus: loyers trimestriels + PV de cession + produits de trésorerie. Frais: commission de souscription (incluse dans le prix de la part à l'achat), commission de gestion (prélevée sur revenus), commission d'arbitrage (en cas de cession). Accessible à personnes physiques ou morales, résidents ou non.
- Exceptions : Parts de SCPI incluses dans l'assiette IFI (contrairement aux SIIC)

### PAT-025 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CSS art. L.353-1 et s. (pension de reversion regime general)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 14-15
- Règle : Pension de réversion des régimes obligatoires: réservée aux personnes ayant été MARIÉES avec l'assuré décédé (ni concubins ni pacsés). Montant: 54% de la pension de retraite du défunt (minimum et maximum). Partagée au prorata de la durée du mariage si ex-conjoints divorcés. Peut être majorée (charges enfants, ressources faibles, invalidité). Conditions d'attribution: âge, ressources du ménage, situation maritale (variables selon régime de base ou complémentaire).
- Conditions : mariage obligatoire | conditions de ressources pour certains régimes
- Seuils : `{"taux_reversion_pct": 54}`

### PAT-026 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 156, II-2 (pension alimentaire) et art. 196 B (enfant majeur) ; C. pen. art. 227-3
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 9-10
- Règle : Pension alimentaire entre parents et enfants (et gendres/belles-filles ↔ beaux-parents si mariés): déductible intégralement des revenus imposables si hors foyer fiscal; si enfant majeur au domicile: déduction forfaitaire 3 592 € (logement + nourriture), autres dépenses réelles justifiées dans la limite de 6 042 € par enfant (12 084 € si marié/pacsé). Abandon de famille > 2 mois: peine d'emprisonnement jusqu'à 2 ans et 15 000 € d'amende.
- Conditions : enfant hors foyer fiscal
- Seuils : `{"deduction_forfaitaire_domicile": 3592, "plafond_deduction": 6042, "plafond_marie": 12084}`

### PAT-027 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 779, II (abattement personne handicapee) ; art. 199 septies (contrat epargne handicap)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 12-12
- Règle : Dispositifs fiscaux pour enfants handicapés: abattement fiscal supplémentaire de 159 325 € (en plus des 100 000 € standard = 259 325 € total par parent sans droits de donation/succession). Contrat d'épargne handicap: réduction d'impôt de 25% des primes, plafond annuel 1 525 € + 300 €/enfant à charge. Rente survie: mêmes avantages fiscaux. AAH (2021): 903,60 €/mois maximum.
- Conditions : infirmité empêchant une activité professionnelle normale
- Seuils : `{"abattement_specifique": 159325, "abattement_total_par_parent": 259325, "plafond_reduction_contrat": 1525, "majoration_par_enfant": 300}`
- Taux : `{"reduction_impot_pct": 25}`

### PAT-028 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 196 B et art. 197 (rattachement enfant majeur, plafond QF) ; art. 81, 36 (job etudiant)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 17-17
- Règle : Rattachement enfant majeur au foyer fiscal: conditions: < 21 ans (ou < 25 ans si étudiant) au 1er janvier de l'année. Avantage: majoration du quotient familial. Économie d'impôt plafonnée: 1 592 €/enfant (les 2 premiers), 3 184 € à partir du 3ème, 3 756 € pour parent isolé. Réductions supplémentaires: 153 € (lycée) / 183 € (université). Job étudiant: revenus exonérés jusqu'à 3 SMIC mensuels; gratification stage: exonération jusqu'au SMIC annuel. Inconvénient: peut faire perdre bourses/aides sociales calculées sur les revenus des parents.
- Seuils : `{"age_max_sans_etudes": 21, "age_max_etudes": 25, "plafond_qf_par_enfant": 1592, "plafond_3eme_enfant": 3184, "plafond_parent_isole": 3756, "reduction_lycee": 153, "reduction_universite": 183}`

### PAT-029 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : Loi 89-462 du 06/07/1989 art. 15 (conge bailleur) et art. 22 (depot de garantie)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 38-39
- Règle : Congé par le bailleur: préavis 6 mois (location nue) ou 3 mois (location meublée) avant l'échéance du bail. Motifs valables: reprise pour habiter/loger un proche, vente, motif légitime et sérieux (non-paiement, comportement). Forme: lettre recommandée AR, acte d'huissier, ou remise en main propre. Restitution dépôt de garantie: 2 mois après départ (1 mois si états des lieux conformes). Pénalité retard: 10% du loyer HC par mois de retard.
- Seuils : `{"preavis_nu_mois": 6, "preavis_meuble_mois": 3, "depot_restitution_mois_max": 2, "depot_restitution_etdl_conformes_mois": 1}`
- Taux : `{"penalite_retard_pct_loyer": 10}`
- Exceptions : Locataire > 65 ans avec ressources faibles: protection spéciale, bailleur doit proposer relogement

### PAT-030 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : C. assur. art. L.113-12-2 et L.313-30 (resiliation infra-annuelle, loi Lemoine 2022-270 du 28/02/2022)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 48-48
- Règle : Loi Lemoine (fév. 2022): possibilité de résilier l'assurance de prêt immobilier à TOUT MOMENT (plus uniquement à date anniversaire). Délégation d'assurance: souscrire auprès d'un autre assureur que la banque permet des économies importantes (jusqu'à plusieurs milliers d'euros pour jeunes emprunteurs en bonne santé). Banque dispose de 10 jours pour accepter ou refuser (uniquement si garanties non équivalentes).

### PAT-031 | règle
- Module : M6
- Statut : `candidate_to_validate`
- Ancre : CGI art. 199 decies H (reduction GFI) ; art. 793, 2-3 (exoneration DMTG) ; art. 976 (IFI)
- source_ingest : 6-guide_gestion_patrimoine.pdf, p. 60-60
- Règle : Parts de GFI (groupements forestiers d'investissement): réduction d'impôt 18% du prix d'acquisition dans la limite de 5 700 € (personne seule) ou 11 400 € (couple). Parts exclues de l'assiette IFI sous conditions. Exonération droits de mutation à titre gratuit sur 75% de la valeur si détention ≥ 2 ans avant transmission par donation/succession. Placement long terme (≥ 12 ans), rendement ~2%/an nets de frais.
- Seuils : `{"plafond_personne_seule": 5700, "plafond_couple": 11400, "duree_min_transmission_ans": 2}`
- Taux : `{"reduction_impot_pct": 18, "exoneration_mutation_pct": 75}`

### CGP-001 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 5-6
- Règle : Patrimoine familial = ensemble des actifs économiques (fonciers, immobiliers, financiers, 'assurantiels') sur lesquels des droits de propriété peuvent être exercés, diminués des dettes. Inclut les droits et obligations appréciables en argent. Attaché aux personnes (spécificité française: transmission aux descendants pour une part minimum fixée par la loi).

### CGP-002 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 10-11
- Règle : Bien-être financier (CFPB, 2015): état dans lequel la personne a le sentiment (i) d'avoir le contrôle de ses finances courantes, (ii) d'avoir la capacité d'absorber un choc financier, (iii) d'être sur la bonne voie pour atteindre ses objectifs financiers/patrimoniaux à moyen et long terme, (iv) d'avoir la liberté financière de profiter de la vie.

### CGP-003 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 9-10
- Règle : 5 caractéristiques-clés d'une famille pour l'optimisation patrimoniale: (1) Capital humain (éducation, expérience, revenus futurs actualisés); (2) Étape du cycle de vie familiale/professionnelle; (3) Objectifs de vie financiers et patrimoniaux; (4) Préférences vis-à-vis du risque, du temps et de la solidarité intergénérationnelle; (5) Connaissance et expérience financières (financial literacy).

### CGP-004 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 13-14
- Règle : 5 éléments-clés de situation à auditer pour tout conseil patrimonial: (D1) Situation juridique civile des personnes et des biens (mode de conjugalité, enfants, famille recomposée, modes de détention); (D2) Situation patrimoniale (volume actifs fonciers/immo/financiers/assurantiels, modes de gestion); (D3) Situation assurantielle/sociale (protections risques personnes et biens); (D4) Situation fiscale (impôts et prélèvements); (D5) Situation financière (créances, dettes, niveau d'endettement net).

### CGP-005 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 11-12
- Règle : 5 étapes du cycle de vie familiale et professionnelle avec objectifs patrimoniaux associés: (1) Entrée dans la vie active + constitution famille: choisir mode de conjugalité, devenir propriétaire RP, constituer/valoriser un capital; (2) Développement familial/professionnel: constituer capital, protéger proches (donation conjoint), préparer retraite; (3) Maturité: financer études enfants, sécuriser patrimoine professionnel, optimiser fiscalité (IR/IFI), SCI; (4) Terme vie professionnelle + retraite: revenus complémentaires, liquidité du patrimoine, organiser transmission; (5) Vie longue à la retraite: concilier couverture risques vie longue (santé, dépendance) et transmission.

### CGP-006 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 14-15
- Règle : Compte de résultat familial: Revenus (salaires, revenus financiers, loyers) - Dépenses de consommation - IR - Taxes foncières/habitation - Frais financiers nets - Primes assurance = ÉPARGNE DE LA PÉRIODE. Tableau de financement familial: Emplois (investissements: épargne liquide, assurance-vie, immobilier) = Ressources (épargne période + nouveaux emprunts - remboursements). Capacité d'épargne = flux à allouer aux investissements.

### CGP-007 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 15-16
- Règle : 4 domaines de stratégies patrimoniales élémentaires: (1) Actions sur la situation juridique des personnes et des biens (mode de conjugalité, protection conjoint, transmission familiale recomposée); (2) Actions sur la situation patrimoniale: investissements/désinvestissements, prises d'assurances; (3) Actions sur la situation financière; (4) Gestion de la contribution fiscale. Ces stratégies combinées dans un plan patrimonial global cohérent constituent le plan de gestion patrimoniale familiale.

### CGP-008 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 19-19
- Règle : Processus de conseil certifié CGPC en 6 étapes: (1) Établir la relation et spécifier le champ; (2) Recueillir les informations pertinentes (questionnaire approfondi); (3) Analyser la situation patrimoniale et tirer un bilan global (D1 juridique + D2 patrimonial + D3 assurantiel + D4 fiscal); (4) Développer et présenter des recommandations personnalisées; (5) Contribuer à la mise en œuvre; (6) Suivre la situation et les recommandations dans le temps. Regroupable en 4 phases: découverte/collecte (front office) → analyse/recommandations (back office) → mise en œuvre (coréalisation) → suivi.

### CGP-009 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 19-20
- Règle : 4 blocs d'activités et compétences du conseil certifié (référentiel RNCP): B1 — Conduire la relation client en conformité avec la réglementation (questionnement, objectifs, mission); B2 — Réaliser un bilan patrimonial global (audit D1 juridique + D2 patrimonial + D3 assurantiel + D4 fiscal); B3 — Concevoir une stratégie patrimoniale globale (actions sur situation juridique, investissement/désinvestissement, assurances, préparation retraite, gestion fiscale); B4 — Assurer la mise en œuvre et l'actualisation (révision selon évolution situation et réglementation).

### CGP-010 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 13-13
- Règle : 3 types de préférences clés à appréhender chez le client: (iv.1) Aversion au risque (mesurée par perte maximale acceptable, varie selon but de l'investissement et étape du cycle de vie); (iv.2) Préférence pour le temps (taux d'actualisation personnel: préférence forte pour le présent = défavorable à l'épargne long terme); (iv.3) Solidarité intergénérationnelle (propension à transmettre vs dépenser pour soi). Biais comportementaux à corriger: asymétrie gains/pertes (l'effet négatif d'une perte > effet positif d'un gain équivalent), surpondération des probabilités d'événements rares.

### CGP-011 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 81-82
- Règle : Le CGP est exposé à 4 types de réglementations selon ses activités: (1) CIF (conseiller en investissements financiers) sous tutelle AMF pour instruments financiers; (2) IAS (intermédiaire en assurance) sous tutelle ACPR pour produits d'assurance vie et non-vie; (3) IOBSP sous tutelle ACPR pour opérations de crédit; (4) IOI (intermédiaire immobilier) pour transactions immobilières (carte T, loi Hoguet/ALUR). Formation continue obligatoire: CIF 7h/an, IAS 15h/an (DDA), IOBSP 7h/an, IOI 14h/an.
- Seuils : `{"formation_CIF_heures_an": 7, "formation_IAS_heures_an": 15, "formation_IOBSP_heures_an": 7, "formation_IOI_heures_an": 14}`
- Exceptions : Certification CGPC donne accès à toutes les activités

### CGP-012 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 74-77
- Règle : Certification CGPC (Conseiller en Gestion de Patrimoine Certifié) enregistrée au RNCP niveau 7 (grade master): 2 paliers — CFC (Conseiller Financier Certifié, palier 1, 1 an expérience) et E-CGPC (Expert-Conseil en Gestion de Patrimoine Certifié, palier 2, 3 ans expérience, cas complexes). Engagement éthique en 8 principes: intérêt du client, intégrité, objectivité, honnêteté, professionnalisme, compétence, confidentialité, diligence. Formation continue: 30h/an validée.
- Seuils : `{"experience_CFC_ans": 1, "experience_ECGPC_ans": 3, "formation_continue_heures_an": 30}`

### CGP-013 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 57-60
- Règle : Risques spécifiques de la vie longue à couvrir: accidents de la vie, dépendance (maladie, perte d'autonomie). Outils de la vie longue: prêt viager hypothécaire, vente en viager, rente viagère à titre onéreux (assurance-vie), mandat de protection future, donations en nue-propriété ou PP. Stratégies de 'dé-accumulation' du patrimoine en cas de vie longue. Espérance de vie à l'âge de la retraite: ~23,2 ans (hommes) et ~27,5 ans (femmes).
- Seuils : `{"esperance_vie_retraite_hommes_ans": 23.2, "esperance_vie_retraite_femmes_ans": 27.5}`

### CGP-014 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 91-91
- Règle : Types d'actes juridiques (décret 2008-1484): Conservatoires (urgents, nécessaires, faible dépense, ne modifient pas le patrimoine); D'administration (gestion courante: entretien, bail < 9 ans, conservent et font fructifier le patrimoine); De disposition (modifications graves et irrévocables: vente, bail > 9 ans, hypothèque); De la vie courante (faible valeur, réalisables par mineurs ou majeurs sous tutelle). La capacité juridique d'une personne = aptitude à acquérir et exercer des droits, à accomplir les actes conservatoires, d'administration et de disposition.

### CGP-015 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 91-92
- Règle : Actifs patrimoniaux: actifs économiques sur lesquels des droits de propriété peuvent être exercés et qui procurent des avantages économiques (financiers ou non financiers). Actifs réels (métaux précieux, énergie, etc.): peu corrélés aux classes financières classiques, performants en phase d'inflation ou taux réels bas. Actifs réels = diversification patrimoniale. Cryptomonnaies: intrinsèquement spéculatives (valeur déterminée uniquement par le nombre de participants), à éviter pour le CGP professionnel.

### CGP-016 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 70-72
- Règle : Conseil indépendant (statut CIF): rémunéré uniquement en honoraires client; ne peut percevoir de commissions des producteurs (interdiction des 'inducements'); doit analyser un nombre suffisant de produits sur le marché pour formuler ses recommandations. Conseil non-indépendant (semi-indépendant): peut percevoir rétrocessions de commissions des producteurs, autorisé à vendre les produits conseillés. Déclaration d'adéquation obligatoire dans les deux cas (explique en quoi la recommandation est adaptée au client).

### CGP-017 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 9-10
- Règle : Capital humain: valeur actualisée des revenus futurs qu'une personne peut espérer tirer de son travail. Composé de la formation initiale, des formations continues et de l'expérience acquise. Procure l'employabilité. Cycle: constant/croissant en début de carrière, décroissant à l'approche de la retraite (la formation continue ralentit cette décroissance). Objectif fondamental: 'que le capital humain ait été transformé en capital financier', c'est-à-dire avoir constitué un patrimoine pendant la vie active.

### CGP-018 | définition
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 77-78
- Règle : Tendances lourdes nécessitant une gestion patrimoniale renforcée: (1) Vie plus longue = risque de survie à son capital + dépendance; (2) Situations matrimoniales moins stables (PACS sans vocation successorale légale, divorces tardifs = précarité); (3) Parcours professionnels moins linéaires = besoin de solidarité familiale accru; (4) Successions volumineuses à venir (patrimoines des baby-boomers); (5) Familles recomposées (1 sur 5); (6) Coexistence 3 générations = solidarité intergénérationnelle; (7) Crise des régimes de retraite = épargne retraite obligatoire.

### CGP-019 | obligation
- Module : M7
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : Livret-daccueil-2-Optimiser-un-patrimoine-familial-et_conseiller-sur-sa-gestion-en-professionnel-certifie.pdf, p. 66-68
- Règle : Obligations réglementaires du CGP (MIF2 pour instruments financiers, DDA pour assurances): (1) Agir honnêtement, loyalement et professionnellement dans le meilleur intérêt du client; (2) Identifier et gérer les conflits d'intérêts; (3) Recueillir les informations sur situation financière, objectifs, connaissance/expérience, tolérance au risque; (4) Test d'adéquation: vérifier que la recommandation est adaptée à la situation et aux objectifs du client; (5) Remettre une déclaration d'adéquation; (6) Informations précontractuelles standardisées (DIC/PRIIPS); (7) Gouvernance produit (marchés cibles).
- Exceptions : Champ MIF2/DDA = volet financier/assurance uniquement; la dimension juridique/civile n'est pas couverte par la réglementation mais l'est par la certification CGPC

### RF-001 | condition
- Module : M9
- Statut : `candidate_to_validate`
- Ancre : CGI art. 32 (micro-foncier, abattement 30 %) ; BOI-RFPI-DECLA-10
- source_ingest : M5_location_meublee_fiscal_2025_rawtext.txt
- Règle : Le régime micro-foncier s'applique aux propriétaires dont les revenus fonciers bruts annuels n'excèdent pas 15 000 €. L'abattement forfaitaire est de 30 % (représente les charges). Revenu net foncier imposable = revenus bruts × 70 %. Pas de déclaration 2044 nécessaire — report directement sur la 2042.
- Conditions : revenus fonciers bruts ≤ 15 000 € | location nue uniquement
- Seuils : `{"seuil_micro_foncier": 15000, "abattement_pct": 30}`
- Exceptions : Contribuables détenant des parts de SCPI ou bénéficiant de certains dispositifs (Malraux, Monuments historiques) ne peuvent pas être au micro-foncier | Option pour le régime réel: exercée par dépôt d'une 2044, valable 3 ans irrévocablement

### RF-002 | règle
- Module : M9
- Statut : `candidate_to_validate`
- Ancre : CGI art. 28 et art. 31 (regime reel foncier) ; BOI-RFPI-BASE-10
- source_ingest : M5_location_meublee_fiscal_2025_rawtext.txt
- Règle : Le régime réel foncier s'applique obligatoirement si les revenus fonciers bruts dépassent 15 000 €, ou sur option si ≤ 15 000 € (option irrévocable 3 ans). Revenu net foncier = Loyers bruts encaissés − charges déductibles. Déclaration sur formulaire 2044. Le revenu net foncier est ensuite reporté sur la 2042.
- Conditions : revenus fonciers > 15 000 € OU option pour le réel
- Seuils : `{"seuil_regime_reel": 15000}`

### RF-003 | règle
- Module : M9
- Statut : `candidate_to_validate`
- Ancre : CGI art. 31, I-1 (charges deductibles des revenus fonciers) ; BOI-RFPI-BASE-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 65-66
- Règle : Charges déductibles des revenus fonciers au régime réel: (1) Intérêts d'emprunts et frais de dossier (pour acquisition, construction, réparation); (2) Travaux d'entretien, réparation et amélioration (pas les travaux de construction ou d'agrandissement); (3) Taxe foncière (hors ordures ménagères si récupérable); (4) Primes d'assurance (PNO, loyers impayés, GLI); (5) Frais de gestion et d'administration (agence immobilière, syndic, comptable); (6) Provisions pour charges de copropriété; (7) Frais de procédure (contentieux locatif).
- Conditions : régime réel foncier | charges payées dans l'année civile
- Exceptions : Travaux de construction ou d'agrandissement: non déductibles (augmentent le prix d'acquisition pour le calcul de la PV) | Charges de travaux: déductibles l'année du paiement (et non l'année d'exécution)

### RF-004 | règle
- Module : M9
- Statut : `candidate_to_validate`
- Ancre : CGI art. 156, I-3 (deficit foncier, imputation sur le revenu global) ; BOI-RFPI-BASE-30
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 65-66
- Règle : Déficit foncier au régime réel: le déficit résultant de charges autres que les intérêts d'emprunt est imputable sur le revenu global dans la limite de 10 700 € par an. La fraction de déficit excédant 10 700 € est reportable sur les revenus fonciers des 10 années suivantes. Le déficit imputable sur le revenu global est conditionné à la location du bien pendant les 3 années suivant l'imputation (clause de maintien de location).
- Conditions : régime réel foncier | bien loué pendant 3 ans après imputation du déficit
- Seuils : `{"plafond_imputation_revenu_global": 10700, "report_annees": 10}`
- Exceptions : La part du déficit provenant des INTÉRÊTS D'EMPRUNT est reportable uniquement sur les revenus fonciers des 10 années suivantes (pas imputable sur le revenu global) | Dispositif Monuments Historiques: pas de plafond d'imputation sur le revenu global

### RF-005 | règle
- Module : M9
- Statut : `candidate_to_validate`
- Ancre : CGI art. 32 (foncier) et art. 35 / 50-0 (BIC) ; art. 39 C (amortissements LMNP)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 65-66
- Règle : Différences fiscales clés entre location nue (revenus fonciers) et location meublée (BIC): Location nue → revenus fonciers, micro si < 15 000 €, déficit imputable sur RG (plafond 10 700 €), PV régime particuliers avec abattements durée détention. Location meublée → BIC, micro si < 77 700 € (50 % abattement), amortissements déductibles (art. 39-C), mais PV depuis 2025 réintègre les amortissements.

### PV-RP-001 | règle
- Module : M9
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150 U, II-1 (exoneration residence principale) ; BOI-RFPI-PVI-10-40-10 (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046860944/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 70-70
- Règle : La cession de la résidence principale est totalement exonérée de plus-value immobilière (IR + prélèvements sociaux), sans condition de durée de détention. Condition unique: le bien doit constituer la résidence habituelle et effective du cédant au moment de la cession. L'exonération s'applique aussi aux dépendances immédiates et nécessaires cédées simultanément (garage, cave, terrain contigu).
- Conditions : résidence principale effective et habituelle au moment de la cession
- Exceptions : Délai entre départ du logement et cession: exonération maintenue si délai 'normal' (généralement ≤ 12 mois, appréciation au cas par cas) | Logement mis en location avant la vente: perte de l'exonération si le bien n'est plus la RP effective | Résidence principale dans une SCI: exonération possible si le cédant des parts est aussi l'occupant

### PV-IMM-001 | règle
- Module : M9
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150 V a 150 VC (assiette PV immobiliere) ; BOI-RFPI-PVI-20-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 70-71
- Règle : Plus-value brute = Prix de cession − Prix d'acquisition. Prix de cession: prix stipulé dans l'acte diminué des frais de cession (diagnostics, honoraires d'agence si à la charge du vendeur). Prix d'acquisition: prix d'achat majoré des frais d'acquisition (droits de mutation, honoraires notaire réels ou forfait 7,5 % si cédé plus de 5 ans après acquisition) et des travaux (frais réels ou forfait 15 % si bien cédé > 5 ans après acquisition).
- Seuils : `{"forfait_frais_acquisition_pct": 7.5, "forfait_travaux_pct": 15, "duree_min_forfait_ans": 5}`
- Exceptions : Bien reçu par donation ou succession: prix d'acquisition = valeur retenue pour le calcul des droits de mutation

### PV-IMM-002 | seuil
- Module : M9
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150 VC (abattement pour duree de detention) ; art. 150 VE ; BOI-RFPI-PVI-20-20
- source_ingest : _GUIDE DU LOUEUR EN MEUBLES FINAL.pdf, p. 62-63
- Règle : Abattements pour durée de détention applicables sur la PV brute (autres biens que RP): Pour l'IR: 0 % jusqu'à 5 ans; 6 %/an de la 6ème à la 21ème année; 4 % pour la 22ème année complète → exonération IR complète après 22 ans de détention. Pour les PS: 0 % jusqu'à 5 ans; 1,65 %/an de la 6ème à la 21ème; 1,6 % la 22ème; 9 %/an de la 23ème à la 30ème → exonération PS complète après 30 ans de détention.
- Seuils : `{"exoneration_IR_annees": 22, "exoneration_PS_annees": 30}`
- Taux : `{"abattement_IR_6_21_pct_an": 6, "abattement_IR_22_pct": 4, "abattement_PS_6_21_pct_an": 1.65, "abattement_PS_22_pct": 1.6, "abattement_PS_23_30_pct_an": 9}`

### PV-IMM-003 | règle
- Module : M9
- Statut : `candidate_to_validate`
- Ancre : CGI art. 200 B (IR 19 %) et art. 1609 nonies G (taxe PV elevee) ; CSS art. L.136-7 (PS) ; BOI-RFPI-PVI-30
- source_ingest : M4_location_meublee_regime_2024_rawtext.txt
- Règle : Taux d'imposition des PV immobilières nettes (après abattements): IR = 19 %; Prélèvements sociaux = 17,2 %. Taxe supplémentaire si PV imposable (pour l'IR, après abattement) > 50 000 €: de 2 % à 6 % selon le montant (barème progressif: 2 % pour PV entre 50 001 € et 100 000 €; 3 % entre 100 001 € et 150 000 €; 4 % entre 150 001 € et 200 000 €; 5 % entre 200 001 € et 250 000 €; 6 % au-delà de 250 000 €). C'est le notaire qui calcule et acquitte l'impôt lors de la vente.
- Seuils : `{"seuil_taxe_supplementaire": 50000}`
- Taux : `{"IR_pct": 19, "PS_pct": 17.2}`

### PV-IMM-004 | règle
- Module : M9
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150 U, II (cas d'exoneration) ; BOI-RFPI-PVI-10-40 (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046860944/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 70-70
- Règle : Cas d'exonération de PV immobilière hors résidence principale: (1) Première cession d'un logement autre que la RP si le cédant n'a pas été propriétaire de sa RP dans les 4 années précédentes ET il réutilise le produit pour acquérir/construire sa RP dans les 24 mois; (2) Cession à un organisme de logement social ou intercommunalité; (3) Cession par des titulaires de pension retraite ou invalidité ayant un RFR modeste; (4) Bien détenu > 22 ans (IR) ou > 30 ans (PS) → exonération totale.
- Seuils : `{"delai_remploi_rp_mois": 24, "non_proprietaire_rp_ans": 4}`

### PV-IMM-005 | règle
- Module : M9
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150 UB (cession de parts de societes a preponderance immobiliere) ; BOI-RFPI-SPI-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 20-20
- Règle : Cession de parts de SCI soumise à l'IR: PV imposée selon le régime des PV immobilières des particuliers (abattements durée de détention, taux 19 % + 17,2 % PS). La durée de détention est calculée depuis l'acquisition des parts. Si la SCI a opté pour l'IS: la cession de parts relève du régime des PV mobilières (PFU 30 % ou barème IR, sans abattement durée de détention).
- Exceptions : SCI à l'IS: perte de l'abattement pour durée de détention → PV imposée à 12,8 % + 17,2 % PS = PFU 30 %

### DSD-001 | règle
- Module : M10
- Statut : `candidate_to_validate`
- Ancre : CGI art. 796-0 bis (exoneration conjoint / PACS, loi TEPA 2007) ; CGI art. 790 E (abattement donation entre epoux)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 79-81
- Règle : Exonération totale de droits de succession pour: (1) le conjoint survivant (depuis loi TEPA du 21/08/2007); (2) le partenaire de PACS survivant. Ces exonérations s'appliquent aux transmissions par décès uniquement. Pour les donations entre époux/partenaires PACS, des droits peuvent s'appliquer selon les barèmes (mais abattement spécifique de 80 724 € entre époux).
- Conditions : transmission par décès
- Seuils : `{"abattement_donation_epoux": 80724}`
- Exceptions : Les donations entre époux sont imposables selon le barème en ligne directe avec abattement de 80 724 €

### DSD-002 | seuil
- Module : M10
- Statut : `candidate_to_validate`
- Ancre : CGI art. 777 (bareme ligne directe) ; art. 779 (abattements) ; BOI-ENR-DMTG-10-50-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 81-83
- Règle : Barème des droits de succession/donation en ligne directe (parents→enfants, enfants→parents, grands-parents→petits-enfants) après déduction des abattements applicables: Fraction de la part nette taxable: jusqu'à 8 072 € → 5 %; de 8 073 € à 12 109 € → 10 %; de 12 110 € à 15 932 € → 15 %; de 15 933 € à 552 324 € → 20 %; de 552 325 € à 902 838 € → 30 %; de 902 839 € à 1 805 677 € → 40 %; au-delà de 1 805 677 € → 45 %.
- Conditions : après déduction des abattements applicables
- Seuils : `{"tranche_1_max": 8072, "tranche_2_min": 8073, "tranche_2_max": 12109, "tranche_3_min": 12110, "tranche_3_max": 15932, "tranche_4_min": 15933, "tranche_4_max": 552324, "tranche_5_min": 552325, "tranche_5_max": 902838, "tranche_6_min": 902839, "tranche_6_max": 1805677}`
- Taux : `{"tranche_1_pct": 5, "tranche_2_pct": 10, "tranche_3_pct": 15, "tranche_4_pct": 20, "tranche_5_pct": 30, "tranche_6_pct": 40, "tranche_7_pct": 45}`

### DSD-003 | seuil
- Module : M10
- Statut : `candidate_to_validate`
- Ancre : CGI art. 777 (bareme freres et soeurs) ; art. 788, I (abattement specifique)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 79-81
- Règle : Barème entre frères et sœurs: Jusqu'à 24 430 € (après abattement de 15 932 €): 35 %. Au-delà de 24 430 €: 45 %. Abattement spécifique de 15 932 € applicable uniquement si le bénéficiaire est célibataire, veuf, divorcé ou séparé de corps au moment du décès ET âgé de plus de 50 ans ou atteint d'infirmité.
- Seuils : `{"tranche_1_max": 24430, "abattement_specifique": 15932}`
- Taux : `{"tranche_1_pct": 35, "tranche_2_pct": 45}`
- Exceptions : Abattement de 15 932 € uniquement si bénéficiaire: célibataire/veuf/divorcé/séparé ET > 50 ans ou infirmité

### DSD-004 | seuil
- Module : M10
- Statut : `candidate_to_validate`
- Ancre : CGI art. 777 (bareme jusqu'au 4e degre / non parents) ; art. 779, IV et art. 788 (abattements)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 81-83
- Règle : Barèmes de droits de succession/donation selon le degré de parenté: Entre parents jusqu'au 4ème degré (oncles/tantes, neveux/nièces, cousins germains): 55 % (avec abattement de 7 967 €). Entre non-parents ou parents au-delà du 4ème degré: 60 % (avec abattement de 1 594 €). Entre grands-parents et petits-enfants (ligne directe): barème ligne directe avec abattement de 31 865 €.
- Seuils : `{"abattement_neveux": 7967, "abattement_non_parents": 1594, "abattement_petits_enfants": 31865}`
- Taux : `{"oncles_neveux_pct": 55, "non_parents_pct": 60}`

### DSD-005 | règle
- Module : M10
- Statut : `candidate_to_validate`
- Ancre : CGI art. 784 (rappel fiscal des donations)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 81-83
- Règle : Rappel fiscal des donations antérieures: pour calculer les droits sur une nouvelle donation ou une succession, les abattements et le barème s'appliquent sur l'ensemble des donations reçues du même donateur/défunt au cours des 15 années précédentes. Si des donations ont été faites il y a moins de 15 ans, les abattements sont réduits du montant déjà utilisé. Au-delà de 15 ans, les abattements sont totalement reconstitués.
- Seuils : `{"delai_reconstitution_ans": 15}`

### DSD-006 | définition
- Module : M10
- Statut : `candidate_to_validate`
- Ancre : CGI art. 777 et 779 (calcul des droits en ligne directe)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 72-73
- Règle : Exemple de calcul droits de succession: patrimoine net taxable transmis à un enfant après abattement de 100 000 €. Si part nette taxable = 200 000 €: 8 072 × 5 % = 404 €; (12 109−8 072) × 10 % = 404 €; (15 932−12 109) × 15 % = 573 €; (200 000−15 932) × 20 % = 36 814 €. Total = 38 195 €. Taux effectif = 38 195/200 000 = 19 %. Soit sur un patrimoine brut de 300 000 € transmis à un enfant unique: 38 195 € de droits.
- Taux : `{"taux_effectif_exemple_pct": 19}`

### IFI-001 | règle
- Module : M10
- Statut : `candidate_to_validate`
- Ancre : CGI art. 964 a 966 (champ IFI) et art. 977 (seuil) ; art. 973, II (abattement RP) ; BOI-PAT-IFI (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036384999/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 73-75
- Règle : L'IFI est dû lorsque la valeur nette taxable du patrimoine immobilier dépasse 1 300 000 € au 1er janvier de l'année d'imposition. L'assiette est constituée de la valeur de marché des biens immobiliers détenus directement ou via des sociétés (SCI, SCPI, OPCI, foncières non cotées), diminuée du passif déductible (emprunts immobiliers, taxes foncières dues). Abattement de 30 % sur la valeur de la résidence principale.
- Conditions : patrimoine net immobilier > 1 300 000 €
- Seuils : `{"seuil_IFI": 1300000, "abattement_RP_pct": 30}`
- Exceptions : SIIC cotées: actifs immobiliers exclus si détention < 5 % du capital | Biens professionnels: exclus de l'assiette | Parts de SCI à l'IS: incluses dans l'assiette à proportion des actifs immobiliers

### IFI-002 | seuil
- Module : M10
- Statut : `candidate_to_validate`
- Ancre : CGI art. 977 (bareme IFI) ; BOI-PAT-IFI-40-10-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 76-78
- Règle : Barème IFI 2025 (calculé sur la valeur nette taxable, à partir de 800 000 €): De 0 à 800 000 € → 0 %; De 800 001 € à 1 300 000 € → 0,5 %; De 1 300 001 € à 2 570 000 € → 0,7 %; De 2 570 001 € à 5 000 000 € → 1 %; De 5 000 001 € à 10 000 000 € → 1,25 %; Au-delà de 10 000 000 € → 1,5 %. Note: si le patrimoine net dépasse 1 300 000 €, l'IFI est calculé DEPUIS 800 000 € (pas uniquement sur la fraction > 1 300 000 €).
- Conditions : patrimoine net IFI > 1 300 000 €
- Seuils : `{"tranche_0_max": 800000, "tranche_1_min": 800001, "tranche_1_max": 1300000, "tranche_2_min": 1300001, "tranche_2_max": 2570000, "tranche_3_min": 2570001, "tranche_3_max": 5000000, "tranche_4_min": 5000001, "tranche_4_max": 10000000}`
- Taux : `{"tranche_0_pct": 0, "tranche_1_pct": 0.5, "tranche_2_pct": 0.7, "tranche_3_pct": 1.0, "tranche_4_pct": 1.25, "tranche_5_pct": 1.5}`
- Exceptions : Décote si patrimoine net entre 1 300 000 € et 1 400 000 €: IFI = IFI calculé × (3 − 2,5 × patrimoine / 1 400 000)

### IFI-003 | définition
- Module : M10
- Statut : `candidate_to_validate`
- Ancre : CGI art. 977 (bareme) et art. 979 (plafonnement IFI+IR) ; BOI-PAT-IFI-40-30-10
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 76-78
- Règle : Exemple de calcul IFI: Patrimoine immobilier net taxable = 2 000 000 €. IFI = (1 300 000 − 800 000) × 0,5 % + (2 000 000 − 1 300 000) × 0,7 % = 2 500 + 4 900 = 7 400 €. Taux effectif = 7 400/2 000 000 = 0,37 %. Rappel: plafonnement — IFI + IR ne peut excéder 75 % des revenus de l'année précédente (excédent en diminution de l'IFI à payer).
- Taux : `{"taux_effectif_exemple_pct": 0.37, "plafonnement_pct": 75}`

### IFI-004 | règle
- Module : M10
- Statut : `candidate_to_validate`
- Ancre : CGI art. 974 (passif deductible IFI) ; BOI-PAT-IFI-20-30-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 75-75
- Règle : Passif déductible de l'assiette IFI: (1) Emprunts immobiliers contractés pour l'acquisition, la réparation ou l'amélioration des biens taxables; (2) Travaux à réaliser (engagements pris mais non encore exécutés); (3) Taxe foncière et IFI de l'année courante dus mais non encore payés. Ne sont PAS déductibles: impôts sur le revenu, emprunts contractés pour l'achat de valeurs mobilières, découverts bancaires non liés à l'immobilier.
- Exceptions : Règle anti-abus: emprunt in fine auprès d'un associé ou souscription d'emprunt auprès d'une société familiale → sous conditions restrictives

### TRM-001 | seuil
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 777, 779, 788, 790 B a 790 E (abattements DMTG) ; BOI-ENR-DMTG-10-50
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 79-81
- Règle : Tableau complet des abattements DMTG 2025 (reconstitution tous les 15 ans): SUCCESSION: Conjoint/PACS: EXONÉRATION TOTALE; Enfant ou ascendant: 100 000 €; Petit-enfant: 1 594 €; Arrière-petit-enfant: 1 594 €; Frère/sœur: 15 932 € (ou exonération sous conditions*); Neveu/nièce: 7 967 €; Handicapé: 159 325 € (cumulable); Autres bénéficiaires: 1 594 €. DONATION: Conjoint/PACS: 80 724 €; Enfant: 100 000 €; Petit-enfant: 31 865 €; Arrière-petit-enfant: 5 310 €; Frère/sœur: 15 932 €; Neveu/nièce: 7 967 €; Handicapé: 159 325 € (cumulable). *Frère/sœur exonération succession si: célibataire/veuf/divorcé/séparé + âgé > 50 ans ou infirmité + domicilié avec défunt 5 ans avant décès.
- Conditions : 15 ans de rappel fiscal
- Seuils : `{"succession_conjoint": "exonération totale", "succession_enfant": 100000, "succession_petit_enfant": 1594, "donation_conjoint_PACS": 80724, "donation_enfant": 100000, "donation_petit_enfant": 31865, "donation_arriere_petit_enfant": 5310, "donation_frere_soeur": 15932, "don_numeraire_supp": 31865, "abattement_handicape": 159325}`
- Exceptions : Exonération succession frères/sœurs sous triple condition (célibataire + âge + cohabitation) | Abattement handicapé de 159 325 € CUMULABLE avec les abattements par lien de parenté

### TRM-002 | condition
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 790 G (don de sommes d'argent) ; art. 790 A bis (don creation entreprise/RP, LDF 2025)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 81-81
- Règle : Don en numéraire exonéré de droits: abattement spécifique de 31 865 € par donateur, cumulable avec l'abattement général (100 000 € parent/enfant). Conditions: donateur < 80 ans ET donataire majeur ou mineur émancipé. Bénéficiaires: enfants, petits-enfants, arrière-petits-enfants, ou à défaut neveux/nièces. LDF 2025: exonération renforcée jusqu'à 100 000 € par donateur ET par donataire pour dons affectés à la création d'entreprise ou construction de la résidence principale du donataire.
- Conditions : donateur < 80 ans | donataire majeur ou mineur émancipé
- Seuils : `{"abattement_numeraire": 31865, "exoneration_renforcee_LDF2025": 100000}`
- Exceptions : Exonération renforcée LDF 2025 (100 000 €) limitée à certains usages: création entreprise ou construction RP

### TRM-003 | condition
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 787 B (Pacte Dutreil, exoneration 75 %) ; BOI-ENR-DMTG-10-20-40 (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047623071/) (verifie le 2026-06-05)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 83-84
- Règle : Pacte Dutreil (art. 787 B CGI): exonération de 75 % de la valeur de l'entreprise transmise par donation ou succession. Le donataire/héritier n'est imposé que sur 25 % de la valeur réelle. Conditions: les donataires s'engagent à CONSERVER les biens affectés à l'exploitation + l'un d'entre eux s'engage à POURSUIVRE l'exploitation (ou exercer une activité dans l'entreprise) jusqu'au terme de l'engagement individuel de conservation. En cas de profession réglementée: le donataire doit justifier des diplômes et/ou habilitations professionnelles.
- Conditions : engagement collectif de conservation préalable | engagement individuel de conservation post-donation | poursuite d'exploitation par au moins un donataire
- Taux : `{"exoneration_pct": 75}`
- Exceptions : Non applicable si l'entreprise n'est pas transmise à un descendant direct | Doit être combiné avec d'autres abattements pour optimiser

### TRM-004 | seuil
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 669 (bareme de l'usufruit) ; BOI-ENR-DMTG-10-40-10-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 84-85
- Règle : Barème de l'usufruit (art. 669 CGI) utilisé pour calculer la valeur de la nue-propriété transmise lors d'une donation avec réserve d'usufruit. La valeur de la nue-propriété transmise (soumise aux droits) est déterminée par: Valeur NP = Valeur PP × (100 % − Valeur usufruit). Barème: âge usufruitier < 21 ans: usufruit 90 %, NP 10 %; 21-30 ans: 80 %/20 %; 31-40 ans: 70 %/30 %; 41-50 ans: 60 %/40 %; 51-60 ans: 50 %/50 %; 61-70 ans: 40 %/60 %; 71-80 ans: 30 %/70 %; 81-90 ans: 20 %/80 %; > 90 ans: 10 %/90 %.
- Conditions : barème applicable à tous les démembrements (donation, succession, IFI)
- Seuils : `{"age_moins_21_usufruit_pct": 90, "age_21_30_usufruit_pct": 80, "age_31_40_usufruit_pct": 70, "age_41_50_usufruit_pct": 60, "age_51_60_usufruit_pct": 50, "age_61_70_usufruit_pct": 40, "age_71_80_usufruit_pct": 30, "age_81_90_usufruit_pct": 20, "age_plus_90_usufruit_pct": 10}`
- Exceptions : Au décès de l'usufruitier: le nu-propriétaire devient plein propriétaire EN FRANCHISE DE DROITS (pas de nouvelle taxation)

### TRM-005 | obligation
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 641 et 642 (delais de declaration) ; art. 1701 et 1717 ; BOI-ENR-DG-50
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 84-85
- Règle : Délais de paiement des droits de mutation à titre gratuit: DONATION: paiement dans le mois suivant la donation. SUCCESSION: paiement avant la fin du 6ème mois suivant le mois du décès (pour décès en France). Modalités dérogatoires: paiement fractionné en 3 versements égaux à intervalles de 6 mois maximum sur une période maximale d'1 an; paiement différé possible dans certains cas (notamment en présence d'usufruit ou de biens professionnels non liquides).
- Seuils : `{"delai_donation_mois": 1, "delai_succession_mois": 6, "paiement_fractionne_versements": 3, "paiement_fractionne_max_mois": 12}`
- Exceptions : Décès hors de France: délai porté à 12 mois | Paiement différé possible si héritier reçoit des biens non liquides (parts de sociétés, entreprises)

### TRM-006 | règle
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : Loi n2021-1104 du 22/08/2021 (Climat et resilience), art. 160 ; Loi n89-462 du 06/07/1989 art. 6 (decence energetique) ; CCH art. L.173-1-1 (seuils DPE)
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 56-58
- Règle : Calendrier d'interdiction de location selon le DPE (loi Climat): depuis 25 août 2022: gel des loyers pour logements G; depuis 1er janvier 2023: interdiction de mise en location des biens dont consommation > 450 kWh/m2 (classe G++); depuis 1er janvier 2025: interdiction location classe G (ensemble des G); depuis 1er janvier 2028: interdiction location classe F; depuis 1er janvier 2034: interdiction location classe E. Le DPE doit être intégré au dossier de diagnostic technique (DDT) remis au locataire ou à l'acheteur.
- Conditions : applicable à la location à usage de résidence principale
- Seuils : `{"interdiction_G_plus_plus_annee": 2023, "interdiction_G_annee": 2025, "interdiction_F_annee": 2028, "interdiction_E_annee": 2034}`
- Exceptions : Ces interdictions concernent la résidence principale du locataire | Monopropriété: calendrier potentiellement aménagé

### TRM-007 | règle
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 156, I-3 (doublement deficit foncier renovation energetique) ; BOI-RFPI-BASE-30
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 65-66
- Règle : Le plafond d'imputation du déficit foncier sur le revenu global est porté de 10 700 € à 21 400 € lorsque le déficit est lié à des dépenses de travaux de rénovation énergétique permettant au bien de passer d'une classe énergétique E, F ou G à une classe A, B, C ou D. Cette mesure s'applique aux dépenses de rénovation énergétique payées entre le 1er janvier 2023 et le 31 décembre 2025. Le double plafond est conditionné à la nature des travaux (attestée par un professionnel certifié RGE).
- Conditions : dépenses de rénovation énergétique payées entre 01/01/2023 et 31/12/2025 | bien passant de classe E/F/G vers A/B/C/D | travaux réalisés par professionnel certifié RGE
- Seuils : `{"plafond_standard": 10700, "plafond_renovation_energetique": 21400}`
- Exceptions : Applicable seulement aux dépenses payées avant le 31/12/2025 | Exige un changement de classe énergétique attesté (pas uniquement des travaux d'entretien)

### TRM-008 | règle
- Module : M12
- Statut : `candidate_to_validate`
- Péremption : Pinel : fermé aux nouvelles acquisitions depuis le 01/01/2025 (seuls les investissements antérieurs continuent à produire leurs réductions). Censi-Bouvard : fermé aux nouvelles acquisitions depuis le 01/01/2023.
- Ancre : CGI art. 199 novovicies (Pinel, extinction 31/12/2024) ; BOI-IR-RICI-360
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 59-60
- Règle : Les dispositifs Pinel (métropole), Pinel+ et Pinel Outre-Mer ne s'appliquent plus aux acquisitions réalisées depuis le 1er janvier 2025. En revanche, les investissements Pinel réalisés avant cette date bénéficient du dispositif jusqu'à son terme contractuel (engagement de location de 6, 9 ou 12 ans maintenu). Les taux de réduction en cours d'application restent: 9 %/12 %/14 % (Pinel 2023) ou 12 %/18 %/21 % (Pinel+ 2023-2024).
- Conditions : acquisitions avant 01/01/2025 uniquement
- Taux : `{"pinel_plus_6ans": 12, "pinel_plus_9ans": 18, "pinel_plus_12ans": 21}`
- Exceptions : VEFA signée avant 01/01/2025 mais livraison postérieure: vérifier date prise en compte | Pinel Outre-Mer: règles spécifiques à vérifier

### TRM-009 | règle
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 199 tricies (Loc'Avantages) ; BOI-IR-RICI-235
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 62-63
- Règle : Loc'Avantages: réduction d'impôt pour les bailleurs qui louent NU à usage de résidence principale dans le cadre d'une convention ANAH (avant le 31 décembre 2027) pour une durée de 6 ans. Le loyer et les ressources des locataires ne doivent pas excéder certains plafonds (secteur intermédiaire, social ou très social). Les locataires ne peuvent pas être ascendants ou descendants du propriétaire. Le taux de réduction varie selon le niveau de loyer pratiqué (secteur intermédiaire: ~15 %; secteur social: ~35 %; secteur très social: ~65 % avec intermédiaire de gestion). Non soumis au plafonnement global des niches fiscales.
- Conditions : convention ANAH signée avant 31/12/2027 | durée 6 ans minimum | location nue résidence principale | locataire non ascendant/descendant | loyer ≤ plafonds selon zone
- Taux : `{"intermediaire_pct": 15, "social_pct": 35, "tres_social_pct": 65}`

### TRM-010 | règle
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 156, I-3 et II-1 ter (Monuments Historiques) ; BOI-RFPI-SPEC-30
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 63-64
- Règle : Dispositif Monuments Historiques: déduction sur le revenu global (sans plafond ni plafonnement des niches) du montant des travaux de restauration et d'entretien réalisés sur un immeuble classé monument historique, inscrit à l'inventaire supplémentaire (ISMH) ou labellisé par la Fondation du patrimoine. Les travaux sont soumis à autorisation de l'État et donnent droit à des subventions publiques (20 à 80 % du coût total). Pas d'obligation de location ni d'occupation. Immeuble soumis au contrôle des Architectes des Bâtiments de France.
- Conditions : immeuble classé MH ou ISMH ou labellisé Fondation du patrimoine | travaux autorisés par l'État
- Taux : `{"subvention_etat_min_pct": 20, "subvention_etat_max_pct": 80}`
- Exceptions : Si le bien est ouvert au public: charges déductibles à 100 %; si non ouvert: à 50 % si revenus locatifs

### TRM-011 | règle
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 977 (decote IFI) ; BOI-PAT-IFI-40-10-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 75-76
- Règle : Mécanisme de décote IFI pour atténuer l'effet de seuil: si la valeur nette taxable du patrimoine (P) est comprise entre 1 300 000 € et 1 400 000 €, l'IFI calculé selon le barème est réduit d'une somme égale à: Décote = 17 500 € − 1,25 % × P. Exemple: patrimoine net = 1 350 000 €. IFI brut selon barème = (1 300 000 - 800 000) × 0,5 % + (1 350 000 - 1 300 000) × 0,7 % = 2 500 + 350 = 2 850 €. Décote = 17 500 − 1,25 % × 1 350 000 = 17 500 − 16 875 = 625 €. IFI net = 2 850 − 625 = 2 225 €.
- Conditions : patrimoine net IFI entre 1 300 000 € et 1 400 000 €
- Seuils : `{"decote_min_patrimoine": 1300000, "decote_max_patrimoine": 1400000}`
- Taux : `{"coefficient_decote_pct": 1.25}`
- Exceptions : Au-delà de 1 400 000 €: plus de décote, barème plein s'applique

### TRM-012 | règle
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 968 (usufruit en valeur PP) et art. 974 (prets in fine) ; BOI-PAT-IFI-20-20-30
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 73-75
- Règle : Biens grevés d'un droit d'usufruit: les biens sont compris dans le patrimoine IFI de l'USUFRUITIER pour leur valeur en pleine propriété (pas répartie entre usufruitier et nu-propriétaire). Exception: lorsque l'usufruit résulte d'une succession avec ouverture d'un usufruit légal au profit du conjoint survivant, la valeur peut être répartie entre usufruitier et nu-propriétaire pour l'IFI. Biens affectés à l'activité professionnelle du redevable: EXONÉRÉS de l'IFI sous conditions. Prêts remboursables in fine: déductibles partiellement — annuités théoriques = capital / durée totale; seule la somme des annuités restant à courir est déductible.
- Exceptions : Usufruit légal du conjoint survivant: répartition possible entre usufruitier et nu-propriétaire | Prêts in fine: déductibilité partielle uniquement (annuités théoriques)

### TRM-013 | définition
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CCH art. L.300-1 et s. (MaPrimeRenov', aide ANAH) ; decret n2020-26 du 14/01/2020
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 59-59
- Règle : MaPrimeRénov' est une aide de l'État (ANAH) pour financer les travaux de rénovation énergétique des logements. Trois formes: (1) MaPrimeRénov' individuelle: aide directe au propriétaire pour travaux d'économie d'énergie (isolation, fenêtres, chaudière, etc.); montant variable selon revenus et nature des travaux. (2) MaPrimeRénov' Copropriété: aide collective pour rénovation globale d'une copropriété immatriculée, construite > 15 ans, ≥ 75 % de tantièmes habitations principales. (3) MaPrimeAdapt': aide pour travaux d'adaptation du logement aux personnes âgées ou handicapées à revenus modestes. Service public France Rénov': france-renov.gouv.fr / 0 808 800 700.
- Conditions : selon les revenus du ménage pour MPR individuelle | copropriété immatriculée + > 15 ans + 75 % habitations principales pour MPR Copropriété

### TRM-014 | obligation
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 1418 (declaration d'occupation des locaux d'habitation) ; BOI-IF-AUT
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 54-55
- Règle : Tous les propriétaires de biens immobiliers à usage d'habitation doivent déclarer chaque année, avant le 1er juillet, sur impots.gouv.fr, la nature d'occupation de chaque bien: résidence principale/secondaire du propriétaire, bien mis en location (avec identité du locataire), bien mis à disposition gratuitement, ou bien vacant. Cette déclaration permet à l'administration de calculer la taxe d'habitation, la taxe sur les logements vacants, etc. Nouveauté 2025: les contribuables qui louent ou occupent gratuitement des locaux meublés non utilisés en résidence principale doivent également indiquer l'adresse et les éléments d'identification du bien dans leur déclaration de revenus.
- Seuils : `{"delai_declaration_avant_juillet": 1}`

### TRM-015 | condition
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150 U, II-7 et 8 (exoneration PV cession logement social) ; BOI-RFPI-PVI-10-40-100
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 70-70
- Règle : Les plus-values immobilières résultant d'une vente de biens immobiliers en vue de la réalisation de logements sociaux sont exonérées d'impôt sur le revenu (et de prélèvements sociaux). Condition temporelle: la vente doit être réalisée avant le 31 décembre 2025 et être consentie à un organisme en charge du logement social ou à des tiers privés s'engageant à construire du logement social.
- Conditions : vente avant 31 décembre 2025 | acheteur: organisme logement social ou tiers privé s'engageant à construire du logement social
- Seuils : `{"date_limite_2025": "31/12/2025"}`

### TRM-016 | règle
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : CGI art. 14 A et 29 (revenus fonciers SCPI) ; art. 150 UB ; BOI-RFPI-CHAMP-30
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 70-70
- Règle : Parts de SCPI: les loyers perçus par la SCPI et redistribués aux porteurs de parts sont soumis à l'impôt sur le revenu dans la catégorie des REVENUS FONCIERS (et non BIC), même si les biens sont des immeubles commerciaux. Ces revenus sont soumis aux prélèvements sociaux de 17,2 %. Les parts de SCPI sont INCLUSES dans l'assiette de l'IFI (contrairement aux SIIC cotées si détention < 5 %). Les plus-values de cession de parts relèvent du régime des plus-values immobilières (abattements pour durée de détention, IR 19 % + PS 17,2 %).
- Taux : `{"PS": 17.2, "PV_IR": 19, "PV_PS": 17.2}`
- Exceptions : OPCI (Organisme de Placement Collectif Immobilier): alternative aux SCPI avec revenus imposés en BIC si OPCI de type LMNP

### TRM-017 | définition
- Module : M12
- Statut : `candidate_to_validate`
- Ancre : a_verifier
- source_ingest : 2019-11-REVUE-PHARMA-GUIDE-PATRIMOINE.pdf, p. 1-1
- Règle : OBO (Owner Buy-Out / vente à soi-même): opération permettant à un dirigeant de dégager du capital à titre personnel en vendant son entreprise (pharmacie, cabinet libéral) à une holding SPFPL qu'il contrôle. Effets: (1) le dirigeant perçoit un prix de vente exonéré ou taxé à 12,8 % (PFU); (2) la holding emprunte pour payer le prix et rembourse le crédit avec les dividendes de l'entreprise (effet de levier); (3) le dirigeant anticipe l'organisation de sa retraite tout en maintenant le contrôle. Utilisé notamment lors de la cession de pharmacies d'officine avant retraite.
- Exceptions : Risque de requalification en abus de droit si opération sans substance économique | Frais importants: notaire, avocat, banque

### RISK-004 | risque
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 206, 2 et art. 219 (IS) ; art. 150 VC a contrario (perte abattement) ; BOI-IS-BASE-20-10
- source_ingest : M6_gestion_patrimoniale.jsonl
- Règle : RISQUE: Option IS irrévocable d'une SCI puis cession des parts → perte de l'abattement pour durée de détention sur PV immobilières (abattement qui exonère après 22 ans d'IR et 30 ans de PS). En IS, la PV de cession est imposée à l'IS 25 % quel que soit le nombre d'années de détention. Erreur fréquente lors d'une structuration patrimoniale à long terme.

### RISK-008 | risque
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 787 B (engagements de conservation Pacte Dutreil) ; BOI-ENR-DMTG-10-20-40-20
- source_ingest : 00788-bp-guidefiscaliteprofessionsliberales-210x240-042025-vf.pdf, p. 83-84
- Règle : RISQUE: Non-respect des engagements de conservation dans un Pacte Dutreil → remise en cause de l'exonération de 75 % et rappel des droits avec pénalités et intérêts de retard. Les engagements collectifs et individuels de conservation doivent être strictement respectés sur toute leur durée. RISQUE annexe: cession de l'entreprise pendant la période d'engagement → rupture du pacte, sauf exceptions prévues (transmission dans le cadre familial sous conditions).
- Exceptions : Transmission dans le cadre familial sous conditions peut préserver le pacte

## location_meublee_lmnp_lmp

### LMN-001 | définition
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 35, I-5 bis (location meublee = BIC) ; BOI-BIC-CHAMP-40
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 4-6
- Règle : La location meublée est fiscalement une activité commerciale relevant des BIC (art. 35 CGI), même si juridiquement c'est une activité civile. Elle se distingue de la location nue par le fait que le logement est muni du mobilier nécessaire à la vie quotidienne.

### LMN-002 | obligation
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : Decret 2015-981 du 31/07/2015 (liste du mobilier) ; loi 89-462 art. 25-4
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 6-7
- Règle : Liste des meubles obligatoires en location meublée à usage de résidence principale (décret 2015-981): literie avec couette/couverture, occultation des fenêtres chambre, plaques de cuisson, four/micro-ondes, réfrigérateur+congélateur (ou frigo avec compartiment ≤ -6°), vaisselle, ustensiles cuisine, table et sièges, étagères de rangement, luminaires, matériel d'entretien ménager.
- Conditions : résidence principale uniquement
- Exceptions : Locations saisonnières: liste non réglementée, logement doit être habitable

### LMN-003 | condition
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 155, IV (statut LMP) ; loi 2019-1479 du 28/12/2019 (suppression RCS) ; BOI-BIC-CHAMP-40-10
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 12-12
- Règle : Le statut LMP (Loueur Meublé Professionnel) requiert DEUX conditions cumulatives: (1) recettes annuelles de location de l'ensemble du foyer fiscal > 23 000 €; (2) ces recettes excèdent les autres revenus professionnels du foyer fiscal (traitements et salaires nets, BIC autres que LM, BNC, BA, rémunérations art. 62 CGI). L'inscription au RCS n'est plus requise depuis le 1er janvier 2020.
- Conditions : appréciation à l'année civile | inscription RCS abrogée depuis loi 2019-1479 du 28/12/2019
- Seuils : `{"recettes_min": 23000}`

### LMN-004 | condition
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 155, IV (LMNP a defaut des conditions LMP) ; BOI-BIC-CHAMP-40-10
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 13-15
- Règle : Le statut LMNP (Loueur Meublé Non Professionnel) s'applique dès que l'une des deux conditions LMP n'est pas remplie: recettes ≤ 23 000 € OU recettes ≤ revenus professionnels du foyer fiscal. Le changement de qualité LMP/LMNP n'entraîne pas de cessation d'activité fiscale.
- Seuils : `{"recettes_max": 23000}`

### LMN-005 | seuil
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 50-0 (micro-BIC) ; loi 2024-322 (loi Le Meur) ; BOI-BIC-DECLA-10-10 (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042159220/) (verifie le 2026-06-05)
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 28-29
- Règle : Seuils micro-BIC pour revenus 2025 (déclarés 2026) selon type: meublés tourisme CLASSÉS + chambres d'hôtes + gîtes classés: CA < 77 700 € → abattement 50%; meublés tourisme NON classés: CA < 15 000 € → abattement 30%; autres locations (longue durée, résidence principale, EHPAD, résidences services): CA < 77 700 € → abattement 50%. Abattement minimum: 305 €.
- Seuils : `{"tourisme_classe_CA": 77700, "tourisme_classe_abattement_pct": 50, "tourisme_non_classe_CA": 15000, "tourisme_non_classe_abattement_pct": 30, "autres_CA": 77700, "autres_abattement_pct": 50, "abattement_minimum": 305}`
- Exceptions : Revenus 2024 déclarés 2025: anciens seuils applicables (188700€/71% classés; 77700€/50% non classés) selon loi Le Meur 2024 | Indivisions et sociétés de personnes: exclues du micro-BIC

### LMN-006 | obligation
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 50-0 (obligations micro-BIC) ; art. 158, 7 ; BOI-BIC-DECLA-10-10
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 27-28
- Règle : En micro-BIC: (1) tenir un livre-journal des recettes; (2) tenir un registre des achats; (3) déclarer les loyers sur 2042-C PRO; (4) pas de liasse fiscale; (5) pas de réduction d'impôt pour frais de comptabilité/OGA (RIOGA supprimée pour revenus 2025, loi de finances 2025 art. 11).

### LMN-007 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 53 A et 302 septies A bis (regimes reels) ; BOI-BIC-DECLA-30
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 29-31
- Règle : Au régime réel BIC: comptabilité BIC complète obligatoire (FEC compatible); déclarations 2031 + 2033 pour réel simplifié (CA meublé tourisme classé: 188 700 €-840 000 € en 2024, 77 700 €-840 000 € en 2025; autres: 77 700 €-254 000 €) ou 2031 + 2050 pour réel normal (CA meublé tourisme classé > 840 000 €; autres > 254 000 €). Option exercée avant la date limite de déclaration des revenus de N-1, valable 1 an, tacite reconduction.
- Seuils : `{"reel_simplifie_max_tourisme_classe_2025": 840000, "reel_normal_min_tourisme_classe_2025": 840000, "reel_simplifie_max_autres": 254000, "reel_normal_min_autres": 254000}`

### LMN-008 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : PCG art. 212-1 et CGI art. 39, 1-2 (charges vs immobilisations) ; BOI-BIC-CHG-20-10-20
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 31-32
- Règle : Seuil de comptabilisation: montant unitaire ≤ 500 € HT → charge déductible immédiatement; > 500 € HT → immobilisation obligatoire. Exception: le premier achat de mobilier meublant est TOUJOURS immobilisé quel que soit le montant. Les factures d'achat de meubles ou travaux antérieures à la date de début d'activité ne peuvent pas être comptabilisées.
- Seuils : `{"seuil_immobilisation_HT": 500}`
- Exceptions : Premier mobilier meublant: toujours immobilisation | Erreur de comptabilisation: un amortissement non déduit à la date limite est définitivement perdu

### LMN-009 | option
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 38 quinquies (frais d'acquisition des immobilisations, option) ; art. 39, 1 ; BOI-BIC-CHG-20-20-10
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 32-33
- Règle : Les frais d'acquisition (droits de mutation, honoraires notaire, frais actes, commissions) peuvent au choix: (A) être immobilisés en ajout au coût d'acquisition, ou (B) être déduits immédiatement en charges. Option irrévocable dès le 1er bien et s'applique à toutes les immobilisations ultérieures.

### LMN-010 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39, 1-2 (le terrain n'est pas amortissable) ; PCG art. 214-9 ; BOI-BIC-AMT-10-30
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 35-36
- Règle : Le terrain est obligatoirement inscrit au bilan comme composant de l'immeuble (même appartement). Il N'EST PAS amortissable. Valorisation par ordre de priorité: (1) comparaison terrains nus voisins récents, (2) coût de reconstruction vétusté déduite, (3) taux moyens comparatifs. La valeur du terrain est celle à la date d'entrée au bilan.

### LMN-011 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39, 1-2 (amortissements) ; PCG art. 214-9 et BOI-ANNX-000115 (amortissement par composants)
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 36-37
- Règle : Amortissement obligatoire par composants (BOI-ANNX-000115): terrain (non amortissable); gros œuvre (40-50% valeur bien, >50 ans, max 2%/an); étanchéité/façade/toiture/menuiserie ext (5-20%, 20-50 ans, 2-5%/an); installations générales/techniques (20-30%, 15-30 ans, 3-7%/an); agencement (20-25%, 5-15 ans, 7-20%/an). Mobilier: 5 ans linéaire.
- Taux : `{"gros_oeuvre_max_pct_an": 2, "etancheite_min_pct_an": 2, "etancheite_max_pct_an": 5, "installations_min_pct_an": 3, "installations_max_pct_an": 7, "agencement_min_pct_an": 7, "agencement_max_pct_an": 20, "mobilier_duree_ans": 5}`
- Exceptions : Taux indicatifs à adapter selon état réel du bien

### LMN-012 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 C, II (limitation des amortissements LMNP) ; BOI-BIC-AMT-20-40-10
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 44-45
- Règle : L'art. 39-C CGI limite la déduction des amortissements: Amortissement déductible ≤ Loyers acquis - Charges hors amortissements liées au bien. Les amortissements excédentaires sont DIFFÉRÉS (non perdus): stockés et déductibles des exercices futurs bénéficiaires dans la même limite. En cas de pluralité de biens: appréciation globale, répartition proportionnelle des ARD.

### LMN-013 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39, 1 (charges deductibles BIC) ; BOI-BIC-CHG
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 34-35
- Règle : Sont déductibles au réel BIC: charges de copropriété, entretien/petites réparations, frais d'agence, honoraires comptabilité (1/3 si RIOGA applicable), assurances PNO/loyers impayés, intérêts d'emprunts + frais de dossier, taxe foncière, CFE, électricité/eau/téléphone/internet. Les amendes ne sont pas déductibles (réintégration 2033-B rubrique 330).
- Conditions : charges nécessaires à l'exploitation | charges justifiées par factures
- Exceptions : Usage privé partiel: extourner les charges au prorata (LMP) ou inclure valeur locative dans les produits (LMNP)

### LMN-014 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 156, I-1 bis (deficits LMP imputables sur le revenu global) ; BOI-BIC-DEF-20-10
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 27-28
- Règle : En LMP: déficits imputables sur le revenu global du foyer fiscal SANS limitation de montant. Si revenu global insuffisant: déficit global reportable sur les 6 années suivantes.
- Conditions : statut LMP l'année de réalisation du déficit

### LMN-015 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 156, I-1 ter (deficits LMNP reportables sur BIC LMNP) ; BOI-BIC-DEF-20-20
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 45-47
- Règle : En LMNP: déficits reportables EXCLUSIVEMENT sur les revenus de location meublée non professionnelle des 10 années suivantes. Impossible de les imputer sur d'autres revenus (salaires, BNC, BIC professionnels, etc.). Suivi cases 5GA à 5GJ de la 2042-C PRO.
- Conditions : statut LMNP
- Exceptions : Passage LMNP → LMP: déficits LMNP ni imputables sur revenu global LMP ni reportables sur bénéfices LMP

### LMN-016 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 261 D, 4 (exoneration TVA location meublee ; para-hotellerie) ; BOI-TVA-CHAMP-30-10-50
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 49-49
- Règle : La location meublée est EXONÉRÉE de TVA de principe (art. 261-D-4° CGI), qu'elle soit occasionnelle, permanente ou saisonnière. Exception principale: para-hôtellerie (location < 30 nuits + ≥ 3 prestations parmi: petit-déjeuner, nettoyage régulier, linge de maison, accueil) → soumise à TVA de plein droit.
- Taux : `{"hebergement": 10, "parking": 20, "EHPAD_maison_retraite": 5.5, "Corse_Martinique_Guadeloupe_Reunion": 2.1}`
- Exceptions : Para-hôtelière soumise à TVA | Résidences services avec ≥ 3 prestations | Caravanes/mobil-homes: TVA à 20% (10% si terrain camping classé)

### LMN-017 | seuil
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 293 B (franchise en base de TVA) ; directive UE 2020/285 ; BOI-TVA-DECLA-40-10
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 50-51
- Règle : Franchise en base TVA pour locations meublées soumises à TVA (depuis 1er jan 2025 selon directive UE 2020/285): seuil de base 85 000 €, seuil majoré 93 500 €. Franchise cesse si CA dépasse 93 500 € en cours d'année (dès le 1er jour du mois de dépassement). Mention obligatoire sur factures: 'TVA non applicable - art. 293 B du CGI'. Réforme à 25 000 € suspendue jusqu'au 1er juin 2025.
- Seuils : `{"franchise_base": 85000, "franchise_majoree": 93500}`
- Exceptions : Option pour le paiement de la TVA: valable 2 ans, renouvelable tacitement; option par écrit au SIE; effet au 1er jour du mois de l'option

### LMN-018 | obligation
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 1447 et s. (CFE) et art. 1586 ter (CVAE) ; BOI-IF-CFE
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 56-57
- Règle : CFE: due par tous les loueurs en meublé (LMP et LMNP); exonération la 1ère année; exonération si CA ≤ 5 000 €; base réduite de moitié la 2ème année; déclaration initiale 1447-C-SD avant le 31/12 de l'année de création. CVAE: due uniquement si CA > 500 000 €; taux plafonnement CET: 1,438% VA pour 2025; suppression prévue en 2030.
- Seuils : `{"CFE_exoneration_CA": 5000, "CVAE_CA_min": 500000}`
- Taux : `{"plafonnement_CET_2025": 1.438}`
- Exceptions : Location occasionnelle de partie résidence principale: exonération CFE | Sous-location d'une partie du domicile à prix raisonnable: exonération CFE

### LMN-019 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 1407 et 1414 (taxe d'habitation, suppression RP) ; BOI-IF-TH
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 57-57
- Règle : Taxe d'habitation résidence principale supprimée depuis 1er janvier 2023. En location saisonnière/courte durée: bien considéré résidence secondaire du propriétaire → taxe d'habitation maintenue. En location longue durée résidence principale du locataire: taxe due par le locataire. Obligation déclarative annuelle avant 1er juillet pour tous les propriétaires.

### LMN-020 | condition
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CSS art. L.611-1 et art. L.613-7 (affiliation SSI loueurs courte duree)
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 60-62
- Règle : Assujettissement aux cotisations sociales (SSI): (1) recettes de location de COURTE DURÉE > 23 000 €/an, OU (2) statut LMP (recettes > 23 000 € ET supérieures aux revenus professionnels du foyer). En dessous de ces seuils: prélèvements sociaux de 17,2% uniquement (pas de droits retraite/assurance maladie). Exception: propriétaires ayant délégué la gestion à un professionnel de l'immobilier → pas d'affiliation même si > 23 000 €.
- Seuils : `{"cotisations_sociales_seuil_courte_duree": 23000}`
- Taux : `{"prelevements_sociaux_sous_seuil": 17.2}`
- Exceptions : Gestion déléguée à un professionnel: prélèvements sociaux uniquement (RM Pellois, JO 10/07/2018)

### LMN-021 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CSS art. L.131-6 (assiette cotisations) et art. L.613-7
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 63-66
- Règle : Abattements sur recettes pour calcul des cotisations sociales: 60% pour location courte durée standard; 87% pour meublé de tourisme classé. 1ère année d'affiliation: assiette = (recettes - 23 000 €) × (1 - abattement%). Années suivantes: assiette = recettes × (1 - abattement%). Statuts possibles: régime général (salariés, si CA ≤ 77 700 €), auto-entrepreneur (CA ≤ 77 700 € / 188 700 €), travailleur indépendant.
- Seuils : `{"auto_entrepreneur_max_non_classe": 77700, "auto_entrepreneur_max_classe": 188700}`
- Taux : `{"abattement_courte_duree": 60, "abattement_tourisme_classe": 87}`

### LMN-022 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150 U et s. (PV particuliers) ; art. 150 VB, II (reintegration amortissements LMNP, LDF 2025 art. 84) ; BOI-RFPI-PVI (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046860944/) (verifie le 2026-06-05)
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 68-69
- Règle : En LMNP (cession sous statut LMNP): régime des plus-values des particuliers. À compter du 1er janvier 2025: PV = Prix vente - (Prix acquisition - Amortissements déduits pendant la détention). Avant 2025: PV = Prix vente - Prix acquisition. Imposition: 19% IR + 17,2% PS, après abattements pour durée de détention.
- Taux : `{"IR": 19, "PS": 17.2, "taxe_supplement_seuil_PV": 50000}`
- Exceptions : Résidences jeunes en formation/apprentissage: exception au régime des amortissements 2025

### LMN-023 | seuil
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150 VC (abattements duree de detention) et art. 200 B ; CSS art. L.136-7
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 70-72
- Règle : Abattements IR et PS pour durée de détention (LMNP, régime particuliers): 0-5 ans: 0% IR et PS; 6ème-21ème année: 6%/an IR, 1,65%/an PS; 22ème année: 4% IR, 1,6% PS; au-delà 22 ans: exonération IR (taux de base 19%); 23ème-30ème année: 9%/an PS; au-delà 30 ans: exonération totale IR+PS. Taxe supplémentaire si PV imposable > 50 000 €: de 2 à 6%.
- Seuils : `{"exoneration_IR_annees": 22, "exoneration_totale_annees": 30}`
- Taux : `{"IR_taux_base": 19, "PS_taux_base": 17.2}`

### LMN-024 | règle
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 duodecies a 39 quindecies (PV professionnelles LMP) ; BOI-BIC-PVMV
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 72-73
- Règle : En LMP (cession sous statut LMP): régime des PV professionnelles. PV = Prix cession - VNC (VNC = valeur d'origine - amortissements DÉDUITS, les ARD de l'art. 39-C majorent la VNC). Qualification: < 2 ans → PV court terme; > 2 ans → PV CT dans la limite des amortissements déduits + PV LT au-delà. PV CT: imposition au barème progressif IR. PV LT: 12,8% IR + 17,2% PS.
- Conditions : statut LMP l'année de cession
- Seuils : `{"duree_CT_ans": 2}`
- Taux : `{"PV_LT_IR": 12.8, "PV_LT_PS": 17.2}`

### LMN-025 | condition
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 151 septies, 151 septies A, 151 septies B et 238 quindecies (exonerations PV pro) ; BOI-BIC-PVMV-40
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 73-73
- Règle : Exonérations PV professionnelles LMP (activité ≥ 5 ans): Art. 151 septies: totale si recettes moy. N-1/N-2 < 90 000 € (250 000 € tourisme classé), partielle entre 90 000 € et 126 000 € (250 000-300 000 € classé). Art. 151 septies B: abattement 10%/an sur PV LT immobilière au-delà de 5 ans (exonération totale à 15 ans). Art. 238 quindecies: cession < 500 000 € → totale, entre 500 000 € et 1 000 000 € → partielle (exclusion: immeubles). Art. 151 septies A: départ retraite dans 2 ans avant/après cession → totale (exclusion: immeubles).
- Conditions : activité exercée ≥ 5 ans | exercice à titre professionnel l'année de cession
- Seuils : `{"art151septies_totale": 90000, "art151septies_partielle_max": 126000, "art151septies_tourisme_totale": 250000, "art151septies_tourisme_partielle_max": 300000, "art238quindecies_totale": 500000, "art238quindecies_partielle_max": 1000000}`
- Taux : `{"art151septiesB_abattement_pct_an": 10}`
- Exceptions : PV CT exonérées par 151 septies: restent soumises aux cotisations sociales | PV LT exonérées: pas de cotisations sociales

### LMN-026 | obligation
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : C. com. art. R.123-32 (immatriculation, guichet unique INPI) ; CGI art. 286 (declaration d'existence) ; art. 1447 (CFE)
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 15-16
- Règle : Déclaration d'activité via guichet unique INPI (inpi.fr) dans les 15 jours suivant le début d'activité. Date de début = date de la 1ère dépense (achat meuble, signature notaire). Résultat: SIRET (code APE 6820-A), ROF fiscal, imprimé 1447-C CFE. Créer aussi un espace professionnel sur impots.gouv.
- Seuils : `{"delai_declaration_jours": 15}`
- Exceptions : Pas de sanction si immatriculation tardive mais démarche indispensable

### LMN-027 | obligation
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : LPF art. L.47 A, I et art. A.47 A-1 (FEC) ; CGI art. 1729 D (amende)
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 26-27
- Règle : Toute comptabilité informatisée doit permettre la production d'un FEC conforme (art. A47 A-1 LPF). Un tableur Excel ne satisfait pas à cette exigence. Sanction en cas de défaut: amende de 5 000 € par exercice contrôlé ou 10% des droits rappelés si montant supérieur.
- Conditions : comptabilité informatisée
- Seuils : `{"amende_FEC_euros": 5000, "amende_FEC_pct_droits": 10}`

### LMN-028 | obligation
- Module : M5
- Statut : `candidate_to_validate`
- Ancre : CGI art. 201 (declaration en cas de cessation) ; BOI-BIC-CESS-10
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 66-68
- Règle : Déclaration de cessation dans les 30 jours sur entreprendre.service-public.fr. Au réel: dernière 2031 dans les 60 jours après cessation. Au micro: déclaration des loyers lors de la campagne revenus de l'année suivante. CFE: demande de réduction au prorata possible (avant 31/12 N+1).
- Seuils : `{"delai_declaration_cessation_jours": 30, "delai_2031_jours": 60}`

### LMP-001 | règle
- Module : M5bis
- Statut : `candidate_to_validate`
- Ancre : CGI art. 35 et art. 8 (imposition de l'usufruitier en BIC) ; BOI-BIC-CHAMP-40
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 80-82
- Règle : En cas de démembrement de propriété sur un bien loué meublé: L'USUFRUITIER est imposable dans la catégorie des BIC (et non les revenus fonciers) à raison des revenus de la location meublée. Il peut amortir la valeur de l'usufruit (et non la pleine propriété). Il supporte les charges d'entretien et d'amélioration, la taxe foncière, la taxe d'habitation éventuelle. LE NU-PROPRIÉTAIRE ne perçoit aucun revenu, n'est pas imposable et ne peut déduire aucune charge (même s'il inscrit la nue-propriété à l'actif d'une activité BIC).

### LMP-002 | règle
- Module : M5bis
- Statut : `candidate_to_validate`
- Ancre : CGI art. 669 (valeur de l'usufruit) et art. 39, 1-2 (amortissement) ; CE 24/04/2019 n419912
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 80-80
- Règle : L'usufruitier qui loue le bien meublé peut amortir la valeur de l'usufruit (et non la pleine propriété). La valeur de l'usufruit est déterminée selon le barème de l'article 669 du CGI (fonction de l'âge de l'usufruitier). La durée d'amortissement = durée du démembrement (si temporaire) ou espérance de vie résiduelle selon données INSEE (si viager). En usufruit, il n'y a pas de décomposition par composants: toute la valeur de l'usufruit est amortie en une seule ligne. La valeur retenue est celle à la date de début de la location (âge actuel de l'usufruitier, pas l'âge au jour de la donation si antérieure).
- Conditions : usufruitier = locateur du bien meublé
- Exceptions : CE, Arrêt n°419912 du 24 avril 2019: amortissement de l'usufruit viager confirmé | Compte comptable: compte 207 (valeur de l'usufruit)

### LMP-003 | règle
- Module : M5bis
- Statut : `candidate_to_validate`
- Ancre : C. civ. art. 605 et 606 (repartition des travaux usufruit/nue-propriete) ; BOI-RFPI-BASE-20-30
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 80-82
- Règle : Répartition des travaux en démembrement: JURIDIQUEMENT: nu-propriétaire = grosses réparations (art. 606 Code civil); usufruitier = entretien et améliorations (art. 605). FISCALEMENT: la distinction juridique ne s'applique pas — c'est la personne qui a payé et supporté définitivement les travaux qui peut les déduire, quelle que soit leur nature.

### LMP-004 | règle
- Module : M5bis
- Statut : `candidate_to_validate`
- Ancre : CGI art. 35 bis (exoneration location d'une partie de la RP) ; BOI-BIC-CHAMP-40-20
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 82-83
- Règle : La résidence principale peut être louée en meublé sous conditions d'exonération d'impôt: (1) les pièces louées font partie de la RP du bailleur ET constituent la résidence principale du locataire (ou résidence temporaire d'un salarié saisonnier); (2) le prix de location reste dans des limites raisonnables (plafond 2024: 213 €/m²/an en Île-de-France, 157 €/m²/an en province). Si loyer > plafond: totalité du loyer imposable. Limitation: 120 nuits/an maximum pour une location touristique de RP (loi ELAN); communes en zone tendue peuvent réduire à 90 nuits par délibération.
- Conditions : pièces louées = RP du bailleur | locataire = sa RP (ou résidence temporaire salarié saisonnier) | loyer ≤ plafond annuel
- Seuils : `{"plafond_IDF_2024_m2_an": 213, "plafond_province_2024_m2_an": 157, "limite_nuits_an": 120}`
- Exceptions : Exonération applicable jusqu'au 31/12/2026 (art. 38 LDF 2024) | Location touristique hors RP: plafond 120 nuits sans exonération de loyers | Revenus < 760 €/an pour location occasionnelle de pièces isolées: exonération spécifique

### LMP-005 | règle
- Module : M5bis
- Statut : `candidate_to_validate`
- Péremption : Pinel : fermé aux nouvelles acquisitions depuis le 01/01/2025 (seuls les investissements antérieurs continuent à produire leurs réductions). Censi-Bouvard : fermé aux nouvelles acquisitions depuis le 01/01/2023.
- Ancre : CGI art. 199 sexvicies (Censi-Bouvard, extinction 31/12/2022) ; BOI-IR-RICI-220
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 83-84
- Règle : Le dispositif Censi-Bouvard permettait une réduction d'impôt pour les LMNP ayant acquis un logement neuf ou en VEFA entre le 1er janvier 2013 et le 31 décembre 2022 dans certaines résidences de services. Certains contribuables peuvent donc encore en bénéficier (sur les investissements encore en cours d'application). Logements éligibles: résidences avec services pour étudiants; résidences avec services agréées pour personnes âgées ou handicapées; résidences d'accueil et de soins agréées (EHPAD). Résidences de tourisme classées: éligibles uniquement jusqu'au 31/12/2016.
- Conditions : acquisition neuf ou VEFA entre 01/01/2013 et 31/12/2022 | résidences de services éligibles
- Exceptions : Résidences de tourisme classées: éligibilité terminée au 31/12/2016 | Dispositif terminé pour les nouvelles acquisitions depuis 01/01/2023

### LMP-006 | règle
- Module : M5bis
- Statut : `candidate_to_validate`
- Péremption : Pinel : fermé aux nouvelles acquisitions depuis le 01/01/2025 (seuls les investissements antérieurs continuent à produire leurs réductions). Censi-Bouvard : fermé aux nouvelles acquisitions depuis le 01/01/2023.
- Ancre : CGI art. 199 sexvicies, II (taux et plafond) ; BOI-IR-RICI-220-30
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 84-85
- Règle : Réduction d'impôt Censi-Bouvard: taux 11 % du prix de revient HT des logements, réparti sur 9 ans (réduction de 1/9ème par an). Plafond d'investissement: 300 000 € (quel que soit le nombre de logements). Réduction d'impôt maximale: 33 000 € sur 9 ans (soit 3 667 €/an). La réduction est reportable sur les 6 années suivantes si elle dépasse l'impôt dû. Cumul avec l'amortissement: si le contribuable a bénéficié de la réduction Censi-Bouvard, il ne peut pas amortir le bien immobilier lui-même (il peut en revanche amortir le mobilier).
- Seuils : `{"plafond_investissement": 300000, "reduction_totale_max": 33000, "reduction_annuelle_max": 3667}`
- Taux : `{"taux_reduction_pct": 11, "duree_ans": 9}`
- Exceptions : L'amortissement du mobilier reste possible même en cas de réduction Censi-Bouvard

### LMP-007 | règle
- Module : M5bis
- Statut : `candidate_to_validate`
- Ancre : CGI art. 35, 5 bis (location meublee imposee en BIC) ; art. 14 (revenus fonciers location nue) ; BOI-BIC-CHAMP-40-20 (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048103564/) (verifie le 2026-06-05)
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 78-80
- Règle : Passage d'une location nue (revenus fonciers) à une location meublée (BIC): deux régimes déclaratifs distincts s'appliquent successivement la même année. La partie de l'année en location nue est déclarée en revenus fonciers (2044 ou micro-foncier). La partie en location meublée est déclarée en BIC (2031/2033 ou micro 2042 C PRO). Les charges restent déductibles sur chaque période selon les règles propres à chaque régime. En cas de passage au réel meublé: inscription du bien au bilan à sa valeur de marché au jour du changement d'usage.
- Exceptions : Les déficits fonciers antérieurs ne peuvent pas être imputés sur les revenus BIC futurs

### LMP-008 | règle
- Module : M5bis
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150 U et s. (PV particuliers, donation LMNP) ; RM Frassa Senat 28/05/2015 n14933 ; art. 39 duodecies (LMP)
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 78-80
- Règle : Donation d'un bien loué en LMNP: La donation d'un bien immobilier faisant l'objet d'une location meublée exercée à titre NON PROFESSIONNEL (LMNP) ne constitue PAS le fait générateur d'une plus-value imposable (seules les mutations à titre onéreux déclenchent la PV en régime particuliers). En revanche, la donation d'un bien LMP constitue le fait générateur d'une PV professionnelle imposable. (RM Frassa, JO Sénat 28/05/2015, question n°14933).
- Exceptions : LMNP: donation = pas de PV imposable | LMP: donation = fait générateur de PV professionnelle

### FORM-001 | formule
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 C, II (amortissements differes ARD) ; BOI-BIC-AMT-20-40-10
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 41-44
- Règle : Amortissement déductible (art. 39-C) = MAX(0 ; Loyers acquis − Charges hors amortissements afférentes au bien). Amortissements différés (ARD) = Amortissements comptabilisés − Amortissements déductibles. Accumulation ARD: Solde N = Solde N-1 + ARD N − Imputations N. Imputation possible si exercice bénéficiaire dans la même limite (loyers − charges hors amort ≥ 0).
- Conditions : réel BIC location meublée | art. 39-C CGI
- Exceptions : En cas de vente LMNP: ARD définitivement perdus | En cas de vente LMP: ARD majorent la VNC

### FORM-002 | formule
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 150 VB, II (reintegration amortissements LMNP, LDF 2025) et art. 150 V/VC ; BOI-RFPI-PVI
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 69-70
- Règle : PV brute LMNP (depuis 2025) = Prix cession − (Prix acquisition − Amortissements déduits pendant la détention). Prix acquisition majoré: + frais d'acquisition réels OU + 7,5 % forfait si > 5 ans; + travaux réels OU + 15 % forfait si > 5 ans. PV nette imposable IR = PV brute × (1 − Abattement IR durée détention). PV nette imposable PS = PV brute × (1 − Abattement PS durée détention). IR = PV nette IR × 19 %. PS = PV nette PS × 17,2 %. Taxe supplémentaire = f(PV nette IR) si > 50 000 €.
- Conditions : statut LMNP à la date de cession | cession depuis 1er janvier 2025
- Seuils : `{"seuil_taxe_supplementaire": 50000}`
- Taux : `{"IR_pct": 19, "PS_pct": 17.2}`
- Exceptions : Avant 2025: PV brute = Prix cession − Prix acquisition (amortissements non réintégrés) | Résidences étudiantes/apprentissage: exception au régime de réintégration des amortissements

### RISK-001 | risque
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 39 C ; BOI-BIC-AMT-20-40-10 (amortissement non deduit perdu)
- source_ingest : GUIDE_FISCAL_LOCATION_MEUBLEE_2025.pdf, p. 26-26
- Règle : RISQUE: Oubli de comptabiliser un amortissement dans la déclaration 2031 avant la date limite → amortissement définitivement perdu fiscalement (art. 39-C). Ne peut pas être rattrapé ultérieurement, même si l'amortissement est régularisé comptablement. L'amortissement non déduit à temps ne peut pas être inscrit dans le stock d'ARD.

### RISK-002 | risque
- Module : FORM
- Statut : `candidate_to_validate`
- Ancre : CGI art. 206, 2 (IS de plein droit si location meublee par SCI) ; art. 239 ; BOI-IS-CHAMP-10-30
- source_ingest : M6_gestion_patrimoniale.jsonl
- Règle : RISQUE: SCI optant pour la location meublée → soumise à l'IS de plein droit (activité commerciale). Cette option IS est IRRÉVOCABLE. La SCI perd: (1) l'abattement pour durée de détention sur les PV immobilières; (2) la possibilité de retourner à l'IR. Les dividendes distribués sont ensuite imposés au PFU 30 % (double imposition IS + PFU). Piège fréquent lors de la mise en location meublée d'un bien détenu en SCI IR.
