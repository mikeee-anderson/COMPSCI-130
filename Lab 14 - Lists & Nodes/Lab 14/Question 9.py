def print_node_chain(a_node):
    # Base case: If the node is None, just return
    if a_node is None:
        return

    # If it's the last node (next node is None), print the data without a trailing space
    if a_node.get_next() is None:
        print(a_node.get_data())
    else:
        # Print the data value from the current node followed by a space
        print(a_node.get_data(), end=' ')

    # Recursive call to the next node
    print_node_chain(a_node.get_next())