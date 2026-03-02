import math

def degree_to_radian(degrees):
    """Convert degrees to radians"""
    return degrees * (math.pi / 180)

# Get input from user
try:
    degrees = float(input("Input degree: "))
    radians = degree_to_radian(degrees)
    print(f"Output radian: {radians:.6f}")
    
    # Alternative using math.radians()
    print(f"Using math.radians(): {math.radians(degrees):.6f}")
    
except ValueError:
    print("Please enter a valid number.")