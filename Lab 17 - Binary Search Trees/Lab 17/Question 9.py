class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, value):
        if self.data == value:
            return
        elif value < self.data:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def get_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.get_max()


def get_height(tree):
    # Base case: if the tree is empty, the height is -1
    if tree is None or (tree.left is None and tree.right is None):
        return 0

    # Recursively calculate the height of the left and right subtrees
    left_height = get_height(tree.left)
    right_height = get_height(tree.right)

    # Return the greater height plus one for the current node
    return 1 + max(left_height, right_height)