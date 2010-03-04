#!/bin/bash
################################################################################
#  Author: Borja Garcia <debuti@gmail.com>
# Program: syncWinMobile.sh
# Descrip: This script syncs my pocket pc and my portable pc (florido)
# Version: 0.0.0
#    Date: 2008-11-10:18:52:00
# License: This script doesn't require any license since it's not intended to be
#          redistributed.
#          In such case, unless stated otherwise, the purpose of the author is
#          to follow GPLv3.
# Version: 0.0.0 (2008-11-10:18:52:00)
#           - Initial release
################################################################################

#TODO: salvar program files tambien
#TODO: añadir opcion para preguntar al inicio numero de albums q se quiere copiar

#Parameters
NUM_ALBUMS=100

DATE=`date +%Y%m%d_%H%M%S`
TAG="pocketpc.$DATE.imported"

# Constants
DEFAULT_LOG_PATH="$PWD/syncWinMobile.$DATE.log"

DEFAULT_POCKET_PC="/media/disk"
DEFAULT_PPC_OLDMEDIA_PATH="/My Documents/Old media"
DEFAULT_PPC_VIDEOS_PATH="/My Documents/My videos"
DEFAULT_PPC_PHOTOS_PATH="/My Documents/My pictures"
DEFAULT_PPC_MUSIC_PATH="/My Documents/My music"
DEFAULT_PPC_MOVIES_PATH="/My Documents/My movies"
DEFAULT_PPC_BACKUPS_PATH="/My Documents/backups"
DEFAULT_PPC_PROGRAMS_PATH="/My Documents/Other/Installers"
DEFAULT_PPC_DOCUMENTS_PATH="/My Documents/*"
DEFAULT_PPC_PERSONAL_PATH="/My Documents/Personal"
DEFAULT_PPC_SAVEGAMES_PATH="/My Documents/Savegames"

DEFAULT_LINUX="/media/datos"
DEFAULT_LINUX_VIDEOS_PATH="/Data/Photos/Inbox/$TAG"
DEFAULT_LINUX_PHOTOS_PATH="/Data/Photos/Inbox/$TAG"
DEFAULT_LINUX_MUSIC_PATH="/Data/Music/Albums"
DEFAULT_LINUX_MOVIES_PATH="/_queues/winMobile/to_winMobile/Movies"
DEFAULT_LINUX_BACKUPS_PATH="/Data/Private/Mobile/p3300/backups"
DEFAULT_LINUX_PROGRAMS_PATH="/Software/windowsMe"
DEFAULT_LINUX_PASSWD_PATH="/media/Dropbox/Data/Private/Info/Passwd/passwd.kdb"
DEFAULT_LINUX_STUFF_PATH="/Data/Private/Mobile/p3300/data"
DEFAULT_LINUX_CONTACTS_PATH="/Data/Private/Info/Contacts/contacts.xls"

# Global variables
log=$DEFAULT_LOG_PATH

pocketPC=$DEFAULT_POCKET_PC
ppc_oldmedia_path="$pocketPC""$DEFAULT_PPC_OLDMEDIA_PATH"
ppc_videos_path="$pocketPC""$DEFAULT_PPC_VIDEOS_PATH"
ppc_photos_path="$pocketPC""$DEFAULT_PPC_PHOTOS_PATH"
ppc_music_path="$pocketPC""$DEFAULT_PPC_MUSIC_PATH"
ppc_movies_path="$pocketPC""$DEFAULT_PPC_MOVIES_PATH"
ppc_backups_path="$pocketPC""$DEFAULT_PPC_BACKUPS_PATH"
ppc_programs_path="$pocketPC""$DEFAULT_PPC_PROGRAMS_PATH"
ppc_documents_path="$pocketPC""$DEFAULT_PPC_DOCUMENTS_PATH"
ppc_personal_path="$pocketPC""$DEFAULT_PPC_PERSONAL_PATH"
ppc_savegames_path="$pocketPC""$DEFAULT_PPC_SAVEGAMES_PATH"

linux=$DEFAULT_LINUX
linux_videos_path="$linux""$DEFAULT_LINUX_VIDEOS_PATH"
linux_photos_path="$linux""$DEFAULT_LINUX_PHOTOS_PATH"
linux_music_path="$linux""$DEFAULT_LINUX_MUSIC_PATH"
linux_movies_path="$linux""$DEFAULT_LINUX_MOVIES_PATH"
linux_backups_path="$linux""$DEFAULT_LINUX_BACKUPS_PATH"
linux_programs_path="$linux""$DEFAULT_LINUX_PROGRAMS_PATH"
linux_passwd_path="$DEFAULT_LINUX_PASSWD_PATH"
linux_stuff_path="$linux""$DEFAULT_LINUX_STUFF_PATH"
linux_contacts_path="$linux""$DEFAULT_LINUX_CONTACTS_PATH"


