
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
sys.path.append(os.path.dirname(os.path.abspath(sys.argv[0])) + "/..")
sys.path.append(os.path.dirname(os.path.abspath(sys.argv[0])) + "/../utils")
import getValue
import systemInfoCfg as syc

retimer_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
logs = os.path.join(retimer_dir,"logs")

def clone_sdk():
    clone_cmd="export https_proxy=http://proxy-chain.mirlan.com:912 ; git clone https://github.com/OPAE/opae-sdk.git opae-sdk"
    os.chdir(retimer_dir)
    if os.path.exists("opae-sdk"):
        shutil.rmtree("opae-sdk")
    print (retimer_dir)
    try:
        os.system(clone_cmd)
    except Exception as git_fail:
        print (git_fail)

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

def clear_bus(bus):
    cmd="sudo fpgainfo errors -b 0x{0} -c all ; sudo hssi_loopback -B 0x{0} status clear".format(bus)
    print(cmd)
    os.system(cmd)

def load_gbs_Ret_10(bus):
    os.chdir(retimer_dir)
    cmd = "sudo fpgaconf -v -b 0x%s %s"%(bus,syc.bitstream10_Ret)
    print(cmd)
    os.system(cmd)

def load_gbs_Ret_40(bus):
    os.chdir(retimer_dir)
    cmd = "sudo fpgaconf -v -b 0x%s %s"%(bus,syc.bitstream40_Ret)
    print(cmd)
    os.system(cmd)

def time_stamp():
    cmd="echo $(date +%Y-%m%d-%H%M)"
    ts=getValue.getValue(cmd).strip()
    return ts

def log_dir_name(bus,soc):
    dir="{}_{}_Retimer-socket{}".format(time_stamp(),bus,soc)
    return dir

class tester (object):
    def __init__(self,bus="F1",soc="0",gbs="40",internal=False,external=True,dest=str(1),build=True,iter_num=1):
        self.busn = bus
        self.bus = busN(self.busn)
        self.soc = soc
        self.gbs = gbs
        self.dirname = os.path.join(logs,log_dir_name(self.bus, self.soc))  # self.dirname is test directory name
        self.internal = internal
        self.external = external
        self.build = False
        self.iter_num = iter_num
        self.dest = dest

        if not os.path.exists("/bin/fpgaconf"):
            os.system("pushd .. ; ./opaeInstall.sh ; popd")        

        if not os.path.exists(os.path.join(retimer_dir,"opae-sdk")):
            clone_sdk()
            build_sdk()

        if not os.path.exists("/bin/hssi_loopback"):
            sys.exit("Please install hssi_loopback")

        clear_bus(self.bus)

        if self.gbs == "10":
            load_gbs_Ret_10(self.bus)
        if self.gbs == "40":
            load_gbs_Ret_40(self.bus)

        if not os.path.exists(logs):
            os.mkdir(logs)

        if not os.path.exists(self.dirname):
            os.mkdir(self.dirname)

    def test_int(self):
        cmd1="sudo hssi_loopback -B 0x{} send {}".format(self.bus,self.soc)
        log_file = "{}/intternal-loopback.log".format(self.dirname)
        with open(log_file,"a+") as log:                
            process = subprocess.Popen([cmd1], stdout=PIPE, stderr=PIPE, shell=True)
            stdoutg, stderr = process.communicate()
            log.write("\n======================= iteration: "+str(it)+"========================\n")
            log.write("command: " + cmd1 + ": \nfor bus: " + self.bus+" "+self.gbs+ "G option "+" \n"*3)
            print(stderr)
            log.write(stderr)
            log.write(stdoutg)
            print(stdoutg)
            for i in stdoutg.splitlines():
                tx = re.findall("TX STAT.*",i)
                rx = re.findall("RX STAT.*",i)
                er = re.findall("RX CRC.*",i)        
                if tx:
                    global tx0
                    global tx1
                    tx0=tx[0].split(":")[1].split("|")[0].strip()
                    tx1=tx[0].split(":")[1].split("|")[1].strip()            
                    print("tx0: "+tx0)
                if rx:
                    global rx0
                    global rx1
                    rx0=rx[0].split(":")[1].split("|")[0].strip()
                    rx1=rx[0].split(":")[1].split("|")[1].strip()            
                    print("rx0: "+rx0)
                if er:
                    global er0
                    global er1
                    global resultInt            
                    er0=er[0].split(":")[1].split("|")[0].strip()
                    er1=er[0].split(":")[1].split("|")[1].strip()
                    print("er0"+er0)
            if self.soc == "0":                 
                diff = int(tx0) - int(rx0)
                resultInt = diff - int(er0)
            if self.soc =="1":
                diff = int(tx1) - int(rx1)
                resultInt = diff - int(er1)
            if len(str(tx0)) < 3:
                print(str(tx0)+": bul eki emes")
                resultExt = 2

            if resultInt:
                log.write("\n"*2+"FAILED")
            else:
                log.write("\n"*2+"PASSED")
        
    def test_ext(self):
        global log_file
        cmd2 = "sudo hssi_loopback -B 0x{0} send {1} {2}".format(self.bus,self.soc,self.dest)
        log_file = "{}/external-loopback.log".format(self.dirname)
        with open(log_file,"a+") as log:                
            process = subprocess.Popen([cmd2], stdout=PIPE, stderr=PIPE, shell=True)
            stdoutg, stderr = process.communicate()
            log.write("\n====================== iteration: "+str(it)+"========================\n")
            log.write("command: " + cmd2 + ": \nfor bus: " + self.bus+" "+self.gbs+ "G option "+" \n"*3)
            print(stderr)
            log.write(stderr)
            log.write(stdoutg)
            print(stdoutg)
            for i in stdoutg.splitlines():
                tx = re.findall("TX STAT.*",i)
                rx = re.findall("RX STAT.*",i)
                er = re.findall("RX CRC.*",i)        
                if tx:
                    global tx0
                    global tx1
                    tx0=tx[0].split(":")[1].split("|")[0].strip()
                    tx1=tx[0].split(":")[1].split("|")[1].strip()            
                    print("tx0: "+tx0)
                if rx:
                    global rx0
                    global rx1
                    rx0=rx[0].split(":")[1].split("|")[0].strip()
                    rx1=rx[0].split(":")[1].split("|")[1].strip()            
                    print("rx1: "+rx1)
                if er:
                    global er0
                    global er1
                    global resultExt            
                    er0=er[0].split(":")[1].split("|")[0].strip()
                    er1=er[0].split(":")[1].split("|")[1].strip()
                    print("er0"+er0)
            if self.soc == "0":
                diff = int(tx0) - int(rx1)
            if self.soc =="1":
                diff = int(tx1) - int(rx0)
            resultExt = diff - int(er0) - int(er1)

            if len(str(tx0)) < 3:
                print(str(tx0)+": bul eki emes")
                resultExt = 2

            if resultExt:
                log.write("\n"*2+"FAILED")
            else:
                log.write("\n"*2+"PASSED")

class test(unittest.TestCase):
    def test_exec(self):       # test function has to be  started with "test_name()"
        p1 = tester()
        global it
        for it in range(1,p1.iter_num+1):                
            if p1.internal:
                p1.test_int()
                self.assertEqual(resultInt, 0)
                print("Errors: %d"%resultInt)

            if p1.external:
                p1.test_ext()
                self.assertEqual(resultExt, 0)
                print("Errors: %d"%resultExt)

if __name__ == "__main__":
    unittest.main()







