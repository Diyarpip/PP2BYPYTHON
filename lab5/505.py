import re

text = input()
pattern = r'^[A-Za-z].*[0-9]$'

if re.search(pattern, text):
    print("Yes")
else:
    print("No")