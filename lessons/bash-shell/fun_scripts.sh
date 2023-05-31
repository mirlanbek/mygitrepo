#!/bin/bash


# ------------ eval -------------------

net1=1-r-s-f-l
net2=2-f-e-f-s


for i in `seq 2`; do

        eval a=\$net$i
        echo $a

done


## ********************* add space with sed   ******************************

# sed '21i \       \ ma-01.ma.osh.com\:' ma2-23.yml

for host in `cat hosts.txt`; do

        if  grep -q $host ra2-2300.yml; then
                echo " "
                echo $host exists,  skipping...
                echo " "
        else
                GROUP=`echo $host | awk -F '-' {'print $3'}`
                GROUP_NUM=`grep -nr ${GROUP}: ra2-2300.yml | awk -F ':' {'print $1'}`
                INSERT_NUM=`expr ${GROUP_NUM} + 2`

                echo " "
                echo "$host doesn't exist, adding it to recipe..."
                echo " "
               sed -i "${INSERT_NUM}i \       \ $host\:" ra2-2300.yml
        fi
done




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


---- bul optiondu berip jana valusun dagy CLI dan----------  options step by step ----------------

while getopts "s:u:h" opt; do


        echo $OPTARG              # $OPTARGS value for option M:  ./sh.sh  -s LOLA  desen, echo $OPTARGS --> LOLA chygat
	echo $opt                 # 's'  chygat 

done

-----------------------------------------------------------------------------------------

while getopts 'a:u:h' opt ; do

        case $opt in
                a) echo bul option ALL=$opt ;;
                u) echo bul username is $OPTARG, option is $opt ;;
                h) usage ;;
                *) echo Give correct option

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

# --------------------------------------------------------------------------------------------------------------------

#!/bin/bash

# This script runs tests  until it passes or up to N times with reboot or without reboot
# Author: Mirlan Tokonbekov
# RUN  in ~/android-cts/tools directory " ./RETEST.sh -h "   to get help


tools_path=$PWD
cd $tools_path

n=3
reboot="no"
results_file=./results_file.txt

if [[ $# -le 0 ]]; then
        echo
        echo "No options are used. Please check ./RETEST.sh -h"
        echo
        exit 2
fi

help (){
        cat << EOF

cd ~/android-cts/tools/ directory


-m --- module   \$module

-t --- list of testcases in the file  \$test_list_file

-a --- ABI     \$abi

-s ---  serial |  \$host


=========================== below options are not mandatory, they have default values=======================


-n ---  number of times to test. Default '3'  |  \$n

-r ---  reboot='yes|no' Default 'NO' |   \$reboot

-h --  help


USAGE:  ./RETEST.sh -m CtsCameraTestCases -t ~/tests.txt -a x86_64 -s 4-6-4 -n 5 -r no


check ./results_file.txt for results

EOF
        exit 0
}


while getopts "s:t:a:m:n:r:h" option ; do
        case $option in

                s) host=$OPTARG ;;

                t) test_list_file=$OPTARG ;;

                a) abi=$OPTARG ;;

                m) module=$OPTARG ;;

                n) n=$OPTARG ;;

                r) reboot=$OPTARG ;;

                h) help ;;

                *) echo "Please provide currect options. see 'RETEST.sh -h' "
                   help


        esac

done


# echo "$host, $module, $test_list_file, $abi, $reboot, $n"


echo "" >> $results_file
echo "++++++++++++++ $abi $module STARTED at `date +\%Y-\%m\%d-\%H:\%M` ++++++++++++++++++++" >> $results_file
echo "" >> $results_file

