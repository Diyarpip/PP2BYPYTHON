def squares_up_to_n(n):
    """Generator that yields squares of numbers from 0 to N"""
    for i in range(n + 1):
        yield i * i

# Test the generator
print("=== Squares up to N ===")
n = 10
print(f"Squares of numbers from 0 to {n}:")
for square in squares_up_to_n(n):
    print(square, end=" ")
print("\n")

# Alternative: Convert to list
squares_list = list(squares_up_to_n(5))
print(f"List of squares up to 5: {squares_list}")