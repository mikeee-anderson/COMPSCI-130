class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def size(self):
        return self.count

    def add(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def clear(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def __str__(self):
        if self.is_empty():
            return ""

        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return "Head: " + " --> ".join(result)

    def insert_after_first_even(self):
        current = self.head
        while current:
            if current.data % 2 == 0:
                new_node = Node(0, current.next)
                current.next = new_node
                self.count += 1
                return
            current = current.next

    def increment_data(self):
        current = self.head
        while current:
            current.data += 1
            current = current.next

    def remove_first(self):
        if self.is_empty():
            return
        self.head = self.head.next
        self.count -= 1

    def remove_last(self):
        if self.is_empty():
            return
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        self.count -= 1

    def simple_remove(self, value):
        if self.is_empty():
            return

        # If the value to be removed is at the head of the list
        if self.head.data == value:
            self.head = self.head.next
            self.count -= 1
            return

        # Traverse the list to find the node with the specified value
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next  # Skip the node with the value
                self.count -= 1
                return
            current = current.next