# 21. Write a Python program to find the substrings within a string.  

import re

pattern = "exercises"
str1 = 'Python exercises, PHP exercises, C# exercises'


lst =  re.findall(pattern, str1)
print(f"Substrings : {lst}")