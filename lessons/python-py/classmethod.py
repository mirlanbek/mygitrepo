
# @staticmethod - bul classtyn ichindegi methodgo (self) debei ele jaza beresin ishteit
# @classmethod  - 1. bul classtyn ichindegi method-n 1 je andan kop variable bar bolso (self dbei ele,name, lastname)
                  # 2. misaly: def func(cls) b-so  any chakyrganda func("X") berish kk bolotta, @classmetod
                  # bolso jon ele  func()  

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




 