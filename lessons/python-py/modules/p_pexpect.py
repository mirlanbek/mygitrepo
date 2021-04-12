import pexpect

def ipmi_reboot(username, password, bmc_ip):
    """
    Cold reboot the device using rmm.
    :return: exit code from ipmitool.
    """

    off_cmd = 'ipmitool -H ' + bmc_ip + ' -U ' + username + ' -I lanplus power off'
    on_cmd = 'ipmitool -H ' + bmc_ip + ' -U ' + username + ' -I lanplus power on'
    
    child = pexpect.spawn("bash")
    child.logfile = sys.stdout
    print ("Powering off: %s" % off_cmd)
    child.sendline(off_cmd)
    child.expect ('Password: ')
    child.sendline (password)
    child.expect ('Chassis Power Control: Down/Off')
    
    time.sleep (10)
    
    print ("Powering on: %s" % on_cmd)
    child.sendline(on_cmd)
    child.expect ('Password: ')
    child.sendline (password)
    child.expect ('Chassis Power Control: Up/On')
    child.close()
    print(child.exitstatus, child.signalstatus)
    
    return child.exitstatus
