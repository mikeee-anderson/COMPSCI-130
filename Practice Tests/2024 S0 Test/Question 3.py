def get_median_value(numbers):
    new_list = sorted(numbers)
    if len(numbers) % 2 == 0:
        index_1 = len(numbers) // 2
        index_2 = index_1 - 1
        median = (new_list[index_2] + new_list[index_1]) / 2
        return median
    else:
        return new_list[len(numbers) // 2]


numbers = [3, 9, 4]
print(get_median_value(numbers))
print(numbers)
print(get_median_value([13, 10, 9, 3]))
print(get_median_value([13, 10, 9, 3, 4]))