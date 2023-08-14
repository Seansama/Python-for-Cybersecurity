class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return 'x: {}, y: {}'.format(self.x, self.y)


vector1 = Vector(3, 4)
vector2 = Vector(5, 9)

print(vector1)
print(vector2)

vector3 = vector1 + vector2
print(vector3)

vector4 = vector3 - vector2
print(vector4)
