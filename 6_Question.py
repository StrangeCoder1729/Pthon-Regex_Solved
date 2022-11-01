# 6. Write a Python program that matches a string that has an a followed by two to three 'b'.

import re

str1 = input("Enter String : ")

res = re.findall(r'^ab{2,3}$',str1)
print(res)