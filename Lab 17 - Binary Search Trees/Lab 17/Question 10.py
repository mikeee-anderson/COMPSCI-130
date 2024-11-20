def is_balanced(bst):
    if bst is None:
        return True  # An empty tree is balanced

    # Get the height of the left and right subtrees
    left_height = get_height(bst.left)
    right_height = get_height(bst.right)

    # Check if the current node is balanced
    if abs(left_height - right_height) > 1:
        return False

    # Recursively check if the left and right subtrees are balanced
    return is_balanced(bst.left) and is_balanced(bst.right)
