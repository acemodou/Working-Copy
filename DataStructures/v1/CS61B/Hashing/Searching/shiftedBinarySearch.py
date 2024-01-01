from typing import List 
from binarySearch import simple_assert


# # O(log(n)) time | O(log(n)) space 
# def shiftedBinarySearch(array : List[int], target : int) -> int:
#     return binarySearch(array, target, 0, len(array)-1)


# def binarySearch(array : List[int], target : int, low, high) -> int:
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     lowNum = array[low]
#     highNum = array[high]
#     potentialMatch = array[mid]

#     if target == potentialMatch:
#         return mid 
#     if lowNum <= potentialMatch:
#         if target < potentialMatch and target >= lowNum:
#             return binarySearch(array, target, low, mid-1)
#         else:
#             return binarySearch(array, target, mid+1, high)

#     else:
#         if target > potentialMatch and target <= highNum:
#             return binarySearch(array, target, mid + 1, high)
#         else:
#             return binarySearch(array, target, low, mid -1)


def shiftedBinarySearch(array : List[int], target : int) -> int:
    return binarySearch(array, target, 0, len(array)-1)


def binarySearch(array : List[int], target : int, low, high) -> int:
    while low < high:
        mid = (low + high) // 2
        lowNum = array[low]
        highNum = array[high]
        potentialMatch = array[mid]

        if target == potentialMatch:
            return mid 
        if lowNum <= potentialMatch:
            if target < potentialMatch and target >= lowNum:
                high = mid -1 
            else:
                low = mid + 1 
        else:
            if target > potentialMatch and target <= highNum:
                low = mid + 1
            else:
                high = mid -1 
    return -1 




simple_assert(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33), 8)