# O(n) time | O(n) space 
# def invertBinaryTree(tree):
#     queue = [tree]
#     while len(queue):
#         current = queue.pop(0)
#         if not current:
#             continue
#         swapLeftRight(current)
#         queue.append(current.left)
#         queue.append(current.right)

def invertBinaryTree(tree):
    if tree is None:
        return 
    swapLeftRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swapLeftRight(Node):
    Node.left, Node.right = Node.right, Node.left 




# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
