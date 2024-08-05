def simple_assert(a, b):
    assert a == b, f"{a}!{b}"


# O(nlog(n)) time | O(h) space 
# def allKindsOfNodeDepths(root):
#     sumOfAllDepths = 0
#     stack = [root]
#     while len(stack) > 0:
#         node = stack.pop()
#         if node is None:
#             continue
#         sumOfAllDepths += nodeDepths(node)
#         stack.append(node.left)
#         stack.append(node.right)
#     return sumOfAllDepths

# O(nlog(n)) time | O(h) space 
# def allKindsOfNodeDepths(root):
    # if root is None:
    #     return 0 
    # return allKindsOfNodeDepths(root.left) + allKindsOfNodeDepths(root.right) + nodeDepths(root)


def allKindsOfNodeDepths(root):
    return getTreeInfo(root).sumOfAllDepths 


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0, 0)
    
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)
    
    sumOfLeftDepths = leftTreeInfo.sumOfDepth + leftTreeInfo.numNodesInTree
    sumOfRightDepths = rightTreeInfo.sumOfDepth + rightTreeInfo.numNodesInTree
    
    numNodesInTree = 1 + leftTreeInfo.numNodesInTree + rightTreeInfo.numNodesInTree
    sumOfDepths = sumOfLeftDepths + sumOfRightDepths
    sumOfAllDepths = sumOfDepths + leftTreeInfo.sumOfAllDepths + rightTreeInfo.sumOfAllDepths
    
    return TreeInfo(numNodesInTree, sumOfDepths, sumOfAllDepths) 
    
    
     

class TreeInfo:
    def __init__(self, numNodesInTree, sumOfDepth, sumOfAllDepths) -> None:
        self.numNodesInTree = numNodesInTree
        self.sumOfDepth = sumOfDepth
        self.sumOfAllDepths = sumOfAllDepths
        



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right = BinaryTree(5)
root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
actual = allKindsOfNodeDepths(root)
simple_assert(actual, 26)
