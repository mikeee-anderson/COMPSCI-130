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