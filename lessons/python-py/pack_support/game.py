class game_enemy():
    
    count=12

    def __init__(self, name="Nuku", age=25):
        self.name = name
        self.age = age

    def attack(self):
        print("{} attacks, who is {} years old. life: left 10, total  {}".format(self.name,self.age,game_enemy.count))


# p1=game_enemy("Aibek",43)
# p2=game_enemy()  
# p2.attack()
# p1.attack()
