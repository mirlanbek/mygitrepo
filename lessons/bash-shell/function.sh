#!/bin/bash
yesno ()
{
  while :
   do
	echo -n  "$* (Y/N)? " 
	read yn junk
     
      case $yn in
	y|Y|yes|YES|yeS) return 0 ;;
	no|NO|n|N|nO) return 1 ;;
	*) echo Please answer YES or NO ;;
      esac
  done
}
while true
        do
                if yesno Do you really wish to quit now
                then
                        exit
                fi
        done


