def increment_node_chain(first_node):
    # Increment the data of the first node
    first_node.set_data(first_node.get_data() + 1)

    # Start with the next node
    current = first_node.get_next()

    # Traverse the rest of the nodes in the chain
    while current is not None:
        # Increment the data of the current node
        current.set_data(current.get_data() + 1)
        # Move to the next node
        current = current.get_next()