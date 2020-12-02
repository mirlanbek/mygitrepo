
import glob
import subprocess
import os

dirname = "/home/tokonbekov/dir/learn/python-test/lessons/practice1/test"

def check_diff(a,b):
    check = subprocess.call(["diff",a,b],stdout=open(os.devnull, "w"))
    if check:
        return False
    else:
        return True
    return True

container1 = [] 
for dir_name in glob.glob(dirname+"/*"):
    file_name = dir_name + "/"+ os.path.split(dir_name)[1] 
    container1.append(file_name)

while True:
    
    for i in container1:
        for dir_name in glob.glob(dirname+"/*"):
            k = dir_name + "/"+ os.path.split(dir_name)[1]
            matches=[]

            if i != k:
                
                if check_diff(i,k):
                    for tmp in (i,k):
                        if i and k not in matches:
                            matches.append(tmp)
                    f_file = dirname + "/../pre_output.txt"
                    # print(f_file)
                    
                    with open (f_file, "a+") as myfile:
                        myfile.write(r"""


{
    %s
}


                        """%(str(matches)))


                    
            del matches[:]         
        container1.remove(i)    

    if len(container1) < 1:
        break


with open (dirname + "/../pre_output.txt","r") as output:
    print(output.read())
