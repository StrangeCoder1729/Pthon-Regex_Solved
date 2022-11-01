# 2. Write a Python program that matches a word containing 'z'. 

import re


def matching(str1):
    res = re.findall(r'\w*[z]{1}\w+',str1)
    if res:
        return "Matched !!"
    else:
        return "Not Matched !!"
str1 = input("Enter String : ")



print(matching(str1))
