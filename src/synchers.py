#!/usr/bin/env python
###############################################################################################
#  Author:
_author = '<a href="mailto:debuti@gmail.com">Borja Garcia</a>'
# Program:
_name = 'synchers'
# Descrip:
_description = '''This scripts sync all data between devices'''
# Version:
_version = '0.0.0'
#    Date:
_date = '2009-05-18:11:51:43'
# License: This script doesn't require any license since it's not intended to be redistributed.
#          In such case, unless stated otherwise, the purpose of the author is to follow GPLv3.
# History: 0.0.0 (YYYY-MM-DD:hh:mm)
#            -Initial release
###############################################################################################

# imports
import logging
import sys
import doctest
import datetime, time
import os
import subprocess
import optparse
import inspect

import shellutils

# User-libs imports
LIB_PATH = 'lib'
sys.path.append(LIB_PATH)
print sys.path

# Parameters n' Constants
APP_PATH = os.getcwd() + os.path.sep + '.' + _name
LOG_PATH = APP_PATH + os.path.sep + 'logs'
LOG_FILENAME = LOG_PATH + os.path.sep + _name + '_' + time.strftime("%Y%m%d_%H%M%S") + '.log'

# Global variables
global now
global logger
global verbose
now = time.strftime("%Y-%m-%d:%H:%M:%S")
logger = ""

#Names
DESKTOP_NAME_C = shellutils.getSystemVariable("DESKTOP_NAME")
NETTOP_NAME_C  = shellutils.getSystemVariable("NETTOP_NAME")
MOBILE_NAME_C  = shellutils.getSystemVariable("MOBILE_NAME")

#Paths
DESKTOP_QUEUES_C = shellutils.getSystemVariable("DESKTOP_NAME")

# Error declaration
error = { "" : "",
          "" : "",
          "" : "" }

# Usage function, logs, utils and check input
def createWorkDir():
    '''This function is for creating the working directory, if its not already
 
    --Description--

    --Test--
    >>> print createWorkDir()
    '''
    if not os.path.isdir(APP_PATH):
        os.mkdir(APP_PATH)
    if not os.path.isdir(LOG_PATH):
        os.mkdir(LOG_PATH)
    if not os.path.isfile(LOG_FILENAME):
        f = open(LOG_FILENAME, "w")
        f.close()

def openLog():
    '''This function is for initialize the logging job
 
    --Description--

    --Test--
    >>> print openLog()
    '''
 
    global logger

    desiredLevel = logging.DEBUG
    logger = logging.getLogger(_name)
    logger.setLevel(desiredLevel)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(LOG_FILENAME)
    fh.setLevel(desiredLevel)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(desiredLevel)
    # create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

def closeLog():
    '''This function is for shutdown the logging job

    --Description--

    --Test--
    >>> print closeLog()
    '''
 
    logging.shutdown()

def checkInput():
    '''This function is for treat the user command line parameters.

    --Description--

    --Test--
    >>> print checkInput()
 
    '''

    #####THIS SECTION IS A EXAMPLE#####
        #Global variable use declaration

    global verbose
       
    #Create instance of OptionParser Module, included in Standard Library
    p = optparse.OptionParser(description=_description,
                              prog=_name,
                              version=_version,
                              usage='''\
%prog [options]''')
    p.add_option('--ip','-i', action="store_true", help='gets current IP Address')
    p.add_option('--usage', '-u', action="store_true", help='gets disk usage of homedir')
    p.add_option('--verbose', '-v',
                action = 'store_true',
                help='prints verbosely',
                default=False)

    #Option Handling passes correct parameter to runBash
    options, arguments = p.parse_args()

    if len(arguments) == 1:
        p.print_help()
        sys.exit(-1)
    if options.verbose:
        verbose=True
    if options.ip:
        value = runBash(IPADDR)
        report(value,"IPADDR")
    elif options.usage:
        value = runBash(HOMEDIR_USAGE)
        report(value, "HOMEDIR_USAGE")
    else:
        p.print_help()
    #####/THIS SECTION IS A EXAMPLE#####

