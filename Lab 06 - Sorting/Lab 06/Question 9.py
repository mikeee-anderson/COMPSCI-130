def shifting(data, index):
    # Temporary variable to hold the value to be inserted
    value_to_insert = data[index]
    # Retrieve the current_index
    current_index = index - 1

    # Shift elements to the right while the current_index is valid and the element at current_index is greater than value_to_insert
    while current_index >= 0 and data[current_index] > value_to_insert:
        data[current_index + 1] = data[current_index]
        current_index -= 1