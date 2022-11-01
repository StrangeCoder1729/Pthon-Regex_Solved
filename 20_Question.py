# 20. Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.

import re

def matching(str1,patterns):
    lst_str1 = str1.split('.')
    str1_new = ' '.join(lst_str1)
    lst2 = str1_new.split(' ')
    count = 0
    for pattern in patterns:
        matching = re.search(pattern,str1_new)
        if re.findall(pattern,str1_new):
            print(f"For {pattern} Got a Match !!")
            print(f"Position : {matching.start()} - {matching.end()}")
        else:
            print("Not a Match !!")


# str1 = input("Enter String : ")
str1 = "The quick brown fox jumps over the lazy dog."
patterns = ["dog","lazy","fox"]

matching(str1,patterns)