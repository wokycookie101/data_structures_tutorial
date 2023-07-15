# Building Trees

![Tree](images/tree.webp)

When we think of trees, we think of this biological structure with branches jutting out of the main root. There's sort of a heirarchy when we think of tree branches. There's the trunk, which is the root that connections to the ground, then there are the branches that jut out of the trunk, and then those branches may either produce leaves, or create more branches, which those branches will have the same possibility. 

Trees are easy to understand, mostly because they're right there in front of us, and we're able to see it. However, trees as a data structure, are a bit trickier to grasp, possibly due to the abstractness of it all. 

Trees in the data structure world have *nodes,* where the data is stored. These nodes are connected by *pointers.* These nodes can connect to other nodes inside the tree, hence the name of this data structure.

![Tree_Data_Structure](images/tree_data_structure.jpg)

A *parent node* is a node that's connected to a *child node*, and is higher up on the heirarchy of the tree, while a child node is lower on the heirarchy. 

The *root* is the first parent inside of the tree, or rather, the starting node. A *leaf* is a node that doesn't have any children. 

Finally, if we want to define a *subtree,* we would find all of the child nodes associated with one parent node. 

## The Different Types of Trees

There are three types of trees in the data structure world:

* Binary Tree - These trees only have two children per node

* Binary Search Tree - These trees organize values depending on if they're less or more than the root. If the value is more than the root, it's sorted to the right. If it's less, it's sorted to the left

* Balanced Search Tree (BST)- This is like the Binary Search Tree, but it instead aims to be balanced on both sides, rather than having one side weigh more than the other. These are usually ideal. 

As you may guess, there's also a bit of a heirarchy here as well. balanced search trees ARE binary search trees, and binary search trees are binary trees. 

Balanced Search Trees are the ideal trees to work with, since they make finding values inside of a tree very fast and convenient. 

## Accessing Binary Search Trees

We would access the binary tree in three ways:

* In-order: This means starting on the left node, then the root, then the right node. This is usually ideal for binary search trees. 

* Pre-order: This means starting at the root, then going left, then going right

* Post-order: This means starting at the left node, then the right node, then visiting the root last. 

To establish a tree within your code, you would first create a Node class.

```python 

class Node {

    def __init__(self, data):
        # These establish the left and right nodes within the tree. 
        self.left = None
        self.right = None
        # This is a current placeholder for data that we may need to run within our tree.
        self.data = data
    
    # This prints the tree we're establishing within our code. 
    def PrintTree(self):
        print(self.data)

}

```

Next, if we wanted to insert data within the tree we've created, we would create an `Insert()` method

```python
class Node {

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

```

## Traversing a Tree

First, if we wanted to program a pre-order traversal (Root -> Left -> Right), we would simply code the following. 

```python

def in_order_traversal(self, root):
    res = []
    if root:
        res.append(root.data)
        res = self.in_order_traversal(root.left)
        res = res + self.in_order_traversal(root.right)
    return res

```

If we wanted to program an in-order traversal (Left -> Root -> Right), we would write a method like this:

```python

def in_order_traversal(self, root):
    res = []
    if root:
        res = self.in_order_traversal(root.left)
        res.append(root.data)
        res = res + self.in_order_traversal(root.right)
    return res

```

Finally, if we wanted to program a post-order traversal (Left -> Right -> Root), we would write the following method:

```python

def in_order_traversal(self, root):
    res = []
    if root:
        res = self.in_order_traversal(root.left)
        res = res + self.in_order_traversal(root.right)
        res.append(root.data)
    return res

```

Do you notice a pattern here? We're basically just rearanging the order that we search these nodes in. 

# Problem

In [this code](find_numbers.py), write a method that'll be able to find the numbers 16, 1, and 20 located in this tree. 

If you get stuck, here's the [solution](find_numbers_solution.py)

[Welcome!](welcome.md)