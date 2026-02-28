import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# расстояние между точками
AB = math.hypot(x2 - x1, y2 - y1)

# расстояния до центра
OA = math.hypot(x1, y1)
OB = math.hypot(x2, y2)

# расстояние от центра до отрезка
vx = x2 - x1
vy = y2 - y1
t = (-x1*vx - y1*vy) / (vx*vx + vy*vy)
t = max(0, min(1, t))
px = x1 + t*vx
py = y1 + t*vy
dist = math.hypot(px, py)

if dist >= R:
    print(f"{AB:.10f}")
else:
    alpha = math.acos(R / OA)
    beta = math.acos(R / OB)
    theta = math.acos((x1*x2 + y1*y2) / (OA*OB))
    phi = theta - alpha - beta
    
    answer = math.sqrt(OA*OA - R*R) \
           + math.sqrt(OB*OB - R*R) \
           + R * phi
    
    print(f"{answer:.10f}")