def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# O(n) time | O(n) space 
# def findSuccessor(tree, node):
#     # Write your code here.
#     inorderTraversalOrder = getInOrderTraversalOrder(tree)

#     for idx, currentNode in enumerate(inorderTraversalOrder):
#         if currentNode != node:
#             continue

#         if idx + 1 == len(inorderTraversalOrder) - 1:
#             return None
        
#         return inorderTraversalOrder[idx + 1]

# def getInOrderTraversalOrder(node, order=[]):
#     if node is None:
#         return order 
#     getInOrderTraversalOrder(node.left, order)
#     order.append(node)
#     getInOrderTraversalOrder(node.right, order)
#     return order 

def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftMostChild(node.right)
    
    return getRightMostParent(node)

def getLeftMostChild(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left

    return currentNode

def getRightMostParent(node):
    currentNode = node 
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
        
    return currentNode.parent 


root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.parent = root
root.right = BinaryTree(3)
root.right.parent = root
root.left.left = BinaryTree(4)
root.left.left.parent = root.left
root.left.right = BinaryTree(5)
root.left.right.parent = root.left
root.left.left.left = BinaryTree(6)
root.left.left.left.parent = root.left.left
node = root.left.right
expected = root
actual = findSuccessor(root, node)
simple_assert(actual, expected)