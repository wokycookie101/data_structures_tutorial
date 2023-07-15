class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
      
# Insert method to create nodes
    def insert(self, data):
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
            
            
# TO DO: Create the find_num method.
    def find_num(self, num):
        pass
            
            
# Print the tree
    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
         
# Test Values
# Expected: 16 is Found, 1 not Found, 20 not Found
root = Node(5)
root.insert(19)
root.insert(27)
root.insert(16)
print(root.find_num(16))
print(root.find_num(1))
print(root.find_num(20))