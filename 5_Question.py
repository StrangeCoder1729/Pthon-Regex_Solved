# 5. Write a Python program that matches a string that has an a followed by three 'b'.

import re

str1 = input("Enter string : ")

res = re.findall(r'^ab{3}$',str1)
print(res)