# This is an input class. Do not edit.
def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(h) space 
# def symmetricalTree(tree):
#     # Write your code here.
#     leftStack = [tree.left]
#     rightStack =[tree.right]
    
#     while len(leftStack) > 0:
#         leftNode = leftStack.pop()
#         rightNode = rightStack.pop()

#         if leftNode is None and rightNode is None:
#             continue 

#         if leftNode is None or rightNode is None or leftNode.value != rightNode.value:
#             return False 
#         leftStack.append(leftNode.left)
#         leftStack.append(leftNode.right)

#         rightStack.append(rightNode.right)
#         rightStack.append(rightNode.left)
    
#     return True 

def symmetricalTree(tree):
    return treesAreMirrored(tree.left, tree.right)

def treesAreMirrored(left, right):
    if left is not None and right is not None and left.value == right.value:
        return treesAreMirrored(left.left, right.right) and treesAreMirrored(left.right, right.left)
    return left == right 


tree = BinaryTree(10)
tree.left = BinaryTree(5)
tree.right = BinaryTree(5)
tree.left.left = BinaryTree(7)
tree.left.right = BinaryTree(9)
tree.right.left = BinaryTree(9)
tree.right.right = BinaryTree(7)
expected = True
actual = symmetricalTree(tree)
simple_assert(actual, expected)
