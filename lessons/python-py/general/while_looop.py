import socket


if "2" not in socket.gethostname():
    file=open("/home/tokonbekov/src/mesa_jenkins/vulkancts-test/bxt.conf")

else:
    file = open(r"Z:\src\mesa_jenkins\vulkancts-test\bxt.conf")


erro = list(file)
errors = erro

limited_errors = []
while True:
  
    for i in errors:
        if len(limited_errors) == 9:
            print (len(limited_errors))
            print ("\n" * 2)
            for  k in limited_errors:
                if k in errors:
                    errors.remove(k)
            limited_errors.clear()
        else:
            limited_errors.append(i) 
   
    if len(errors) < 9:
        break
print("last: ")
print(len(errors))

