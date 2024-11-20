class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)[:-1] + ' <-'

def delete_mid(a_stack):
    if a_stack.is_empty():
        return
    middle_index = a_stack.size() // 2
    temp_stack = Stack()

    if a_stack.size() % 2 == 0:
        for i in range(middle_index - 1):
            temp_stack.push(a_stack.pop())
    else:
        for i in range(middle_index):
            temp_stack.push(a_stack.pop())

    a_stack.pop()
    while not a_stack.is_empty():
        temp_stack.push(a_stack.pop())

    while not temp_stack.is_empty():
        a_stack.push(temp_stack.pop())



my_stack = Stack()
print(my_stack)
delete_mid(my_stack)
print(my_stack)