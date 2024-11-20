def cumulative_sum(numbers):
    total = 0

    for i in range(len(numbers)):
        total += numbers[i]
        numbers[i] = total
