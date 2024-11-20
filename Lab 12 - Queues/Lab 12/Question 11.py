class CircularQueue:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.front = 0
        self.back = self.capacity - 1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("ERROR: The queue is full.")
        # Update back and wrap around using modulo
        self.back = (self.back + 1) % self.capacity
        self.items[self.back] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty.")
        # Retrieve the item to return
        item = self.items[self.front]
        # Update front and wrap around using modulo
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return item

    def show_contents(self):
        return f"{self.items}, front:{self.front}, back:{self.back}, count:{self.count}"

    def __str__(self):
        if self.is_empty():
            return "-> || ->"
        # Get all elements from front to back in the queue order
        queue_items = [str(self.items[(self.front + i) % self.capacity]) for i in range(self.count)]
        # Reverse the list as per the example format
        reversed_items = ", ".join(reversed(queue_items))
        return f"-> |{reversed_items}| ->"


