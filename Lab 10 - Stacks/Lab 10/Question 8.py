class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("ERROR: The stack is empty!")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The stack is empty!")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        result_stack = str(self.items)[:-1] + " <-"
        return result_stack

    def clear(self):
        self.items = []
        return self.items

    def to_list(self):
        return self.items[::-1]



my_stack = Stack()
for num in range(4,7):
    my_stack.push(num)
result = my_stack.to_list()
my_stack.pop()
print(my_stack)
print(result)
print(type(result))