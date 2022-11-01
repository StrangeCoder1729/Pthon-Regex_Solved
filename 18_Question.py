# 18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.


import re
def matching(str1):
    res = re.finditer(r'(\d{1,3})',str1)
    return res
str1 = input("Enter String : ")

ans = matching(str1)

for i in ans:
    print(i.group())

 