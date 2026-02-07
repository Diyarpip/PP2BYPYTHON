a = int(input())
numbers = input().split()

count_pos = 0
for x in numbers:
    if int(x) > 0:
        count_pos += 1
print(count_pos)