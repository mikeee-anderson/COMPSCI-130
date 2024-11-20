def get_consecutive_sum_string_lengths(first_node):
    # Initialize an empty list to store string lengths
    string_lengths = []

    # Traverse the linked list to gather the lengths of each string
    current_node = first_node
    while current_node is not None:
        string_lengths.append(len(current_node.data))  # Use data attribute directly
        current_node = current_node.next  # Move to the next node

    # Calculate consecutive sums
    consecutive_sums = []
    total_length = sum(string_lengths)  # Start with the sum of all lengths
    for length in string_lengths:
        consecutive_sums.append(total_length)  # Append the current total
        total_length -= length  # Subtract the current length to get the next total

    return consecutive_sums

