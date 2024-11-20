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
            if current.data % 2 == 0:  # Check if the current node contains an even number
                new_node = Node(0, current.next)  # Create a new node with value 0
                current.next = new_node  # Insert the new node after the first even number
                self.count += 1  # Increase the count of nodes
                return  # Exit after inserting the node
            current = current.next

    def increment_data(self):
        current = self.head
        while current:
            current.data += 1  # Add 1 to the value of each node's data
            current = current.next