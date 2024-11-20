numbers = [92, 33, 63, 6, 66, 77, 74, 51, 30, 86]
def my_bubble_sort(data):
    for index in range(len(data) - 1, 0, -1):
        for j in range(0, index):
            if data[j + 1] < data[j]:
                data[j + 1], data[j] = data[j], data[j + 1]


my_bubble_sort(numbers)
print(numbers)