def simple_assert(a, b):
    assert a == b, f"{a}!{b}"


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(n) space 
# def flattenBinaryTree(root):
#     # Write your code here.
#     inOrderNodes = getInOrderNodes(root, [])
#     for nodeIdx in range(0, len(inOrderNodes) -1):
#         leftNode = inOrderNodes[nodeIdx]
#         rightNode = inOrderNodes[nodeIdx + 1]
#         leftNode.right = rightNode
#         rightNode.left = leftNode
#     return inOrderNodes[0]

# def getInOrderNodes(tree, array):
#     if tree is not None:
#         getInOrderNodes(tree.left, array)
#         array.append(tree)
#         getInOrderNodes(tree.right, array)
#     return array 

def flattenBinaryTree(root):
    leftMost, _ = flattenTree(root)
    return leftMost 
    
def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubTreeLeftMost, leftSubTreeRightMost = flattenTree(node.left)
        connectNodes(leftSubTreeRightMost, node)
        leftMost = leftSubTreeLeftMost

    if node.right is None:
        rightMost = node 
    else:
        rightSubTreeLeftMost, rightSubTreeRightMost = flattenTree(node.right)
        connectNodes(node, rightSubTreeLeftMost)
        rightMost = rightSubTreeRightMost
    
    return [leftMost, rightMost]

def connectNodes(left, right):
    left.right = right 
    right.left = left 


class BinaryTree(BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

    def leftToRightToLeft(self):
        nodes = []
        current = self
        while current.right is not None:
            nodes.append(current.value)
            current = current.right
        nodes.append(current.value)
        while current is not None:
            nodes.append(current.value)
            current = current.left
        return nodes

root = BinaryTree(1).insert([2, 3, 4, 5, 6])
root.left.right.left = BinaryTree(7)
root.left.right.right = BinaryTree(8)
leftMostNode = flattenBinaryTree(root)
leftToRightToLeft = leftMostNode.leftToRightToLeft()
expected = [4, 2, 7, 5, 8, 1, 6, 3, 3, 6, 1, 8, 5, 7, 2, 4]
simple_assert(leftToRightToLeft, expected)
