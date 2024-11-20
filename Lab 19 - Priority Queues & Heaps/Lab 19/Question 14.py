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
            self.binary_heap[index], self.binary_heap[index // 2] = self.binary_heap[index // 2], self.binary_heap[
                index]
            # Increment the swap counter
            self.number_of_swaps += 1
            # Move to the parent index
            index = index // 2

    def insert(self, element):
        self.binary_heap.append(element)
        self.size += 1
        self.percolate_up(self.size)

    def get_smaller_child_index(self, index):
        left_child_index = 2 * index
        right_child_index = (2 * index) + 1
        if right_child_index > self.size:
            return left_child_index

        if self.binary_heap[left_child_index] > self.binary_heap[right_child_index]:
            return right_child_index
        else:
            return left_child_index

    def percolate_down(self, index):
        # While the current index has a child (i.e., is not a leaf node)
        while (index * 2) <= self.size:
            # Get the index of the smaller child
            smaller_child_index = self.get_smaller_child_index(index)

            # If the heap property is violated, swap the current node with its smaller child
            if self.binary_heap[index] > self.binary_heap[smaller_child_index]:
                # Swap
                self.binary_heap[index], self.binary_heap[smaller_child_index] = (
                    self.binary_heap[smaller_child_index],
                    self.binary_heap[index],
                )
                # Increment the swap counter
                self.number_of_swaps += 1
            else:
                break  # If the heap property is maintained, stop percolating down

            # Move to the next index (i.e., the smaller child's index)
            index = smaller_child_index

    def create_heap_fast(self, values):
        # Step 1: Add all elements from the list to the binary heap
        self.binary_heap.extend(values)
        self.size = len(values)

        # Step 2: Set the starting index position (index of the last element which has a child)
        start_index = self.size // 2

        # Step 3: Rearrange the elements by percolating down starting from the start_index
        for index in range(start_index, 0, -1):
            self.percolate_down(index)

    def delete_minimum(self):
        if self.size == 0:
            raise IndexError("delete_minimum() called on an empty heap")

        # The minimum element is always the root at index 1
        min_element = self.binary_heap[1]

        # Move the last element to the root and remove the last element
        self.binary_heap[1] = self.binary_heap[self.size]
        self.binary_heap.pop()
        self.size -= 1

        # Percolate down to restore the heap property
        if self.size > 0:
            self.percolate_down(1)

        return min_element