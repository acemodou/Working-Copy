# This is an input class. Do not edit.
def simple_assert(a, b):
    assert a == b, f"{a}!{b}"

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, currSum, canBeSplit) -> None:
        self.currSum = currSum
        self.canBeSplit = canBeSplit

def splitBinaryTree(tree):
    # Write your code here.
    desiredSum = getTreeSum(tree) / 2
    canBeSplit = trySubTrees(tree, desiredSum).canBeSplit
    return desiredSum if canBeSplit else 0

def getTreeSum(tree):
    if tree is None:
        return 0 
    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)

def trySubTrees(tree, desiredSum):
    if tree is None:
        return TreeInfo(0, False)
    
    leftInfo = trySubTrees(tree.left, desiredSum)
    rightInfo= trySubTrees(tree.right, desiredSum)

    currentSum = tree.value + leftInfo.currSum + rightInfo.currSum
    canBeSplit = leftInfo.canBeSplit or rightInfo.canBeSplit or currentSum == desiredSum
    return TreeInfo(currentSum, canBeSplit)


tree = BinaryTree(2)
tree.left = BinaryTree(4)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(6)
tree.right = BinaryTree(10)
tree.right.left = BinaryTree(3)
tree.right.right = BinaryTree(3)
expected = 16
actual = splitBinaryTree(tree)
simple_assert(actual, expected)
