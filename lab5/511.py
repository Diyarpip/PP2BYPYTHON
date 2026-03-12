import re


text = input()

uppercase_chars = re.findall(r'[A-Z]', text)
count = len(uppercase_chars)


print(count)