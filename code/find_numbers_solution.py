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
            
            
# method to compare the value with nodes
    def find_num(self, num):
        if num < self.data:
         if self.left is None:
            return str(num) + " Not Found"
         return self.left.find_num(num)
        elif num > self.data:
            if self.right is None:
               return str(num) + " Not Found"
            return self.right.find_num(num)
        else:
            print(str(self.data) + ' is Found')
            
            
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