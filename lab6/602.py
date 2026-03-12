
n = int(input())

numbers = list(map(int, input().split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
count = len(even_numbers)

print(count)