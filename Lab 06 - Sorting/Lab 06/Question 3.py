numbers = [76, 53, 48, 24, 12]
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

def selection_single_pass(data, index):
    largest_index = get_position_of_largest(data, index)
    data[largest_index], data[index] = data[index], data[largest_index]
    return data


selection_single_pass(numbers, 4)
print(numbers)