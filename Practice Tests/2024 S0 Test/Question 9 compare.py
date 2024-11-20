class ConnectedLine:
    def __init__(self):
        self.points = [Point(0, 0)]
    def add_point(self, point):
        if isinstance(point, Point):
            self.points.append(point)
        else:
            raise TypeError("Expected a Point object")
    def get_total_score(self):
        return sum(point.get_score() for point in self.points)
    def __str__(self):
        if len(self.points) == 1 and self.points[0] == Point(0, 0):
            return ""
        return ' -> '.join(str(point) for point in self.points)
    def get_middle_points(self):
        middle_points = []
        for i in range(len(self.points) - 1):
            middle_point = self.points[i].get_middle_point(self.points[i + 1])
            middle_points.append(middle_point)
        return middle_points