#REGEX
import re


#(starts ends)

# ^wp.*php$
#if re.search("^[A-Z].*py$", x):

strings="men 1980-jyly Kyrgyzstanda tuuldum. 16 jashymda kyrgyzstanda men Universitette okup bashtagam entry_value_key"


re_text = []

for i in strings.split(" "):
    if i.endswith("."):
        i=i[:-1]

    re_text.append(i)
# print(re_text)

    a2=re.compile("^[A-Z].*a$")
    k=re.search(a2,i)
    if k:
        print(i)
#  "Kyrgyzstanda" ----- chygat

# ******************************
def strip_int(string):
    return re.sub("\D", "", string)

str1 = "Mirlan1980"
print(strip_int(str1)) # -----> 1980


# my_str = "The ape was at the apex"

# if re.search("ape", my_str):
#     print("bar eken")

# k=re.split(" ", my_str)
# print(k)

# ff = my_str.split(" ")


# owlFood = "rat cat mat pat"

# REGEX = re.compile("[cr]at")
# owlFood = REGEX.sub('owl',owlFood)
# print(owlFood)

my_str2 = """There is plenty of types of files.420-str we can differ them by their extension: file.txt, file.doc, file.pdf"""

# regex=re.compile('file\.\w{1,3}')

# test = re.findall(regex,my_str2)


# test2 = re.search(regex, my_str2)


# print(  test2.group()    )
  
found_w = re.compile(r"\w+\.\d{3}\-\w+")

print(  re.findall(found_w,my_str2)    )

print(       found_w.sub("Roto", my_str2)    )

found_1 = re.search(found_w,my_str2)
print(      found_1.group()                 )





foods = ("potato", "carot", "onion", "bread", "grape", "melon")
my_str2 = """There is plenty of types of files.420-str we can differ them by their extension: file.txt, file.doc, file.pdf"""

my_test = "Salam meinin atym 'Mitt-12 1900', 'Su-12 1980' ilgeri bivr zamanda bir nerse boluptur "

aa = re.compile(" 'w{2}\-\d{2} \d")

bb = re.compile("\w{2,4}-\d{2}\s\d{4}")
print(  re.findall(bb, my_str2)   )

print(  re.findall(bb,my_test)  )





######################################################################


abc     Letters
123     Digits
\d      Any Digit
\D      Any Non-digit character
.       Any Character
\.      Period
[abc]   Only a, b, or c
[^abc]  Not a, b, nor c
[a-z]   Characters a to z
[0-9]   Numbers 0 to 9
\w      Any Alphanumeric character
\W      Any Non-alphanumeric character
{m}     m Repetitions
{m,n}   m to n Repetitions
star: *       Zero or more repetitions
+       One or more repetitions
?       Optional character
\s      Any Whitespace
\S      Any Non-whitespace character
^   $   Starts and ends                --- ^Mission: successful$  ------- Mission: successful
(   )   Capture Group  ----------  ^(file.+)\.pdf$  ----- file_record_transcript.pdf and file_07241999.pdf
(a(bc)) Capture Sub-group  ---  (\w+ (\d{4}))  ---  Jan 1987 1987 |  ( first_aprt+(2nd_part - this is for 1st and 2nd 1987)  )
(.*)    Capture all
(abc|def)       Matches abc or def










