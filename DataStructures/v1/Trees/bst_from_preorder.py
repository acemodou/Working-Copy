# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n^2) time & O(h) space
# def reconstructBst(preOrderTraversalValues):
#     # Write your code here.
#     if len(preOrderTraversalValues) == 0:
#         return None 
#     currentValue = preOrderTraversalValues[0]
#     rightSubttreeIdx  = len(preOrderTraversalValues)

#     for idx in range(1, len(preOrderTraversalValues)):
#         value = preOrderTraversalValues[idx]

#         if value >= currentValue:
#             rightSubttreeIdx = idx 
#             break
#     leftSubtree = reconstructBst(preOrderTraversalValues[1: rightSubttreeIdx])
#     rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtree:])
#     return BST(currentValue, leftSubtree, rightSubtree)

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx

def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float("-inf"), float("inf"),preOrderTraversalValues,treeInfo)
    
def reconstructBstFromRange(lower, upper,preOrderTraversalValues,currentSubTreeInfo):
    if currentSubTreeInfo.rootIdx == len(preOrderTraversalValues):
        return None 
    rootValue = preOrderTraversalValues[currentSubTreeInfo.rootIdx]
    if rootValue < lower or rootValue > upper:
        return None 
    
    currentSubTreeInfo.rootIdx += 1
    leftSubtree = reconstructBstFromRange(lower, rootValue, preOrderTraversalValues, currentSubTreeInfo)
    rightSubtree = reconstructBstFromRange(rootValue, upper, preOrderTraversalValues, currentSubTreeInfo)
    return BST(rootValue, leftSubtree, rightSubtree)
    