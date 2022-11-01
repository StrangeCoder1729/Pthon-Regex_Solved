# 4. Write a Python program that matches a string that has an a followed by zero or one 'b'.

import re

str1 = input("Enter string : ")

res = re.findall(r'^a(b?)$',str1)

print(res)