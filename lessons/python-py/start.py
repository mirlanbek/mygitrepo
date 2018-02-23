class family(object):
    middle = "Adykovich"

    def __init__(self,at,fio,age):
        self.at = at
        self.fio = fio
        self.age = age
        self.full = self.at + " " + self.middle + " " + self.fio  
    
    def __repr__(self):
        return f" Menin atym" + self.at + "al emi familyam" + self.fio + " jana men " + str(self.age) + "jashtamyn"+ \
        " menin toluk atym: " + self.full

# mem1 = family("Mirlan", "Tokonbekov",37)
# print(mem1) 

class kids (family):
    def __init__(self,at,fio,age):                    # pay attention here: just "self"
        family.__init__(self,at,fio,age)   


    def onp(self):

        return ("Menin atym" + self.at + "al emi familyam" + self.fio + " jana men")


p1=kids("Mirlan", "Tokonbekov",37)
print(p1.onp())
