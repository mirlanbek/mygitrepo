#!/usr/bin/python
import os,sys
import re
import collections

cwd = os.path.dirname(os.path.abspath(sys.argv[0]))
file_name = os.path.join(cwd, "test.txt")
result_file = os.path.join(cwd, "new_text.txt")

class process_file (object):
    """
    For now, script works only for "sda-pt.sf"  file.
    In order to use this script rename test file names  with "sda-pt.sf"
    """

    def __init__(self,file):
        super(process_file,self).__init__()
        self.file = file
        self.body = []
        self.main_body = []
        self.full = []
        self.header = []

        with open(self.file,"r") as uid_file:
            disk_uid = uid_file.read().splitlines()
            for line in disk_uid:
                if not line.startswith("/"):
                    # print(line)
                    self.header.append(line)
                else:
                    self.body.append(line)


    def strip_line(self,line):
        self.full += self.header
        s_line=re.sub("\s+", "", line)
        return s_line


    #  workaround for getting the 3rd 4th dict keys
    @staticmethod
    def get_key(dic,n):
        keys = dic.keys()
        key = ""
        for a,b in enumerate(keys,1):
            if a == n:
                key += b
        return key

    # Changes disk order and values  for 3 and 4 partition
    @staticmethod
    def change_disk_names (dic,new_dic={}):
        for i,k in dic.items():
            new_dic[i] = dic[i]
            
        new_dic["sda5"] = new_dic[disk4]
        new_dic[disk4] = new_dic[disk3]
        new_dic[disk3] = new_dic["sda5"]
        new_dic.pop("sda5")

        # ######  the lines in [ body ] get str
    @staticmethod
    def parse_disk(disk,dict={}):
        for b_key,b_val in changed_body.items():
            if b_key == disk:
                for i in [ b_val.split(",") ]:
                    for c in i:
                         val_key = c.split("=")[0]
                         val_val = c.split("=")[1]
                         disk_sw = collections.OrderedDict()
                         disk_sw[val_key] = val_val
                         dict.update(disk_sw)

    def formatt (self, part_dict,disk):
        start = self.get_key(part_dict,1)
        size = self.get_key(part_dict,2)
        type = self.get_key(part_dict,3)
        uuid = self.get_key(part_dict,4)
        a1= "{} : {}=       {}, {}=    {}, {}={}, {}={}".format(disk,start,part_dict['start'],size,part_dict['size'],type,part_dict['type'],uuid,part_dict['uuid'])
        return a1



def main():
    p1 = process_file(file_name)
    body_lines={}
    for d_k in p1.body:
        disk_key= p1.strip_line(d_k).split(":")[0]
        disk_value =  p1.strip_line(d_k).split(":")[1]
        body_line = collections.OrderedDict()
        body_line[disk_key] = disk_value
        body_lines.update(body_line)
    # print (body_lines)
    global disk1
    disk1 = p1.get_key(body_lines,1)
    global disk2
    disk2 = p1.get_key(body_lines,2)
    global disk3
    disk3 = p1.get_key(body_lines,3)
    global disk4
    disk4 = p1.get_key(body_lines,4)

    global changed_body
    changed_body={}             #----------------- ready
    p1.change_disk_names(body_lines,changed_body)
    # print(changed_body)

    ######################## Parse disk value ##############################

    boot_disk = {}
    root_disk = {}
    swap_disk = {}

    p1.parse_disk(disk2,boot_disk)
    p1.parse_disk(disk4,root_disk)
    p1.parse_disk(disk3,swap_disk)

    root = "start: 5244928, size: 124338176"
    swap= "start: 29583104,  size: 20971520"

    swap_disk['start'] = int(boot_disk['start']) + int(boot_disk['size'])
    root_disk['start'] = int(swap_disk['start']) + int(swap_disk['size'])

    real_body =[]
    for i in p1.body:
        if i.startswith(disk1) or i.startswith(disk2):
            real_body.append(i)

    for n in (swap_disk,root_disk):
        if n == root_disk:
            disk = disk4
        if n == swap_disk:
            disk = disk3
        real_body.append(p1.formatt(n,disk))
    print(real_body)

    if os.path.exists(result_file):
        os.remove(result_file)
    p1.whole_body = p1.header + real_body
    for i in p1.whole_body:
        with open("new_text.txt","a+") as new_uid:
            new_uid.write(i + "\n")


if __name__ == '__main__':
    main()



# vi test.txt:

#label: gpt
#label-id: F8EC2324-35FA-4FB4-81CF-67316C1A17BB
#device: /dev/sda
#unit: sectors
#first-lba: 34
#last-lba: 234441614
#
#/dev/sda1 : start=        2048, size=     1048576, type=C12A7328-F81F-11D2-BA4B-00A0C93EC93B, uuid=B6A6BDE7-F76C-48F5-AA05-4276ECE6AA61, name="EFI System Partition"
#/dev/sda2 : start=     1050624, size=     4194304, type=EBD0A0A2-B9E5-4433-87C0-68B6B72699C7, uuid=0873E9DE-8663-487F-A0AC-DBE870F39326
#/dev/sda3 : start=     5244928, size=   124338176, type=EBD0A0A2-B9E5-4433-87C0-68B6B72699C7, uuid=623B428D-6782-488C-915F-F8243E4B48BD
#/dev/sda4 : start=   129583104, size=    20971520, type=0657FD6D-A4AB-43C4-84E5-0933C84B4F4F, uuid=284D59E0-6816-4F7C-ABE3-2EBAE51706BE
#


