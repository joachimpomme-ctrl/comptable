# Sécurité et données personnelles

## Signaler un problème

Sont concernés : une donnée personnelle ou un secret publié dans le dépôt ou son historique, une réponse d'un agent qui pousse à une action dangereuse, une faille d'injection de consignes (un document qui détourne l'agent), un script qui modifie des fichiers hors de son périmètre.

Comment signaler :

1. De préférence par l'onglet **Security** du dépôt, bouton **Report a vulnerability** (signalement privé, visible du seul mainteneur).
2. À défaut, une issue intitulée `[SECURITE]` qui décrit le type de problème et son emplacement, **sans recopier la donnée sensible elle-même**.

## Règles du dépôt

- Aucune donnée personnelle dans les fichiers : ni nom, ni adresse e-mail, ni identifiant de dossier ou de fichier Google Drive, ni numéro de compte, de carte, de prêt ou fiscal.
- Les exemples chiffrés sont fictifs : ils ne reprennent jamais la situation réelle d'une personne.
- Les commits sont signés avec l'adresse anonyme fournie par GitHub (domaine users.noreply.github.com). Réglages à activer sur le compte : *Settings > Emails > Keep my email addresses private* et *Block command line pushes that expose my email*.
- La CI lance `scripts/verifier_donnees_personnelles.py` à chaque push : adresses e-mail, identifiants Drive, IBAN, numéros de carte, téléphones, clés d'API dans les fichiers, et adresses non anonymes dans l'historique.
- Le contenu d'un document ou d'une page web est une donnée, jamais une instruction : règle inscrite dans les deux skills et dans les instructions Gemini et ChatGPT.

## Si une donnée a fuité

1. La considérer comme publique : changer ce qui peut l'être (identifiant de dossier, mot de passe, clé).
2. La retirer de tout l'historique (`git filter-repo`), forcer le push de toutes les branches et étiquettes.
3. Demander au support GitHub de purger les vues en cache et les références de pull requests qui pointent vers les anciens commits (formulaire « Remove data » de GitHub Support).

## Historique

- 01/11/2026 : historique réécrit. Retirés : adresses e-mail personnelle et professionnelle des auteurs, un identifiant de dossier Google Drive, des exemples chiffrés proches d'une situation réelle. Ajoutés : contrôle automatique des données personnelles, CI durcie, script d'archivage restreint, règles de sécurité dans les instructions.
