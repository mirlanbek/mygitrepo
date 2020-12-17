class Countries(object):

    def __init__(self, country):
        self.country = country


    def lang (self):
        if "France" in self.country:
            l = "French"
        elif "Kenia" in self.country:
            l= "Swahili"
        return l
        