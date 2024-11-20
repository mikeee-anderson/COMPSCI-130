
def my_selection_sort(data):
    for index in range(len(data) - 1, 0, -1 ):
        max_index = 0
        for j in range(1, index + 1):
            if data[j] > data[max_index]:
                max_index = j
        data[max_index], data[index] = data[index], data[max_index]




numbers = [76, 53, 48, 24, 12]
my_selection_sort(numbers)
print(numbers)