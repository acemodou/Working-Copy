def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

def findClosestValueInBst(tree, target):
    # Write your code here.
    closest_distance = float("inf")
    currNode = tree 
    while currNode is not None:
        if abs(target - closest_distance) > abs(target - currNode.value):
            closest_distance = currNode.value 
        if target < currNode.value:
            currNode = currNode.left
        elif target > currNode.value:
            currNode = currNode.right 
        else:
            break 
    return closest_distance 


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = BST(10)
root.left = BST(5)
root.right = BST(15)
root.left.left = BST(2)
root.left.right = BST(5)
root.left.left.left = BST(1)
root.right.left = BST(13)
root.right.right = BST(22)
root.right.left.right = BST(14)
simple_assert(findClosestValueInBst(root, 12), 13)
