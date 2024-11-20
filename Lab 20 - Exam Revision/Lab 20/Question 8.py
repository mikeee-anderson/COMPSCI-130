class Queue:
    def __init__(self):
        self.items = []
        self.count = 0
    def is_empty(self):
        return self.count == 0
    def enqueue(self, item):
        self.items.insert(0,item)
        self.count += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        self.count -= 1
        return self.items.pop()
    def size(self):
        return self.count
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        return self.items[-1]
    def __str__(self):
        return '-> |' + str(self.items)[1:-1] + '| ->'
    def clear(self):
        self.items = []


def collecting_sweets(sweet_queue):
    while not sweet_queue.is_empty():
        child = sweet_queue.dequeue()  # Get the child at the front of the queue
        name, sweets = child  # Unpack the child's name and current sweets count

        # Give 5 sweets to the child
        sweets += 5

        if sweets >= 50:
            print(f"{name} has {sweets} sweets and goes home happy!")
        else:
            print(f"{name} has {sweets} sweets and rejoins the queue!")
            sweet_queue.enqueue((name, sweets))  # Re-add the child to the end of the queue