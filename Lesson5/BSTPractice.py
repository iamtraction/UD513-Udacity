class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_node(self.root, Node(new_val))
    
    def insert_node(self, start, new_node):
        if new_node.value < start.value:
            if start.left:
                self.insert_node(start.left, new_node)
            else:
                start.left = new_node
        else:
            if start.right:
                self.insert_node(start.right, new_node)
            else:
                start.right = new_node

    def search(self, find_val):
        return self.search_recursive(self.root, find_val)

    def search_recursive(self, start, find_val):
        if start:
            if start.value > find_val:
                self.search_recursive(start.left, find_val)
            elif start.value < find_val:
                self.search_recursive(start.right, find_val)
            else:
                return True
        return False
    
    def display(self):
        return self.display_recursive(self.root)[:-1]
    
    def display_recursive(self, start, traversal=""):
        if start:
            traversal = str(start.value) + "-" \
                + self.display_recursive(start.left, traversal) \
                + self.display_recursive(start.right, traversal)
        return traversal
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
