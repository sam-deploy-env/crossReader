from config import config

# DISCORD
FILE_KO = "La commande $setfile doit être suivie de 0 (non envoyé) ou 1 (déjà envoyé)"
FILE_OFF = "Le fichier est considéré comme non envoyé, l'envoie automatique est activé"
UNKNOWN_EXTENSION = "Extension du fichier non reconnue. Fichier non pris en compte"
STARTED_KO = "La commande $started doit être suivie de \"on\", \"off\", 0 ou 1"
FILE_ON = "Le fichier est considéré comme déjà envoyé et ne sera pas renvoyé"

DB_INIT = "La base de données à été complètement réinitialisée"
FILE_TREATED = "Fichier traité par le " + config.PC_NAME
DB_DELETE = "Les coureurs ont été supprimés de la base"
STARTED_OFF = "La course est arrêtée"
STARTED_ON = "La course est démarée"
OK = "Ok " + config.PC_NAME

# CMD
CMD = "Commandes disponibles :\n\n\
    $rewards : Envoie sur discord le fichier word des récompenses.\n\
    $delete : Supprime les coureurs de la base de données.\n\
    $init : Initialise la base de données.\n\
    $setfile [0/1] : Enregistre le fichier des recompenses comme déjà envoyé ou non\n\
    $started [on/off/0/1] : Démarrer ou arrêter la course\n\
    $test : Lance un appel aux bots connectés.\n\
    $clear [nombre] : Supprime les messages dans le channel.\n\
    $cmd : Affiche les commandes" #