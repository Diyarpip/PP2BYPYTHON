
n = int(input())

numbers = list(map(int, input().split()))

unique_numbers = sorted(set(numbers))
result = " ".join(map(str, unique_numbers))

print(result)