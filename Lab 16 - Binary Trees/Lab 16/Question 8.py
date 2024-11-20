class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.left)
            self.left = t

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.right)
            self.right = t

    def is_internal(self):
        return self.left != None or self.right != None

b_tree = BinaryTree(3)
print(b_tree.is_internal())
tree1 = BinaryTree(7, BinaryTree(2, BinaryTree(1), BinaryTree(5)), BinaryTree(9, None, BinaryTree(14)))
print(tree1.is_internal())
print(tree1.left.is_internal())
print(tree1.left.left.is_internal())
