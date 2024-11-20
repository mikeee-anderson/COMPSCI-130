def create_tree_from_nested_list(node_list):
    # Base case: if the list is None, return None (empty subtree)
    if node_list is None:
        return None

    # Extract the root, left subtree, and right subtree from the node_list
    root_value = node_list[0]
    left_subtree_list = node_list[1]
    right_subtree_list = node_list[2]

    # Recursively create the left and right subtrees
    left_subtree = create_tree_from_nested_list(left_subtree_list)
    right_subtree = create_tree_from_nested_list(right_subtree_list)

    # Create and return the BinaryTree node with the root value and its subtrees
    return BinaryTree(root_value, left_subtree, right_subtree)