# Chantier de sourcing en cours — lot final (206 regles, tous modules restants)

Etat au 2026-08-26 : le module M2 est entierement source (185/391 ancres verifiees,
commit 906e65e). Les 206 regles restantes sont decoupees en 8 lots (`reste_lot_0.json`
a `reste_lot_7.json`) ; la verification a ete interrompue par l'epuisement des credits
d'utilisation avant qu'aucun verdict ne soit ecrit.

## Pour reprendre (dans une session Claude Code sur ce depot)

Demander : « reprends le sourcing des lots restants » — ou manuellement :

1. Pour chaque lot i (0..7) : lancer un agent avec `protocole_sourcing.md` (verdicts
   conservateurs, preuve obligatoire, sources officielles uniquement) sur
   `sourcing/reste_lot_<i>.json`, sortie JSON `[{"id","verdict","methode","evidence",
   "ancre_corrigee","source_url"}]`.
2. Agreger, contre-verifier les `erronee` independamment, puis appliquer :
   - crosswalk 07 : `anchor_status: "sourced"` + `anchor_verified_le` + verdict/evidence
     (voir les entrees GFPL-* deja traitees comme modele) ;
   - 02_golden_rules : corrections datees pour les `erronee`, lignes « Precision (verif.
     source officielle AAAA-MM-JJ) » pour les `nuancee`, « Ancre precisee » pour les
     ancres corrigees ;
   - compteurs README / ROADMAP / index.html / SKILL.md, puis
     `python3 scripts/build_skill_package.py`, commit et push.

Ce dossier `sourcing/` peut etre supprime une fois les 391 ancres traitees.
