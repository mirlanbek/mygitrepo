------------------- install python3 env on Centos -------------------------------

sudo yum install centos-release-scl
sudo yum install rh-python38
python --version
scl enable rh-python38 bash
pip install virtualenv
 python -m virtualenv  ~/.venv
. ~/.venv/bin/activate


-----------------------------------------------------------------------

import os
import sys

f='file.txt'
sys.path.append(      os.path.join( os.path.dirname(os.path.abspath(sys.argv[0])), "utils"  )             )
import util

my_loc = os.getcwd()

my_file= my_loc + "/utils/" + f

o=open(my_file, "r")


for i in o.read().splitlines():
        if not i.startswith("#"):
                with open(my_loc + "/utils/file2","a+") as f2:
                        f2.write(i)

o.close()


times={
    "Japan": -16, 
    "Kyrgyzstan": -12,
    "Russia": -10
}

def time_zone(x):
    USA=time.localtime().tm_hour
    a=USA- times[x]
    return "For {}, it is {}".format(x,a)


print(time_zone("Russia"))

#!/root/.venv/bin/python
def get_tukum():
    return "Took tuudu"

def get_took():
    return "took, satyp aldym"


def get_rooster(tukum, took):
    # tooktun {tukum} tap
    # tukumdu {took}tu aldyna koi 30 kun
    # chojolordun ichinen korzun tap
    # any chonoit
    # urushkanga uirot
    return "Koroz"




Rooster = ( get_rooster(get_tukum(), get_took())   )
rooster = "Koroz"


print(Rooster)
print(rooster)




# --------------------------------------------------------
import os

def install_packages(x):
    os.system(r"echo 'yum install {x}' ")



def get_hostname():
    return os.system("hostname")



def is_hostname_set():
    if get_hostname() is not None:
        return True
    else:
        return False




def greeting(n):
    print ("E {}, kandaisyn?".format(n))


greeting("Venera")
b=greeting("Beka")

print(  get_hostname()   )

if get_hostname() == "DESKTOP-3U2JPUV":
    print("OK")

# if greeting("Venera") == ?:
#     print("OK")

# if install_packages("nmap") == ?

print(is_hostname_set())


# ----------------------------------------------------------

n = [12,23,34,41, 65, 50, 14]

m = [76,12,34,56,41]

box=[]

def five_maker(x):
    for i in x:
        b=str(i)
        if int(b[0]) + int(b[1]) == 5:
            box.append(i)
    return box


# print(five_maker(m))


import os, sys

os.chdir('/root')




def is_same(x, y):

    diff = os.system(' diff {} {}'.format(x,y))
    if diff != 0:
        return False
    else:
        return True



f1 = "file_3"
f2 = "file_2"


if is_same(f1,f2):
    print(f"{f1}  menen  {f2} Bul eki file chyndap okshosh eken")
else:
    print(f"{f1} menen  {f2}  Bul eki file  okshosh EMES eken")


-----------------------------

def money_converter(amount, currency_from, currency_to):

    ratio = {"USD": 1, "KGS": 85, "TL": 10}

    dol = amount / ratio[currency_from]

    if currency_from == "KGS":
        if currency_to == "USD":
            return dol
        elif currency_to == "TL":
            return dol * ratio["TL"]


    if currency_from == "TL":
        if currency_to == "USD":
            return dol
        elif currency_to == "KGS":
            return dol * ratio["KGS"]



print(money_converter(10, "TL", "KGS") )




#--------------------------------------------------------------



class Family:

    middle_name = 'Adykovich'

    def __init__(self, taga_jurt, ata_jurt, kainy_jurt):
        self.ata_jurt = ata_jurt
        self.taga_jurt = taga_jurt
        self.kainy_jurt = kainy_jurt
        


    def is_beka (self):

        if self.ata_jurt == "savai" and self.taga_jurt == "kytai":
            return True
     

    def is_emil (self):

        if self.ata_jurt == "savai" and self.taga_jurt == "latysh":
            return True


    def is_sayan (self):

        if self.ata_jurt == "monok" and self.taga_jurt == "savai":
            return True
    

    def member1(self):
        if self.is_beka():
            return "Menin atym Beka, men 16ga chyktym. Atam Mirlan"

        if self.is_emil():
            return "Menin atym Emil, men 10ga chyktym. Atam Nurik"

        if self.is_sayan():
            return "Menin atym Sayan, men 11ga chyktym. Atam Ilim"
        else:
            return "You are not in our family"



