/**
 * archivage_analyses.gs
 *
 * Range dans le dossier d'archive les Google Docs et Sheets que l'agent a
 * crees a la racine du Drive, nommes selon la convention de l'agent :
 * date AAAA-MM-JJ, type, sujet, separes par des tirets.
 *
 * Perimetre volontairement etroit (securite) :
 *   - uniquement les fichiers places a la RACINE du Drive ;
 *   - uniquement ceux dont l'utilisateur est PROPRIETAIRE ;
 *   - uniquement ceux crees depuis moins de AGE_MAX_JOURS jours ;
 *   - uniquement les noms "AAAA-MM-JJ - Type - Sujet" (tiret court, demi-cadratin ou cadratin).
 * Un document range dans un dossier, partage par un tiers ou ancien n'est jamais deplace.
 *
 * CONFIGURATION :
 *   Remplacez 'VOTRE_FOLDER_ID_ICI' par l'ID de votre dossier d'archive.
 *   L'ID est la chaine apres /folders/ dans l'URL du dossier.
 *   Ne publiez jamais cet ID (depot public, capture d'ecran, message).
 *
 * INSTALLATION :
 *   1. script.google.com -> Nouveau projet, coller ce code, enregistrer.
 *   2. Executer simulerArchivage() : liste ce qui serait deplace, sans rien deplacer.
 *   3. Executer moveAnalysesToArchive() une premiere fois (autorisation OAuth).
 *   4. Optionnel : executer installDailyTrigger() pour un passage chaque nuit vers 2 h.
 */

const ARCHIVE_FOLDER_ID = 'VOTRE_FOLDER_ID_ICI'; // <- Remplacer par votre ID
const AGE_MAX_JOURS = 2;

// "2026-05-12 - Analyse - Sujet" ; tirets acceptes : - (U+002D), demi-cadratin (U+2013), cadratin (U+2014)
const NAMING_REGEX = /^\d{4}-\d{2}-\d{2} [\u002D\u2013\u2014] [^\u002D\u2013\u2014]+ [\u002D\u2013\u2014] .+/;

function moveAnalysesToArchive() {
  return archiver_(false);
}

function simulerArchivage() {
  return archiver_(true);
}

function archiver_(simulation) {
  if (ARCHIVE_FOLDER_ID === 'VOTRE_FOLDER_ID_ICI') {
    throw new Error("Renseignez ARCHIVE_FOLDER_ID avant de lancer l'archivage.");
  }
  const targetFolder = DriveApp.getFolderById(ARCHIVE_FOLDER_ID);
  const limite = Date.now() - AGE_MAX_JOURS * 24 * 3600 * 1000;
  const mimeTypes = [MimeType.GOOGLE_DOCS, MimeType.GOOGLE_SHEETS];

  let moved = 0;
  let failed = 0;
  const log = [];

  for (const mime of mimeTypes) {
    const files = DriveApp.searchFiles(
      "'root' in parents and 'me' in owners and trashed = false and mimeType = '" + mime + "'"
    );
    while (files.hasNext()) {
      const file = files.next();
      const name = file.getName();
      if (!NAMING_REGEX.test(name)) continue;
      if (file.getDateCreated().getTime() < limite) continue;
      if (simulation) {
        log.push('A deplacer : ' + name);
        moved++;
        continue;
      }
      try {
        file.moveTo(targetFolder);
        moved++;
        log.push('OK : ' + name);
      } catch (e) {
        failed++;
        log.push('ECHEC : ' + name + ' (' + e.message + ')');
      }
    }
  }

  const summary = [
    '=== ' + (simulation ? 'Simulation' : 'Archivage') + ' du ' + new Date().toLocaleString('fr-FR') + ' ===',
    (simulation ? 'Seraient deplaces : ' : 'Deplaces : ') + moved,
    'Echecs : ' + failed,
    '',
  ].concat(log).join('\n');
  Logger.log(summary);
  return summary;
}

/**
 * Installe un declencheur quotidien vers 2 h (a lancer une seule fois).
 */
function installTrigger() {
  removeTrigger();
  ScriptApp.newTrigger('moveAnalysesToArchive')
    .timeBased()
    .everyDays(1)
    .atHour(2)
    .create();
  Logger.log('Declencheur quotidien installe (vers 2 h).');
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

// Alias pour compatibilite avec le guide d'installation
var installDailyTrigger = installTrigger;
var removeDailyTrigger = removeTrigger;
