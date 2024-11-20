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

    def get_string_length(self):
        return len(self.data)

    def get_sum_string_lengths(self):
        total_length = len(self.data)
        current = self.next
        while current is not None:
            total_length += len(current.data)
            current = current.next

        return total_length

node1 = Node('abc')
node2 = Node('def')
node1.next = node2
print(node1.get_sum_string_lengths())
print(node2.get_sum_string_lengths())
