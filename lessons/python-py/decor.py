### New decor: pass args

import os, sys


def dir_maker(get_file):
    def wrapper (f):
        name = get_file(f).split(".")[0]
        print(name)
        # os.mkdir(os.path.join(os.getcwd(), name))
    return wrapper

@dir_maker
def get_file(f):
    return f

get_file("photo.img")


#####################################
def greet (name):
    def message():
        return "Salam "+ name
    result = message() + " kandai bala chaka jakshybby?"
    return result
a=greet("Miki")
print(a)

########################################


class employee():
    
    lastname = "Tokonbekov"

    def __init__(self,name='Mirlan',age=37):
        self.name = name
        self.age = age
        
    @property
    def onp(self):
        print("Bizdin baarybyzdyn familyabyz {}, atym  bolso {}, jashym {} jashta".format(employee.lastname,self.name,self.age))

emp1 = employee("Nurken",23)
emp1.onp


def decor (decorate):
    def wrapper():
        print("################## salam bul decorator ********************")
        decorate()
        print("################## bye ********************")
    return wrapper

@decor
def onp():
    print("Erten Ainash New-Yorkko ketet")

onp()
