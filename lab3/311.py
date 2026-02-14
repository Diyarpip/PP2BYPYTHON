class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other):
        return Pair(self.a + other.a, self.b + other.b)



a, b, c, d = map(int, input().split())

p1 = Pair(a, b)
p2 = Pair(c, d)

result = p1.add(p2)

print(f"Result: {result.a} {result.b}")
