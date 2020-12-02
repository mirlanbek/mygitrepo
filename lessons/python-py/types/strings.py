print('Hello')

a = "Hello"
print(a)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")



for x in "banana":
  print(x)


print("\n" * 5)
print("hi")

print("Menin atym Mirlan", end='')
print(" fiom Tokonbekov")



name = """  Menin atyn 

Mirlan"""

lastname = " Tokonbekov"

a = (name[13:] + lastname[:-1])
print(a)

str_test = "mirlan Tokonbekov"

spl=str_test.split(" ")
num=enumerate(spl)

for i,v in num:
    print(i,v)


# dir(str)  === get all info

a=str_test.capitalize()
print(a)


b = "Hello, World!"
print(b[2:5])


############  NEW REPLACE  #######


soz = "Mirlan ztokonbekov"
print(  soz.replace("zt","T")  )


txt = "The best things in life are free!"
print("free" in txt)   ===> True

txt="I go to Stoller, my teacher is Mrs. Bing"
txt.find('my')  ===> 17
txt[17:]    ===> string  starting with 'my'

txt = """ 
“This year, more than ever before, some of our most creative and connected moments happened in apps. 
This was thanks to the amazing work of developers who introduced fresh, helpful app experiences 
throughout the year,” said Phil Schiller, Apple Fellow. “Around the world, we saw remarkable efforts from so many developers,
and these Best of 2020 winners are 15 outstanding examples of that innovation. From helping us stay fit and mindful, 
to keeping our children’s education on track, to helping fight hunger, their impact was meaningful to so many of us.”

"""
print( txt.splitlines()[3].split(" ")[3].strip(",") )



