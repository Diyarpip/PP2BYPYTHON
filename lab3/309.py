import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius * self.radius


r = int(input())


circle = Circle(r)


print(f"{circle.area():.2f}")