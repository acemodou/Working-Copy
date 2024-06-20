def simple_assert(a, b):
    assert a == b, f'{a}!{b}'


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    # Write your code here.
    if tree.value >= 0:
        return tree.value 
    
    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return leftValue + rightValue
    if tree.value == -2:
        return leftValue - rightValue
    if tree.value == -3:
        return int(leftValue // rightValue)
    if tree.value == -4:
        return leftValue * rightValue 


tree = BinaryTree(-1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(-2)
tree.right.left = BinaryTree(5)
tree.right.right = BinaryTree(1)
expected = 6
actual = evaluateExpressionTree(tree)
simple_assert(actual, expected)