n = int(input())
numbers = input().split()

max_num = numbers[0]
position = 0
for  x in numbers:
    if int(x) > int(max_num):
        max_num = x
print(max_num)