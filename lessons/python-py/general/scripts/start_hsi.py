#  **********************************************************************/
#  * Author:
#  *   Mirlan Tokonbekov <mirlan.ax.tokonbekov@mirlan.com>
#  **********************************************************************/

import shutil
import datetime
import unittest
import subprocess
from subprocess import Popen, PIPE
import sys
import time
import argparse
import os
import commands
import re
import glob
sys.path.append(os.path.dirname(os.path.abspath(sys.argv[0])) + "/..")
sys.path.append(os.path.dirname(os.path.abspath(sys.argv[0])) + "/../utils")
import getValue
import systemInfoCfg as syc
import fpgaDevice

retimer_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
logs = os.path.join(retimer_dir,"logs")

############################# SETTINGS ########################################## 
global bus
global port
global gbs
global internal
global external
global iter_num
global https_proxy
global git_opae_sdk
global project

project = "Alaska"                                  #  Options:      "Retimer", "Alaska"        --- FPGA bus number              
bus = "F0"                                          #  Options:      "F0", "F1", "F2"           --- FPGA bus number
port = "all"                                        #  Options:      "0", "1" , "all"           --- sockets or ports on Retimer card
gbs = "10"                                          #  Options:      "10", "40" for Retimer     ---  hssiE2Ee10G or hssiE2Ee40G gbs file
internal = True                                     #  Options:      True, False                --- Enable/Disable  internal test 
external = True                                     #  Options:      True, False                --- Enable/Disable  external test
iter_num = 1                                        #  Options:      1,2,3..n                   --- Itaration number
https_proxy = "http://proxy-chain.mirlan.com:912"
git_opae_sdk = "https://github.com/OPAE/opae-sdk.git"
alaska_release = "lab@atp-lab:/srv/data/XFER/fpga-regress/OPAE-Releases/1.0.0-RC5/Alaska_release_ww19.4.tar.gz"


#################################################################################


def clone_sdk():
    clone_cmd="export https_proxy={} ; git clone {} opae-sdk".format(https_proxy, git_opae_sdk)
    os.chdir(retimer_dir)
    if os.path.exists("opae-sdk"):
        shutil.rmtree("opae-sdk")
    print (retimer_dir)
    try:
        os.system(clone_cmd)
    except Exception as git_fail:
        print (git_fail)

def install_opae_tools_Alaska(bus):
    os.chdir(retimer_dir)
    os.system("scp -r {} {}".format(alaska_release,retimer_dir))
    os.system("tar zxf {} && pushd Alaska_release_* && tar zxf opae-tools-Alaska-* && cd opae-tools-Alaska-* && sudo yum install ./*.rpm -y ; popd".format(os.path.split(alaska_release)[1]))
    os.chdir(glob.glob(os.getcwd()+"/Alaska_release_*")[0])
    os.system("sudo ./init-optical.sh /sys/devices/pci0000\:%s/0000\:%s\:00.0/resource0"%(bus,bus))



def build_sdk():
    if os.path.exists(os.path.join(retimer_dir,"opae-sdk")):
        os.chdir(os.path.join(retimer_dir,"opae-sdk"))        
    if os.path.exists("build"):
        os.system("rm -rf build/*")
    else:
        os.mkdir("build")
    os.chdir("build")

    try:
        os.system("cmake .. -DCMAKE_BUILD_TYPE=Debug")
    except Exception as msg:
        print (msg)

    try:
        os.system("make hssi_config hssi_loopback")
    except Exception as msg:
        print (msg)

def busN(bus):
    if bus == "F0":
        cmd = "lspci | grep acc| awk -F ':' {'print $1'}| sed -n 1p"
    elif bus == "F1":
        cmd = "lspci | grep acc| awk -F ':' {'print $1'}| sed -n 2p"
    elif bus == "F2":
        cmd = "lspci | grep acc| awk -F ':' {'print $1'}| sed -n 3p"
    elif bus == "F3":
        cmd = "lspci | grep acc| awk -F ':' {'print $1'}| sed -n 4p"
    _,output=commands.getstatusoutput(cmd)
    return output

def is_MCP(bus):
    myType=fpgaDevice.check_FPGA_type(bus)
    if myType == "DCP":
        return False
    return True

def clear_status(bus):
    cmd="sudo hssi_loopback -B 0x{0} status clear".format(bus)
    print(cmd)
    os.system(cmd)

def load_gbs_Ret_e10(bus):
    os.chdir(retimer_dir)
    os.system("sudo fpgainfo errors -c all")
    cmd = "sudo fpgaconf -v -b 0x%s %s"%(bus,syc.bitstream10_Ret)
    print(cmd)
    os.system(cmd)

