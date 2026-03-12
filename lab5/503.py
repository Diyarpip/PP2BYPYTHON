import re


s = input()  
p = input()  


matches = re.findall(p, s)


count = len(matches)


print(count)