class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def swap_ends(self):
        if self.is_empty() or self.count == 1:
            # No swap needed if the list is empty or has only one node
            return

        first = self.head
        last = self.head
        second_last = None

        # Traverse to find the last and second last nodes
        while last.next is not None:
            second_last = last
            last = last.next

        # If there's only one node, do nothing
        if last == first:
            return

        # Swap the first and last nodes
        if second_last is not None:
            second_last.next = first  # Set the second last node's next to first
        first.next, last.next = None, first.next  # Set the new next for the first and last nodes
        self.head = last  # Update head to point to the new first node

    def __str__(self):
        self_str = "head --> "
        if self.is_empty():
            self_str += "None"
        else:
            current = self.head
            while current != None:
                if current.next == None:
                    self_str += str(current)
                else:
                    self_str += str(current) + " --> "
                current = current.next
        return self_str