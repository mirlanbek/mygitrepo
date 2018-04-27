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


################ on comand line############   python start.py -a "savai" -t "monok" -k kayny   ###############
