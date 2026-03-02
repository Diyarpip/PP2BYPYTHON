def countdown(n):
    """Generator that yields numbers from n down to 0"""
    for i in range(n, -1, -1):
        yield i

# Test the generator
print("=== Countdown from n to 0 ===")
n = 10
print(f"Numbers from {n} down to 0:")
for num in countdown(n):
    print(num, end=" ")
print("\n")

# With user input
try:
    n = int(input("Enter a number to countdown from: "))
    print(f"Countdown from {n} to 0:")
    countdown_list = list(countdown(n))
    print(", ".join(map(str, countdown_list)))
except ValueError:
    print("Please enter a valid integer.")