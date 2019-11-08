class Onp:

    def test(self):
        return "Test"


    def meth1(self, p2):
        return(p2.meth3())


    def meth2 (self, meth1 = False):
        p2 = Onp()
        return p2.meth1(p2)

    def meth3 (self):
        return "I'm from meth-3"


p1 = Onp()
print(p1.meth2())
