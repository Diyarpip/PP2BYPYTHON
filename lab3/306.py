class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Получаем длину и ширину прямоугольника
length, width = map(int, input().split())

# Создаем объект Rectangle
rectangle = Rectangle(length, width)

# Выводим площадь
print(rectangle.area())