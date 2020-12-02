##############################################################

# 12. Integer to Roman

dic={     
     "1": "I",
     "5": "V",
     "10": "X",
     "50": "L",
     "100": "C",
     "500": "D",
     "1000": "M"
    }

def get_roman_100(t):
    if t == 9:
        tmp = "CM"
    elif t == 8:
        tmp = "DCCC"
    elif t == 7:
        tmp = "DCC"
    elif t == 6:
        tmp = "DC"
    elif t == 5:
        tmp = "D"
    elif t == 4:
        tmp = "CD"
    elif t == 3:
        tmp = "CCC"
    elif t == 2:
        tmp = "CC"
    elif t == 1:
        tmp = "C"
    return tmp
    
def get_roman_10(t):
    if t == 9:
        tmp = "XC"
    elif t == 8:
        tmp = "LXXX"
    elif t == 7:
        tmp = "LXX"
    elif t == 6:
        tmp = "LX"
    elif t == 5:
        tmp = "L"
    elif t == 4:
        tmp = "XL"
    elif t == 3:
        tmp = "XXX"
    elif t == 2:
        tmp = "XX"
    elif t == 1:
        tmp = "X"
    return tmp

def get_roman_1(t):
    if t == 9:
        tmp = "IX"
    elif t == 8:
        tmp = "VIII"
    elif t == 7:
        tmp = "VII"
    elif t == 6:
        tmp = "VI"
    elif t == 5:
        tmp = "V"
    elif t == 4:
        tmp = "IV"
    elif t == 3:
        tmp = "III"
    elif t == 2:
        tmp = "II"
    elif t == 1:
        tmp = "I"
    return tmp


def intToRoman(num):
    s_num = str(num)
    le = len(s_num)
    li = []
    rom = ""
    for i,k in enumerate(s_num):
        if le == 4:
            for r in range(int(k)):
                rom += "M"
            le -= 1

        elif le == 3:
            rom += get_roman_100(int(k))
            le -= 1

        elif le == 2:
            rom += get_roman_10(int(k))
            le -= 1

        elif le == 1:
            rom += get_roman_1(int(k))
            le -= 1
    return rom


num=2994
print(intToRoman(num))



#####################################################################
# get currect century

def centuryFromYear(year):
    l=len(str(year))
    z = "1"
    for i in range(int(l)-2):
        z += "0"
    cen = year % int(z)
    if cen == 0:
        return int(year/100)
    else:
        ext = year % 100
        adj_year = year - ext
        century = (adj_year / 100) + 1
        return int(century)

print(centuryFromYear(2001))

##############################################################################

# 48. Rotate image: 

# c=[[1,2,3],   b=[[7,4,1],
#    [4,5,6],      [8,5,2],
#    [7,8,9]]      [9,6,3]]

c=[[1,2,3], 
   [4,5,6],  
   [7,8,9]] 

a=[[],[],[]]

for i in c:
    for j in i:
        a[0].append(j)
        a[1].append(j)
        a[2].append(j)
a[0]=a[0][::-1]
a[1]=a[1][::-1]
a[2]=a[2][::-1]



s1 = [] 
for k,j in enumerate(a[0]):
    if k == 2 or k == 5 or k == 8:
        s1.append(j)

s2= [] 
for k,j in enumerate(a[0]):
    if k == 1 or k == 4 or k == 7:
        s2.append(j)

s3 = [] 
for k,j in enumerate(a[0]):
    if k == 0 or k == 3 or k == 6:
        s3.append(j)

a[0]=s1
a[1]=s2
a[2]=s3


for i in c:
    print(i)

print("ANSWER IS: ")

for i in a:
    print (i)

# print(s1)
# print(s2)
# print(s3)



############################################################################

#35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lis = nums
        t = target
        t_position = 0

        if t <= lis[0]:
            t_position = 0
        else:       
            
            for i in lis:
                try:
                    nex = lis[lis.index(i)+1]
                except Exception:
                    nex = lis[lis.index(i)]
                    t_position = len(lis)
                    break
                if t > i and t < nex:
                    t_position += (lis.index(i)+1)
                    break
                elif t == i:
                    t_position += (lis.index(i))

                    break
        
        return t_position       

# lis=[1,3]
# t = 5

# def ff (lis,t):
#     index = 0
#     for i,e in enumerate(lis):
#         if e < t:
#             index += 1
#         else:
#             break

#     return index

# print(ff(lis,t))


##########################################################################


# def isPalindrome(self, x: int) -> bool:
# x=123454321

x=1000
def isPalindrome(x):
    i = x
    palindroms = []
    while i >= 100:
        s = str(i)
        is_odd = len(s)%2
        if is_odd == 1 and not s.startswith("-"):
            id = ( len(s) - 1) /2
            half = s[:int(id)]
            if str(half)[::-1] == str(s[int(id+1):]):
                palindroms.append(i)
                i -= 1
            else:
                i -= 1
                continue
        else:
            i -= 1
            continue
    return palindroms

