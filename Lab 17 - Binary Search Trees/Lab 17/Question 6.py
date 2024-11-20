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




tree = BinarySearchTree(15)
tree.insert(99)
tree.insert(199)
tree.insert(6)
print_tree(tree, 0)

