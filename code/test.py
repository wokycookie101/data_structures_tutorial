class Node:

    def __init__(self, data):
        # These establish the left and right nodes within the tree. 
        self.left = None
        self.right = None
        # This is a current placeholder for data that we may need to run within our tree.
        self.data = data
    
    def insert(self, data):
        # To create a balanced search tree, we would need some comparison operators to put these numbers inside of the right nodes in the data.
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # This prints the tree we're establishing within our code. 
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

# Test Code
# Expected: 3, 6, 12, 14
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
