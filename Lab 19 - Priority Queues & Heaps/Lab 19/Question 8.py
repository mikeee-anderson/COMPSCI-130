class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
        self.number_of_swaps = 0

    def __str__(self):
        return str(self.binary_heap)

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def add_all_ignore_order(self, a_list):
        for element in a_list:
            self.size += 1
            self.binary_heap.append(element)


priority_queue = PriorityQueue()
priority_queue.add_all_ignore_order([9, 5, 11, 4, 18])
print(priority_queue)