for test in `cat $test_list_file`; do

    for i in `seq $n` ;do

        if [[ $reboot == 'yes' ]]; then

            while true; do
                echo '\n' | ~/bin/DUT_login_connect.sh $host
                adb devices | grep $host:22
                if [ $? == '1' ]; then
                        continue
                else

                    ./cts-tradefed run commandAndExit cts -m $module -t $test -s $host:22 -a $abi -d -o --disable-reboot
                    echo "" >> $results_file
                    echo $test >> $results_file
                    ./cts-tradefed list results 2>/dev/null | tail -n3 | head -n1 >> $results_file
                fi
                break
            done #while

        else # if no reboot
            ./cts-tradefed run commandAndExit cts -m $module -t $test -s $host:22 -a $abi -d -o --disable-reboot
            echo $test >> $results_file
            ./cts-tradefed list results 2>/dev/null | tail -n3 | head -n1 >> $results_file
        fi

        passed=`cat $results_file | tail -n1 |  awk '{if ($2 ~ "1") print $2}'`
        if [[ $passed == 1 ]]; then
                break
        fi

    done # for loop {1..5}


done # for loop `cat test_list_file`


############################################# SORT tests ____________________________

#!/bin/bash

# This script sorts output of failed testcase names copied from WRS.
# Author: Mirlan Tokonbekov
# RUN  in ~/android-cts/tools directory " ./SORT.sh -h "   to get help


