class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_helper(self.root, key)

    def _insert_helper(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self._insert_helper(root.left, key)
        else:
            root.right = self._insert_helper(root.right, key)
        return root

    def search(self, data):
        return self._search_helper(self.root, data)

    def _search_helper(self, root, data):
        if root is None:
            return root
        elif root.data == data:
            return root.data
        if data < root.data:
            return self._search_helper(root.left, data)
        return self._search_helper(root.right, data)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_helper(self.root, result)
        return result

    def _inorder_traversal_helper(self, root, result):
        if root:
            self._inorder_traversal_helper(root.left, result)
            result.append(root.data)
            self._inorder_traversal_helper(root.right, result)


bst = BST()
bst.insert(10)
bst.insert(20)
bst.insert(30)
bst.insert(40)
bst.insert(50)
print(bst.inorder_traversal())
print(bst.search(20))
