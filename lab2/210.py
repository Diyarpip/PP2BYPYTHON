a = int(input())
list = input().split()
numbers = []
for x in list:
    numbers.append(int(x))

numbers.sort()
numbers.reverse()
for i in numbers:
    print(i, end=' ')
    