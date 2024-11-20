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

my_stack = Stack()
my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
print(my_stack)
print(my_stack.size())
my_stack.clear()
print(my_stack.size())
stack2 = Stack()
stack2.push("hello")
stack2.push("world")
print(stack2)