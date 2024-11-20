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
            return  # If the list is empty, do nothing
        self.head = self.head.next  # Move the head to the next node, effectively removing the first node
        self.count -= 1  # Decrease the count of nodes