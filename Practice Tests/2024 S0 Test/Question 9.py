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

class ConnectedLine:
    def __init__(self):
        self.points = [Point(0, 0 )]
    def add_point(self, point):
        if isinstance(point, Point):
            self.points.append(point)
    def get_total_score(self):
        total_score = sum(Point.get_score() for Point in self.points)
        return total_score
    def __str__(self):
        if len(self.points) == 1 and self.points[0] == Point(0, 0):
            return ""
        return ' -> '.join(str(Point) for Point in self.points)
    def get_middle_points(self):
        # Obtain a list of middle points between each pair of consecutive points
        middle_points = []
        for i in range(len(self.points) - 1):
            middle_point = self.points[i].get_middle_point(self.points[i + 1])
            middle_points.append(middle_point)
        return middle_points




points = [Point(), Point(10, 20), Point(20, 30)]
line = ConnectedLine()
for point in points:
    line.add_point(point)
print(line, type(line))
print(line.get_total_score())
result = line.get_middle_points()
print(type(result))
print('\n'.join(str(point) for point in result))
line2 = ConnectedLine()
print(line2)
print(line)

