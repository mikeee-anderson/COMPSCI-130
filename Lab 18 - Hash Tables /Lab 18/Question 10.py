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
            while self.slots[new_index] is not None:
                initial_index += 1
                new_index = (initial_index + 1) % self.size
            self.slots[new_index] = key
        else:
            self.slots[initial_index] = key

my_hash_table = SimpleHashTable(13)
my_hash_table.put(13)
my_hash_table.put(26)
my_hash_table.put(39)
my_hash_table.put(52)
print(my_hash_table)
