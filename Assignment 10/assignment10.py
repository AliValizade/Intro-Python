class Shape:

    def __init__(self):
        self.Perimeter = 0
        self.Area = 0


class Rectangle(Shape):

    def __init__(self, length, breadth):
        Shape.Perimeter = (length + breadth) * 2
        Shape.Area = length * breadth

    def show_perimeter(self):
        return Shape.Perimeter

    def show_area(self):
        return Shape.Area


class Circle(Shape):

    def __init__(self, radius):
        Shape.Perimeter = (radius * 2) * 3.14
        Shape.Area = (radius * radius) * 3.14

    def show_perimeter(self):
        return Shape.Perimeter

    def show_area(self):
        return Shape.Area


r = Rectangle(2, 3)
print(f"Rectangle perimeter: {r.show_perimeter()} area: {r.show_area()}")
c = Circle(1 / 3.14)
print(f"Circle perimeter: {c.show_perimeter()} area: {c.show_area()}")