
# 11. Write a Python program that matches a word at the end of string, with optional punctuation.

import re


def matching(text):
    res = re.findall(r'\w\W$',str1)
    if res:
        return "Matched !!"
    else:
        return "Not Matched !!"
str1 = input("Enter String : ")

print(matching(str1))
 