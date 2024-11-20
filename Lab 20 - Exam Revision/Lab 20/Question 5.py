class ParkingSlot:
    def __init__(self, code='UNKNOWN', available=True):
        self.code = code
        self.available = available
    def is_available(self):
        if self.available == True:
            return True
        else:
            return False
    def set_occupied(self):
        self.available = False
    def __str__(self):
        if self.available == True:
            return f"{self.code} (available)"
        else:
            return f"{self.code} (occupied)"


slot1 = ParkingSlot('A0')
print(slot1.is_available())
print(slot1)
print(type(slot1))
slot1.set_occupied()
print(slot1)
slot2 = ParkingSlot('A1')
print(slot2)
print(slot1 == slot2)
slot3 = ParkingSlot()
print(slot3)