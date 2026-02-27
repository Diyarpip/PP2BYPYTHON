def generator(lst, n):
    for i in range(n):
        for item in lst:
            yield item
elements = input().split()
n = int(input())
print(" ".join(generator(elements, n)))