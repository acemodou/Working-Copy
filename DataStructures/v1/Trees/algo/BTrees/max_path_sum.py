
# This is an input class. Do not edit.
def simple_assert(a, b):
    assert a == b, f"{a}!{b}"

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

def maxPathSum(tree):
    return findMaxSum(tree).rps  

def findMaxSum(tree):
    if tree is None:
        return TreeInfo(0, float("-inf"))
    
    leftTreeInfo = findMaxSum(tree.left)
    rightTreeInfo = findMaxSum(tree.right)
    maxChildSum = max(leftTreeInfo.msb, rightTreeInfo.msb)

    value = tree.value 
    maxSumAsBranch = max(maxChildSum + value, value)
    maxSumAsRootNode = max(maxSumAsBranch, leftTreeInfo.msb + rightTreeInfo.msb + value)
    maxPathSum = max(leftTreeInfo.rps, rightTreeInfo.rps, maxSumAsRootNode)

    return TreeInfo(maxSumAsBranch, maxPathSum)

   

class TreeInfo:
    def __init__(self, maxSumBranch, runningPathSum):
        self.msb = maxSumBranch
        self.rps = runningPathSum
  



class TreeInfo:
    def __init__(self, maxSumBranch, runningPathSum):
        self.msb = maxSumBranch
        self.rps = runningPathSum




test = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
simple_assert(maxPathSum(test), 18)