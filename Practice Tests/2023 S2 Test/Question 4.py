def calculate_changes(numbers):
    raw_list = [f"{(numbers[i + 1] - numbers[i]) / abs(numbers[i]) * 100:.0f}" for i in range(len(numbers)-1)]
    return [int(number) for number in raw_list]

print(calculate_changes([60, 71, 60]))
print(calculate_changes([-9, 3, 4, 6, 2]))