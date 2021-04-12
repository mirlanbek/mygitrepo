# Class

#  Class − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. 
#        The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

#  Class variable − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. 
#                 Class variables are not used as frequently as instance variables are.

#  Instance − An individual object of a certain class. 
#             An object obj that belongs to a class Circle, for example, is an instance of the class Circle
    
    
class enemy():

    lastname = "Jorge"                  #   this is class attribute, it belongs to all ojects.  it can be changed: enemy.lastname = "Mark"
    
    def __init__(self, name, age):      #    'name' and 'age'  are  class arguments or instance attribute
        self.name = name
        self.age = age

    def attack(self):
        print("{} attacks which is {} let".format(self.name,self.age))


p1=enemy("Niki",23)                      # p1 --- object
p2=enemy("Nuku",25)

p1.attack()
p2.attack()

class enemy():

    count=12

    def __init__(self, name="Nuku", age=25):
        self.name = name
        self.age = age

    def attack(self):
        print("{} attacks which is {} let, baary {}".format(self.name,self.age,enemy.count))


p1=enemy("Aibek",43)
p2=enemy()


p2.attack()
p1.attack()

class employee():

    lastname = "Tokonbekov"

    def __init__(self,name='Mirlan',age=37):
        self.name = name
        self.age = age


    def onp(self):
        print("Bizdin baarybyzdyn familyabyz {}, atym  bolso {}, jashym {} jashta".format(employee.lastname,self.name,self.age))

emp1 = employee("Nurken",23)
emp2=employee()

emp1.onp()
emp2.onp()

#!/usr/bin/env python

class family ():
    lastname = "Tokonbekov"

    def __init__(self, name,age):
        self.name=name
        self.age=age

    def member(self):
        return "Bizdin baarybyzdyn familyabyz {}, atym {} jana men {} jashtamyn".format(family.lastname,self.name,self.age)

member1=family("Mirlan",37)

print(member1.member())

print(family.member(member1), family.lastname )


##############################################
# Inherit from older Class

class Point():

    def __init__(self, at, fio):
        self.at = at
        self.fio = fio

class onp(Point):
    def member(self):
        return "Menin atym %s familyam %s"%(self.at, self.fio)
p1 = onp("Mirlan", "Tokonbekov")

print(p1.member())
################################################ use __str__ #################
### note: if use __str__ use return, otherwise wont work #################
class family:

    lastname = "Tokonbekov"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return (  "bizdin familyabyz %s, menin atym %s, men %d jashtamyn"%(self.lastname, self.name, self.age)  ) # here

p1 = family("Nurken", 31)

print(p1)


class family:
    lastname = "Tokonbekov"
    def __init__(self, ata_jurt="Tokonbekov", taga_jurt="",kainy_jurt=""):
        self.ata_jurt = ata_jurt
        self.taga_jurt = taga_jurt
        self.kainy_jurt = kainy_jurt


    def __str__(self):
        return ("Kosh keldiner bizdin ui-bulobuzgo")





    @property
    def about_me (self):

        def is_mirlan():
            if self.kainy_jurt == "monok":
                return True
            else:
                return False
            return True

        def is_nurik ():
            if self.kainy_jurt == "latysh":
                return True
            else:
                return False
            return True
        # bros = family()
        if is_mirlan():
            at="Mirlan"

        elif is_nurik():
            at = " Nurik"


        print("Menin atym %s jana familyam %s. Al emi baldarymym familyasy %s bolgon menen, taga jurtu %s"%(at, self.ata_jurt,self.lastname,self.kainy_jurt))

p1 = family("Tokonov","","monok")

print(p1)

p1.about_me



# ===================================================================================================


def one (name):
    return "Menin atym "+ name

def two (name):
    return "my name is " + name


def caller (assign):
    a= "Mirlan"
    b= "Nurken"
    c= "Suiun"
    d = "Ainash"

    return assign( a)

print (     caller(two)          )

###################################### imp ###################

import pdb
def one(decor):

        def wrapperr ():
                print("$$$$$$$$$$$$$$$$$$$$$")
                decor()
                print "%%%%%%%%%%%%%%%%%%%%%"
        return wrapperr

#pdb.set_trace()
@one
def eki():
        print "Salam bul decordun ortosu"
eki()

################################################################


class onp:
        lastname = "Tokonbekov"

        def __init__(self,at="Miki",age="37"):
                self.at = at
                self.age = age
                self.apam = "Erkaim"

        def one (self):
                self.a = "Mirlan"

                return "Bizdin familiyabyz %s, menin atym %s men %s jashtamyn, al emi apamyn aty %s %s"%(onp.lastname,self.at, self.age,self.apam,self.a)
        @property
        def fullname (self):
                return " test " + self.lastname #, self.apam, self.at, self.age



def eki():

        return "\nSalam bul jon ele 2chi def"

p1 = onp("Nurik",31)

print(   p1.fullname, p1.one()  )


# print(   p1.apam + " " + eki()      )

s = onp().one()[:29]    ###################    check this out  ###################


print(s)



