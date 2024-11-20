def create_stack_square(numbers):
    my_stack = Stack()
    numbers = numbers[::-1]
    for number in numbers:
        my_stack.push(number ** 2)
    return my_stack