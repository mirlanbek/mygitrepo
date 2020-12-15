import os, sys

class Project_Map():

    root = os.path.dirname(sys.argv[0])
     
    def __init__(self,config_name="/"):
        self.config_name = config_name

    def root_path (self):
        return os.path.join(self.root, self.config_name)




# p1=Project_Map("Beka.conf") 
# print (  p1.root_path()  )
