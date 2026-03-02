import math

def test_all_calculations():
    """Test all calculations with sample values"""
    print("="*50)
    print("TESTING ALL CALCULATIONS")
    print("="*50)
    
    # Test 1: Degree to Radian
    degrees = 15
    radians = degrees * math.pi / 180
    print(f"\n1. Degree to Radian:")
    print(f"   Input: {degrees}°")
    print(f"   Output: {radians:.6f} rad")
    print(f"   Expected: 0.261799 rad")
    
    # Test 2: Trapezoid Area
    h, b1, b2 = 5, 5, 6
    area_trap = 0.5 * (b1 + b2) * h
    print(f"\n2. Trapezoid Area:")
    print(f"   Height: {h}, Base1: {b1}, Base2: {b2}")
    print(f"   Area: {area_trap}")
    print(f"   Expected: 27.5")
    
    # Test 3: Regular Polygon Area
    n, s = 4, 25
    area_poly = (n * s**2) / (4 * math.tan(math.pi / n))
    print(f"\n3. Regular Polygon Area:")
    print(f"   Sides: {n}, Side length: {s}")
    print(f"   Area: {area_poly:.1f}")
    print(f"   Expected: 625")
    
    # Test 4: Parallelogram Area
    base, height = 5, 6
    area_para = base * height
    print(f"\n4. Parallelogram Area:")
    print(f"   Base: {base}, Height: {height}")
    print(f"   Area: {area_para:.1f}")
    print(f"   Expected: 30.0")
    
    print("\n" + "="*50)
    print("ALL TESTS COMPLETED")
    print("="*50)

# Run the tests
if __name__ == "__main__":
    test_all_calculations()