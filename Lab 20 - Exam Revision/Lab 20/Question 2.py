def remove_even_multiples_of_5(numbers):
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] % 2 == 0:
            if numbers[i] % 5 == 0:
                numbers.pop(i)
    return numbers


data = [6, 8, 12, 15, 6, 2, 31, 28, 38, 49, 44, 41, 18, 17, 36, 25, 30, 9]
remove_even_multiples_of_5(data)
print(data)