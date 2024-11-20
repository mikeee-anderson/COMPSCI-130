class SimpleHashTable:
    def __init__(self, size=7):
        self.size = size
        self.slots = [None] * self.size

    def __str__(self):
        return str(self.slots)

    def get_hash_index(self, key):
        return key % len(self.slots)

my_hash_table = SimpleHashTable()
print(my_hash_table)
print(type(my_hash_table))
print(my_hash_table.get_hash_index(12))