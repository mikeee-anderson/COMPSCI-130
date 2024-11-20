numbers = [76, 53, 48, 24, 12]
def bubble_single_pass(data, index):
    for i in range(0, index):
        if data[i + 1] < data[i]:
            data[i + 1], data[i] = data[i], data[i + 1]





bubble_single_pass(numbers, 4)
print(numbers)