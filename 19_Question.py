# 19. Write a Python program to search some literals strings in a string.

import re

def matching(str1,name):
    pattern = ['fox', 'dog', 'horse' ]
    # res = re.findall(r'.fox ',str1)
    for word in pattern:
        if re.findall(word,str1):
            print("Got a Matched !!!")
        else:
            print("Not a match !!")

str1 = input("Enter String : ")
name = "fox"

matching(str1,name)