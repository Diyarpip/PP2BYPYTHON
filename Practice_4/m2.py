def trapezoid_area(height, base1, base2):
    """Calculate area of a trapezoid: Area = ½(a + b) × h"""
    return 0.5 * (base1 + base2) * height

# Get input from user
try:
    height = float(input("Height: "))
    base1 = float(input("Base, first value: "))
    base2 = float(input("Base, second value: "))
    
    area = trapezoid_area(height, base1, base2)
    print(f"Expected Output: {area}")
    
except ValueError:
    print("Please enter valid numbers.")