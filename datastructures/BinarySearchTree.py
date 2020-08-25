from Node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.nodes = 0

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        return None
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        return None
                    current_node = current_node.right

    def print_node(self, node):
        print(f"value: {node.data}, left: {node.left}, right: {node.right}")

    def lookup(self, value):
        if self.root.data == value:
            self.print_node(self.root)
            return None
        current_node = self.root
        while True:
            if value < current_node.data:
                if current_node.left.data == value:
                    self.print_node(current_node.left)
                    break
                elif current_node.left is None:
                    return False
                current_node = current_node.left
            else:
                if current_node.right.data == value:
                    self.print_node(current_node.left)
                    break
                elif current_node.right is None:
                    return False
                current_node = current_node.right

# Test cases
my_binary_tree = BinarySearchTree()
my_binary_tree.insert(50)
my_binary_tree.insert(70)
my_binary_tree.insert(40)
my_binary_tree.insert(30)
my_binary_tree.insert(20)
print(my_binary_tree.lookup(40))
print(my_binary_tree.lookup(50))