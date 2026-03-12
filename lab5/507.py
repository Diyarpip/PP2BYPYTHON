import re

s = input()      
p = input()     
r = input()      

escaped_p = re.escape(p)

result = re.sub(escaped_p, r, s)

print(result)