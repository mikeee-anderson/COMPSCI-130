numbers = [70, 48, 54, 79, 33]

def selection_sort(data):
    comparison_list = []
    swaps_list = []
    for pass_num in range(len(data) - 1, 0, -1):
        comparison = 0
        position_largest = 0
        for i in range(1, pass_num + 1):
            comparison += 1
            if data[i] > data[position_largest]:

                position_largest = i
        data[position_largest], data[i] = data[i], data[position_largest]
        swaps_list.append(1)
        comparison_list.append(comparison)

    return (comparison_list, swaps_list)


result = selection_sort(numbers)
print(result)