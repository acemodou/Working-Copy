def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    if isDescendant(nodeTwo, nodeOne):
        return isDescendant(nodeThree, nodeTwo)
    
    if isDescendant(nodeTwo, nodeThree):
        return isDescendant(nodeOne, nodeTwo)
    
    return False 

def isDescendant(node, target):
    if node is None:
        return False 
    
    if node is target:
        return True 
    return(
        isDescendant(node.left, target) if target.value < node.value else 
        isDescendant(node.right, target)
    )

root = BST(5)
root.left = BST(2)
root.right = BST(7)
root.left.left = BST(1)
root.left.right = BST(4)
root.right.left = BST(6)
root.right.right = BST(8)
root.left.left.left = BST(0)
root.left.right.left = BST(3)

nodeOne = root
nodeTwo = root.left
nodeThree = root.left.right.left
expected = True
actual = validateThreeNodes(nodeOne, nodeTwo, nodeThree)
simple_assert(actual, expected)