# Helper functions
def syncDesktopQueues():
    '''This is the procedure thats resolve the desktop's queues.
	This computer is constantly attached to Dropbox and sometimes the following devices are attached to it:
	 -HD_Data
	 -HD_Backup (To recover all backups)
	 -Mobile
	 -Camera
	 -Pendrive
	 -Psp
	'''
    
    #From Desktop to HD_Data
    if (shellutils.mv(shellutils.ls(Desktop_HDData_Queues_Path), HDData_HDData_Queues_Path) != 0):
        print ("Error copying from Desktop to HD_Data queues")
    
    #From Desktop to HD_Backup
    
    #From Desktop
    
    #From Desktop to 

   
   #De mendigo a hd
   # echo "----Florido -> HD----"
   # echo "    ----Queues----"
#    mv -v "$FLORIDO_PATH"/_queues/A_HD/* "$HD_PATH"/_queues/INCOMING/
 #   sleep 5

   #De mendigo a florido
  #  echo
   # echo
    #echo "----Florido -> Mendigo----"

#    echo "    ----Queues----"
 #   mv -v "$FLORIDO_PATH"/_queues/A_mendigo/* "$HD_PATH"/_queues/A_mendigo/
  #  sleep 5

   #De quien sea a mendigo
   # echo
    #echo
#    echo "----* -> Florido----"

 #   echo "    ----Queues----"
  #  mv -v "$HD_PATH"/_queues/A_florido/* "$FLORIDO_PATH"/_queues/INCOMING/

   # sync


def syncNettopQueues():
    '''This is the procedure thats resolve the nettop's queues.
	This computer is constantly attached to:
     -Dropbox
	 -Family exchange directory 
	and sometimes the following devices are attached to it:
	 -HD_Data
	 -HD_Backup (To recover all backups)
	'''

#echo Pon el screen antes de hacer esto tio!
#read ok

#De mendigo a hd
#echo "----Mendigo -> HD----"

 #videos transcodeados
#echo "    ----Videos transcodeados----"
#mkdir /media/sdc1/_queues/INCOMING/AVIS
#mv -v /media/sdb1/_proceso/VIDEOS/AVIS/* /media/sdc1/_queues/INCOMING/AVIS/
#sleep 5


 #incoming del mldonkey
#echo "    ----Incoming----"
#mkdir /media/sdc1/_queues/INCOMING/INCOMING_MLNET
#mkdir /media/sdc1/_queues/INCOMING/INCOMING_MLNET/files
#mkdir /media/sdc1/_queues/INCOMING/INCOMING_MLNET/directories
#mv -v /media/sdb1/DOWNLOAD/INCOMING/files/* /media/sdc1/_queues/INCOMING/INCOMING_MLNET/files/
#mv -v /media/sdb1/DOWNLOAD/INCOMING/directories/* /media/sdc1/_queues/INCOMING/INCOMING_MLNET/directories/
#sleep 5

 #resto de cosas
#echo "    ----Queues----"
#mv -v /media/sdb1/_queues/A_HD/* /media/sdc1/_queues/INCOMING/
#sleep 5

#De mendigo a florido
#echo
#echo
#echo "----Mendigo -> florido----"
 #musica
#echo "    ----Musica tratada----"
#mkdir /media/sdc1/_queues/A_florido/4.-TRANSFERIR
#mv -v /media/sdb1/_proceso/MUSICA/4.-TRANSFERIR/* /media/sdc1/_queues/A_florido/4.-TRANSFERIR/
#sleep 5

 #resto de cosas
#echo "    ----Queues----"
#mv -v /media/sdb1/_queues/A_florido/* /media/sdc1/_queues/A_florido/
#sleep 5


#De mama a HD
#echo
#echo
#echo "----Mama -> HD----"
#echo "    ----Queues----"
#mv -v /media/emulatron/_queues/A_HD/* /media/sdc1/_queues/INCOMING/


#De quien sea a mendigo
#echo
#echo
#echo "----* -> Mendigo----"
#echo "    ----Queues----"
#mv -v /media/sdc1/_queues/A_mendigo/* /media/sdb1/_queues/INCOMING/



def syncMobile():
    '''This is the main procedure'''
    syncAndroid()

def syncAndroid():
    '''This is the main procedure'''

##TODO: salvar program files tambien
##TODO: aadir opcion para preguntar al inicio numero de albums q se quiere copiar

    NUM_ALBUMS=100 #TODO PONER AQUI EL 80% DEL DISCO LIBRE!!
