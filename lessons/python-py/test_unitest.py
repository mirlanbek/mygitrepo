import sys,os
import datetime
import start
import unittest


def bir():
    return "Bir"

def eki():
    return "eki"


################# usually test file has to be in separate file but it works like this: ##############################################

class test(unittest.TestCase):

    def test_exec(self):       # test function has to be  started with "test_name()"
        print(bir(),eki())


if __name__ == "__main__":
    unittest.main()


#################### result  looks like below: ##########################

#    Bir eki
#    .                           # "." --pass     "F" -- fail
#    ----------------------------------------------------------------------
#    Ran 1 test in 0.000s         # duration amd total test run
#
#    OK #    result status


######################################################################################## 


import unittest

def bir(n):
    a = n ** 2
    return a

def eki(n):
    return n * n


class test (unittest.TestCase):
    def test_1(self):
        self.assertEqual(bir(4), 16)

    def test_2(self):
        self.assertEqual(eki(5), 25)

if __name__ == '__main__':
    unittest.main()





