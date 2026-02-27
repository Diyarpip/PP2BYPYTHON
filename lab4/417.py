import math

def solve():
    
    R = float(input().strip())
    x1, y1 = map(float, input().strip().split())
    x2, y2 = map(float, input().strip().split())
    

    dx = x2 - x1
    dy = y2 - y1
    
    
    
    a = dx*dx + dy*dy
    b = 2*(x1*dx + y1*dy)
    c = x1*x1 + y1*y1 - R*R
    
    
    if a == 0:
        
        if x1*x1 + y1*y1 <= R*R:
            return 0.0
        return 0.0
    
   
    discriminant = b*b - 4*a*c
    
    
    if discriminant < 0:
        return 0.0
    
    
    sqrt_disc = math.sqrt(discriminant)
    t1 = (-b - sqrt_disc) / (2*a)
    t2 = (-b + sqrt_disc) / (2*a)
    
    
    t_intersections = sorted([t for t in [t1, t2] if 0 <= t <= 1])
    
    
    if len(t_intersections) == 2:
        
        x_int1 = x1 + t_intersections[0]*dx
        y_int1 = y1 + t_intersections[0]*dy
        x_int2 = x1 + t_intersections[1]*dx
        y_int2 = y1 + t_intersections[1]*dy
        
        segment_length = math.sqrt((x_int2 - x_int1)**2 + (y_int2 - y_int1)**2)
        return segment_length
    
    
    a_inside = (x1*x1 + y1*y1 <= R*R)
    b_inside = (x2*x2 + y2*y2 <= R*R)
    
    if a_inside and b_inside:
        
        return math.sqrt(dx*dx + dy*dy)
    
    elif a_inside and not b_inside:
        
        if len(t_intersections) == 1:
            
            x_int = x1 + t_intersections[0]*dx
            y_int = y1 + t_intersections[0]*dy
            return math.sqrt((x_int - x1)**2 + (y_int - y1)**2)
    
    elif not a_inside and b_inside:
        
        if len(t_intersections) == 1:
            x_int = x1 + t_intersections[0]*dx
            y_int = y1 + t_intersections[0]*dy
            return math.sqrt((x2 - x_int)**2 + (y2 - y_int)**2)
    
    
    return 0.0


result = solve()
print(f"{result:.10f}")