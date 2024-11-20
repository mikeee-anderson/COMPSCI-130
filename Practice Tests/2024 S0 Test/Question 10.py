def selection_sort(data):
    counts = [0, 0]
    for pass_num in range(len(data) - 1, 0, -1):
        position_largest = 0
        for i in range(1, pass_num + 1):
            counts[0] += 1
            if data[i] > data[position_largest]:
                position_largest = i
        # Swap the largest element with the element at the end of the current pass
        if position_largest != pass_num:
            data[position_largest], data[pass_num] = data[pass_num], data[position_largest]
            counts[1] += 1  # Increment swaps count
    return tuple(counts)

def bubble_sort(data):
    counts = [0, 0]
    for pass_num in range(len(data) - 1, 0, -1):
        for i in range(pass_num):
            counts[0] += 1
            if data[i] > data[i + 1]:
                counts[1] += 1
                data[i], data[i + 1] = data[i + 1], data[i]
    return tuple(counts)


def compare(value, item_to_insert, counts_list):
    counts_list[0] += 1  # Add 1 to number of comparisons
    return value > item_to_insert


def insertion_sort(data):
    counts = [0, 0]  # counts[0] for comparisons, counts[1] for swaps
    for index in range(1, len(data)):
        item_to_insert = data[index]
        i = index - 1
        while i >= 0 and compare(data[i], item_to_insert, counts):
            data[i + 1] = data[i]
            i -= 1
            counts[1] += 1  # Increment swaps count
        data[i + 1] = item_to_insert
    return tuple(counts)


def analysis_sortings(numbers):
    # Create copies of the list to avoid sorting the same list multiple times
    numbers_for_selection = numbers[:]
    numbers_for_bubble = numbers[:]
    numbers_for_insertion = numbers[:]

    selection_sort_data = selection_sort(numbers_for_selection)
    bubble_sort_data = bubble_sort(numbers_for_bubble)
    insertion_sort_data = insertion_sort(numbers_for_insertion)

    print(f"Numbers: {numbers}")
    print(f"{'Sorting':>9}|{'Length':>7}|{'Comparisons':>12}|{'Swaps':>6}|")
    print("======================================")
    print(f"{'Selection':>9}|{len(numbers):>7}|{selection_sort_data[0]:>12}|{selection_sort_data[1]:>6}|")
    print(f"{'Bubble':>9}|{len(numbers):>7}|{bubble_sort_data[0]:>12}|{bubble_sort_data[1]:>6}|")
    print(f"{'Insertion':>9}|{len(numbers):>7}|{insertion_sort_data[0]:>12}|{insertion_sort_data[1]:>6}|")


# Example usage


# Example usage
analysis_sortings([3, 1, 5, 7, 6, 4, 2])