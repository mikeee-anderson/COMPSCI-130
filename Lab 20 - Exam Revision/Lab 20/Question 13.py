def reconstruct_tree(inorder_sequence, preorder_sequence):
    # Base case: if the sequences are empty, return None
    if not inorder_sequence or not preorder_sequence:
        return None

    # The first element of the preorder sequence is the root
    root_value = preorder_sequence[0]

    # Create the root node representation
    root = [root_value, None, None]

    # Find the index of the root in the inorder sequence
    root_index = inorder_sequence.index(root_value)

    # Recursively reconstruct the left subtree
    left_inorder = inorder_sequence[:root_index]
    left_preorder = preorder_sequence[1:1 + len(left_inorder)]
    root[1] = reconstruct_tree(left_inorder, left_preorder)

    # Recursively reconstruct the right subtree
    right_inorder = inorder_sequence[root_index + 1:]
    right_preorder = preorder_sequence[1 + len(left_inorder):]
    root[2] = reconstruct_tree(right_inorder, right_preorder)

    return root