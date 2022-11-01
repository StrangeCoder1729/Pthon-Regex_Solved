
# 10. Write a Python program that matches a letter at the beginning of a string.

import re

str1 = input("Enter String : ")

 
res = re.findall(r'^\w',str1)
print(res)