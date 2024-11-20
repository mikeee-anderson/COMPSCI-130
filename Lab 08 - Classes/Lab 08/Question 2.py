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
octagon1 = Octagon()
print(octagon1.side_length)
octagon2 = Octagon(2.5)
print(octagon2.get_interior_angle())
print(octagon2.get_exterior_angle())
print("perimeter = {:.2f},area = {:.2f}".format(octagon1.get_perimeter(), octagon1.get_area()))
print("perimeter = {:.2f},area = {:.2f}".format(octagon2.get_perimeter(), octagon2.get_area()))

