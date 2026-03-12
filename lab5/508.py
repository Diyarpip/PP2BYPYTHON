import re


s = input()  
d = input()  

parts = re.split(d, s)
result = ','.join(parts)

print(result)