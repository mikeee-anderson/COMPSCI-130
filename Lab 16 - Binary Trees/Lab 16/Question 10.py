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


def create_a_bigger_tree():
    tree = BinaryTree(88)

    tree.insert_left(66)
    tree.insert_right(58)

    tree.left.insert_left(78)
    tree.left.insert_right(42)

    tree.right.insert_left(60)
    tree.right.insert_right(10)
    return tree

