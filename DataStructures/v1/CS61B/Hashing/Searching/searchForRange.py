from typing import List
from binarySearch import binarySearch,simple_assert

# TARGETNOTFOUND = -1 

# # (ONlog(n)) time | O(1) space
# def searchForRange(array : List[int], target : int) -> List[int]:
#     # Write your code here.
#     # Use binary search to find the target, once we find a target we expand left and right 
#     # return a list [left + 1, right + 1 ]
#     targetIndex = binarySearch(array, target)
#     if targetIndex == TARGETNOTFOUND:
#         return [-1, -1]
#     result = expandLeftRight(array, target, targetIndex)
#     return result 



# def expandLeftRight(array : List[int], target : int, targetIndex : int) -> int:
#     left = targetIndex - 1 
#     while left >= 0 and array[left] == target:
#         left -= 1
    
#     right = targetIndex + 1
#     while right < len(array) and array[right] == target:
#         right += 1
    
#     return [left +1, right -1]


#Olog(n) time | Olog(n) space 
# def searchForRange(array : List[int], target : int) -> List[int]:
#     finalRange = [-1, -1]
#     alteredBinarySearch(array, target, 0, len(array)-1, finalRange, True)
#     alteredBinarySearch(array, target, 0, len(array)-1, finalRange, False)
#     return finalRange

# def alteredBinarySearch(array : List[int], target : int, left : int, right : int, finalRange : List[int], goLeft : bool) -> List[int]:
#     if left > right:
#         return finalRange
#     mid = (left + right) // 2

#     if array[mid] < target:
#         return alteredBinarySearch(array, target, mid + 1 , right, finalRange, goLeft) 
#     elif array[mid] > target:
#         return alteredBinarySearch(array, target, left , mid - 1, finalRange, goLeft) 
        
#     else:
#        if goLeft:
#            if mid == 0 or array[mid - 1] != target:
#                finalRange[0] = mid 
#            else:
#                return alteredBinarySearch(array, target, left , mid -1, finalRange, goLeft)
#        else:
#            if mid == len(array)-1 or array[mid + 1] != target:
#                finalRange[1] = mid
#            else:
#             return alteredBinarySearch(array, target, mid + 1 , right, finalRange, goLeft)

# O(log(n)) time | O(1) space     
def searchForRange(array : List[int], target : int) -> List[int]:
    finalRange = [-1, -1]
    alteredBinarySearch(array, target, 0, len(array)-1, finalRange, True)
    alteredBinarySearch(array, target, 0, len(array)-1, finalRange, False)
    return finalRange

def alteredBinarySearch(array : List[int], target : int, left : int, right : int, finalRange : List[int], goLeft : bool) -> List[int]:
    while left <= right:
        mid = (left + right) // 2

        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid -1 
        else:
            if goLeft:
                if mid == 0 or array[mid - 1] != target:
                    finalRange[0] = mid
                    return 
                else:
                    right = mid -1 
            else:
                if mid == len(array)-1 or array[mid + 1] != target:
                    finalRange[1] = mid
                    return 
                else:
                    left = mid + 1

simple_assert(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45), [4, 9])
