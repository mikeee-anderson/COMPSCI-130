class Octagon:
    def __init__(self, side_length=1):
        self.side_length = side_length

    def set_side_length(self, side_length):
        if side_length > 0:
            self.side_length = side_length


octagon1 = Octagon()
print(octagon1.side_length)
octagon2 = Octagon(12)
print(octagon2.side_length)
octagon1.set_side_length(-1)
print(octagon1.side_length)
octagon1.set_side_length(6)
print(octagon1.side_length)