p1  =  Family("kytaii", "savai", None)

p2  =  Family("kytai", "savai", None)

p3  =  Family("latysh", "savai", None)

p4  =  Family("savai", "monok", None)


print (   p1.member1()   )

print (   p2.member1()   )

print (   p3.member1()   )

print (   p4.member1()   )




# ################################################ multiple Inheritances #####################################

# vi start.py:

balance=500
class Clothing:
    def __init__(self, shoes,pants,shirt,person):
        self.shoes=shoes
        self.pants=pants
        self.shirt=shirt
        self.person=person
        

    def shoe_fit(self):
        if self.person >= 16:
            if self.shoes<10.5:
                return "Shoes too small"
            elif self.shoes>=10.5:
                return "Fits perfectly"
        else:
            return "Your shoe size is from a kids 10 to an adults 10"
    def pants_fit(self):
        if self.person >= 16:
            if self.pants<33:
                return "Shoes too small"
            elif self.pants>=33:
                return "Fits perfectly"
        else:
            return "Your shoe size is from a kids 10 to an adults 10"

    def shirt_fit(self):
        if self.person >= 16:
            if self.shirt<18:
                return "Shirt too small"
            elif self.shirt>=18:
                return "Fits perfectly"
        else:
            return "Your shoe size is from a kids 10 to an adults 10" 
class Buy(Clothing):
    def __init__(self,year=None, shoes=None ,pants=None,shirt=None,person=None):
        self.year = year        
        Clothing.__init__(self,shoes,pants,shirt,person)

    def purchase(self):
        if self.shirt_fit() or self.pants_fit or self.shoe_fit == False:
            return "I have enough money to buy almost everything I want :D"
        else:
            return "I can't buy everything!"

# vi test.py:


import start

class Test(start.Buy):

    def __init__(self, age=None, year=None, shoes=None ,pants=None,shirt=None,person=None ):
        self.age = age
        start.Buy.__init__(self, year,shoes,pants,shirt,person)

    def test1(self):
        return "ishtedi"



# o = Test(16, 2022, 43, 33, 18, 16)
o = Test(person=13, shoes=43)


print(  o.shoe_fit()   )


# #################################################### end of multiple Inheritances ######################################

### Decorators

import os,sys



def choco(candy):
    def wrapper():
        print( "~~~~~~~~~~~~~~~~")
        candy()
        print("~~~~~~~~~~~~~~~~~~~~~")
    return wrapper

def caramel(candy):
    def wrapper():
            
        print("^-^-^-^-^")
        candy()
        print( "^-^-^-^-^-^-^-^")
    return wrapper

def cookie(candy):
    def wrapper():

        print("---------------")
        candy()
        print( "-------------------")
    return wrapper
    
@choco
@caramel
@cookie
def candy():
    print("Twix")

candy()


++++++++++++++++++++++++++ Dunders ++++++++++++++++++++++++

doc:   https://www.section.io/engineering-education/dunder-methods-python/  

