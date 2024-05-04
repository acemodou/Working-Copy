class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(n) space - where n is the number of nodes in the tree
# def findKthLargestValueInBst(tree, k):
#     # Write your code here.
#     kth_largest = inOrderTraverse(tree, [])
#     return kth_largest[-k]

# def inOrderTraverse(tree, sortedNodeValues):
#     if tree is not None:
#         inOrderTraverse(tree.left, sortedNodeValues)
#         sortedNodeValues.append(tree.value)
#         inOrderTraverse(tree.right, sortedNodeValues)
#     return sortedNodeValues

class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue) -> None:
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue

def reverseInOrderTraverse(node, k, treeInfo):
    if node is None or treeInfo.numberOfNodesVisited >= k:
        return
    
    reverseInOrderTraverse(node.right, k, treeInfo)
    if treeInfo.numberOfNodesVisited < k:
        treeInfo.numberOfNodesVisited += 1
        treeInfo.latestVisitedNodeValue = node.value
    reverseInOrderTraverse(node.left, k, treeInfo)
    
def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)
    return treeInfo.latestVisitedNodeValue
   
     


root = BST(15)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.left.right = BST(3)
root.left.right = BST(5)
root.right = BST(20)
root.right.left = BST(17)
root.right.right = BST(22)
print(findKthLargestValueInBst(root, 3))