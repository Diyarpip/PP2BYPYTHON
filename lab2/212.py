a = int(input())
numbers = input().split()

for x in range(a):
    num = int(numbers[x])
    square = num * num
    print(square, end=' ')
