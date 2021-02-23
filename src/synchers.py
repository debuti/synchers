#!/usr/bin/env python3
##########################################################################
#  Author:
__author__ = '<a href="mailto:debuti@gmail.com">Borja Garcia</a>'
# Program:
__program__ = 'synchers'
# Package:
__package__ = ''
# Descrip:
__description__ = '''Sync data between devices'''
# Version:
__version__ = '0.0.0'
#  Date:
__date__ = '20210223'
# License: GPLv3
# History:
#      0.0.0 (20210223)
#      -Initial release
##########################################################################

# TODO: el fichero de destino tiene q llamarse igual pero con .tmp para evitar tener que poner ningun lock
# TODO: ojo que mv tiene que mergear si hay nombres de directorio iguales en origen y destino
# TODO: Ojo que tiene que ser estable incluso si lo apagan a la mitad
# TODO: Ojo que tiene que funcionar en windows y android

# metodos para shellutils
# df (ruta) devuelve el numero de bytes que quedan en el disco donde
# reside ruta


# DOXYGEN para generar documentacion para cualquier lenguaje


####### OTRAS COSAS ######################################################
#  Debe sincronizarlas a traves del 80% del espacio libre del dropbox o si estan enchufados directamente, en una primera version deberia hacerlo de archivo en archivo
#  ####version2####Debe poder fraccionar las sincronizaciones (al llegar al tope de espacio llenable mete un archivo de finished)
# Tiene que haber otro script que le planifique un cron, a este y al de
# los backups, al de deploy music y al de videos (en VARIOS DISPOSITIVOS)
# y al de cargar el movil cuando esta conectado


# Imports
import logging
import sys
import time
import os
import glob
import argparse
try:
  import thepyutilities.shellutils as shellutils
except BaseException:
  print("Install thepyutilities (https://github.com/debuti/thepyutilities)")
  sys.exit(-1)

# Parameters n' Constants
DEFAULT_LOCATION_FILE = "stopover.location"
QUEUES_RELATIVE_PATH = "Queues"
OTHER_RELATIVE_PATH = "Other"
ALLOWED_FOLDERS = ["Videogames",
           "Other",
           "Music",
           "Videos",
           "Torrents",
           "Software",
           "Photos",
           "Documents",
           "Data"]
FREE_SPACE_PERCENTAGE_LIMIT = 20
KIBI = 1024
MEBI = 1024 * KIBI
LOG_MODE = "File"
LOG_LEVEL = logging.DEBUG
LOG_MAX_BYTES = 1 * MEBI
VOLUME_LIMIT_PER_FILE = 200 * MEBI


realScriptPath = os.path.realpath(__file__)
realScriptDirectory = os.path.dirname(realScriptPath)
callingDirectory = os.getcwd()
if os.path.isabs(__file__):
  linkScriptPath = __file__
else:
  linkScriptPath = os.path.join(callingDirectory, __file__)
linkScriptDirectory = os.path.dirname(linkScriptPath)

propertiesName = __program__ + ".properties"
propertiesPath = os.path.join(realScriptDirectory, '..', propertiesName)

logFileName = __program__ + '_' + time.strftime("%Y%m%d%H%M%S") + '.log'
logDirectory = os.path.join(realScriptDirectory, '..', 'logs')
logPath = os.path.join(logDirectory, logFileName)
loggerName = __package__ + "." + __program__


