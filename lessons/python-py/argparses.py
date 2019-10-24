import argparse
import math

parser = argparse.ArgumentParser(description="Calculate valume of cylinder")
 

parser.add_argument('-r','--radius',type=int, help="ayant surabai googlefan kara")
parser.add_argument('-H','--height',type=int, help="Biyiktik menden surabai googledan kara")


args = parser.parse_args()


def cyl_vol (radius, height):
    vol=(math.pi)*(radius**2)*(height)
    return vol

print (  cyl_vol(args.radius, args.height)    )

######################################################

# import argparse
# import math


# pars_container = argparse.ArgumentParser("Cilinderdin ayntyn tabuu")

# pars_container.add_argument("-r","--radius", type=int, help="Bul degen radius")
# pars_container.add_argument("-H","--height", type=int, help="Bul degen biyiktik")

# argus = pars_container.parse_args()



# def syl_volue(height,radius):
#     vol = math.pi * height * radius
#     return vol
# print (  syl_volue(argus.height , argus.radius)   )


parse_er = argparse.ArgumentParser(description="This is description for pasrser")

parse_er.add_argument("--miki","-m",help="googldan sura")
parse_er.add_argument("--nurken", "-n", help="Latviyanyn googlanan sura")

args = parse_er.parse_args()


def family (miki,nurken):
    print("menin atym %s jana  ukam %s,  familyabyz Tokonbekov"%(miki,nurken))

family(args.miki, args.nurken)
################ on comand line############   python start.py -m "Mirlanbek" -n "Nurkenbek"   ###############
-------------------------------------------------------------------------------------------------------

import argparse
import os
import sys


class family:
    global lastname
    lastname = "Tokonbekov"

    def __init__(self, a_jurt, t_jurt, k_jurt):
        self.a_jurt = a_jurt
        self.t_jurt = t_jurt
        self.k_jurt = k_jurt

    def is_beka(self):
        if self.t_jurt == "monok":
            return True
        else:
            return False
        return True

    def is_emil(self):
        if self.t_jurt == "latysh":
            return True
        else:
            return False
        return True


    def member(self):
        if self.is_beka():
            return "menin atym Beka menin atamyn aty Mirlan fiom {} tagalarym {}, kainy jurtum {}".format(lastname, self.t_jurt, self.k_jurt)

        if self.is_emil():
            return "menin atym Emil menin atamyn aty Nurik fiom {} tagalarym {}, kainy jurtum {}".format(lastname, self.t_jurt, self.k_jurt)

parser = argparse.ArgumentParser(description="Family status script")
parser.add_argument("-a", "--atajurt", default=False, help = "Option about atajurt" )
parser.add_argument("-t", "--tagajurt", default=False, help = "Option about tagajurt" )
parser.add_argument("-k", "--k_jurt", default=False, help = "Option about k_jurt" )
args = parser.parse_args()

if args.tagajurt:
    t_jurt = args.tagajurt

if args.atajurt:
    a_jurt = args.atajurt

if args.k_jurt:
    k_jurt = args.k_jurt

a_jurt = lastname
t_jurt = "monok"
k_jurt = None



p1 = family(a_jurt, t_jurt, k_jurt)

print(p1.member())

---------------------------------------------------------------------------------------------------
#!/usr/bin/python
import os, sys
import argparse



class family (object):
    lastname = "Tokonbekov"

    def __init__(self,a_jurt,t_jurt,k_jurt):
        self.a_jurt = a_jurt
        self.k_jurt = k_jurt
        self.t_jurt = t_jurt


    @property
    def member(self):
        def is_beka():
            if self.a_jurt == "savai" and self.t_jurt == "monok":
                return True
            else:
                return False
            return True

        def is_emil():
            if self.a_jurt == "savai" and self.t_jurt == "latysh":
                return True
            else:
                return False
            return True



        if is_beka():
            return "Menin atym Beka Men Mirlandyn balasymyn i have no " +self.k_jurt
        if is_emil():
            return "Menin atym Emil Men Nurkendin balasy and i have no " + self.k_jurt

parser = argparse.ArgumentParser(description='Family Info')

parser.add_argument("-a", "--a_jurt", default = False, help = "ata jurtunu aitasin")
parser.add_argument("-t", "--t_jurt", default = False, help = "taga jurtunu aitasin")
parser.add_argument("-k", "--k_jurt", default = False, help = "kainy jurtunu aitasin")
args = parser.parse_args()
argsl = vars(args)

def check_args(argumentss):
    for i in argsl.keys():
        if argsl[i]:
            return True
        else:
            return False
    return True

if check_args(argsl):


    a_jurt = args.a_jurt
    k_jurt = args.k_jurt
    t_jurt = args.t_jurt


else:

    a_jurt = "savai"
    k_jurt = "Kayny jurt"
    t_jurt = "latysh"



p1=family(a_jurt,t_jurt,k_jurt)

print(p1.member)

# -----------------------------------------  LAST VERSION --------------------------------------------------

import argparse
import os, sys

class Family(object):
    lastname = "Tokonbekov"

    def __init__(self, a_jurt, t_jurt, k_jurt=None):
        self.a_jurt = a_jurt
        self.t_jurt = t_jurt
        self.k_jurt = k_jurt

    def is_beka(self):
        if self.t_jurt == "monok":
            return True
        else:
            return False
        return False

    def is_emil(self):
        if self.t_jurt == "latysh":
            return True
        else:
            return False
        return True

    def member(self):
        if self.is_beka():
            print("menin atym Beka menin ata jurtum %s jana \
                taga jurtum %s, menin kayny jurtum %s"%(self.a_jurt,self.t_jurt,self.k_jurt))

        if self.is_emil():
            print("menin atym Emil menin ata jurtum %s jana \
                taga jurtum %s, menin kayny jurtum %s"%(self.a_jurt,self.t_jurt,self.k_jurt))

parser = argparse.ArgumentParser(description="Fammily info")

parser.add_argument("-a", "--a_jurt", default=False, help="Ata jurtunu Aitkin")
parser.add_argument("-t", "--t_jurt", default=False, help="Taga jurtunu ait")
parser.add_argument("-k", "--k_jurt", default=False, help="Kainy jurtunu ait")

args = parser.parse_args()


a_jurt = "Savai"
k_jurt = None
t_jurt = 'monok'

# NOTE: compare here with other versions above , this looks shorter, using '--a_jurt' as args.a_jurt

if args.a_jurt:
    a_jurt = args.a_jurt
    print(a_jurt)
else:
    a_jurt = a_jurt

if args.t_jurt:
    t_jurt = args.t_jurt
    print(t_jurt)
else:
    t_jurt = t_jurt




p1 = Family(a_jurt,t_jurt)
p1.member()



################ on comand line############   python start.py -a "savai" -t "monok" -k kayny   ###############
