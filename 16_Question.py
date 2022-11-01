# 16. Write a Python program to remove leading zeros from an IP address.

import re

def matching(str1):
    res = re.sub(r'\.[0]*','.',str1)
    return res


str1 = input("Enter String : ")

print(matching(str1))

