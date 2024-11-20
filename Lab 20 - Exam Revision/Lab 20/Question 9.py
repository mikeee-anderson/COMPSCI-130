def get_max_odd_num(positive_numbers):
    # Base case: If the list is empty, return 0
    if not positive_numbers:
        return 0

    # Get the first number and the rest of the list
    first = positive_numbers[0]
    rest = positive_numbers[1:]

    # Check if the first number is odd
    if first % 2 != 0:
        # Get the maximum odd number from the rest and compare with the first
        max_odd_from_rest = get_max_odd_num(rest)
        return max(first, max_odd_from_rest)
    else:
        # Skip the first number and continue searching in the rest
        return get_max_odd_num(rest)

positive_numbers = [30, 3, 4, 37, 49, 43]
print(f"Maximum odd number = {get_max_odd_num(positive_numbers)}")