# Protocole de vérification d'ancres légales (sourcing)

Tu vérifies des règles fiscales françaises contre les textes officiels. Pour CHAQUE règle du lot :

1. Lis l'ancre légale citée et l'énoncé de la règle.
2. Si l'ancre principale est un article CGI présent dans le corpus local (liste dans articles_locaux.txt),
   extrais son texte OFFICIEL avec :
   python3 /home/user/comptable/.claude/skills/expert-comptable/scripts/lookup.py cgi "<numéro>"
   et compare l'énoncé de la règle au texte. Méthode = "cgi_local".
3. Sinon, vérifie par recherche web en te limitant aux sources officielles ou institutionnelles
   (legifrance.gouv.fr, bofip.impots.gouv.fr, service-public.fr, urssaf.fr, impots.gouv.fr).
   NB : l'accès direct aux sites .fr peut être bloqué — la recherche web (WebSearch) fonctionne et restitue
   le contenu des pages officielles. Méthode = "web".
4. Verdict par règle (SOIS CONSERVATEUR — en cas de doute : "inverifiable", jamais "confirmee" sans preuve) :
   - "confirmee" : l'énoncé correspond au texte officiel, l'ancre citée est la bonne.
   - "confirmee_ancre_corrigee" : énoncé exact mais ancre à préciser/corriger → donne "ancre_corrigee".
   - "nuancee" : énoncé globalement juste mais imprécis ou daté (ex. valeur millésime 2025 modifiée en 2026,
     condition manquante) → donne la nuance dans "evidence".
   - "erronee" : l'énoncé contredit le texte officiel → donne la correction et la preuve.
   - "inverifiable" : impossible à établir sur source officielle dans le temps imparti.
5. "evidence" : OBLIGATOIRE pour tout verdict ≠ inverifiable. Une phrase : la citation courte ou la référence
   précise (article + alinéa, ou intitulé BOFiP) qui fonde le verdict. Pas de paraphrase vague.

Contexte utile :
- Les barèmes du corpus sont calibrés millésime 2025 : une valeur 2025 exacte citée avec son contexte n'est PAS
  "erronee" ; si elle a changé en 2026 (ex. micro-BNC 77 700 → 83 600, PASS 47 100 → 48 060, CNAVPL 8,23 → 8,73),
  verdict "nuancee" avec la valeur 2026.
- Le référentiel local des chiffres vérifiés : python3 .../lookup.py referentiel --list (depuis /home/user/comptable).

SORTIE : écris UN fichier JSON (uniquement le tableau, rien d'autre) au chemin indiqué, format :
[{"id": "GFPL-XXX", "verdict": "confirmee", "methode": "cgi_local", "evidence": "...", "ancre_corrigee": null, "source_url": null}, ...]
Chaque règle du lot doit avoir exactement une entrée. Vérifie que ton JSON est valide avant de terminer.

## Addendum (lots « reste ») — ancres non fiscales
Beaucoup de règles de ces lots sont comptables ou patrimoniales : ancres PCG (règlement ANC n° 2014-03, consultable sur anc.gouv.fr / legifrance), Code de commerce (art. L.123-12 et s.), Code civil (successions, démembrement), Code des assurances (L.132-12 s.), Code monétaire et financier, CSS. Même exigence : vérifier l'énoncé contre le texte officiel (Légifrance en priorité), verdict conservateur avec preuve. Pour les formules financières (BFR, CAF, seuil de rentabilité — module FORM/M8) sans ancre légale possible : vérifier la cohérence mathématique et l'usage normalisé (définitions PCG/ANC si applicables) ; si c'est une convention de gestion sans texte, verdict "confirmee" admis avec evidence = définition de référence citée, sinon "inverifiable".
