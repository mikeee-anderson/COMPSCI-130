class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
    def add_after(self, value):
        new_node = Node(value,self.next )
        self.next = new_node
    def remove_after(self):
        self.next = self.next.get_next()
    def __str__(self):
        return str(self.data)

def print_node_chain(first_node):
    current = first_node
    while current:
        print(f"Node({current})", end=" -> ")
        current = current.get_next()
    print("None")

def create_chain_nodes_from_list(a_list):
    first_node = None
    for node in reversed(a_list):
        new_node = Node(node, first_node)
        first_node = new_node
    return first_node

chain_nodes = create_chain_nodes_from_list([1, 2, 3])
print_node_chain(chain_nodes)
print(type(chain_nodes))
print(type(chain_nodes.get_next()))
print(type(chain_nodes.get_next().get_next()))
print(chain_nodes.get_next().get_next().get_next())