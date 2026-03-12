import re

s = input()

match = re.search(r'Name: (.*), Age: (.*)', s)

name = match.group(1)
age = match.group(2)

print(name, age)