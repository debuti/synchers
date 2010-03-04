#!/bin/bash
###############################################################################################
#  Author: Borja Garcia <debuti@gmail.com>
# Program: syncHD_florido.sh
# Descrip: This script syncs my pc and my portable hd
# Version: 0.0.0
#    Date: 2008-10-16:14:05:00
# License: This script doesn't require any license since it's not intended to be redistributed.
#          In such case, unless stated otherwise, the purpose of the author is to follow GPLv3.
###############################################################################################

# Constants
 HD_PATH="/media/disk"
 FLORIDO_PATH="/media/datos"

# Usage function

  function usage() {
    echo "">>/dev/null
  }
  
# Input validation function

  function checkInput() {
    echo "">>/dev/null
  }

# Helper functions
  
  
# Main function

  function main() {
    
   #De mendigo a hd
    echo "----Florido -> HD----"

    echo "    ----Queues----"
    mv -v "$FLORIDO_PATH"/_queues/A_HD/* "$HD_PATH"/_queues/INCOMING/
    sleep 5
 
   #De mendigo a florido
    echo
    echo
    echo "----Florido -> Mendigo----"

    echo "    ----Queues----"
    mv -v "$FLORIDO_PATH"/_queues/A_mendigo/* "$HD_PATH"/_queues/A_mendigo/
    sleep 5

   #De quien sea a mendigo
    echo
    echo
    echo "----* -> Florido----"
    
    echo "    ----Queues----"
    mv -v "$HD_PATH"/_queues/A_florido/* "$FLORIDO_PATH"/_queues/INCOMING/

    sync

  }

# Entry point
  checkInput $@
  main
