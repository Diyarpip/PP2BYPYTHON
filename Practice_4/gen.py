def even_numbers(n):
    for i in range(2, n + 1):
        if i % 2 == 0:
           yield i
n = int(input())
for num in even_numbers(n):
     print(num, end=" ")
