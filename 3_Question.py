# 3. Write a Python program that matches a string that has an a followed by one or more b's.  



import re 

str1 = input("Enter String : ")

res = re.findall(r'^a(b+)$',str1)

print(res)