class Family(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    



    def __repr__(self):
        return "This class prints developer's chapter"
   
    def __str__(self):
        return f"This class is about our familly {__name__}, {__class__}"




    def member(self):
        return f"My name is {self.name}, and i'm {self.age} {__file__} {__name__}"



p1 = Family("miki", 42)

print(p1.member())

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Setattr and getattr info

# setattr is when youre passing a new attribute with a value into the class. when you do add the atrtibute, it actually becomes part of the class
# and not like a demo. for example if you edit something in a string and when you print it, it prints it but the edit isn't actually final. this is the 
# opposite for setattr. syntax is setattr(object w/o quotations, "new attribute in quotations", value of that attribute)
class Random:
    def __init__(self, w1, w2, w3, w4):
        self.w1=w1
        self.w2=w2
        self.w3=w3
        self.w4=w4


    def test(self):
        return self.w1, self.w2,self.w3,self.w4, self.w5

p = Random(1,2,3,4)
setattr(p, "w5", 5)

#   getattr is basically calling the value of the attribute you want to call. syntax is getattr(Object w/o quotations, "attribute name in quotations")
class Random:
    def __init__(self, w1, w2, w3, w4):
        self.w1=w1
        self.w2=w2
        self.w3=w3
        self.w4=w4


    def test(self):
        return self.w1, self.w2,self.w3,self.w4

p = Random(1,2,3,4)

name = getattr(p, "w3")
print(name)




###########################################################



import requests
import json
import os, sys

# BMC info 
username = 'Administrator'
password ='Administrator'


# auth=(username, password)

ip='141.112.44.77'
url="http://141.112.44.77:8080/redfish/v1/Managers/BMC_0/LogServices/Messages/Entries"

resp=requests.get(url, auth=(username,password))

e=json.loads(resp.text)

print(len(e["Members"]))

# before you request and print it out in text form you have to first load it into the memory
# you can not manage it before you load it `
with open("peem.json", "w") as w:
    
    w.write(json.dumps(e))
       
# you need to dump the output in order to write it in a json file


# you cant write while its in the memory, therefore you need to dump it 


yum install jq
cat test.json | jq

cat test.json | jq '."Members"'

# if the output is in brackets, list
 
#cat test.json | jq '."Members" | .[] '

# 
#cat test.json | jq '."Members" | .[] | ."another key"'

#cat test.json  | jq '."Members" | .[-1]'




###############################################################

# Subprocess

#example ata made

from subprocess import Popen, PIPE
import subprocess, os

subprocess.call(["ping", "-c 4","google.com"],stdout=open("ping.log",'w'))
os.remove("ping.log")


process = Popen(['cat', '/home/tokonbekov/src/sixonix/xonotic/install.py'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
# print(stdout)  

s = subprocess.check_output(["ping", "-c 4", "google.com"])
output = s.decode("utf-8")
 
lines = output.split('\n')
 
for line in lines:
    print(line)


# our example




cmd="./start.sh"


with open("log.log", "w") as log:
    proc = subprocess.Popen(cmd, shell=True,
                            stderr=open(os.devnull, "w"),
                            stdout=subprocess.PIPE)


    (out, _) = proc.communicate()
    for line in out.decode().splitlines():
        log.write(str(line))


--------------------------- xml example 2 -----------------------------------
import xml.etree.ElementTree as ET

tree = ET.parse('first.xml')
for node in tree.iter():
    if int(node.attrib.get('age', 0)) > 21:
        node.attrib['alcohol'] = 'yes'
root = tree.getroot()
ET.register_namespace("", "XYZ")
print(ET.tostring(root))

-------
vi first.xml <--' 

<root xmlns="XYZ" usingPalette="">

<grandParent hostName="XYZ">
<parent>
        <child name="JohnsDad">
            <grandChildren name="John" sex="male" age="22" alcohol="no"/>
        </child>
        <child name="PaulasDad">
            <grandChildren name="Paula" sex="female" age="15" alcoho="no"/>
        </child>
</parent>
</grandParent>     
</root> 
----------------------------------------------------------------------------------


class School:
    def __init__(self, year, st_count, GPA):
        self.y=year
        self.st=st_count
        self.gpa=GPA


    def basketball(self):
        return "They make up " + str(50/self.st) + f"percent of our school in {self.y} and had a GPA of {self.gpa}"
    
    
    def average(self):
        return f"Average GPA is {self.gpa} out of {self.st} in the year {self.y}"

    @staticmethod ---  works exactly like normal function instead of a method which can only use the class's attributes
    def info(self):
        return f"The school was made {self.y} , and has {self.st} students enrolled in it and the average GPA is {self.gpa}"

    @classmethod --- You use the attributes of the class and replace one of the attributes with it. for example here we are trying to figure out a way to replace gpa using the rest of the attributes only and cls is to remind python that this is the final output and this would change all the other gpa's
    def get_gpa(cls,year, st_count,  gpu_spelled):
        d={"bir": 1, "eki": 2, "uch": 3, "tort":4}
        return cls(year,st_count, d.get(gpu_spelled, 4.0))
        

p1=School.get_gpa(1995, 245, "tort")


print(p1.info())

p2=School.info(1995, 245, 3.5)
print(p2)




