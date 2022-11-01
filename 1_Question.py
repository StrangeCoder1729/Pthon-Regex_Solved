
# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

import re

str1 = input("Enter string : ")

res = re.findall(r'\w',str1)

res1 = ' '.join(res)
print(res1)