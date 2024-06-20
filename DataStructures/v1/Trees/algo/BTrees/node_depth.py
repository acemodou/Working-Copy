# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# def nodeDepths(root, depth= 0):
#     # Write your code here.
#     if root is None:
#         return 0
#     return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


def nodeDepths(root):
    stack = [{"node": root, "depth" : 0}]
    sumOfDepths = 0
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth" : depth + 1})
        stack.append({"node": node.right, "depth" : depth + 1})
    return sumOfDepths
        




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

nodeDepths(bst)