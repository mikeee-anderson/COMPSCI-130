import math
class Octagon:
    def __init__(self, side_length=1):
        self.side_length = side_length

    def set_side_length(self, side_length):
        if side_length > 0:
            self.side_length = side_length
    def get_interior_angle(self):
       return 135
    def get_exterior_angle(self):
        return 45
    def get_perimeter(self):
        return 8 * self.side_length
    def get_area(self):
        return 2 * (1 + math.sqrt(2)) * self.side_length * self.side_length
    def __repr__(self):
        return f"Octagon({self.side_length})"
    def __str__(self):
        perimeter = round(self.get_perimeter(), 2)
        area = round(self.get_area(), 2)
        return f"An octagon with a perimeter of {perimeter:.2f} and an area of {area:.2f}."
    def __eq__(self, other):
        if not isinstance(other, Octagon):
            return False
        return self.side_length == other.side_length

octagon1 = Octagon()
octagon2 = Octagon(5)
print(octagon1 == octagon2)
print(octagon2 == (5))
print(octagon1 == 1)
print(octagon1 == (1,))
octagon3 = Octagon(1)
print(octagon1 == octagon3)

octagon1 = Octagon(4)
octagon2 = Octagon(5)
octagon3 = Octagon(5)
print(octagon1  == octagon3 )
print(octagon2  == octagon3 )
print(octagon1  == octagon2 )