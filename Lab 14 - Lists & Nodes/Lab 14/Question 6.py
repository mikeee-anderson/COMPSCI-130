class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def add_after(self, value):
        new_node = Node(value, self.next)
        self.next = new_node

    def increment_data(self):
        self.data += 1

