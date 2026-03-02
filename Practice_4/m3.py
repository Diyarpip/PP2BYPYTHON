import math

def regular_polygon_area(n_sides, side_length):
    """Calculate area of a regular polygon
    Area = (n × s²) / (4 × tan(π/n))
    where n = number of sides, s = side length
    """
    return (n_sides * side_length ** 2) / (4 * math.tan(math.pi / n_sides))

# Get input from user
try:
    n_sides = int(input("Input number of sides: "))
    side_length = float(input("Input the length of a side: "))
    
    area = regular_polygon_area(n_sides, side_length)
    print(f"The area of the polygon is: {area:.1f}")
    
    # Alternative calculation for specific polygons
    if n_sides == 3:
        print(f"(This is a triangle with area: {area:.2f})")
    elif n_sides == 4:
        print(f"(This is a square with area: {area:.2f})")
    elif n_sides == 5:
        print(f"(This is a pentagon with area: {area:.2f})")
    elif n_sides == 6:
        print(f"(This is a hexagon with area: {area:.2f})")
    
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Number of sides must be at least 3 for a polygon.")