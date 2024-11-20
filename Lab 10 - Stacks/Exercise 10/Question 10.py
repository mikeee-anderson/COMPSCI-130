def join(a_stack):
    result = ''
    for i in range(a_stack.size()):
        result += str(a_stack.pop())
    return result

my_stack = Stack()
my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
result = join(my_stack)
print(type(result))
print(result)

