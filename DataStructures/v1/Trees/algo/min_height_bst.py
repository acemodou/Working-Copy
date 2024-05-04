def minHeightBst(array):
    return constructMinHeightBst(array, None, 0, len(array)-1)


# def constructMinHeightBst(array, bst, startIdx, endIdx):
#     if endIdx < startIdx:
#         return 
#     midIdx = (startIdx + endIdx) // 2
#     value = array[midIdx]
#     if bst is None:
#         bst = BST(value)
#     else:
#         bst.insert(value)
#     constructMinHeightBst(array, bst, startIdx, midIdx - 1)
#     constructMinHeightBst(array, bst, midIdx + 1, endIdx)
#     return bst 

# def constructMinHeightBst(array, bst, startIdx, endIdx):
#     if endIdx < startIdx:
#         return 
#     midIdx = (startIdx + endIdx) // 2
#     value = array[midIdx]
#     newBstNode = BST(value)
#     if bst is None:
#         bst = BST(value)
#     else:
#         if value < bst.value:
#             bst.left = newBstNode
#             bst = bst.left 
#         else:
#             bst.right = newBstNode
#             bst = bst.right
#     constructMinHeightBst(array, bst, startIdx, midIdx - 1)
#     constructMinHeightBst(array, bst, midIdx + 1, endIdx)
#     return bst 

def constructMinHeightBst(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return 
    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
    bst.left = constructMinHeightBst(array, bst, startIdx, midIdx - 1)
    bst.right = constructMinHeightBst(array, bst, midIdx+1, endIdx)
    return bst 
         

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)



array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
minHeightBst(array)