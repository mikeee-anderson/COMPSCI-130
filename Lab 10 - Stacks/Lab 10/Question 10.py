def zip_list_stack(a_list, a_stack):
    new_stack = Stack()
    for i in a_list:
        new_stack.push(i)
        new_stack.push(a_stack.pop())
    return new_stack
