class SimpleHashTable:
    def __init__(self, size=7):
        self.size = size
        self.slots = [None] * self.size

    def __str__(self):
        return str(self.slots)

    def get_hash_index(self, key):
        return key % len(self.slots)

    def put(self, key):
        initial_index = self.get_hash_index(key)
        if self.slots[initial_index] is not None:
            new_index = (initial_index + 1) % self.size
            count = 0
            while self.slots[new_index] is not None:
                initial_index += 1
                count += 1
                if count == self.size:
                    raise IndexError("ERROR: The hash table is full.")
                new_index = (initial_index + 1) % self.size
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




