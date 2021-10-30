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

