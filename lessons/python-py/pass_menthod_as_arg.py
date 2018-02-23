class Foo:
    
    def method1(self,p2):
        print (p2.method3)

    def method2(self, method1="HI"):
        p2=Foo()
        return self.method1(p2)

    @property
    def method3(self):
        return("method3mun")

foo = Foo()
foo.method2()



class Foo(object):
    
    def method1(self):
        print "Salam"

    def method2(self, method1):
        return method1()

#####################################
class Foo:
    
    def method1(self,p2):
        print (p2.method3)

    def method2(self):
        p2=Foo()
        return p2.method1(p2)   #pay attention here p2 is used as instance and arg.

    @property
    def method3(self):
        return("I'm from method3")

foo = Foo()
foo.method2()


####################  VERY IMPORTANT ###########################
################################################################

class point(object):

    def __init__(self, at="Ainash", fio="Takanbekova"):
        self.at = at
        self.fio = fio

    def fun(self):
        return "Salam " + self.at + " " + self.fio 

p1=point()

p2 = point("Miki","Tokon")


def func(p1):    # pass whole class
    # a=bir.fun     # method  w/o "()" 

    p3=point("Nurik","Takan")
    print (p1.fun() + "\n" + p3.fun() + "\n" + p2.fun()) 


func(p1)

