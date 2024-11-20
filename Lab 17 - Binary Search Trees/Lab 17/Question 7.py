class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.get_max()

my_tree = BinarySearchTree(15)
print(my_tree.get_max())