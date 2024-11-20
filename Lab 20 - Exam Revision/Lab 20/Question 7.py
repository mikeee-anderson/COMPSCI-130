def interleave_stacks(stack1, stack2):
    new_stack = Stack()
    temp_stack1 = Stack()  # Temporary stack for stack1
    temp_stack2 = Stack()  # Temporary stack for stack2

    # Interleave items from both stacks
    while not stack1.is_empty() and not stack2.is_empty():
        temp_stack1.push(stack1.pop())  # Pop from stack1 to temp1
        temp_stack2.push(stack2.pop())  # Pop from stack2 to temp2

    # If one stack is empty, we need to push the remaining items from the other stack
    while not stack1.is_empty():
        temp_stack1.push(stack1.pop())

    while not stack2.is_empty():
        temp_stack2.push(stack2.pop())

    # Now transfer items from temp_stack1 and temp_stack2 to new_stack
    while not temp_stack1.is_empty() or not temp_stack2.is_empty():
        if not temp_stack1.is_empty():
            new_stack.push(temp_stack1.pop())
        if not temp_stack2.is_empty():
            new_stack.push(temp_stack2.pop())

    return new_stack