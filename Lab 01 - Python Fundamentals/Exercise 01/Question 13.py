def generate_odd_numbers(max_value):
    list1 = [ n for n in range(1, max_value + 1, 2)]
    return list1
print(generate_odd_numbers(10))