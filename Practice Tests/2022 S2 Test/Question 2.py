def get_first_digits(numbers):
    return [int(str(number)[0]) for number in numbers]

print(get_first_digits([20, 23, 16, 19, 16, 5]))
print(get_first_digits([146, 23, 1]))