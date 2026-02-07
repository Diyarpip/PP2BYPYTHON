a =int(input())
list = input().split()
numbers = []

for x in list:
    numbers.append(int(x))

max_val = numbers[0] 
max_pos = 1

for s in range(1, a):
    if numbers[s] > max_val:
        max_val = numbers[s]
        max_pos = s + 1
print(max_pos)        