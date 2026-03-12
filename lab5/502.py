import re


s = input()


p = input()


result = re.search(p, s)


if result is not None:  
    print("Yes")
else:
    print("No")