class BST:
    def __init__(self, value : int) -> None:
        self.value = value 
        self.left = None 
        self.right = None 


def inOrderTraverse(tree, array):
    # Write your code here.
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array 


def preOrderTraverse(tree, array):
    # Write your code here.
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array 


def postOrderTraverse(tree, array):
    # Write your code here.
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array 



bst = BST(10)
bst.left = BST(5)
bst.right = BST(15)
bst.left.left = BST(2)
bst.left.right = BST(5)
bst.right.right = BST(22)
bst.left.left.left = BST(1)

print(inOrderTraverse(bst, []))
print(preOrderTraverse(bst, []))
print(postOrderTraverse(bst, []))
