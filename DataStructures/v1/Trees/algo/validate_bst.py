# This is an input class. Do not edit.
def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, lower, upper):
    # Write your code here.
    if tree is None:
        return True 
    if tree.value < lower or tree.value > upper:
        return False
    
    return validateBst(tree.left, lower, tree.value) and \
           validateBst(tree.right, tree.value, upper)
    


bst = BST(2)
bst.left = BST(1)
bst.right = BST(3)
simple_assert(validateBst(bst, float("-inf"), float("inf")), True)