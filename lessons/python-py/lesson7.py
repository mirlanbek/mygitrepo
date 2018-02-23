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
