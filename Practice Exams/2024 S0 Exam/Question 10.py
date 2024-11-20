class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
    def add_after(self, value):
        new_node = Node(value,self.next )
        self.next = new_node
    def remove_after(self):
        self.next = self.next.get_next()
    def __str__(self):
        return str(self.data)

    def remove_first_odd_node(self):
        # Check if the list is empty
        if self.is_empty():
            return None

        # Check if the head node itself has an odd value
        if self.head.get_data() % 2 != 0:
            odd_value = self.head.get_data()
            self.head = self.head.get_next()
            self.count -= 1
            return odd_value

        # Traverse the list to find the first odd node
        current = self.head
        while current.get_next() is not None:
            if current.get_next().get_data() % 2 != 0:
                odd_value = current.get_next().get_data()
                current.set_next(current.get_next().get_next())
                self.count -= 1
                return odd_value

            current = current.get_next()

        # Return None if no odd node was found
        return None