#
#DATE=`date +%Y%m%d_%H%M%S`
#TAG="pocketpc.$DATE.imported"
#
## Constants
#DEFAULT_LOG_PATH="$PWD/syncWinMobile.$DATE.log"
#
#DEFAULT_POCKET_PC="/media/disk"
#DEFAULT_PPC_OLDMEDIA_PATH="/My Documents/Old media"
#DEFAULT_PPC_VIDEOS_PATH="/My Documents/My videos"
#DEFAULT_PPC_PHOTOS_PATH="/My Documents/My pictures"
#DEFAULT_PPC_MUSIC_PATH="/My Documents/My music"
#DEFAULT_PPC_MOVIES_PATH="/My Documents/My movies"
#DEFAULT_PPC_BACKUPS_PATH="/My Documents/backups"
#DEFAULT_PPC_PROGRAMS_PATH="/My Documents/Other/Installers"
#DEFAULT_PPC_DOCUMENTS_PATH="/My Documents/*"
#DEFAULT_PPC_PERSONAL_PATH="/My Documents/Personal"
#DEFAULT_PPC_SAVEGAMES_PATH="/My Documents/Savegames"
#
#DEFAULT_LINUX="/media/datos"
#DEFAULT_LINUX_VIDEOS_PATH="/Data/Photos/Inbox/$TAG"
#DEFAULT_LINUX_PHOTOS_PATH="/Data/Photos/Inbox/$TAG"
#DEFAULT_LINUX_MUSIC_PATH="/Data/Music/Albums"
#DEFAULT_LINUX_MOVIES_PATH="/_queues/winMobile/to_winMobile/Movies"
#DEFAULT_LINUX_BACKUPS_PATH="/Data/Private/Mobile/p3300/backups"
#DEFAULT_LINUX_PROGRAMS_PATH="/Software/windowsMe"
#DEFAULT_LINUX_PASSWD_PATH="/media/Dropbox/Data/Private/Info/Passwd/passwd.kdb"
#DEFAULT_LINUX_STUFF_PATH="/Data/Private/Mobile/p3300/data"
#DEFAULT_LINUX_CONTACTS_PATH="/Data/Private/Info/Contacts/contacts.xls"
#
## Global variables
#log=$DEFAULT_LOG_PATH
#
#pocketPC=$DEFAULT_POCKET_PC
#ppc_oldmedia_path="$pocketPC""$DEFAULT_PPC_OLDMEDIA_PATH"
#ppc_videos_path="$pocketPC""$DEFAULT_PPC_VIDEOS_PATH"
#ppc_photos_path="$pocketPC""$DEFAULT_PPC_PHOTOS_PATH"
#ppc_music_path="$pocketPC""$DEFAULT_PPC_MUSIC_PATH"
#ppc_movies_path="$pocketPC""$DEFAULT_PPC_MOVIES_PATH"
#ppc_backups_path="$pocketPC""$DEFAULT_PPC_BACKUPS_PATH"
#ppc_programs_path="$pocketPC""$DEFAULT_PPC_PROGRAMS_PATH"
#ppc_documents_path="$pocketPC""$DEFAULT_PPC_DOCUMENTS_PATH"
#ppc_personal_path="$pocketPC""$DEFAULT_PPC_PERSONAL_PATH"
#ppc_savegames_path="$pocketPC""$DEFAULT_PPC_SAVEGAMES_PATH"
#
#linux=$DEFAULT_LINUX
#linux_videos_path="$linux""$DEFAULT_LINUX_VIDEOS_PATH"
#linux_photos_path="$linux""$DEFAULT_LINUX_PHOTOS_PATH"
#linux_music_path="$linux""$DEFAULT_LINUX_MUSIC_PATH"
#linux_movies_path="$linux""$DEFAULT_LINUX_MOVIES_PATH"
#linux_backups_path="$linux""$DEFAULT_LINUX_BACKUPS_PATH"
#linux_programs_path="$linux""$DEFAULT_LINUX_PROGRAMS_PATH"
#linux_passwd_path="$DEFAULT_LINUX_PASSWD_PATH"
#linux_stuff_path="$linux""$DEFAULT_LINUX_STUFF_PATH"
#linux_contacts_path="$linux""$DEFAULT_LINUX_CONTACTS_PATH"

