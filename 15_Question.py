# 15. Write a Python program where a string will start with a specific number

import re

def matching(str1):
    res = re.findall(r'^123',str1)
    if res:
        return "Matched !!!"
    else:
        return "Not matched !!"

str1 = input("Enter String : ")

print(matching(str1))