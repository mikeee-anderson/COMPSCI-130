def sum_numbers(n):
    total = 0
    number = 0
    counter = 4
    while number < n:
        total += number
        number += 1
        counter += 3
    print(f"Number of operations: {counter}")
    return total


sum_numbers(2)