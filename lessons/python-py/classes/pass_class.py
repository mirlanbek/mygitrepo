class point(object):
    
    def __init__(self, at="Ainash", fio="Takanbekova"):
        self.at = at
        self.fio = fio

    def fun(self):
        return "Salam " + self.at + " " + self.fio + "! bul point class function,"


def func(bir):    # pass whole class
    a=bir.fun     # method  w/o "()" 

    print a() +  " Salam bul bolso jon ele function " 

func(point())