#
#  function dirEmpty {
#    if [ -e "$1" ]; then
#      dir="$1"
#    else
#      return -1
#    fi
#
#    cd "$dir"
#    counter=0
#    for i in *; do
#      let counter=$counter+1
#    done
#
#    cd - >> /dev/null > /dev/null
#
#    if [ $counter -eq 1 ]; then
#      if [ "$i" = "*" ]; then
#        echo 1
#        return 1
#      else
#        echo 0
#        return 0
#      fi
#    else
#      echo 0
#      return 0
#    fi
#  }
#
#
#    logging.info("Using $pocketPC as mobile phone directory"
#    #I set up all vars
#ppc_oldmedia_path="$pocketPC""$DEFAULT_PPC_OLDMEDIA_PATH"
#ppc_videos_path="$pocketPC""$DEFAULT_PPC_VIDEOS_PATH"
#ppc_photos_path="$pocketPC""$DEFAULT_PPC_PHOTOS_PATH"
#ppc_music_path="$pocketPC""$DEFAULT_PPC_MUSIC_PATH"
#ppc_movies_path="$pocketPC""$DEFAULT_PPC_MOVIES_PATH"
#ppc_backups_path="$pocketPC""$DEFAULT_PPC_BACKUPS_PATH"
#ppc_programs_path="$pocketPC""$DEFAULT_PPC_PROGRAMS_PATH"
#ppc_documents_path="$pocketPC""$DEFAULT_PPC_DOCUMENTS_PATH"
#ppc_personal_path="$pocketPC""$DEFAULT_PPC_PERSONAL_PATH"
#ppc_savegames_path="$pocketPC""$DEFAULT_PPC_SAVEGAMES_PATH"
#  }

    def photosNvideos():

        logging.info("Saving photos and videos with the handset")

        if not os.path.isdir(linux_videos_path):
            if (os.mkdir(linux_videos_path) != 0):
                logging.error("Unable to make dir " + linux_videos_path)

        logging.info(" Saving videos")

        shellutils.cp("$ppc_videos_path"/*,
                      "$ppc_oldmedia_path") #TODO:Copia una lista de archivos al destino (hacer una version recurrente)
        shellutils.mv("$ppc_videos_path"/*,
                      "$linux_videos_path") #TODO:Mueve una lista al destino!


        if not os.path.isdir(linux_photos_path):
            if (os.mkdir(linux_photos_path) != 0):
                logging.error("Unable to make dir " + linux_photos_path)

        logging.info("Syncing photos")

        shellutils.cp("$ppc_photos_path"/*,
                      "$ppc_oldmedia_path") #TODO:Copia una lista de archivos al destino (hacer una version recurrente)
        shellutils.mv("$ppc_photos_path"/*,
                      "$linux_photos_path") #TODO:Mueve una lista al destino!


        if shellutils.isDirEmpty(linux_photos_path):   #TODO:if os.listdir(path) == []:    print "yes" else:    print "no"
            shellutils.rm_rf(linux_photos_path) #TODO: Espera una lista!
            logging.debug("No photos or videos so deleting " +linux_photos_path)


        logging.info("Saving photos and videos with the handset done")



    def music():
#TODO: Poner un ||exit detras del fillMP3 cuando arregle el fillmp3 para que saque mensajes si rula mal :S

        if shellutils.existsExecutable("fillMP3player.sh"): #TODO:es ver si un which devuelve algo o no :S
           logging.error("fillMP3player.sh utility not found, please append it to the path to complete music copy process")

        else
           logging.info("Transfering music to your mobile")
           shellutils.runBash("fillMP3player.sh "+linux_music_path+" "+NUM_ALBUMS+" "+ppc_music_path+" "+S)
           logging.info("You have new music for free, fuck sgae!")
           logging.info("Transfering music to your mobile done")



    def movies():
        logging.info("Copying the movies to your device")
        shellutils.rm_rf(ppc_movies_path"/*)
        shellutils.mv(linux_movies_path"/*,
                      ppc_movies_path)
        logging.info("Copying the movies to your device done")

#
#  function backups {
#    logging.info("Backupin the backup"
#    cp -fuv "$ppc_backups_path"/* "$linux_backups_path"/. 2>> $log >> $log || (logging.error("Unable to backup the backups" && exit -1)
#    logging.info("Done backupin backups"
#  }
#
#  function programs {
#    logging.info("Backupin the programs"
#    cp -furv "$ppc_programs_path"/* "$linux_programs_path"/. 2>> $log >> $log || (logging.error("Unable to backup the programs" && exit -1)
#    logging.info("Done backupin programs"
#  }
#
#  function passwords {
#    logging.info("Backupin the passwords"
#    cp -fv "$linux_passwd_path" "$ppc_personal_path" 2>> $log >> $log || (logging.error("Unable to copy the passwd file" && exit -1)
#    logging.info("Done backupin passwords"
#  }
#
#  function contacts {
##TODO: Recode this part when my contacts software is rockin' hard
#    logging.info("Importing contacts"
#    cp -fv "$linux_contacts_path" "$ppc_personal_path" 2>> $log >> $log || (logging.error("Unable to copy the contacts data" && exit -1)
#    logging.info("Done importin contacts"
#  }
#
#  function stuff {
##TODO: mydownloads y personal y el root de my documents, salvar al directorio /BORJA/DATOS/MOVIL/p3300/datos
#    logging.info("Backuping the other data on the phone"
#    cp -fv "$ppc_documents_path" "$linux_stuff_path" 2>> $log >> $log || (logging.error("Unable to copy the documents data" && exit -1)
#    cp -fvR "$ppc_personal_path" "$linux_stuff_path" 2>> $log >> $log || (logging.error("Unable to copy the personal data" && exit -1)
#    cp -fvR "$ppc_savegames_path" "$linux_stuff_path" 2>> $log >> $log || (logging.error("Unable to copy the savegames data" && exit -1)
#    logging.info("Done backupin common data"
#  }
#

# Main android sync function
#TODO: Insert command line options to select which of these execute, default all
    photosNvideos()      #DEBUG: ; read
    music()              #DEBUG: ; read
#    movies()             #DEBUG: ; read
#    backups()            #DEBUG: ; read
#    programs()           #DEBUG: ; read
#    passwords()          #DEBUG: ; read
#    contacts()           #DEBUG: ; read
#    stuff()              #DEBUG: ; read
#TODO Sincronize here the buffers


# Main function
def main():
    '''This is the main procedure
 
    --Description--
 
    --Test--
    >>> print main()
 
    '''
   
    #Get the current system where im running on
    if shellutils.getSystemName() == DESKTOP_NAME_C: #Florido or something seemfull
	   #Resolve specific data
	   if isDriveConnected(PSP_NAME_C):
	      syncDesktopPsp()
		  
	   elif isDriveConnected(MOBILE_NAME_C):
	      syncDesktopMobile()
		  
	   elif isDriveConnected(CAMERA_NAME_C):
	      syncDesktopCamera()
		  
       syncDesktopQueues()

    elif shellutils.getSystemName() == NETTOP_NAME_C: #Mendigo or something like that
        syncNettopQueues()

    elif shellutils.getSystemName() == MOBILE_NAME_C:
        syncMobileQueues()

    else:
        logging.error('System not recognized, named ' + shellutils.getSystemName())


# Entry point
if __name__ == '__main__':
    #doctest.testmod()   # automaticly run tests
    #checkInput()
    createWorkDir()
    openLog()
    main()
    closeLog()

	
#Requisitos para este software
# Tiene que sincronizar las queues de los dispositivos
#  Debe sincronizarlas teniendo en cuenta contenidos
#  Debe sincronizarlas a traves del 80% del espacio libre del dropbox o directamente si estan enchufados directamente
#  Debe poder fraccionar las sincronizaciones (al llegar al tope de espacio llenable mete un archivo de finished)
# Tiene que poder hacer el handshake con el movil
# Tiene que poder hacer el handshake con la psp

# Tiene que haber otro script que lo autoplanifique, a este y al de los backups, al de deploy music y al de videos (en VARIOS DISPOSITIVOS)
# Tiene qe haber otro script que cada vez que corra un programa mire por si hay cambios en este y lo actualicee

