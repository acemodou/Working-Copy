def simple_assert(a, b):
    assert a == b, f"{a}!{b}"


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n+m) time | O(n+m) space 
# def compareLeafTraversal(tree1, tree2):
#     # Write your code here.
#     tree1TraversalStack = [tree1]
#     tree2TraversalStack = [tree2]
    
#     while len(tree1TraversalStack) > 0 and len(tree2TraversalStack) > 0:
#         tree1Leaf = getNextLeafNode(tree1TraversalStack)
#         tree2Leaf = getNextLeafNode(tree2TraversalStack)
        
#         if tree1Leaf.value != tree2Leaf.value:
#             return False 
        
#     return len(tree1TraversalStack) == 0 and len(tree2TraversalStack) == 0

# def getNextLeafNode(traversalStack):
#     currentNode = traversalStack.pop()
    
#     while not isLeafNode(currentNode):
#         if currentNode.right is not None:
#             traversalStack.append(currentNode.right)
            
#         if currentNode.left is not None:
#             traversalStack.append(currentNode.left)
        
#         currentNode = traversalStack.pop()
#     return currentNode


def compareLeafTraversal(tree1, tree2):
    tree1LeafNodeLinkedList, _ = connectLeafNodes(tree1)
    tree2LeafNodeLinkedList, _ = connectLeafNodes(tree2)
    
    list1CurrentNode = tree1LeafNodeLinkedList
    list2CurrentNode = tree2LeafNodeLinkedList
    
    while list1CurrentNode is not None and list2CurrentNode is not None:
        if list1CurrentNode.value != list2CurrentNode.value:
            return False 
        list1CurrentNode = list1CurrentNode.right 
        list2CurrentNode = list2CurrentNode.right 
    
    return list1CurrentNode is None and list2CurrentNode is None 

def connectLeafNodes(currentNode, head=None, prevNode= None):
    if currentNode is None:
        return head, prevNode
    
    if isinstance(currentNode):
        if prevNode is None:
            head = currentNode
        else:
            prevNode.right = currentNode
        prevNode = currentNode
    
    leftHead, leftPrev = connectLeafNodes(currentNode.left, head, prevNode)
    return connectLeafNodes(currentNode.right, leftHead, leftPrev)
    


def isLeafNode(node):
    return node.left is None and node.right is None 
        
        

tree1 = BinaryTree(1)
tree1.left = BinaryTree(2)
tree1.right = BinaryTree(3)
tree1.left.left = BinaryTree(4)
tree1.left.right = BinaryTree(5)
tree1.right.right = BinaryTree(6)
tree1.left.right.left = BinaryTree(7)
tree1.left.right.right = BinaryTree(8)

tree2 = BinaryTree(1)
tree2.left = BinaryTree(2)
tree2.right = BinaryTree(3)
tree2.left.left = BinaryTree(4)
tree2.left.right = BinaryTree(7)
tree2.right.right = BinaryTree(5)
tree2.right.right.left = BinaryTree(8)
tree2.right.right.right = BinaryTree(6)

expected = True
actual = compareLeafTraversal(tree1, tree2)

simple_assert(actual, expected)

