import math


class BST:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.leftChild = None
            self.rightChild = None

    def insert(self, value):
        new_node = self.Node(value)
        current = self.root

        if self.root is None:
            self.root = new_node
            return

        while True:
            if current.value > value:
                if current.leftChild is None:
                    current.leftChild = new_node
                    break
                current = current.leftChild
            else:
                if current.rightChild is None:
                    current.rightChild = new_node
                    break
                current = current.rightChild

    def find(self, value):
        current = self.root
        while current is not None:
            if value < current.value:
                current = current.leftChild
            elif value > current.value:
                current = current.rightChild
            else:
                return True
        return False

    def pre_order_traversal(self):
        self.helper_pre_order_traversal(self.root)

    def helper_pre_order_traversal(self, root):
        if root is None:
            return

        print(root.value)
        self.helper_pre_order_traversal(root.leftChild)
        self.helper_pre_order_traversal(root.rightChild)

    def in_order_traversal(self):
        self.helper_inorder_traversal(self.root)

    def helper_inorder_traversal(self, root):
        if root is None:
            return

        self.helper_inorder_traversal(root.leftChild)
        print(root.value)
        self.helper_inorder_traversal(root.rightChild)

    def postorder_traversal(self):
        self.helper_postorder_traversal(self.root)

    def helper_postorder_traversal(self, root):
        if root is None:
            return

        self.helper_postorder_traversal(root.leftChild)
        self.helper_postorder_traversal(root.rightChild)
        print(root.value)

    def height(self):
        return self.height_helper(self.root)

    def height_helper(self, root):
        if root is None:
            return -1

        if root.leftChild is None and root.rightChild is None:
            return 0

        return 1 + max(self.height_helper(root.leftChild), self.height_helper(root.rightChild))

    def min(self):
        if self.root is None:
            return
        return self.min_helper(self.root)

    def min_helper(self, root):
        if root is None:
            return float('inf')

        left = self.min_helper(root.leftChild)
        right = self.min_helper(root.rightChild)

        return min(left, right, root.value)

    def equals(self, other):
        if other is None:
            return False
        return self.equals_helper(self.root, other.root)

    def equals_helper(self, first, second):
        if first is None and second is None:
            return True

        if first is not None and second is not None:
            return ((first.value == second.value)
                    and (self.equals_helper(first.leftChild, second.leftChild)
                         and self.equals_helper(first.rightChild, second.rightChild)))

        return False

    def validate_binary_tree(self):
        return self.validate_binary_tree_helper(self.root, float('-inf'), float('inf'))

    def validate_binary_tree_helper(self, root, min_range, max_range):
        if root is None:
            return True

        if root.value < min_range or root.value > max_range:
            return False

        return (self.validate_binary_tree_helper(root.leftChild, min_range, root.value - 1)
                and self.validate_binary_tree_helper(root.rightChild, root.value + 1, max_range))

    def print_nodes_at_distance(self, distance):
        self.print_nodes_at_distance_helper(self.root, distance)

    def print_nodes_at_distance_helper(self, root, distance):
        if root is None:
            return

        if distance == 0:
            print(root.value)
            return

        self.print_nodes_at_distance_helper(root.leftChild, distance - 1)
        self.print_nodes_at_distance_helper(root.rightChild, distance - 1)

    def traverse_level_order(self):
        for i in range(self.height() + 1):
            self.print_nodes_at_distance(i)


bst = BST()
bst.insert(7)
bst.insert(4)
bst.insert(9)
bst.insert(1)
bst.insert(6)
bst.insert(8)
bst.insert(10)

bst.traverse_level_order()
