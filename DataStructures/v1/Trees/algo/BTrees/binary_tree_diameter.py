def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo(tree).diameter



def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)
    
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = (leftTreeInfo.height + rightTreeInfo.height)
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    currHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(currDiameter, currHeight)


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height 


root = BinaryTree(1)
root.left = BinaryTree(3)
root.left.left = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.left.left.left = BinaryTree(9)
root.left.right = BinaryTree(4)
root.left.right.right = BinaryTree(5)
root.left.right.right.right = BinaryTree(6)
root.right = BinaryTree(2)
expected = 6
actual = binaryTreeDiameter(root)
simple_assert(expected, actual)