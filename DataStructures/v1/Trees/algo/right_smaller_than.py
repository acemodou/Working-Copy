def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

# ON^2 time | O(N) space 
# def rightSmallerThan(array):
#     # Write your code here.
#     rightSmallerCounts = []
#     for i in range(len(array)):
#         SmallerCounts = 0
#         for j in range(i+1, len(array)):
#             if array[i] > array[j]:
#                 SmallerCounts += 1
#         rightSmallerCounts.append(SmallerCounts)
#     return rightSmallerCounts


def rightSmallerThan(array):
    if len(array) == 0:
        return []
        
    lastIdx = len(array)-1
    bst = SpecialBST(array[lastIdx], lastIdx, 0)
    for idx in reversed(range(len(array)-1)):
        bst.insert(array[idx], idx)
    
    rightSmallerCounts = array[:]
    getRightSmallerCounts(bst, rightSmallerCounts)
    return rightSmallerCounts

def getRightSmallerCounts(bst, rightSmallerCounts):
    if bst is None:
        return 
    rightSmallerCounts[bst.idx] = bst.numSmallerAtInsertTime
    getRightSmallerCounts(bst.left, rightSmallerCounts)
    getRightSmallerCounts(bst.right, rightSmallerCounts)
  


class SpecialBST:
    def __init__(self, value, idx, numSmallerAtInsertTime):
        self.value = value 
        self.idx = idx
        self.numSmallerAtInsertTime = numSmallerAtInsertTime
        self.leftSubtreeSize = 0
        self.left = None 
        self.right = None 
        
    def insert(self, value, idx, numSmallerAtInsertTime=0):
        if value < self.value:
            self.leftSubtreeSize += 1
            if self.left is None:
                self.left = SpecialBST(value, idx, numSmallerAtInsertTime)
            else:
                self.left.insert(value, idx, numSmallerAtInsertTime)
        else:
            numSmallerAtInsertTime += self.leftSubtreeSize
            if value > self.value:
                numSmallerAtInsertTime += 1
            if self.right is None:
                self.right = SpecialBST(value, idx, numSmallerAtInsertTime)
            else:
                self.right.insert(value, idx, numSmallerAtInsertTime)


array = [8, 5, 11, -1, 3, 4, 2]
expected = [5, 4, 4, 0, 1, 1, 0]
actual = rightSmallerThan(array)
simple_assert(actual, expected)