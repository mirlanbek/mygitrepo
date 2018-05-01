#!/bin/bash

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






