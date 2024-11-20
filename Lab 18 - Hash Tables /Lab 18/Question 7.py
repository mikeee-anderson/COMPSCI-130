def get_last_two_digit_hash(key, table_size):
    square = key ** 2
    square_string = str(square)
    last_2 = square_string[-2:]
    last_2 = int(last_2)
    return last_2 % table_size

print(get_last_two_digit_hash(655, 13))
print(get_last_two_digit_hash(654, 13))
print(get_last_two_digit_hash(653, 13))