def load_gbs_Ret_e40(bus):
    os.chdir(retimer_dir)
    os.system("sudo fpgainfo errors -c all")
    cmd = "sudo fpgaconf -v -b 0x%s %s"%(bus,syc.bitstream40_Ret)
    print(cmd)
    os.system(cmd)

def validate_gbs(bus,gbs):    
    cmd = "sudo timeout 1s sudo hssi_loopback -B 0x{} send 0".format(bus)
    process = subprocess.Popen([cmd], stdout=PIPE, stderr=PIPE, shell=True)
    _,stderr = process.communicate()
    check_l = stderr.splitlines()[3].split(" ")[3].strip(",")
    try:
        assert int(check_l) != 0
    except AssertionError:
        print("                   ERROR:  hssiE2Ee{}G is not compatible GBS file for connected loopback device\n\t\t\t   PLEASE try  other gbs files".format(gbs))
        raise

def time_stamp():
    cmd="echo $(date +%Y-%m%d-%H%M)"
    ts=getValue.getValue(cmd).strip()
    return ts

def log_dir_name(bus,port,gbs):
    if project == "Retimer":
        dir="{}_{}_Retimer-port-{}_{}G".format(time_stamp(),bus,port,gbs)
    elif project == "Alaska":
        dir="{}_{}_Alaska".format(time_stamp(),bus,port)
    return dir

