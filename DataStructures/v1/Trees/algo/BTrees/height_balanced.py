def simple_assert(a, b):
    assert a == b, f"{a}!{b}"

# This is an input class. Do not edit.
class TreeInfo:
    def __init__(self, isBalanced, height) -> None:
        self.isBalanced = isBalanced
        self.height = height


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(h) space 
def heightBalancedBinaryTree(tree):
    # Write your code here.
    treeInfo = getTreeinfo(tree)
    return treeInfo.isBalanced

def getTreeinfo(node):
    if node is None:
        return TreeInfo(True, -1)
    leftSubTreeInfo = getTreeinfo(node.left)
    rightSubTreeInfo = getTreeinfo(node.right)

    isBalanced = leftSubTreeInfo.isBalanced and rightSubTreeInfo.isBalanced and \
                abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <=1 
    height = max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1

    return TreeInfo(isBalanced, height)
    




root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.right = BinaryTree(6)
root.left.right.left = BinaryTree(7)
root.left.right.right = BinaryTree(8)
expected = True
actual = heightBalancedBinaryTree(root)
simple_assert(actual, expected)

