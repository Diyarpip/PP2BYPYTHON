def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


numbers = list(map(int, input().split()))


primes = list(filter(lambda x: is_prime(x), numbers))


if primes:
    print(' '.join(map(str, primes)))
else:
    print("No primes")