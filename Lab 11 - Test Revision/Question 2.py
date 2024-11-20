def create_list(word):
    return [word[:i + 1] for i in range(len(word))]

print(create_list('cat'))
print(create_list('CASE'))
print(create_list('HELLO'))
result = create_list('Python')
print(type(result), result)