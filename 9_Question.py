# 9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re


str1 = input("Enter String : ")

res = re.findall(r'a.*b$',str1)
print(res)