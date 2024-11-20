class Point:
    def __init__(self, x = 1, y = 1):
        self.x = x
        self.y = y
    def get_score(self):
        score = self.x + self.y
        return score
    def __str__(self):
        return f"({self.x}, {self.y})"
    def get_middle_point(self, other):
        x_midpoint = (self.x + other.x) // 2
        y_midpoint = (self.y + other.y) // 2
        return Point(x_midpoint, y_midpoint)
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return (self.x == other.x) and (self.y == other.y)

points = [Point(), Point(10, 20), Point(20, 30)]
for point in points:
    print(point.get_score(), point)
print(type(points[0]))
temp = points[0].get_middle_point(points[1])
print(type(temp))
print(temp)
point4 = Point(10, 20)
print(points[1] == point4)
print(points[0] == point4)
print(point4 == 2)