print(isPalindrome(x))
## --------------------------------------------------
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        is_odd = len(s)%2
        if is_odd == 1 and not s.startswith("-"):
            id = ( len(s) - 1) /2
            half = s[:int(id)]
            if str(half)[::-1] == str(s[int(id+1):]):
                # print(s[int(id)])
                return True



########################################################################3

# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        if num.startswith("-"):
            num = num[1:]
            num = num[::-1]
            num = int(num)*1
            num = str(num)            
            num = "-" + num
        else:
            num = num[::-1]
            num = int(num)*1
            num = str(num)            

        if x == 0 or len(str(x)) > 9:
            return 0
        else:
            return num


########################################################################3
#Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

import re
letters = []
pairs = []
len_num = {0: "nol"}
nums = []

def lengthOfLongestSubstring(string):
    for i in string:
        if i in letters:
            continue
        else:
            letters.append(i)               
            regex = re.compile("[%s]+"%(i))
            r = re.findall(regex, string)
            for k in r:
                if len(k) >= 2:
                    pairs.append(k)

    for m in pairs:
        nums.append(len(m))
        r = len(m)
        len_num.update({r: m})
    oo = max(nums)
    return len((len_num[oo]))

r=lengthOfLongestSubstring("abcuujjuuabcbfffffbbyy")
print(r)

import re
letters = []
pairs = []
len_num = {0: "nol"}
nums = []

def lengthOfLongestSubstring(string):
    for i in string:
        if i in letters:
            continue
        else:
            letters.append(i)               
            regex = re.compile("[%s]+"%(i))
            r = re.findall(regex, string)

just get len
            for k in r:
                if len(k) >= 2:
                    pairs.append(" ")
                else:
                    pairs.append(len(k))



    for m in pairs:
        
        nums.append(len(m))
        r = len(m)
        len_num.update({r: m})
    ready = []
    oo = pairs
    str1 = 0
    for g in pairs:
        if g != " ":
            str1 += 1
        else:
            ready.append(str1)
            str1 = 0
            
            
    kk = max(ready)
    return len((len_num[oo]))
    return kk

r=lengthOfLongestSubstring("abcabcbb")
print(r)






# --------------------------------------------------------
import re
letters = []
pairs = []
len_num = {0: "nol"}
nums = []

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in s:
            if i in letters:
                continue
            else:
                letters.append(i)               
                regex = re.compile("[%s]+"%(i))
                r = re.findall(regex, s)
                for k in r:
                    if len(k) >= 2:
                        pairs.append(k)

        for m in pairs:
            nums.append(len(m))
            r = len(m)
            len_num.update({r: m})
        oo = max(nums)
        return len((len_num[oo]))


# ###########################
# # # 32. Longest Valid Parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        str1 = "()"
        res = []
        for k in s:
            if str1[-2:] == "()" and k == "(" or str1[:] == "()" and k == "(":
                str1 += k
            elif str1[-2:] == ")(" and k == ")":
                    str1 += k
                    res.append(len(str1) - 2)
            else:
                if str1[-2:] == ")(":
                    res.append(len(str1) - 3)
                    str1 = "()("
                else:
                    res.append(len(str1) - 2)
                    str1 = "()"
        if len(res) <= 0:
            return None
        else:
            return (sorted(res)[-1])

s=")()())()((()"
# s=")(()())()()()()()()"

# s="(()"
p1 = Solution()
print(p1.longestValidParentheses(s))

##############################################



# class Solution:
def twoSum(nums, target):
    indexing = []
    List = []
    for k, v in enumerate(nums):
        for i in nums:
            index1 = nums.index(i)
            if index1 != k and i + v == target and index1 not in indexing and k not in indexing:
                print(index1,k)
                List.append(index1)
                List.append(k)
                indexing.append(index1)
                indexing.append(k)
    return List

num = [2, 7, 11, 15, 3, 6, 1, 4,8 ]
twoSum(num,9)     


====================================

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexing = []
        List = []
        for k, v in enumerate(nums):
            for i in nums:
                index1 = nums.index(i)
                if index1 != k and i + v == target and index1 not in indexing and k not in indexing:
                    print(index1,k)
                    List.append(index1)
                    List.append(k)
                    indexing.append(index1)
                    indexing.append(k)
        return List

   















dic={     
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
    }

class Solution:
    
    def __init__(self, rom):
        self.rom = rom

    def romanToInt(self):       
        rev = self.rom[::-1]
        prev = 0
        sum = 0
        for i in rev:
            if dic[i] >= prev:
                prev = 0
                prev += dic[i]
                sum += (dic[i])
            else:
                prev = 0
                prev += dic[i]
                sum -= dic[i]
        return sum
rom = "MMCMXCIV"
p1 = Solution(rom)
a=p1.romanToInt()    
print(a)
        

