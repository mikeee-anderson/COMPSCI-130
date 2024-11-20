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

def print_tree(t, level):
    print(' ' * (level*4) + str(t.data))
    if t.left != None:
        print('(L)', end = '')
        print_tree(t.left, level + 1)
    if t.right != None:
        print('(R)', end = '')
        print_tree(t.right, level + 1)

tree = BinaryTree(1, BinaryTree(2), BinaryTree(3))
print_tree(tree, 0)

def increment_all_nodes(tree):
    if tree is None:
        return  # Base case: If the node is empty, do nothing.

    # Increment the current node's data using the provided increment_data method
    tree.increment_data()

    # Recursively increment all nodes in the left subtree
    increment_all_nodes(tree.left)

    # Recursively increment all nodes in the right subtree
    increment_all_nodes(tree.right)