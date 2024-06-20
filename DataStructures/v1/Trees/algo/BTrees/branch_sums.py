# This is the class of the input root. Do not edit it.
def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums 

def calculateBranchSums(node, newSum, sums):
    if node is None:
        return 
    
    runningSum = newSum + node.value
    if node.left is None and node.right is None:
        sums.append(runningSum)
    calculateBranchSums(node.left, runningSum, sums)
    calculateBranchSums(node.right, runningSum, sums)

bst = BinaryTree(1)
bst.left = BinaryTree(2)
bst.left.left = BinaryTree(4)
bst.left.left.left = BinaryTree(8)
bst.left.left.right = BinaryTree(9)
bst.left.right = BinaryTree(5)
bst.left.right.left = BinaryTree(10)
bst.right = BinaryTree(3)
bst.right.left = BinaryTree(6)
bst.right.right = BinaryTree(7)

expected = [15, 16, 18, 10, 11]
simple_assert(branchSums(bst), expected)