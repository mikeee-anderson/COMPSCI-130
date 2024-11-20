class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def double_push(self, element):
        self.push(element)
        self.push(element)

my_stack = Stack()
my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
my_stack.double_push('d')
print(my_stack.size())
for i in range(my_stack.size()):
    print(my_stack.pop(), end = ' ')