class tester (object):
    def __init__(self,bus=bus,port=port,gbs=gbs,internal=internal,external=external,iter_num=iter_num,project=project):

        self.busn = bus
        self.bus = busN(self.busn)
        self.port = port
        self.gbs = gbs
        self.dirname = os.path.join(logs,log_dir_name(self.bus, self.port,self.gbs))  # self.dirname is test directory name
        self.internal = internal
        self.external = external
        self.iter_num = iter_num
        self.project = project
        self.dest = "1"
        if self.port == "1":
            self.dest = "0"
        if self.project == "Alaska":
            self.dest = "0"
            self.gbs = "640"
        if not os.path.exists("/bin/fpgaconf"):
            os.system("pushd .. ; ./opaeInstall.sh ; popd")        

        if not os.path.exists(os.path.join(retimer_dir,"opae-sdk")):
            clone_sdk()
            build_sdk()

        if self.project == "Alaska":
            _,output = commands.getstatusoutput("rpm -qa| grep Alaska")
            if not output:
                install_opae_tools_Alaska(self.bus)

        if not is_MCP(self.bus):
            sys.exit("\n\n\n\n\n\t\t\tDCP IS NOT SUPPORTED\n\n\n")

        if self.gbs == "10":
            load_gbs_Ret_e10(self.bus)
            validate_gbs(self.bus,self.gbs)
            load_gbs_Ret_e10(self.bus)
        elif self.gbs == "40":
            load_gbs_Ret_e40(self.bus)
            validate_gbs(self.bus,self.gbs)
            load_gbs_Ret_e40(self.bus)
        

        if not os.path.exists(logs):
            os.mkdir(logs)

        if not os.path.exists(self.dirname):
            os.mkdir(self.dirname)

    def test_int(self):
        clear_status(self.bus)
        cmd1="sudo hssi_loopback -B 0x{} send {} ; echo tool returncode: $?".format(self.bus,self.port)
        log_file = "{}/internal-loopback.log".format(self.dirname)
        with open(log_file,"a+") as log:                
            process = subprocess.Popen([cmd1], stdout=PIPE, stderr=PIPE, shell=True)
            stdoutg, stderr = process.communicate()
            log.write("\n======================= Int iteration: "+str(it)+" ========================\n")
            log.write("Command: " + cmd1 + " \nfor bus: " + self.bus+" "+self.gbs+ " option "+" \n"*3)
            print(stderr)
            log.write(stderr)
            log.write(stdoutg)
            print(stdoutg)
            for i in stdoutg.splitlines():
                tx = re.findall("TX STAT.*",i)
                rx = re.findall("RX STAT.*",i)
                er = re.findall("RX CRC.*",i)        
                code = re.findall("tool returncode.*",i)

                if code:
                    global returncode
                    returncode = int(code[0].split(":")[1].strip())

                if tx:
                    global tx0
                    global tx1
                    tx0=tx[0].split(":")[1].split("|")[0].strip()
                    tx1=tx[0].split(":")[1].split("|")[1].strip()            
                if rx:
                    global rx0
                    global rx1
                    rx0=rx[0].split(":")[1].split("|")[0].strip()
                    rx1=rx[0].split(":")[1].split("|")[1].strip()            
                if er:
                    global er0
                    global er1
                    global resultInt            
                    er0=er[0].split(":")[1].split("|")[0].strip()
                    er1=er[0].split(":")[1].split("|")[1].strip()

            if self.port == "0":            
                diff = int(tx0) - int(rx0)
                resultInt = diff - int(er0)
            if self.port =="1":
                diff = int(tx1) - int(rx1)
                resultInt = diff - int(er1)

            if returncode:
                print("\n\n\n\n\t\t\tTOOL EXITED WITH RETURNED CODE {}\n\n\n".format(returncode))
                resultInt = returncode
            if self.project == "Alaska":
                ER = int(er0)
                TX = tx0
                RX = rx0
            else:
                    
                ER = int(er1) - int(er0)
                if self.port == "0":
                    RX = rx0
                    TX = tx0
                if self.port == "1":
                    RX = rx1
                    TX = tx1

            print("TX{}: {}".format(self.port,TX))
            print("RX{}: {}".format(self.port,RX))
            print("RX CRC ERR: %s"%abs(ER))

            if resultInt:
                log.write("\n"*2+"FAILED")
            else:
                log.write("\n"*2+"PASSED")
            log.flush()
            os.fsync(log)
        
    def test_ext(self):
        clear_status(self.bus)
        global log_file
        cmd2 = "sudo hssi_loopback -B 0x{0} send {1} {2} ; echo tool returncode: $?".format(self.bus,self.port,self.dest)
        log_file = "{}/external-loopback.log".format(self.dirname)
        with open(log_file,"a+") as log:                
            process = subprocess.Popen([cmd2], stdout=PIPE, stderr=PIPE, shell=True)
            stdoutg, stderr = process.communicate()
            log.write("\n====================== Ext iteration: "+str(it)+" ========================\n")
            log.write("Command: " + cmd2 + " \nfor bus: " + self.bus+" "+self.gbs+ " option "+" \n"*3)
            print(stderr)
            log.write(stderr)
            log.write(stdoutg)
            print(stdoutg)
            for i in stdoutg.splitlines():
                tx = re.findall("TX STAT.*",i)
                rx = re.findall("RX STAT.*",i)
                er = re.findall("RX CRC.*",i)
                code = re.findall("tool returncode.*",i)

                if code:
                    global returncode
                    returncode = int(code[0].split(":")[1].strip())

                if tx:
                    global tx0
                    global tx1
                    tx0=tx[0].split(":")[1].split("|")[0].strip()
                    tx1=tx[0].split(":")[1].split("|")[1].strip()            
                if rx:
                    global rx0
                    global rx1
                    rx0=rx[0].split(":")[1].split("|")[0].strip()
                    rx1=rx[0].split(":")[1].split("|")[1].strip()            
                if er:
                    global er0
                    global er1
                    global resultExt            
                    er0=er[0].split(":")[1].split("|")[0].strip()
                    er1=er[0].split(":")[1].split("|")[1].strip()

            if self.project == "Alaska":
                ER = int(er0)
                TX = tx0
                RX = rx0
            else:                
                if self.port == "0":
                    diff = int(tx0) - int(rx1)
                if self.port =="1":
                    diff = int(tx1) - int(rx0)
                resultExt = diff - int(er0) - int(er1)

                ER = int(er1) - int(er0)
                if self.port == "0":
                    RX = rx1
                    TX = tx0
                if self.port == "1":
                    RX = rx0
                    TX = tx1

            print("TX{}: {}".format(self.port,TX))
            print("RX{}: {}".format(self.dest,RX))
            print("RX CRC ERR: %s"%abs(ER))

            if len(str(RX)) < 3:
                print("RX STAT: "+str(RX)+"  means NONE or too less packets are transmitted and this will be considered as FAILED ")
                resultExt = 2
            
            if returncode:
                print("\n\n\n\t\t\t\TOOL EXITED WITH RETURNED CODE {}\n\n\n".format(returncode))
                resultExt = returncode

            if resultExt:
                log.write("\n"*2+"FAILED")
            else:
                log.write("\n"*2+"PASSED")
            log.flush()
            os.fsync(log)

class test(unittest.TestCase):
    def test_exec(self):
        prange = port
        if port == "all":
            prange = ("0","1")
        if project == "Alaska":
            prange = "0"
        for cport in prange:             
            p1 = tester(port=str(cport))
            global it
            for it in range(1,p1.iter_num+1):                
                if p1.internal:
                    print("\n\nInternal lpbk iteration: %d"%it)
                    p1.test_int()
                    self.assertEqual(resultInt, 0)

            if p1.project == "Alaska":
                print("reload Alaskagbs if needed")

            else:

                if p1.gbs == "10":
                    load_gbs_Ret_e10(p1.bus)
                elif p1.gbs == "40":
                    load_gbs_Ret_e40(p1.bus)

            for it in range(1,p1.iter_num+1):                
                if p1.external:
                    print("\n\nExternal lpbk iteration: %d"%it)
                    p1.test_ext()
                    self.assertEqual(resultExt, 0)

if __name__ == "__main__":
    unittest.main()


