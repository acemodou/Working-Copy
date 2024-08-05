# This is an input class. Do not edit.
def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sumBsts(tree):
    # Write your code here.
    return getTreeInfo(tree).totalSumBstNodes 


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(
            True, 
            float("-inf"),
            float("inf"),
            0,
            0,
            0,
        )
    leftTreeInfo =  getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)
    
    satisfiesBstProp = tree.value > leftTreeInfo.maxValue and tree.value <= rightTreeInfo.minValue
    isBst = satisfiesBstProp and leftTreeInfo.isBst and rightTreeInfo.isBst

    maxValue = max(tree.value, max(leftTreeInfo.maxValue, rightTreeInfo.maxValue))
    minValue = min(tree.value, min(leftTreeInfo.minValue, rightTreeInfo.minValue))
    
    bstSum = 0
    bstSize = 0
    
    totalSumBstNodes = leftTreeInfo.totalSumBstNodes + rightTreeInfo.totalSumBstNodes
    
    if isBst:
        bstSum = tree.value + leftTreeInfo.bstSum + rightTreeInfo.bstSum
        bstSize =  1 + leftTreeInfo.bstSize + rightTreeInfo.bstSize
        
        if bstSize >=3:
            totalSumBstNodes = bstSum
    
    return TreeInfo(
        isBst, 
        maxValue,
        minValue,
        bstSum,
        bstSize,
        totalSumBstNodes,
        )
            

class TreeInfo:
    def __init__(self, isBst, maxValue, minValue, bstSum, bstSize, totalSumBstNodes) -> None:
        self.isBst = isBst
        self.maxValue = maxValue
        self.minValue = minValue
        self.bstSum = bstSum 
        self.bstSize = bstSize
        self.totalSumBstNodes = totalSumBstNodes
        



root = BinaryTree(8)
root.left = BinaryTree(2)
root.left.left = BinaryTree(1)
root.left.right = BinaryTree(10)
root.right = BinaryTree(9)
root.right.right = BinaryTree(5)
expected = 13
actual = sumBsts(root)
simple_assert(actual, expected)