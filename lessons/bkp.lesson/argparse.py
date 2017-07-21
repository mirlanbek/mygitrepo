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

