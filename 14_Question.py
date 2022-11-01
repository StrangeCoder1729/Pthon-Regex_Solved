
# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores

import re

def matching(str1):
    res = re.findall(r'\w+_+',str1)
    if res:
        return "Matched"
    else:
        return "Not Matched"

str1 = input("Enter String : ")

print(matching(str1))