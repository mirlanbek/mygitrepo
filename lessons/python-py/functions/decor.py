########  decorators #############################

def decor(x):

    def use_later():
        print("++++++++++++++++++++")
        x()
        print("+++++++++++++++++++++")
    return use_later

@decor
def test():
    print("\t\tOXOOOOO") 


# 1. Decorator degen - function syrtyndagyga  w\o ()  return  bolot 
# M:   return use_later





############################## New decor: pass args

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

def decor(x):

    def test(c):
        a = 80 * x(c)
        return a
    return test

@decor
def dollar(d):
    a = 10 * d
    return a
 
print(dollar(5)) 


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

###################### last version   ###############################

import os, sys

class Hero:
    lastname = "Sarykbays"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "salam " + self.lastname
    
    @property
    def member (self):
        return "Menin atym %s, jashym %d, al emi fiom %s"%(self.name, self.age, self.lastname)
    
    
    @classmethod
    def member2 (cls, name, age):
        cls.lastname = "Tokonov"
        if cls.__name__ == "Hero":
            print(cls.__name__)
            return cls(name, age)

    @staticmethod
    def is_girl(name):
        a=name
        if a == "Alina":
            return True
        else:
            return False
        return True


p1 = Hero("Daulet", 15)
print(p1.member)


p2=Hero.member2("Sayan",9)
q=p2.member
print(q)


p3 = Hero.is_girl("Alinaa")
print(p3)


