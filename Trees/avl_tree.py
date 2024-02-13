class AVLTREE:
    def __init__(self):
        self.root = None

    class AVLNODE:
        def __init__(self, value):
            self.height = 0
            self.value = value
            self.leftChild = None
            self.rightChild = None

    def insert(self, value):
        self.root = self.insert_helper(self.root, value)

    def insert_helper(self, root, value):
        if root is None:
            return self.AVLNODE(value)

        if value < root.value:
            root.leftChild = self.insert_helper(root.leftChild, value)
        elif value > root.value:
            root.rightChild = self.insert_helper(root.rightChild, value)

        self.set_height(root)

        return self.balance(root)

    def balance(self, root):
        if self.is_left_heavy(root):
            if self.balance_factor(root.leftChild) < 0:
                root.leftChild = self.rotate_left(root.leftChild)
            return self.rotate_right(root.rightChild)
        elif self.is_right_heavy(root):
            if self.balance_factor(root.rightChild) > 0:
                root.rightChild = self.rotate_right(root.rightChild)
            return self.rotate_left(root)
        return root

    def rotate_left(self, node):
        new_root = node.rightChild

        node.rightChild = new_root.leftChild
        new_root.leftChild = node

        self.set_height(node)
        self.set_height(new_root)

        return new_root

    def rotate_right(self, node):
        new_root = node.leftChild

        node.leftChild = new_root.rightChild
        new_root.rightChild = node

        self.set_height(node)
        self.set_height(new_root)

        return new_root

    def set_height(self, node):
        node.height = max(self.height(node.leftChild), self.height(node.rightChild)) + 1
        return node

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.leftChild) - self.height(node.rightChild)

    def is_left_heavy(self, root):
        return self.balance_factor(root) > 1

    def is_right_heavy(self, root):
        return self.balance_factor(root) < -1

    def height(self, node):
        if node is None:
            return -1
        return node.height

    def pre_order_traversal(self):
        self.helper_pre_order_traversal(self.root)

    def helper_pre_order_traversal(self, root):
        if root is None:
            return

        print(root.value)
        self.helper_pre_order_traversal(root.leftChild)
        self.helper_pre_order_traversal(root.rightChild)


avl_tree = AVLTREE()
avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(30)
avl_tree.pre_order_traversal()
