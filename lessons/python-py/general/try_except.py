class diktor(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_exept(self):
        print("user defined msg: ", self.msg)


# try:
#     raise diktor ("raise kylyp atam")

# except diktor as dr:
#     dr.print_exept()


try:
    f = open("/home/tokonbekov/dir/learn/python-test/lessons/bkp_lesson/short.ini")
    # if f.name == "start.pyc":
    #     raise IOError


except IOError:
    
    print ("File jok go!")

else:
    print(f.read())
    f.close()

finally:
    diktor("fanlly buttu").print_exept()
# except Exception:
#     print("General Error")
