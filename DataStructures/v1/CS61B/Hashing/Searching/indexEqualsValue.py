from typing import List 
from binarySearch import simple_assert


# O(n) time | O(1) space 
# def indexEqualsValue(array : List[int]) -> int:
    # for index in range(len(array)):
    #     value = array[index]
    #     if value == index:
    #         return index 
    # return -1 


# O(log(n)) time | O(log(n)) space 
# def indexEqualsValue(array : List[int]) -> int:
#     return indexEqualsValueHelper(array, 0, len(array)-1)

# def indexEqualsValueHelper(array : List[int], left : int, right : int) -> int:
#     if left > right:
#         return -1 
#     middleIdx = (left + right) // 2
#     middleValue = array[middleIdx]

#     if middleValue < middleIdx:
#         return indexEqualsValueHelper(array, middleIdx + 1, right)
#     elif middleIdx == 0 and middleIdx == middleValue:
#         return middleIdx
#     elif array[middleIdx] == middleValue and array[middleIdx -1] < middleIdx -1:
#         return middleIdx
#     else:
#         return indexEqualsValueHelper(array, left, middleIdx -1)
    
def indexEqualsValue(array : List[int]) -> int:
    return indexEqualsValueHelper(array, 0, len(array)-1)

def indexEqualsValueHelper(array : List[int], left : int, right : int) -> int:
    while left <= right:
        
        middleIdx = (left + right) // 2
        middleValue = array[middleIdx]

        if middleValue < middleIdx:
            left = middleIdx + 1
        elif middleIdx == 0 and middleIdx == middleValue:
            return middleIdx
        elif middleIdx == middleValue and array[middleIdx -1] < middleIdx -1:
            return middleIdx
        else:
            right = middleIdx -1
    return -1

simple_assert(indexEqualsValue([-5, -3, 0, 3, 4, 5, 9]), 3)
simple_assert(indexEqualsValue([-12, 1, 2, 3, 12]), 1)


