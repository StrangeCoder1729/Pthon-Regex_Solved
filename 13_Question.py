# 13. Write a Python program that matches a word containing 'z', not at the start or end of the word

from importlib.abc import ResourceLoader
import re

def matching(str1):
    res = re.findall(r'\B[z]\B',str1)
    if res:
        return "Matched !!!"
    else:
        return "Not matched !!!"

str1 = input("Enter string : ")
print(matching(str1))