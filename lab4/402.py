
n = int(input())


evens = (str(i) for i in range(2, n + 1, 2))


print(",".join(evens))