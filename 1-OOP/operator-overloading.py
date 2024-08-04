class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define what happens when you add two vectors, aka OVERLOADING the ADDITION operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # define what happens when you subtract two vectors, aka OVERLOADING the SUBTRACTION operator
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "X: {}, Y: {}".format(self.x, self.y)

v1 = Vector(4, 5)
v2 = Vector(2, 3)

print(v1)
print(v2)
print(v1 + v2)
print(v1 - v2)