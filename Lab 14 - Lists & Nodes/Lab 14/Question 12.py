def get_sum_cubes(a_node):
    # Base case: If the node is None, return 0
    if a_node is None:
        return 0

    # Get the cube of the current node's data directly
    current_cube = a_node.data ** 3

    # Recursive call to the next node and accumulate the sum
    return current_cube + get_sum_cubes(a_node.next)