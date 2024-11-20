def convert_tree_to_list(tree):
    # Base case: if the tree is empty (None), return None
    if tree is None:
        return None

    # Recursively convert the left and right subtrees
    left_subtree = convert_tree_to_list(tree.left)
    right_subtree = convert_tree_to_list(tree.right)

    # Return the current node's value and the converted subtrees
    return [tree.data, left_subtree, right_subtree]