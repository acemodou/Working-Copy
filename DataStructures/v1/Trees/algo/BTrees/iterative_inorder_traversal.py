def simple_assert(a, b):
    assert a == b, f"{a}!{b}"

class BinaryTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


def testCallback(testArray, tree):
    if tree is None:
        return
    testArray.append(tree.value)

def iterativeInOrderTraversal(tree, callback):
    prevNode = None 
    currNode = tree 
    while currNode is not None:
        if prevNode is None or prevNode == currNode.parent:
            if currNode.left is not None:
                newNode = currNode.left
            else:
                callback(currNode)
                newNode = currNode.right if currNode.right else currNode.parent
        elif prevNode == currNode.left:
            callback(currNode)
            newNode = currNode.right if currNode.right else currNode.parent
        else:
            newNode = currNode.parent
        
        prevNode = currNode
        currNode = newNode

    
root = BinaryTree(1)
root.left = BinaryTree(2, parent=root)
root.left.left = BinaryTree(4, parent=root.left)
root.left.left.right = BinaryTree(9, parent=root.left.left)
root.right = BinaryTree(3, parent=root)
root.right.left = BinaryTree(6, parent=root.right)
root.right.right = BinaryTree(7, parent=root.right)

testArray = []
actualTestCallback = lambda x: testCallback(testArray, x)
iterativeInOrderTraversal(root, actualTestCallback)
simple_assert(testArray, [4, 9, 2, 1, 6, 3, 7])