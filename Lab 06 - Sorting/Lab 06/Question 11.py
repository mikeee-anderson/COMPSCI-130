def my_insertion_sort(a_list):
    # Iterate over the list starting from the second element
    for i in range(1, len(a_list)):
        # Temporary variable to hold the value to be inserted
        value_to_insert = a_list[i]
        # Initialize current_index to the position before i
        current_index = i - 1

        # Shift elements of the sorted portion of the list to the right
        while current_index >= 0 and a_list[current_index] > value_to_insert:
            a_list[current_index + 1] = a_list[current_index]
            current_index -= 1

        # Insert the value_to_insert in the correct position
        a_list[current_index + 1] = value_to_insert