if [[ $1 == "-h" || $# -le 0 ]]; then
cat << EOF

USAGE:  ./sort-failed-test_names.sh failed-tests-from-WRS.txt

The content of failed-tests-from-WRS.txt is copied output from WRS and should look like below:


EXAMPLE:
------------------

"1      android.server.am.ActivityManagerAssistantStackTests#testTranslucentAssistantActivityStackVisibility
FAIL
java.lang.AssertionError: Activity=org.chromium.arc.home/.HomeActivity must NOT be visible. expected:&lt;false&gt; but was:&lt;true&gt;&#13;          auto "


-------------------

Check ./sorted-tests.txt  file for results

EOF
exit 0

fi

while read line ; do
        if [[ -n ${line::1} && ${line::1} -gt 0 ]]; then
                IPS=' ' read -a a_line <<< $line
                echo ${a_line[1]}
                sleep 1
        fi

done < $1 | tee -a sorted-tests.txt

echo
echo done
echo "All test names stored in ./sorted-tests.txt file"


# -------------------------------------  FLASH OS  -----------------------------------------------------------------------------------------------------------


#!/bin/bash

select_mtc=""
while [ "$select_mtc" == "" ] ; do
    echo 'Please select from the following list (default is the latest)'
    echo "${weekly_mtc[@]}"
    read -r select_mtc
        if [ "$select_mtc" == "" ] ;then
            idx=${#weekly_mtc[@]}-1
            select_mtc=${weekly_mtc[$idx]}
            if [ ! -d $BASEDIR/$select_mtc ] ; then
                die 'Directory $BASEDIR/$select_mtc does not exist'
                exit 1
            fi
            break
        elif containsElement "$select_mtc" "${weekly_mtc[@]}" ;then
            break
        else
            echo 'Invalid entry.  Please try again'
            select_mtc=""
        fi
done

case "$platform" in
    "ncf" )
        rm -Rf /opt/APP
        if [ -d $BASEDIR/$select_mtc/MTCTEST ]; then
            pushd $BASEDIR/$select_mtc/MTCTEST
        elif [ -d $BASEDIR/$select_mtc/LinuxPackage ]; then
            pushd $BASEDIR/$select_mtc/LinuxPackage
        else
           die ' Failed to detect $select_mtc file structure'
        fi
        tar -cf - APP|(cd /opt;tar -xvf -)
        popd
        iconv -f utf16 /opt/APP/MTCVersion.txt
        echo $select_mtc now installed in /opt/APP
        ;;
    "bmp" )
        rm -Rf /opt/BMP-*
        if [ -d $BASEDIR/$select_mtc/MTCRHELDir ]; then
            pushd $BASEDIR/$select_mtc/MTCRHELDir
        else
           die ' Failed to detect $select_mtc file structure'
        fi
        mkdir /opt/$select_mtc
        tar -cf - MTCpkg  files |(cd /opt/$select_mtc; tar -xvf -)
        echo $select_mtc now installed in /opt/$select_mtc
        ;;
esac


########################################### Update grub ########################################

#!/bin/bash


# Make sure only root can run our script
if [ $EUID -ne 0 ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
export fptdir=/net/ttp-fs1/export/tools/ISO/MTC/fpt/kernels/fpt2/
# Rebuild grub in a better way
# Restore the original that we clobbered earlier
cp $fptdir/40_custom.orig /etc/grub.d/40_custom
if [[ -e /etc/grub.d/bak/10_linux ]] ;then
    mv /etc/grub.d/bak/10_linux /etc/grub.d/
    rm -Rf /etc/grub.d/bak/
fi

# Make sure grub will save our menu selection so we can reboot to the same kernel w/o user intervention
if ! grep -q "GRUB_DEFAULT=saved" /etc/default/grub ;then
    if grep -q "GRUB_DEFAULT=" /etc/default/grub ;then
        sed -i "s,^\(GRUB_DEFAULT=\).*,\1'saved'," /etc/default/grub
    else
        echo GRUB_DEFAULT=saved >>/etc/default/grub
    fi
fi
if ! grep -q "GRUB_SAVEDEFAULT=true" /etc/default/grub ;then
    if grep -q "GRUB_SAVEDEFAULT=" /etc/default/grub ;then
        sed -i "s,^\(GRUB_SAVEDEFAULT=\).*,\1'true'," /etc/default/grub
    else
        echo GRUB_SAVEDEFAULT=true >>/etc/default/grub
    fi
fi

# While we're at it, make sure the kernel parameters are correct
if ! grep "GRUB_CMDLINE_LINUX" /etc/default/grub | grep -q "console=ttyS0,115200";then
    if grep -q "GRUB_CMDLINE_LINUX=" /etc/default/grub ;then
        sed  -i 's/^\(GRUB_CMDLINE_LINUX=\).*/\1"crashkernel=auto earlyprintk=ttyS0,115200 console=ttyS0,115200 console=tty0 default_hugepagesz=1G hugepagesz=1G hugepages=32"/' /etc/default/grub
    else
        echo  'GRUB_CMDLINE_LINUX="crashkernel=auto earlyprintk=ttyS0,115200 console=ttyS0,115200 console=tty0 nomodeset modprobe.blacklist=qat_c62x default_hugepagesz=1G hugepagesz=1G hugepages=32"' >>/etc/default/grub
    fi
fi

# New BMC firmware requires a couple of extra things unless we are on the 4.10+ kernels
if ! grep "GRUB_CMDLINE_LINUX" /etc/default/grub | grep -q "nomodeset modprobe.blacklist=qat_c62x" ; then
    sed  -i 's/^\(GRUB_CMDLINE_LINUX=\).*/\1"nomodeset modprobe.blacklist=qat_c62x"/' /etc/default/grub
fi

# Backup old grub config (in case we screw up)
cp /boot/grub2/grub.cfg /boot/grub2/grub.cfg.tbd

# Rebuild the grub menu to get the new kernels
echo Building base grub menu
grub2-mkconfig -o /boot/grub2/grub.cfg

# But wait, there's more!  Need entries for IOMMU.  Now for some fun scripting.
echo Extracting kernel entries to customize
sed  -n '/(4.12.8/,/^}/p' /boot/grub2/grub.cfg >>/etc/grub.d/40_custom
sed  -n '/(4.7.0/,/^}/p' /boot/grub2/grub.cfg >>/etc/grub.d/40_custom
sed  -n '/(3.10.0/,/^}/p' /boot/grub2/grub.cfg >>/etc/grub.d/40_custom

# Add a blank line at the end as required by grub2-mkconfig
echo >>/etc/grub.d/40_custom

# Make chages for IOMMU
echo Rebuilding grub menu with added options for IOMMU.
sed -i 's/(Maipo)/(Maipo) IOMMU/g' /etc/grub.d/40_custom
sed -i '/linuxefi/ s/$/ intel_iommu=on,strict/g' /etc/grub.d/40_custom

# Make 40_custom executable (otherwise all is for nothing)
if [[ ! -x /etc/grub.d/40_custom ]] ;then
    chmod +x /etc/grub.d/40_custom
fi

# Rebuild the grub menu to get the new kernels and IOMMU
grub2-mkconfig -o /boot/grub2/grub.cfg
grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg

echo Finished


################################ convert rehel 7.3 to 7.4  #########################


#!/bin/bash

die() {
    echo $1
    echo "Press <Enter> to continue"
    read
    exit 1
}

disableRepos() {
    echo Disabling all repos
    repoList=(`yum repolist all 2>&1|grep enabled | awk '{print $1}'`)
    for repo in ${repoList[*]}; do
        yum-config-manager --disable $repo
    done
}

fixRepos() {
    if [ -z "$1" ]; then
       die "Failure to call fixRepos properly."
    else
        rm /etc/yum.repos.d/*ttp-fs1*
        yum-config-manager --add-repo=/net/ttp-fs1/export/repos/rhel-$1/net_ttp-fs1.repo
        if [ -e /net/ttp-fs1/export/repos/rhel-$1-optional/net_ttp-fs1-optional.repo ]; then
            yum-config-manager --add-repo=/net/ttp-fs1/export/repos/rhel-$1-optional/net_ttp-fs1-optional.repo
        fi
    fi
}

restoreRepo() {
    if [ -z "$1" ]; then
       die "Failure to call fixRepos properly."
    else
       yum-config-manager --add-repo=/net/ttp-fs1/export/repos/rhel-$1/net_ttp-fs1.repo
        if [ -e /net/ttp-fs1/export/repos/rhel-$1-optional/net_ttp-fs1-optional.repo ]; then
            yum-config-manager --add-repo=/net/ttp-fs1/export/repos/rhel-$1-optional/net_ttp-fs1-optional.repo
        fi
       yum clean all
    fi
}

echo This script will upgrade RHEL 7.x to RHEL 7.4

if [[ $EUID != 0 ]]
then
    echo "Please run as root."
    exit
fi

if [ -z $STY ] ;
then
   echo Rerunning in screen
   if [[ ! -x `which screen` ]];
   then
       yum install screen
   fi
   screen -L $0
   exit
else
   echo "Running in screen.  If your connection drops, reconnect with 'screen -r $STY'"
fi

. /etc/os-release

case "$VERSION_ID" in
    "7.2" )
        read -p "This will update your system to RHEL 7.4  Press <CTRL-C> to stop, <enter> to continue"
        disableRepos
        fixRepos 7.2
        ;;
    "7.3" )
        read -p "This will update your system to RHEL 7.4  Press <CTRL-C> to stop, <enter> to continue"
        disableRepos
        fixRepos 7.3
        ;;
    * )
        echo Not running Redhat Release 7.2 or 7.3, exiting
        exit 255
        ;;
esac

echo Updating repo to RHEL 7.4
yum-config-manager --add-repo=/net/ttp-fs1/export/repos/rhel-7.4/net_ttp-fs1.repo
yum-config-manager --add-repo=/net/ttp-fs1/export/repos/rhel-7.4-optional/net_ttp-fs1-optional.repo
yum-config-manager --add-repo=/net/ttp-fs1/export/repos/fpt/net_ttp-fs1-custom.repo
yum-config-manager --enable net_ttp-fs1*
yum clean all
echo Upgrading to RHEL 7.4
#yum distribution-synchronization || restoreRepo $VERSION_ID && die "User canceled or system failed"
yum distribution-synchronization
echo Yum finished with $?
echo System update complete.  Please reboot for the updates to take effect.

echo "Press <Enter> to continue"
read

exit

=================================================================================================================


#!/bin/bash




LOGFILE=/tmp/auto-flash.log

if [[ $# -le 2 ]]; then
        echo
        echo "No options are used. Please check ./auto-flash.sh -h"
        echo
        exit 2
fi


function usage() {
        echo "-i ip address of target machine"
        echo "-c cygdrive letter"
        echo "-h help usage"
        echo "./auto-flash.sh -i 14.1.4.77 -c e"
}

while getopts "i:c:h-:" opt; do
        case "${opt}" in

                i)
                        ip=$OPTARG
                ;;
                h)
                        usage
                        exit 0
                ;;
                c)
                        l=$OPTARG
                ;;
                *)
                        echo "  Invalid argument: $OPTARG"
                        usage
                        exit 1
                ;;
        esac
done

cygdr=/cygdrive/$l/Resources/

function bios_reset(){

                    rm -rf /tmp/REGS
                    mkdir /tmp/REGS
                    unzip /cygdrive/$l/EMM_REGS_DUMP/*.zip -d /tmp/REGS
                    ./RegDump.sh -H $ip -u super -p pass -a config -f /tmp/REGS/EMM_REGS_FPGA                      | tee -a ${LOGFILE}
                    ./RegDump.sh -H $ip -u super -p pass -a config -f /tmp/REGS/EMM_REGS_CPU_SKL_CSR               | tee -a ${LOGFILE}
                    ./RegDump.sh -H $ip -u super -p pass -a config -f /tmp/REGS/EMM_REGS_CPU_SKL_MSR               | tee -a ${LOGFILE}

                    cp -r  /cygdrive/$l/BIOS_SETTINGS/defaultbiossetup* /tmp/REGS/defaultbiossetup
                    ./BiosSettings.sh -H $ip -u super -p pass -a copy -f /tmp/REGS/defaultbiossetup                | tee -a ${LOGFILE}
                    echo 'y' |./BiosSettings.sh -H $ip -u super -p pass -a reset                                   | tee -a ${LOGFILE}
}               

for tool in  FWupg.sh FwUpg.sh ; do


    if [ $tool == "FwUpg.sh" ]; then


        echo 'y' |./FwUpg.sh -H $ip -u super -p pass -D /cygdrive/$l -a upg -M all -f -T 16                | tee -a ${LOGFILE}


    elif [ $tool == "FWupg.sh" ]; then

        for i in BIOS BMC LMC FPGA MCPLD PCPLD ; do

            echo $i

            case $i in

                BIOS)
                    bios_fw=$(ls -1 $cygdr/BIOS |sed -n '1p')
                    ./FWupg.sh -H $ip -u super -p pass  -a upg -b -r -d $cygdr/BIOS -F $bios_fw -E BIOS            | tee -a ${LOGFILE}
                ;;

                BMC)
                    bmc_fw=$(ls $cygdr/EMM/|grep -i bmc)
                    ./FWupg.sh -H $ip -u super -p pass -a upg -d $cygdr/EMM -F $bmc_fw -E MC                       | tee -a ${LOGFILE}
                ;;

                LMC)
                    lmc_fw=$(ls $cygdr/EMM|grep -i lmc)
                    ./FWupg.sh -H $ip -u super -p pass -a upg -d $cygdr/EMM -F $lmc_fw -E LMC -M 16                | tee -a ${LOGFILE}
                ;;

                FPGA)
                    fpga_fw=$(ls $cygdr/FPGA/ | grep -i fpga_cpb)
                    ./bsmFWupg.sh -H $ip -u super -p pass -a upg -d $cygdr/FPGA -F $fpga_fw -E MAIN_FPGA              | tee -a ${LOGFILE}
                ;;

                MCPLD)
                    mcpld_fw=$(ls $cygdr/CPLD/ | grep -i cpld_io) 
                    ./FWupg.sh -H $ip -u super -p pass -a upg -d $cygdr/CPLD -F $mcpld_fw -E MCPLD                | tee -a ${LOGFILE}
                ;;

                PCPLD)
                    pcpld_fw=$(ls $cygdr/CPLD/ | grep -i cpld_p)
                    ./FWupg.sh -H $ip -u super -p pass -a upg -d $cygdr/CPLD -F $pcpld_fw -E PCPLD                | tee -a ${LOGFILE}
                ;;


            esac
        done

    fi
done

bios_reset


