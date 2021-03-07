#  Description:
#      When we inherit parent class, we have to know all functions and attributs get inherited: (self, arg1,arg2,arg3)

# 1. Basic Inherit. note: nor __init__ on child class

class Point():

    def __init__(self, at, fio):
        self.at = at
        self.fio = fio

    def test_Point(self):
        return "test method from Point"

class onp(Point):
    def member(self):
        return "Menin atym %s familyam %s"%(self.at, self.fio)


p1 = onp("Mirlan", "Tokonbekov")


print(p1.member())       # <------------  method from  child class
print(p1.test_Point())   # <------------  method from  parent class

# -------------------------------------------------------------------------------------
# -------------------  inherit method from parent class if method names are same on parent and child classes -------------------


class Point():

    def __init__(self, at, fio):
        self.at = at
        self.fio = fio

    def member(self):
        return "test method from Point"

class onp(Point):
    def member(self):
        return super(onp, self).member()        # OR  return Point.member(self)


# "test method from Point"   chygat



#   +++++++++++++++++++++++======================++++++++++++++++++++++++++++++++++++
#   +++++++++++++++++++++++======================++++++++++++++++++++++++++++++++++++

#  NOTE:  all questions are answered HERE:

class Base(object):

    def __init__(self, username=None, password=None, url=None):
        self.username  = username
        self.password  = password
        self.url = url

# -------------------------------- Onp inherits all args and atriibutes from Base __init__()
#  no need create new __init__(), it is already inherited from Base

class Onp (Base):

    def one(self):
        print(  str(self.username) + " " + str(self.password) +" "+ str(self.url)   )

p1 = Onp("mirlan", "pass", "http://google.com/python")


# -- Parent and Child attributes are combined -----------------------

# username, pasword  and url  are inherited, but we need at, fio, mid :
#

class Onp(Base):

    def __init__(self,at,fio,mid,username,password, url):
        super(Onp,self).__init__(username,password, url)   #super

        self.at = at
        self.fio = fio
        self.mid = mid

    def member(self):
        return "Menin atym %s familyam %s %s"%(self.at, self.fio, self.username)

p1 = Onp("Mirlan", "Tokonbekov", "Adykovich", "miki", "1", "http://google.com")
print(p1.member())


#   +++++++++++++++++++++++======================++++++++++++++++++++++++++++++++++++
#   +++++++++++++++++++++++======================++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




import os,sys
import pack_support as ps
import class_start as cs


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), ".."))

#########################  inherit class form different file ################
cl = cs.point()

print ( cl.func()  )

class Onp(cs.point):     # <--- look at here  "cs.point  is the class  from  class_start.py "
    # def __init__(self,at,fio,mid):
    #     self.mid = mid
    #     cs.point.__init__(self,at,fio)

    def __init__(self,at,fio,mid):
        super(Onp,self).__init__(at,fio)   #super
        self.mid = mid

    def member(self):
        return "Menin atym %s familyam %s %s"%(self.at, self.fio, self.mid)

p1 = Onp("Mirlan", "Tokonbekov", "Adykovich")
print(p1.member())


##################################
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("milton")
print (milton.full_time_wage(5))

################################################


class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber  ## note: Name() is from class Person

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())

#################  Super inherit :

class Base(object):
    def __init__(self):
        print ("Base created")

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

        print(self.__class__ , ChildB )

ChildA()
ChildB()

-------------------------------------------------------------  Inheritance -----------------------------------

class Family(object):

    middle = "Adykovich"

    def __init__(self,at,fio,age):
        self.at = at
        self.fio = fio
        self.age = age
        self.full = self.at + " " + self.middle + " " + self.fio

    def __repr__(self):
        return " Menin atym" + self.at + "al emi familyam" + self.fio + " jana men " + str(self.age) + "jashtamyn"+ \
        " menin toluk atym: " + self.full


class Kids (Family):

    def onp(self):
        return ("Menin atym" + self.at + "al emi familyam" + self.fio + " jana men")




p1=Kids("Mirlan", "Tokonbekov",37)
print(p1)



------------------------------------------------------------- Multiple Inheritance -----------------------------------

class First():
    def __init__(self):
        print("I'm from First")


class Second():
    def __init__(self):
        print("I'm from Second")

class Third():
    def __init__(self):
        print("I'm from Third")


class Combined(First, Second, Third):
    def __init__(self):
        super().__init__()                # calls First
        super(Combined,self).__init__()   # blocks Combined calls First
        super(First,self).__init__()      # blocks First calls Second
        super(Second,self).__init__()     # blocks Second calls Third

        print("I's Combined")

p1 = Combined()
p1