# Error declaration


# Usage and awesome functions

  function usage() {
    # Tell the user how to use me
    echo "Usage: $0 [<pocketPC mount point>]"
  }
  
  function echoNlog {
    echo $@
    echo $@ >> $log
  }

  function dirEmpty {
    if [ -e "$1" ]; then
      dir="$1"
    else
      return -1
    fi

    cd "$dir"
    counter=0
    for i in *; do
      let counter=$counter+1
    done

    cd - >> /dev/null > /dev/null

    if [ $counter -eq 1 ]; then
      if [ "$i" = "*" ]; then
        echo 1
        return 1
      else
        echo 0
        return 0
      fi
    else
      echo 0
      return 0
    fi
  }

  function getFullPath() {
      file=""
      actual=`pwd`
      output=""
      temp=""

    if [ -e "$1" ]; then
      file="$1"
    else
      return -1
    fi

    if [ `echo $file | cut -c1,1` = "/" ]; then
      output=$file
    else
      output="$actual"/"$file"
      output=`echo $output | sed -e "s/\/\.\//\//g"`                          #Ignore /./
      while [ `echo $output | grep "/../"` ]; do
        output=`echo $output | sed -e "s/\/[^\/^(\.\.)]*\/\.\.\//\//g"`       #Delete /somewhere/../
        output=`echo $output | sed -e "s/^\/\.\.\//\//g"`
      done
      output=`echo $output | sed -e "s/\/\//\//g"`                            #Ignore //

    fi

    if [ -e "$output" ]; then
      echo "$output"
    else
      echo "Can't do it :S $output" 1>&2
      return -2
    fi
  }

