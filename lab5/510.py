import re

text = input()

pattern = r'cat|dog'

match = re.search(pattern, text)

if match:
    print("Yes")
else:
    print("No")