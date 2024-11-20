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
    def __eq__(self, other):
        if isinstance(other, Triangle):
            return (self.side_length_a == other.side_length_a) and (self.side_length_b == other.side_length_b) and (self.side_length_c == other.side_length_c)
        return False


    def __lt__(self, other):
        if isinstance(other, Triangle):
            return self.get_perimeter() < other.get_perimeter()
        return False





class Container:
    def __init__(self, min_perimeter = 10):
        self.min_perimeter = min_perimeter
        self.triangles = []
    def add_triangle(self, numbers):
        triangle = Triangle(*numbers)
        if triangle.get_perimeter() >= self.min_perimeter:
            self.triangles.append(triangle)
    def __str__(self):
       result = f"Minimum Perimeter = {self.min_perimeter}\n"
       for triangle in self.triangles:
           result += str(triangle) + "\n"

       return result.strip()





