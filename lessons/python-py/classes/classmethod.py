# @classmethod  - 1. bul classtyn ichindegi cls method. Bunun objecti method (self) emes, (cls) bolot. bul method 
                  # objectin argumnet valuelaryn override kylysh uchun koldonulat. see below:
                  # func(self tin oorduna cls) koldonulat
                    
# @staticmethod - bul classtyn ichindegi methodgo (self,cls) debei ele jaza beresin ishteit, see below

class Hero:

    @staticmethod
    def say_hello():
        print ("Hello Miki")
    
    def onp (self):
        print("men ONP")

    @classmethod
    def say_class_hello(cls):
        if (cls.__name__ == "Hero_son"):
            print("Hi kido")
        elif cls.__name__ == "Hero_Daugter":
            print ("Hi Prinsess")

class Hero_son (Hero):

    def say_son(self):
        print("say son hello")

class Hero_Daugter (Hero):
    
    def say_daugter(self):
        print("say daugter hello")
testson = Hero_son()

testson.say_hello()
testson.say_son()
testson.onp()
# testson.say_class_hello()

# testdaugter = Hero_Daugter()
# testdaugter.say_class_hello()


 # Python program to demonstrate 
# use of class method and static method. 

#####################################################################################
#####################################################################################
from datetime import date

class Family(object):
    lastname = "Tokonbekov"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def member(self):
        return "Menin atym %s, men %d jashtamyn"%(self.name, self.age)

    @classmethod                                                #  <------------ changes values of __init__(self, name. age)
    def changer(cls,name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def taga_jurt(n,l):                                        # <---------- self, degen jok ele, @staticmethod classtyn ichindegi self.tokonbekov (all self.attr)ge accesss bolo albait
        if n in ("Mirlan", "Nurken", "Suiungul", "Ainash"):
            return "Taga jurtum Josholuluk tookelerden"
        else:
            return "men {}dun neberesimin".format(l)

    @property                                                    #  < ----------------- bul methoddu chkyrganda  '()'y jok chakyrylat 
    def last_name(self):
        return "{}".format(self.lastname)

# p1 = Family("Mirlan", 40)
# print(p1.member())

    
p1 = Family.changer("Mirlan", 1980)
print(p1.member())
print(p1.taga_jurt("Beka", p1.last_name))

## ------------------ classmethod in practice -----------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()

#*** joobu *********
# Adam's age is: 19
# John's age is: 34

# ------------------------------------------------------------------------
