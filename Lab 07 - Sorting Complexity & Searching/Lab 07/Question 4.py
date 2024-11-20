numbers = [92, 33, 63, 6, 66, 77, 74, 51, 30, 86]
def bubble_sort(data):
    comparison_list = []
    swaps_list = []
    for pass_num in range(len(data) - 1, 0, -1):
        comparison = 0
        swap = 0
        for i in range(0, pass_num):
            comparison += 1
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swap += 1
        swaps_list.append(swap)
        comparison_list.append(comparison)
    return (comparison_list, swaps_list)

result = bubble_sort(numbers)
print(result)