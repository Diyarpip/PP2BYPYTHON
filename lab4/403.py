def divisible_by_3_and_4_generator(limit):

    for i in range(0, limit + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

numbers = divisible_by_3_and_4_generator(n)
result = ' '.join(str(num) for num in numbers)

print(result)