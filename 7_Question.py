# 7. Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

str1 = input("Enter String : ")

res = re.findall(r'[a-z]+_[a-z]+$',str1)
print(res)