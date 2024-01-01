from typing import List
from typing import Any 


def simple_assert(a : Any, b: Any) -> None:
    assert a == b, f'{a != b}'




def binarySearch(array : List[int], target : int) -> int:
    low, high = 0,  len(array) -1
 
    while low <= high:
        mid = (high - low) // 2 + low 
        if array[mid] == target:
            return mid 
        elif target < array[mid]:
            high = mid -1 
        else:
            low = mid + 1
    return -1 

# def binarySearch(array : List[int], target : int) -> int:
#     return binarySearchHelper(array, target, 0, len(array)-1)

# def binarySearchHelper(array : List[int], target : int, low : int, high : int) -> int:
#     if low > high:
#         return -1
    
#     mid = (high - low) // 2 + low 
#     if array[mid] == target:
#         return mid 
#     elif target < array[mid]:
#         return binarySearchHelper(array, target, low, mid -1)
#     else:
#         return binarySearchHelper(array, target, mid + 1, high)
    






simple_assert(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)