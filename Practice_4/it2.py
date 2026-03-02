def even_numbers_generator(n):
    """Generator that yields even numbers from 0 to n"""
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Get input from console
try:
    n = int(input("Enter a number (n): "))
    
    # Generate even numbers
    even_nums = list(even_numbers_generator(n))
    
    # Print in comma-separated form
    print(f"Even numbers from 0 to {n}:")
    print(", ".join(map(str, even_nums)))
    
except ValueError:
    print("Please enter a valid integer.")