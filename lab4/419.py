import math

def solve():
    # Read inputs
    R = float(input().strip())
    x1, y1 = map(float, input().strip().split())
    x2, y2 = map(float, input().strip().split())
    
    # Check if both points are outside or on the circle
    distA_sq = x1*x1 + y1*y1
    distB_sq = x2*x2 + y2*y2
    
    # If either point is inside the circle (but problem guarantees they're outside)
    # Just to be safe:
    if distA_sq < R*R - 1e-10 or distB_sq < R*R - 1e-10:
        # This shouldn't happen per problem statement
        pass
    
    # Check if the straight line segment from A to B intersects the circle
    # We need to find the closest point on line AB to origin
    
    # Vector from A to B
    dx = x2 - x1
    dy = y2 - y1
    
    # Parameter t for closest point to origin
    # The line: P(t) = A + t*(B-A), t∈[0,1]
    # We want point where derivative of |P(t)|² = 0
    
    # Compute closest point parameter
    if dx*dx + dy*dy > 0:
        t = -(x1*dx + y1*dy) / (dx*dx + dy*dy)
    else:
        t = 0  # A and B are the same point
    
    # Closest point on the infinite line
    x_closest = x1 + t*dx
    y_closest = y1 + t*dy
    
    # Distance from origin to closest point
    dist_closest = math.sqrt(x_closest*x_closest + y_closest*y_closest)
    
    # Check if the closest point is within the circle and between A and B
    intersects = False
    if dist_closest < R - 1e-10:  # Strictly inside
        if 0 <= t <= 1:  # Between A and B
            intersects = True
    
    if not intersects:
        # Check if either endpoint is inside (but they shouldn't be)
        # Return direct distance
        return math.sqrt(dx*dx + dy*dy)
    
    # Path goes around the circle
    # Find tangent points from A and B to the circle
    
    # Distance from A to origin
    dA = math.sqrt(distA_sq)
    
    # Angle between OA and tangent line
    alpha_A = math.acos(R / dA)
    
    # Angle of OA
    theta_A = math.atan2(y1, x1)
    
    # Two possible tangent points - choose the one that makes sense
    # For the shortest path around, we need to choose the correct side
    # Let's calculate both and then decide based on which gives the shorter arc
    
    # Tangent point candidates
    t1_A_x = R * math.cos(theta_A + alpha_A)
    t1_A_y = R * math.sin(theta_A + alpha_A)
    t2_A_x = R * math.cos(theta_A - alpha_A)
    t2_A_y = R * math.sin(theta_A - alpha_A)
    
    # Distance from B to origin
    dB = math.sqrt(distB_sq)
    
    # Angle between OB and tangent line
    alpha_B = math.acos(R / dB)
    
    # Angle of OB
    theta_B = math.atan2(y2, x2)
    
    # Tangent point candidates
    t1_B_x = R * math.cos(theta_B + alpha_B)
    t1_B_y = R * math.sin(theta_B + alpha_B)
    t2_B_x = R * math.cos(theta_B - alpha_B)
    t2_B_y = R * math.sin(theta_B - alpha_B)
    
    # We need to find which combination of tangent points gives the shortest path
    # The path consists of |A→T_A| + arc(T_A→T_B) + |T_B→B|
    
    # Calculate distances from A to each tangent point
    distA_t1 = math.sqrt((t1_A_x - x1)**2 + (t1_A_y - y1)**2)
    distA_t2 = math.sqrt((t2_A_x - x1)**2 + (t2_A_y - y1)**2)
    
    # Calculate distances from B to each tangent point
    distB_t1 = math.sqrt((t1_B_x - x2)**2 + (t1_B_y - y2)**2)
    distB_t2 = math.sqrt((t2_B_x - x2)**2 + (t2_B_y - y2)**2)
    
    # Calculate arc lengths between tangent points
    # Arc length = R * angle_between_points
    
    # Angle between t1_A and t1_B
    angle1 = math.acos((t1_A_x*t1_B_x + t1_A_y*t1_B_y) / (R*R))
    
    # Angle between t1_A and t2_B
    angle2 = math.acos((t1_A_x*t2_B_x + t1_A_y*t2_B_y) / (R*R))
    
    # Angle between t2_A and t1_B
    angle3 = math.acos((t2_A_x*t1_B_x + t2_A_y*t1_B_y) / (R*R))
    
    # Angle between t2_A and t2_B
    angle4 = math.acos((t2_A_x*t2_B_x + t2_A_y*t2_B_y) / (R*R))
    
    # Calculate total path lengths
    path1 = distA_t1 + R*angle1 + distB_t1
    path2 = distA_t1 + R*angle2 + distB_t2
    path3 = distA_t2 + R*angle3 + distB_t1
    path4 = distA_t2 + R*angle4 + distB_t2
    
    # Take the minimum path
    shortest = min(path1, path2, path3, path4)
    
    return shortest

# Run the solution
result = solve()
print(f"{result:.10f}")