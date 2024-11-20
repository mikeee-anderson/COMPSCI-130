def get_recaman_series(n, current_index=0, sequence=None):
    if sequence is None:
        sequence = [0]  # Start the sequence with a(0) = 0

    # Base case: If the sequence has the required length, return it
    if current_index == n:
        return sequence

    # Calculate the next value following Recamán's rule
    prev = sequence[-1]
    next_value = prev - (current_index + 1)

    if next_value > 0 and next_value not in sequence:
        sequence.append(next_value)
    else:
        sequence.append(prev + (current_index + 1))

    # Recursive call to process the next index
    return get_recaman_series(n, current_index + 1, sequence)
