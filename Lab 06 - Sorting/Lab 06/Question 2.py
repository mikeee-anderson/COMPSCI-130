numbers = [53, 48, 24, 76, 28]
def get_position_of_largest(data, index):
    updated_numbers = numbers[0:index + 1]
    for i in range(len(updated_numbers)):
        if i == 0:
            max_value = updated_numbers[i]
            index = i
        else:
            if max_value < updated_numbers[i]:
                max_value = updated_numbers[i]
                index = i
    return index


print(get_position_of_largest(numbers, 3))