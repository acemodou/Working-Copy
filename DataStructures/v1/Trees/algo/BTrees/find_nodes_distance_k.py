def simple_assert(a, b):
    assert a == b, f"{a}!{b}"


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findNodesDistanceK(tree, target, k):
    nodesToParents = {}
    populateNodesToParents(tree, nodesToParents)
    targetNode = getTargetFromValue(tree, target, nodesToParents)

    return breadFirstSearchForNodesDistanceK(targetNode, nodesToParents, k)

def breadFirstSearchForNodesDistanceK(targetNode, nodesToParents, k):
     queue = [(targetNode, 0)]
     seen = {targetNode.value}

     while len(queue) > 0:
         currentNode, distanceFromK = queue.pop(0)

         if distanceFromK == k:
             nodesDistanceK = [node.value for node, _ in queue]
             nodesDistanceK.append(currentNode.value)
             return nodesDistanceK
             
         connectedNodes = [currentNode.left, currentNode.right, nodesToParents[currentNode.value]]
         for node in connectedNodes:
             if node is None:
                 continue
             if node.value in seen:
                 continue 
             seen.add(node.value)
             queue.append((node, distanceFromK+1))

     return []
             
def getTargetFromValue(tree, value, nodesToParents):
    if tree.value == value:
        return tree 
    
    nodeToParent = nodesToParents[value]
    if nodeToParent.left is not None and nodeToParent.left.value == value:
        return nodeToParent.left 
    
    return nodeToParent.right 

def populateNodesToParents(node, nodesToParents, parents=None):
    if node is not None:
        nodesToParents[node.value] = parents
        populateNodesToParents(node.left, nodesToParents, node)
        populateNodesToParents(node.right, nodesToParents, node)


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.right = BinaryTree(6)
root.right.right.left = BinaryTree(7)
root.right.right.right = BinaryTree(8)
target = 3
k = 2
expected = [2, 7, 8]
actual = findNodesDistanceK(root, target, k)
actual.sort()
simple_assert(actual, expected)
