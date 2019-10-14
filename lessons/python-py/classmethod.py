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

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)  # NOTE: proccess value '1985' and get '34' then return it as cls arg

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

# call display() by object regular way
person = Person('Adam', 19)          
person.display()                     


# call display() by object classmethod  way
person1 = Person.fromBirthYear('John',  1985)
person1.display()                     

#*** output: *********
# Adam's age is: 19
# John's age is: 34


# ------------------------------------------------------------------------

from datetime import date 

class Person: 
	def __init__(self, name, age): 
		self.name = name 
		self.age = age
        
        def member (self):
            print ("Menin atym {}, men {} jashtamyn".format(self.name, self.age))
	

	@classmethod
	def fromBirthYear(cls, name, year): 
		return cls(name, year) 
	
	
	@staticmethod
	def isAdult(age): 
		return age > 18

## -----------------------------------------------
p1 = Person("Daulet", "12")
p1.member()

## ---------------- call  classmethod: -------------------------------

p2 = Person.fromBirthYear('Sayan', "9")   # Note:  pass new values as you passing to class, alternative constructor
print(p2.member())                        # then check all args got changed to new value (Sayan,9)
print (p1.age )
print (p2.name )

## ----------------- call staticmethod: ------------------------------

p3 = Person.isAdult(22)
print(p3)   # ===========>  True chygat

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
