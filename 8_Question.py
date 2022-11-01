# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters


import re

str1 = input("Enter String : ")

res = re.findall(r'[A-Z][a-z]+$',str1)

print(res)


 