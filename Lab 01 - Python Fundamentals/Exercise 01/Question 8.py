# if remove elements from a list, do not use regular for loop instead remove from the end

def remove_10(numbers):
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] > 10:
            numbers.pop(i)
    return numbers
