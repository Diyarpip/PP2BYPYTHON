import re
text = input()

digits = re.findall(r'\d', text)

result = ' '.join(digits)
print(result)