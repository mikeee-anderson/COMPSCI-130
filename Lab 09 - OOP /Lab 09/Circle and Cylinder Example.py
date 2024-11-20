import math
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius
    def __str__(self):
        return 'A circle with a radius of {:.2f}cm'.format(self.radius)
    def get_area(self):
        return math.pi * self.radius * self.radius
    def get_perimeter(self):
        return 2 * math.pi * self.radius

class Cylinder:
    def __init__(self, circle, height = 1):
        self.circle = circle
        self.height = height
    def get_total_surface_ara(self):
        return 2 * self.circle.get_area() + self.circle.get_perimeter() * self.height