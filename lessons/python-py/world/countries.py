from .continent import Continent

materic = Continent()


class Countries(object):

    def __init__(self, country):
        self.country = country


    def lang (self):
        if "France" in self.country:
            l = "French " + materic.materic
        elif "Kenia" in self.country:
            l= "Swahili "+ materic.materic
        return l
