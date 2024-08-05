def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# def repairBst(tree):
#    nodeOne = nodeTwo = prevNode = None 
   
#    def inOrderTraversal(node):
#        nonlocal nodeOne, nodeTwo, prevNode
#        if node is None:
#            return 
#        inOrderTraversal(node.left)
#        if prevNode is not None and prevNode.value > node.value:
#            if nodeOne is None:
#                nodeOne = prevNode
#            nodeTwo = node
#        prevNode = node 
#        inOrderTraversal(node.right)
#    inOrderTraversal(tree)
#    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value 
#    return tree 

def repairBst(tree):
    nodeOne = nodeTwo = prevNode = None
    
    stack = []
    currNode = tree 
    while currNode is not None or len(stack) > 0:
        while currNode is not None:
            stack.append(currNode)
            currNode = currNode.left 
        currNode = stack.pop()

        if prevNode is not None and prevNode.value > currNode.value:
            if nodeOne is None:
                nodeOne = prevNode
            nodeTwo = currNode
        prevNode = currNode
        currNode = currNode.right
    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value 
    return tree 

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


tree = BST(2)
tree.left = BST(1)
tree.right = BST(3)
tree.left.left = BST(4)
tree.right.right = BST(0)
expected = [0, 1, 2, 3, 4]
actual = inOrderTraverse(repairBst(tree), [])
simple_assert(actual, expected)