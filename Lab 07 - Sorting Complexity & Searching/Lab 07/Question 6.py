def compare(value, item_to_insert, counts_list):
    counts_list[0] += 1  # Increment the comparison count
    return value > item_to_insert


def insertion_sort(a_list):
    comparisons = []
    shifts = []

    for index in range(1, len(a_list)):
        item_to_insert = a_list[index]
        i = index - 1

        # Initialize counts for this iteration
        counts_list = [0, 0]  # [comparisons, shifts]

        # Perform the insertion sort step
        while i >= 0 and compare(a_list[i], item_to_insert, counts_list):
            a_list[i + 1] = a_list[i]
            counts_list[1] += 1  # Increment the shift count
            i -= 1

        a_list[i + 1] = item_to_insert

        # Append the counts for this iteration
        comparisons.append(counts_list[0])
        shifts.append(counts_list[1])

    return comparisons, shifts
