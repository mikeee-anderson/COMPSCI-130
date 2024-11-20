def add_odd_data(binary_tree):
    # Base case: if the tree is None, return 0
    if binary_tree is None:
        return 0

    # Get the data of the current node
    current_value = binary_tree.get_data()

    # Check if the current value is odd
    if current_value % 2 != 0:
        # If it's odd, include it in the sum
        return current_value + add_odd_data(binary_tree.get_left()) + add_odd_data(binary_tree.get_right())
    else:
        # If it's not odd, just continue the recursion without adding
        return add_odd_data(binary_tree.get_left()) + add_odd_data(binary_tree.get_right())