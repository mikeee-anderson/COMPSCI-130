class Triangle:
    def __init__(self, side_length_a=8, side_length_b=16, side_length_c=17):
        sides = sorted([side_length_a, side_length_b, side_length_c])
        self.side_length_a = sides[0]
        self.side_length_b = sides[1]
        self.side_length_c = sides[2]
    def get_perimeter(self):
        perimeter = self.side_length_a + self.side_length_b + self.side_length_c
        return perimeter
    def __str__(self):
        return f"Triangle: {self.side_length_a}, {self.side_length_b}, {self.side_length_c} (perimeter = {self.get_perimeter()})"



triangle1 = Triangle(16, 17, 8)
print(triangle1.get_perimeter())
print(triangle1)
triangle2 = Triangle(16, 8, 17)
print(triangle2)
print(type(triangle1))
triangle3 = Triangle(9,10,12)
print(triangle3)