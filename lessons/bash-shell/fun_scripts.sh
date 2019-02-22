#!/bin/bash




## ********************* bash options  ******************************

function usage() {
        echo "Usage: ${0##*/} [-s <disk_size>] [-u <user name>]"
        echo "-s <disk_size> with postfix e.g. 2G        default: 1024M"
        echo "-u <user name>                     default: none"
}

while getopts "s:u:h-:" opt; do
        case "${opt}" in
                -)
                        echo "  Invalid argument: $OPTARG"
                        usage
                        exit 1
                ;;
                s)
                        size=$OPTARG
                ;;
                h)
                        usage
                        exit 0
                ;;
                u)
                        user_label=$OPTARG
                ;;
                *)
                        echo "  Invalid argument: $OPTARG"
                        usage
                        exit 1
                ;;
        esac
done




## *********************  new function  ******************************


get_available_port () {
  read LOWERPORT UPPERPORT < /proc/sys/net/ipv4/ip_local_port_range
  while :
  do
    PORT="`shuf -i $LOWERPORT-$UPPERPORT -n 1`"
    ss -lpn | grep -q ":$PORT "  || break
  done
  echo $PORT
}

echo $(get_available_port)


## *********************  read token  ******************************


#!/bin/bash

while read p; do

	  read -a line <<< "$p"
	    echo ${line[0]}

    done </samba/mir/miki.txt



    # while read p; do
    #   if [[ ! $p == \#* ]]
	    #   then
    #     if [[ "$p" =~ [^a-zA-Z0-9] ]]
    #     then
    #       IFS=' ' read -a token <<< "$p"
    #       git clone ${token[1]} ${token[0]}
    #       cd ${token[0]}
    #
    #       if [ "${token[2]}" = "master" ]
    #       then
    #         git checkout ${token[3]}
    #       else
    #         git checkout -b ${token[2]} ${token[3]}
    #       fi
    #
    #       cd /opt/stack
    #     fi
    #    fi
    # done </home/stack/s_commit_ids
    # echo -e "done cloning the Stack repos \n"


