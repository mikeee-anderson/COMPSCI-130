class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            raise IndexError("ERROR: The queue is empty!")

    def peek(self):
        if len(self.items) != 0:
            return self.items[len(self.items)-1]
        else:
            raise IndexError("ERROR: The queue is empty!")
