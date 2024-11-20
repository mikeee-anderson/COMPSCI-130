class CircularQueue:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.front = 0
        self.back = self.capacity - 1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def show_contents(self):
        return f"{self.items}, front:{self.front}, back:{self.back}, count:{self.count}"