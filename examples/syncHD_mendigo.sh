#!/bin/bash

echo Pon el screen antes de hacer esto tio!
read ok

#De mendigo a hd
echo "----Mendigo -> HD----"

 #videos transcodeados
echo "    ----Videos transcodeados----"
mkdir /media/sdc1/_queues/INCOMING/AVIS
mv -v /media/sdb1/_proceso/VIDEOS/AVIS/* /media/sdc1/_queues/INCOMING/AVIS/
sleep 5

 #incoming del mldonkey
echo "    ----Incoming----"
mkdir /media/sdc1/_queues/INCOMING/INCOMING_MLNET
mkdir /media/sdc1/_queues/INCOMING/INCOMING_MLNET/files
mkdir /media/sdc1/_queues/INCOMING/INCOMING_MLNET/directories
mv -v /media/sdb1/DOWNLOAD/INCOMING/files/* /media/sdc1/_queues/INCOMING/INCOMING_MLNET/files/
mv -v /media/sdb1/DOWNLOAD/INCOMING/directories/* /media/sdc1/_queues/INCOMING/INCOMING_MLNET/directories/
sleep 5

 #resto de cosas
echo "    ----Queues----"
mv -v /media/sdb1/_queues/A_HD/* /media/sdc1/_queues/INCOMING/
sleep 5
 
#De mendigo a florido
echo
echo
echo "----Mendigo -> florido----"
 #musica
echo "    ----Musica tratada----"
mkdir /media/sdc1/_queues/A_florido/4.-TRANSFERIR
mv -v /media/sdb1/_proceso/MUSICA/4.-TRANSFERIR/* /media/sdc1/_queues/A_florido/4.-TRANSFERIR/
sleep 5

 #resto de cosas
echo "    ----Queues----"
mv -v /media/sdb1/_queues/A_florido/* /media/sdc1/_queues/A_florido/
sleep 5


#De mama a HD
echo
echo
echo "----Mama -> HD----"
echo "    ----Queues----"
mv -v /media/emulatron/_queues/A_HD/* /media/sdc1/_queues/INCOMING/


#De quien sea a mendigo
echo
echo
echo "----* -> Mendigo----"
echo "    ----Queues----"
mv -v /media/sdc1/_queues/A_mendigo/* /media/sdb1/_queues/INCOMING/
sleep 5

