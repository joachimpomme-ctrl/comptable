/**
 * archivage_analyses.gs
 *
 * Deplace vers le dossier Archive tous les Google Docs et Sheets
 * dont le nom respecte la convention : "AAAA-MM-JJ — Type — Sujet"
 *
 * CONFIGURATION :
 *   Remplacez 'VOTRE_FOLDER_ID_ICI' par l'ID de votre dossier Google Drive Archive.
 *   Pour obtenir l'ID : ouvrez le dossier sur drive.google.com,
 *   l'ID est la chaine de caracteres apres /folders/ dans l'URL.
 *
 * INSTALLATION :
 *   1. Ouvrir script.google.com -> Nouveau projet
 *   2. Coller ce code, enregistrer
 *   3. Executer moveAnalysesToArchive() une premiere fois (autorisation OAuth)
 *   4. Optionnel : executer installDailyTrigger() pour un archivage automatique a 2h
 *
 * USAGE MANUEL :
 *   Selectionner la fonction moveAnalysesToArchive -> Executer
 */

const ARCHIVE_FOLDER_ID = 'VOTRE_FOLDER_ID_ICI'; // <- Remplacer par votre ID

// Correspond a : "2026-05-12 — Analyse — ..." (tirets longs ou courts acceptes)
const NAMING_REGEX = /^\d{4}-\d{2}-\d{2}\s[—\-]\s/;

function moveAnalysesToArchive() {
  const targetFolder = DriveApp.getFolderById(ARCHIVE_FOLDER_ID);

  const mimeTypes = [
    MimeType.GOOGLE_DOCS,
    MimeType.GOOGLE_SHEETS,
  ];

  let moved = 0;
  let skipped = 0;
  const log = [];

  for (const mime of mimeTypes) {
    const files = DriveApp.searchFiles(
      `mimeType = '${mime}' and trashed = false`
    );

    while (files.hasNext()) {
      const file = files.next();
      const name = file.getName();

      if (!NAMING_REGEX.test(name)) {
        continue;
      }

      if (isAlreadyInFolder_(file, ARCHIVE_FOLDER_ID)) {
        skipped++;
        continue;
      }

      file.moveTo(targetFolder);
      moved++;
      log.push('OK : ' + name);
    }
  }

  const summary = [
    '=== Archivage termine — ' + new Date().toLocaleString('fr-FR') + ' ===',
    'Deplaces : ' + moved,
    'Deja en place : ' + skipped,
    '',
  ].concat(log).join('\n');

  Logger.log(summary);
  return summary;
}

/**
 * Installe un declencheur toutes les 15 minutes (a lancer une seule fois).
 */
function installTrigger() {
  ScriptApp.getProjectTriggers()
    .filter(function(t) { return t.getHandlerFunction() === 'moveAnalysesToArchive'; })
    .forEach(function(t) { ScriptApp.deleteTrigger(t); });

  ScriptApp.newTrigger('moveAnalysesToArchive')
    .timeBased()
    .everyMinutes(15)
    .create();

  Logger.log('Declencheur toutes les 15 min installe.');
}

/**
 * Supprime le declencheur.
 */
function removeTrigger() {
  ScriptApp.getProjectTriggers()
    .filter(function(t) { return t.getHandlerFunction() === 'moveAnalysesToArchive'; })
    .forEach(function(t) { ScriptApp.deleteTrigger(t); });

  Logger.log('Declencheur supprime.');
}

// Alias pour compatibilite avec l'ancienne version
var installDailyTrigger = installTrigger;
var removeDailyTrigger  = removeTrigger;

// ─── Utilitaires ─────────────────────────────────────────────────────────────

function isAlreadyInFolder_(file, folderId) {
  var parents = file.getParents();
  while (parents.hasNext()) {
    if (parents.next().getId() === folderId) return true;
  }
  return false;
}
