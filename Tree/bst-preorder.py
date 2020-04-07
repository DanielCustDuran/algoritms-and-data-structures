class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        path = []
        self.preorder_print(self.root, path)
        
        return ('-'.join(map(str, path)))

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        path = []
        path = self.preorder_print(self.root, path)
        return find_val in path

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if not start:
            return
        traversal.append(start.value)
        self.preorder_print(start.left, traversal)
        self.preorder_print(start.right, traversal)

        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())