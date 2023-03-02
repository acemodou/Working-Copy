from typing import List
import math 
def simple_assert(a:int, b:int):
    assert a == b, f'{a}!{b}'

#  nlog(n) and O(1) space 
# def sortedSquaredArray(array: List[int]):
#     for i in range(len(array)):
#         array[i] = array[i] * array[i]
#     array.sort()
#     return array 

# 0(n) time and 0(n) space 
def sortedSquaredArray(array: List[int]):
    start_idx, end_idx = 0, len(array)-1 
    output = [0] * len(array)

    for pos in reversed(range(len(array))):
        if abs(array[start_idx]) > abs(array[end_idx]):
            output[pos] = math.pow(array[start_idx], 2)
            start_idx += 1
        else:
            output[pos] = math.pow(array[end_idx], 2)
            end_idx -= 1 
    return output


simple_assert(sortedSquaredArray([-2, -1]), [1, 4])
simple_assert(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]), [1, 4, 9, 25, 36, 64, 81])
simple_assert(sortedSquaredArray([-7,-5, -4, 3, 6, 8, 9]), [9, 16, 25, 36, 49, 64, 81])
