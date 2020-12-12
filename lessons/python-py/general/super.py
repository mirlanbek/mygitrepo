### NOTE:   SUPER bul inherit bolup atkan Classtagy attribute (self.var) default maanisin saktap turat: 
# BASEtegi __init__ super power bolot
class Base(object):
    
    def __init__(self, username=None, password=None, url=None):   # Misaly: baardyk values "NONE"
        self.username  = username
        self.password  = password
        self.url = url

class Subclass(Base):

    def __init__(self, username="hoss_it87", password="whatsgoodSO", url="www.boss-sauce.com"): # birok bashka maani berip atabyz override kylysh kerek oz, birok SUPERset bolso kaira ele BASE -n default maanisin chygarat  
        # super(Subclass, self).__init__(username="btokon", password="65062", url="www.beka")  # most super power is if you set default values here ######## 
        super(Subclass,self).__init__()    #  NONE NONE degenchygat power Baseke ketti. NOTE and NOTE: kashaanyn ichine (self, username, password) desen Subclasstyn maanisn alat, jazbasan Parenttin(self,username, password) alat
       
        # Base.__init__(self, username, password, url)
    
    def one (self):
        
        print (self.username, self.password, self.url)


p1 = Subclass(username="mtokon", password="1224", url="www.miki") # bul jerden dagy ozgortup korson super set bolso ozgorboi BASE -n default maanisi kelet

p1.one()



# class Base(object):
#     def __init__(self):
#         print("Base init'ed")

# class ChildA(Base):
#     def __init__(self):
#         print("ChildA init'ed")
#         Base.__init__(self)

# class ChildB(Base):
#     def __init__(self):
#         print("ChildB init'ed")
#         super(ChildB, self).__init__()


# d=ChildA()
# d


# s=ChildB
# s()


# --------------------- super for method ---------------------------------------------------------------------------------

class Hero (object):
    lastname = "Tokonbekov"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def member(self):
        print ("My name is HERO {} and I'm {}".format(self.name, self.age))

class Family(Hero):

    def __init__(self, name,age,tel):
        super(Family, self).__init__(name,age)
        self.tel = tel

    def member(self):                    # Note same method() name as in parent class
        super(Family,self).member()



p1 = Family("Miki", 40, "7733669911")

p1.member()

# --------------------------------------------------------------------
