class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def size(self):
        return self.count

    def add(self, item):
        # Add new item at the head of the list
        self.head = Node(item, self.head)
        self.count += 1

    def __iter__(self):
        # Return an iterator object for the linked list
        return LinkedListIterator(self.head)


class LinkedListIterator:
    def __init__(self, head):
        # Initialize the iterator with the head of the list
        self.current = head

    def __next__(self):
        # Check if the iteration has finished
        if self.current is None:
            raise StopIteration

        # Retrieve the current node's data
        data = self.current.data
        # Move to the next node
        self.current = self.current.next
        return data