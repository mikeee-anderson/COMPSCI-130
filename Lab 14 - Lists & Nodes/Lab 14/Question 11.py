def insert_node_chain(current_node, node_chain):
    # Check if current_node is None, do nothing
    if current_node is None or node_chain is None:
        return

    # Find the last node in the node_chain
    last_node_in_chain = node_chain
    while last_node_in_chain.get_next() is not None:
        last_node_in_chain = last_node_in_chain.get_next()

    # Insert the node_chain after current_node
    last_node_in_chain.set_next(current_node.get_next())  # Link the end of node_chain to the next node of current_node
    current_node.set_next(node_chain)  # Link current_node to the head of node_chain