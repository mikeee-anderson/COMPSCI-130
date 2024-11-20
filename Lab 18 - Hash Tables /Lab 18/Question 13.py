class DoubleHashTable:
    def __init__(self, size=7, secondary_hash_value=5):
        self.size = size
        self.secondary_hash_value =  secondary_hash_value
        self.slots = [None] * self.size

    def get_step_size(self, key):
        return self.secondary_hash_value - (key % self.secondary_hash_value)

    def __str__(self):
        return str(self.slots)

    def get_hash_index(self, key):
        return key % len(self.slots)

    def put(self, key):
        initial_index = self.get_hash_index(key)
        if self.slots[initial_index] is not None:
            step = self.get_step_size(key)
            increment_step = step
            new_index = (initial_index + step) % self.size
            count = 0
            while self.slots[new_index] is not None:
                increment_step += step
                count += 1
                if count == self.size:
                    raise IndexError("ERROR: The hash table is full.")
                new_index = (initial_index + increment_step) % self.size
            self.slots[new_index] = key
        else:
            self.slots[initial_index] = key

    def is_empty(self):
        for value in self.slots:
            if value is not None:
                return False
        return True

    def is_full(self):
        for value in self.slots:
            if value is None:
                return False
        return True

    def clear(self):
        self.slots = [None] * self.size

    def __len__(self):
        count = 0
        for key in self.slots:
            if key is not None:
                count += 1
        return count

my_hash_table=DoubleHashTable(13,7)
my_hash_table.put(26)
my_hash_table.put(54)
my_hash_table.put(94)
my_hash_table.put(17)
my_hash_table.put(31)
my_hash_table.put(77)
my_hash_table.put(43)
my_hash_table.put(25)
print(my_hash_table)