# 2. Write a Python program that matches a string that has an a followed by zero or more b's. 

import re

str1 = input("Enter string : ")

result = re.findall(r'^a(b*)$',str1)
print(result)

