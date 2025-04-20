class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_recursive(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_recursive(root.right, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.value, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.value, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.value, end=" ")


# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    keys = [10, 20, 5, 6, 15, 30]

    for key in keys:
        tree.insert(key)

    print("Inorder Traversal:")
    tree.inorder_traversal(tree.root)  # Output: 5 6 10 15 20 30
    print("\nPreorder Traversal:")
    tree.preorder_traversal(tree.root)  # Output: 10 5 6 20 15 30
    print("\nPostorder Traversal:")
    tree.postorder_traversal(tree.root)  # Output: 6 5 15 30 20 10