def openLog(mode, desiredLevel):
  '''This function is for initialize the logging job
  '''
  def openScreenLog(formatter, desiredLevel):
    logging.basicConfig(level=desiredLevel, format=formatter)

  def openScreenAndFileLog(fileName, formatter, desiredLevel):
    logger = logging.getLogger('')
    logger.setLevel(desiredLevel)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(fileName)
    fh.setLevel(desiredLevel)
    fh.setFormatter(formatter)
    # add the handler to logger
    logger.addHandler(fh)

  def openScreenAndRotatingFileLog(
      fileName,
      formatter,
      desiredLevel,
      maxBytes):
    logger = logging.getLogger('')
    logger.setLevel(desiredLevel)
    # create file handler which logs even debug messages
    fh = logging.handlers.RotatingFileHandler(fileName, maxBytes)
    fh.setLevel(desiredLevel)
    fh.setFormatter(formatter)
    # add the handler to logger
    logger.addHandler(fh)

  format = "%(asctime)-15s - %(levelname)-6s - %(message)s"
  formatter = logging.Formatter(format)
  # Clean up root logger
  for handler in logging.getLogger('').handlers:
    logging.getLogger('').removeHandler(handler)
  openScreenLog(format, desiredLevel)

  if mode == "File" or mode == "RollingFile":
    if not os.path.isdir(logDirectory):
      shellutils.mkdir(logDirectory)

    if mode == "File":
      openScreenAndFileLog(logPath, formatter, desiredLevel)

    elif mode == "RollingFile":
      openScreenAndRotatingFileLog(
        logPath, formatter, desiredLevel, LOG_MAX_BYTES)


def closeLog():
  '''This function is for shutdown the logging job
  '''
  logging.shutdown()


def checkInput():
  '''This function is for managing the user command line parameters
  '''
  p = argparse.ArgumentParser(description=__description__,
                prog=__program__)
  args = p.parse_args()


def move(fromFullPath, toFullPath):
  '''This procedure moves only the files in the subdirectories, merges the directories with the same name and performs a secure copy
  '''
  logging.debug("move: " + "Moving all the content from " +
          fromFullPath + " to " + toFullPath)
  # TODO: mv function should be the one in shell utils
  # TODO: splitted copies between devices

  # Identify unknownFiles: every not allowed dir and every file except
  # location.default
  unknownFiles = []
  directories = []
  for entity in shellutils.ls(fromFullPath, fullPath=True):
    if os.path.isdir(entity):
      if shellutils.basename(entity) not in ALLOWED_FOLDERS:
        unknownFiles.append(entity)
      else:
        directories.append(entity)
    elif shellutils.basename(entity) != DEFAULT_LOCATION_FILE:
      unknownFiles.append(entity)

  # Every unknown entity should be in the SOURCE "Other" folder, so move it
  otherFullPath = os.path.join(fromFullPath, OTHER_RELATIVE_PATH)
  for entity in unknownFiles:
    if not shellutils.exists(otherFullPath):
      shellutils.mkdir(otherFullPath)
      directories.append(otherFullPath)
    shellutils.mv(entity, otherFullPath)

  # Make the real work here!!
  for directory in directories:
    dirFullPath = os.path.realpath(os.path.join(
      toFullPath, shellutils.basename(directory), '.'))
    if not shellutils.exists(dirFullPath):
      shellutils.mkdir(dirFullPath)
    for entity in shellutils.ls(directory, fullPath=True):
      if shellutils.du(entity) < VOLUME_LIMIT_PER_FILE:
        # Muevo cada objeto que esta dentro de las carpetas
        # clasificadas de la queue origen a la misma carpeta de la
        # queue destino
        shellutils.mv(entity, dirFullPath)


def hasLocationFile(queue):
  '''This function returns if the selected queue has a default location and what it is
  '''
  for eachFile in shellutils.ls(os.path.join(shellutils.pwd(), queue)):
    if eachFile == DEFAULT_LOCATION_FILE:
      f = open(os.path.join(shellutils.pwd(), queue, eachFile))
      try:
        destiny = f.readline()
        # Remove trailing line feed if any
        destiny = destiny.split("\n")[0]
      finally:
        f.close()
      logging.debug("hasLocationFile: " + "The queue " + queue +
              " has location file, and it points to " + destiny)
      return destiny
  logging.debug("hasLocationFile: " + "The queue " +
          queue + " has no location file")
  return None


