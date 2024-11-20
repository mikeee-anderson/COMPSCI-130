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


def create_a_bigger_bst():
    bigger_tree =  BinarySearchTree(41, BinarySearchTree(22,  BinarySearchTree(18), BinarySearchTree(35) ), BinarySearchTree(61, BinarySearchTree(54), BinarySearchTree(77)))
    return bigger_tree