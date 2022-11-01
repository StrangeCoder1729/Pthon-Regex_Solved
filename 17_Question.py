# 17. Write a Python program to check for a number at the end of a string.

import re

def matching(str1):
    res = re.findall(r'.\d$',str1)
    if res:
        return "Matched !!!"
    else:
        return "Not matched !!"

str1 = input("Enter String : ")

print(matching(str1))