def getConnectedSystems():
  '''Returns a list with all the subsystems and its paths
     The output is a list of dicts holding the name and the path for each subsystem
  '''
  result = []
  if sys.platform.startswith("linux"):
    for l in file('/proc/mounts'):
      if l[0] == '/':
        s = {'name': l.split()[1].split("/")[-1],
             'path': l.split()[1],
             'fs':   l.split()[2]}
        if isSystemConnected(system=system):
          result.append({'name': shellutils.basename(system), 'path': system})

  elif sys.platform.startswith("win"):
    import string
    import ctypes

    def get_drives():
      drives = []
      bitmask = ctypes.windll.kernel32.GetLogicalDrives()
      for letter in string.ascii_uppercase:
        if bitmask & 1: drives.append(letter)
        bitmask >>= 1
      return drives

    for system in get_drives():
      spath = "{}:\\".format(system)
      volumeNameBuffer = ctypes.create_unicode_buffer(1024)
      fileSystemNameBuffer = ctypes.create_unicode_buffer(1024)
      ctypes.windll.kernel32.GetVolumeInformationW(
          ctypes.c_wchar_p(spath),
          volumeNameBuffer,
          ctypes.sizeof(volumeNameBuffer),
          None,
          None,
          None,
          fileSystemNameBuffer,
          ctypes.sizeof(fileSystemNameBuffer)
      )
      s = {'name': volumeNameBuffer.value,
           'path': spath,
           'fs':   fileSystemNameBuffer.value}
      if isSystemConnected(system=s):
        result.append(s)

  else:
    raise Exception("Platform not supported")

  return result

def isSystemConnected(system):
  '''Returns if a system is connected (it means that have a queues folder)
  '''
  return os.path.exists(os.path.join(system['path'], QUEUES_RELATIVE_PATH))

def main():
  '''Main function
  '''
  # For every system connected to this one (Only the connected ones! At
  # least the one executing this)
  for sourceSystem in getConnectedSystems():
    logging.info("main: Analyzing {} queues".format(sourceSystem['name']))

    # It is a valid system if it has queues
    if shellutils.cd(os.path.join(sourceSystem['path'], QUEUES_RELATIVE_PATH)):

      # For every queue in that system
      for queue in shellutils.ls(shellutils.pwd(), fullPath=True):

        destinationSystem = {
          'name': shellutils.basename(queue),
          'sourceQueue': queue,
          'destinationQueue': os.path.join(
            drivesPath,
            shellutils.basename(queue),
            QUEUES_RELATIVE_PATH,
            shellutils.basename(queue))}

        # If the queue is the system that is being analyzed itself, skip
        if destinationSystem['name'] == sourceSystem['name']: continue

        logging.info("main:  Analyzing {} queue of system {}".format(destinationSystem['name'], sourceSystem['name']))

        # Only if that system is connected: Direct transfer
        if isSystemConnected(destinationSystem['name']):

          logging.info("main:   {} to be copied to its final destiny {}".format(destinationSystem['sourceQueue'], destinationSystem['destinationQueue']))

          # Move all the stuff
          #move(destinationSystem['sourceQueue'],destinationSystem['destinationQueue'])

          # Notify info
          logging.info("main:   {} copied to its final destiny {}".format(destinationSystem['sourceQueue'], destinationSystem['destinationQueue']))

        # If it is not connected: Derived transfer
        else:
            # Search for the forward info file
            forward = hasLocationFile(destinationSystem['name'])

            if forward is not None:
              if isSystemConnected(forward):

                middlemanQueue = os.path.join(
                  drivesPath, forward, QUEUES_RELATIVE_PATH, destinationSystem['name'])

                logging.info("main:   {} to be copied to the next step of the chain {}".format(destinationSystem['sourceQueue'], middlemanQueue)

                # Move all the stuff
                #move(destinationSystem['sourceQueue'], middlemanQueue)

                # Notify info
                logging.info("main:   {} copied to the next step of the chain {}".format(destinationSystem['sourceQueue'], middlemanQueue))

              else:
                # Notify info
                logging.info("main:   {} default location ({}) is not connected".format(destinationSystem['sourceQueue'], forward))

            else:

              # Notify info
              logging.info(
                "main:   {} default location file is not available".format(destinationSystem['sourceQueue']))

    logging.info("------------------------------")


# Entry point
if __name__ == '__main__':
  openLog(LOG_MODE, LOG_LEVEL)
  checkInput()
  main()
  closeLog()
