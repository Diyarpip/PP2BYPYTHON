def squares(a, b):
    """Generator that yields squares of all numbers from a to b"""
    for i in range(a, b + 1):
        yield i * i

# Test with a for loop
print("=== Squares from a to b ===")
a, b = 5, 15
print(f"Squares of numbers from {a} to {b}:")
for square in squares(a, b):
    print(f"{square}", end=" ")
print("\n")

# Additional test cases
print("Squares from -3 to 3:")
for square in squares(-3, 3):
    print(square, end=" ")
print("\n")

print("Squares from 10 to 15:")
squares_list = list(squares(10, 15))
print(squares_list)