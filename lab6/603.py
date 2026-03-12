
n = int(input())

words = input().split()

result_parts = []
for index, word in enumerate(words):
    result_parts.append(f"{index}:{word}")

print(" ".join(result_parts))