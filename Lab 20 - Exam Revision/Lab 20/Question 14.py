class MaxHeap:
    def __init__(self):
        self.binary_heap = ['0']
        self.size = 0

    def insert(self, gamer):
        self.binary_heap.append(gamer)
        self.size += 1
        self.percolate_up(self.size)

    def percolate_up(self, index):
        while index // 2 > 0:
            if self.binary_heap[index].score > self.binary_heap[index // 2].score:
                self.binary_heap[index], self.binary_heap[index // 2] = self.binary_heap[index // 2], self.binary_heap[index]
            index = index // 2

    def percolate_down(self, index):
        while (index * 2) <= self.size:
            larger_child = self.get_larger_child_index(index)
            if self.binary_heap[index].score < self.binary_heap[larger_child].score:
                self.binary_heap[index], self.binary_heap[larger_child] = self.binary_heap[larger_child], self.binary_heap[index]
            index = larger_child

    def get_larger_child_index(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.binary_heap[index * 2].score > self.binary_heap[index * 2 + 1].score:
                return index * 2
            else:
                return index * 2 + 1

    def get_max_value(self):
        if self.size == 0:
            return None
        max_value = self.binary_heap[1]
        self.binary_heap[1] = self.binary_heap[self.size]
        self.size -= 1
        self.binary_heap.pop()
        self.percolate_down(1)
        return max_value

    def is_empty(self):
        return self.size == 0