import re

text = input()
pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

match = re.search(pattern, text)

if match:
    print(match.group())
else:
    print("No email")