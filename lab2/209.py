a = int(input())

list = input().split()
numbers = []

for x in list:
    numbers.append(int(x))

min_val = min(numbers)
max_val = max(numbers)

for i in range(a):
    if numbers[i] == max_val:
        numbers[i] = min_val

for num in numbers:
    print(num, end=' ')
 
