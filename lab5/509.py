import re

text = input()
words = re.findall(r'\b\S{3}\b', text)
count = len(words)

print(count)