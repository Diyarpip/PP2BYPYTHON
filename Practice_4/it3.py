def divisible_by_3_and_4(n):
    """Generator that yields numbers divisible by both 3 and 4 (i.e., divisible by 12)"""
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Test the generator
print("=== Numbers divisible by both 3 and 4 ===")
n = 100
print(f"Numbers from 0 to {n} divisible by both 3 and 4:")
for num in divisible_by_3_and_4(n):
    print(num, end=" ")
print("\n")

# Alternative with user input
try:
    n = int(input("Enter a number (n): "))
    result = list(divisible_by_3_and_4(n))
    print(f"Numbers divisible by both 3 and 4 from 0 to {n}: {result}")
except ValueError:
    print("Please enter a valid integer.")