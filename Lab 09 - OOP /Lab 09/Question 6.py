import math
class Point:
    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def get_distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class PolyLine:
    def __init__(self):
        self.points = []
    def get_point(self, index):
        return self.points[index]
    def  add_point(self, x, y):
        p = Point(x, y)
        self.points.append(p)