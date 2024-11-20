def create_numbers_dict(max_value):
    dictionary = {num: num ** 2 for num in range(max_value + 1)if num % 2 == 0}
    return dictionary


print(create_numbers_dict(5))