
n = int(input())

numbers = list(map(int, input().split()))
result = sum(map(lambda x: x**2, numbers))

print(result)