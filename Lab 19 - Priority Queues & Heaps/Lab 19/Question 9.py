class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
        self.number_of_swaps = 0

    def __str__(self):
        return str(self.binary_heap)

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_all_ignore_order(self, a_list):
        for element in a_list:
            self.size += 1
            self.binary_heap.append(element)

    def percolate_up(self, index):
        # While the element has a parent (index > 1) and violates the heap property
        while index // 2 > 0 and self.binary_heap[index] < self.binary_heap[index // 2]:
            # Swap the current node with its parent
            self.binary_heap[index], self.binary_heap[index // 2] = self.binary_heap[index // 2], self.binary_heap[index]
            # Increment the swap counter
            self.number_of_swaps += 1
            # Move to the parent index
            index = index // 2

    def insert(self, element):
        
