class EvenNumbersList:
    def __init__(self, evens=None):
        if evens == None
            self.numbers = []
        else:
            self.numbers = evens

    def add_number(self, value):
        if value % 2 == 0:
            self.numbers.append(value)

    def __str__(self):
        return str(self.numbers)

d1 = EvenNumbersList([2, 4, 6])
d1.add_number(8)
d1.add_number(10)
d2 = EvenNumbersList()
d2.add_number(12)
print("d1:", d1)
print("d2:", d2)