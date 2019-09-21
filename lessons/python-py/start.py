class family(object):
    middle = "Adykovich"

    def __init__(self,at,fio,age):
        self.at = at
        self.fio = fio
        self.age = age
        self.full = self.at + " " + self.middle + " " + self.fio  
    
    def __repr__(self):
        return " Menin atym %s al emi familyam %s jana men %d jashtamyn menin toluk atym: %s"%(self.at, self.fio, self.age, self.full)

# mem1 = family("Mirlan", "Tokonbekov",37)
# print(mem1) 

class kids (family):
    def __init__(self,at,fio,age):                    # pay attention here: just "self"
        family.__init__(self,at,fio,age)   


    def onp(self):

        return ("Menin atym" + self.at + "al emi familyam" + self.fio + " jana men")


p1=kids("Mirlan", "Tokonbekov",37)
print(p1.onp())
