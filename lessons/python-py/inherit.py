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


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 
class Base(object):
    
    def __init__(self, username=None, password=None, url=None):    
        self.username  = username
        self.password  = password
        self.url = url



class onp (Base):
    def __init__(self):                    # pay attention here: just "self"
        Base.__init__(self)                # and here "self" itself


    def one(self):
        
        print(  str(self.username) + " " + str(self.password) +" "+ str(self.url)   )



p1 = onp()
p1.one()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class family(object):
    middle = "Adykovich"

    def __init__(self,at,fio,age):
        self.at = at
        self.fio = fio
        self.age = age
        self.full = self.at + " " + self.middle + " " + self.fio  
    
    def __repr__(self):
        return " Menin atym" + self.at + "al emi familyam" + self.fio + " jana men " + str(self.age) + "jashtamyn"+ \
        " menin toluk atym: " + self.full

# mem1 = family("Mirlan", "Tokonbekov",37)
# print(mem1) 

class kids (family):
    def __init__(self,at,fio,age):                    # pay attention here: just "self"
        family.__init__(self,at,fio,age)   


    def onp(self):

        return ("Menin atym" + self.at + "al emi familyam" + self.fio + " jana men")


p1=kids("Mirlan", "Tokonbekov",37)

print(p1)

