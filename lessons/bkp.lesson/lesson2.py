def san():
    print("Salam dostor")

san()

def kurs(som=12):
    a=70*som
    print(a)
kurs()

def add_num(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
add_num(1,2,333)

classmates={"ulan":"banka zapravkada", "aibo":"jogorku keneshte jurot", "suiun":"echkim bilbeit"}


for i,k in classmates.items():
    print(i,k)

print(classmates['aibo'])
print(len(classmates))


# with open("file2.txt",'r+') as a:
#     print(a.read())









