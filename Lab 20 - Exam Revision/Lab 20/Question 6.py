class ParkingSlot:
    def __init__(self, code='UNKNOWN', available=True):
        self.code = code
        self.available = available
    def is_available(self):
        return self.available
    def set_occupied(self):
        self.available = False
    def __str__(self):
        return f"{self.code} (available)" if self.available else f"{self.code} (occupied)"

class ParkingBlock:
    def __init__(self, name, code_prefix, capacity):
        self.name = name
        self.parking_slots = [ParkingSlot(f"{code_prefix}{i}") for i in range(capacity)]

    def get_first_available_slot(self):
        for slot in self.parking_slots:
            if slot.is_available():
                return slot
        return None

    def get_available_list(self):
        return [slot for slot in self.parking_slots if slot.is_available()]

    def get_available_slots_count(self):
        return len(self.get_available_list())

    def __str__(self):
        available_count = self.get_available_slots_count()
        available_slots = [str(slot) for slot in self.parking_slots if slot.is_available()]
        slots_info = ",".join(available_slots)
        return f"{self.name}({available_count}): {slots_info}"

block1 = ParkingBlock("SOUTH", "S", 3)
print(block1)
slot1 = block1.get_first_available_slot()
slot1.set_occupied()
print(block1)
slot2 = block1.get_first_available_slot()
slot2.set_occupied()
print(block1)
slot3 = block1.get_first_available_slot()
print(slot3)
slot3.set_occupied()
slot4 = block1.get_first_available_slot()
print(slot4)