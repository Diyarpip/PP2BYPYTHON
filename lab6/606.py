
n = int(input())

numbers = list(map(int, input().split()))

all_non_negative = all(x >= 0 for x in numbers)


if all_non_negative:
    print("Yes")
else:
    print("No")