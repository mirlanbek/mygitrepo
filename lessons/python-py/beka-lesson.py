n = [12,23,34,41, 65, 50, 14]

m = [76,12,34,56,41]

box=[]

def five_maker(x):
    for i in x:
        b=str(i)
        if int(b[0]) + int(b[1]) == 5:
            box.append(i)
    return box


# print(five_maker(m))


import os, sys

os.chdir('/root')




def is_same(x, y):

    diff = os.system(' diff {} {}'.format(x,y))
    if diff != 0:
        return False
    else:
        return True



f1 = "file_3"
f2 = "file_2"


if is_same(f1,f2):
    print(f"{f1}  menen  {f2} Bul eki file chyndap okshosh eken")
else:
    print(f"{f1} menen  {f2}  Bul eki file  okshosh EMES eken")

