class RegularPolygon:
    def __init__(self, num_sides=3, side_length=1):
        self.num_sides = num_sides
        self.side_length = side_length
    def get_perimeter(self):
        return self.num_sides * self.side_length
    def __str__(self):
        perimeter = self.get_perimeter()
        return"Polygon({:.2f})".format(perimeter)

polygon1 = RegularPolygon(6, 3.9)
polygon2 = RegularPolygon()
print(polygon1)
print(polygon2)
print(type(polygon1))
print(polygon1.get_perimeter(), polygon2.get_perimeter())