# Input validation function

  function checkInput() {
    # Check input and store params in global variables to use them from main or call usage()
    if [ $# -gt 2 ]; then
      usage $0
      exit -1
    else
      if [ $# -eq 0 ]; then
        response="trick!"
        while [ ! -d "$response" ]; do
          echo "Insert the path of the pocketPC filesystem root ($pocketPC) or die!:"
          read response
          if [ "$response" = "" ]; then
            response=$pocketPC
          fi
        done
        pocketPC=`getFullPath "$response"`
      else
        if [ -d "$1" ]; then
          pocketPC=`getFullPath "$1"`
        else
          usage $0
          exit -1
        fi
      fi
    fi
    
    echoNlog "INFO:  Using $pocketPC as mobile phone directory"
    #I set up all vars
ppc_oldmedia_path="$pocketPC""$DEFAULT_PPC_OLDMEDIA_PATH"
ppc_videos_path="$pocketPC""$DEFAULT_PPC_VIDEOS_PATH"
ppc_photos_path="$pocketPC""$DEFAULT_PPC_PHOTOS_PATH"
ppc_music_path="$pocketPC""$DEFAULT_PPC_MUSIC_PATH"
ppc_movies_path="$pocketPC""$DEFAULT_PPC_MOVIES_PATH"
ppc_backups_path="$pocketPC""$DEFAULT_PPC_BACKUPS_PATH"
ppc_programs_path="$pocketPC""$DEFAULT_PPC_PROGRAMS_PATH"
ppc_documents_path="$pocketPC""$DEFAULT_PPC_DOCUMENTS_PATH"
ppc_personal_path="$pocketPC""$DEFAULT_PPC_PERSONAL_PATH"
ppc_savegames_path="$pocketPC""$DEFAULT_PPC_SAVEGAMES_PATH"
  }

# Helper functions

  function reminders {
    echo "##########################################################################"
    echo "#      Remember to do a full backup with the tool PPCPimBackup.exe!      #"
    echo "#and, if you want movies to see, put them in the TO_PPC dir in the queues#"
    echo "##########################################################################"
  }
  
  function photosNvideos {

    echoNlog "INFO:  Syncin photos and videos!"

    if [ ! -d "$linux_videos_path" ]; then
      mkdir -p "$linux_videos_path" || (echoNlog "ERROR: Unable to make dir $linux_videos_path" && exit -1)
    fi
    echoNlog "INFO:  Syncing videos"
    cp -v "$ppc_videos_path"/* "$ppc_oldmedia_path"/.
    mv -v "$ppc_videos_path"/* "$linux_videos_path" 2>> $log >> $log

    if [ ! -d "$linux_photos_path" ]; then
      mkdir -p "$linux_photos_path" || (echoNlog "ERROR: Unable to make dir $linux_photos_path" && exit -1)
    fi
    echoNlog "INFO:  Syncing photos"
    cp "$ppc_photos_path"/* "$ppc_oldmedia_path"/.
    mv "$ppc_photos_path"/* "$linux_photos_path" 2>> $log >> $log

    if [ "`dirEmpty "$linux_photos_path"`" -eq 1 ]; then
      rm -rf "$linux_photos_path"
      echoNlog "INFO:  NO photos or videos so deletin $linux_photos_path"
    fi
    echoNlog "INFO:  Sync of photos and videos ended"
  }
  
  function music {
#TODO: Poner un ||exit detras del fillMP3 cuando arregle el fillmp3 para que saque mensajes si rula mal :S
    if [ -z `which fillMP3player.sh` ]; then
      echoNlog "ERROR: fillMP3player.sh not found, please install it to complete music copy process"
      echoNlog "       proceeding with next step"
    else
      echoNlog "INFO:  Bringin' new music to your ears"
      fillMP3player.sh "$linux_music_path" "$NUM_ALBUMS" "$ppc_music_path" "S"
      echoNlog "INFO:  You have new music for free, fuck sgae!"
    fi
  }
  
  function movies {
    echoNlog "INFO:  Copying the movies to your device"
    rm -rf "$ppc_movies_path"/*
    mv -v "$linux_movies_path"/* "$ppc_movies_path"/. 2>> $log >> $log
    echoNlog "INFO:  Done copying the fckn' movies"
  }
  
  function backups {
    echoNlog "INFO:  Backupin the backup"
    cp -fuv "$ppc_backups_path"/* "$linux_backups_path"/. 2>> $log >> $log || (echoNlog "ERROR: Unable to backup the backups" && exit -1)
    echoNlog "INFO:  Done backupin backups"
  }
  
  function programs {
    echoNlog "INFO:  Backupin the programs"
    cp -furv "$ppc_programs_path"/* "$linux_programs_path"/. 2>> $log >> $log || (echoNlog "ERROR: Unable to backup the programs" && exit -1)
    echoNlog "INFO:  Done backupin programs"
  }
  
  function passwords {
    echoNlog "INFO:  Backupin the passwords"
    cp -fv "$linux_passwd_path" "$ppc_personal_path" 2>> $log >> $log || (echoNlog "ERROR: Unable to copy the passwd file" && exit -1)
    echoNlog "INFO:  Done backupin passwords" 
  }

  function contacts {
#TODO: Recode this part when my contacts software is rockin' hard
    echoNlog "INFO:  Importing contacts"
    cp -fv "$linux_contacts_path" "$ppc_personal_path" 2>> $log >> $log || (echoNlog "ERROR: Unable to copy the contacts data" && exit -1)
    echoNlog "INFO:  Done importin contacts" 
  }

  function stuff {
#TODO: mydownloads y personal y el root de my documents, salvar al directorio /BORJA/DATOS/MOVIL/p3300/datos
    echoNlog "INFO:  Backuping the other data on the phone"
    cp -fv "$ppc_documents_path" "$linux_stuff_path" 2>> $log >> $log || (echoNlog "ERROR: Unable to copy the documents data" && exit -1)
    cp -fvR "$ppc_personal_path" "$linux_stuff_path" 2>> $log >> $log || (echoNlog "ERROR: Unable to copy the personal data" && exit -1)
    cp -fvR "$ppc_savegames_path" "$linux_stuff_path" 2>> $log >> $log || (echoNlog "ERROR: Unable to copy the savegames data" && exit -1)
    echoNlog "INFO:  Done backupin common data" 
  }


# Main function

  function main() {
#TODO: Insert command line options to select which of these execute, default all
    reminders              #DEBUG: ; read
    photosNvideos              #DEBUG: ; read
    music              #DEBUG: ; read
    movies              #DEBUG: ; read
    backups              #DEBUG: ; read
    programs              #DEBUG: ; read
    passwords              #DEBUG: ; read
    contacts              #DEBUG: ; read
    stuff              #DEBUG: ; read
    sync
  }

# Entry point
  checkInput $@
  main

