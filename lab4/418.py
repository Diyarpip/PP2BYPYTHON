def solve():
    # Read inputs
    x1, y1 = map(float, input().strip().split())
    x2, y2 = map(float, input().strip().split())
    
    # Reflect point B across the x-axis
    # B' = (x2, -y2)
    
    # Find the intersection of line A-B' with the x-axis (y=0)
    # Parametric equation: (x, y) = (x1 + t*(x2-x1), y1 + t*(-y2-y1))
    # Set y = 0 to find t:
    # y1 + t*(-y2 - y1) = 0
    # t*(-y2 - y1) = -y1
    # t = y1 / (y1 + y2)
    
    # Handle special case where y1 + y2 = 0
    if abs(y1 + y2) < 1e-10:
        # If y1 + y2 = 0, then y1 = -y2
        # This means A and B are symmetric about the x-axis
        # The reflection point would be at x where AP + PB is minimum
        # But in this case, any point on x-axis would satisfy angle equality?
        # Actually, when y1 = -y2, the line from A to B' would be horizontal
        # We need to find intersection with x-axis
        
        if abs(y1) < 1e-10:
            # Both points on x-axis - reflection point is anywhere between?
            # According to physics, if both points are on the mirror, 
            # the straight line path is valid
            # Let's take the midpoint
            x = (x1 + x2) / 2
        else:
            # y1 = -y2, so denominator is zero
            # This means the line from A to B' is parallel to x-axis
            # No unique intersection? But we need a point on x-axis
            # The physical interpretation: when y1 = -y2, 
            # the angle of incidence equals angle of reflection for any x
            # Let's take x such that the path length is minimum
            # That would be when x is the projection of A and B on x-axis
            x = (x1 + x2) / 2
    else:
        # Standard case
        t = y1 / (y1 + y2)
        x = x1 + t * (x2 - x1)
    
    # The reflection point is (x, 0)
    return x, 0.0

# Run the solution
x, y = solve()
print(f"{x:.10f} {y:.10f}")