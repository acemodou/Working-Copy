from minmaxstack import simpleAssert
from typing import List 


# time is O(n^2) | O(n)
# def nextGreaterElement(array):
#     result = [-1] * len(array)
    
#     for i in range(len(array)):
#         currValue = array[i]
#         for j in range(i + 1, len(array) * 2):
#             nextElement = array[j % len(array)] 
#             if nextElement > currValue:
#                 result[i] = nextElement
#                 break 
#             if j % len(array) == i:
#                 break 
#     return result

# O(n) time | O(n) space - where n is the length of the array 
def nextGreaterElement(array : List[int]) -> List[int]:
    n = len(array)
    result = [-1] * n
    stack = []
    for idx in range(2 * n):
        circularIdx = idx % n 

        while len(stack) > 0 and array[circularIdx] > array[stack[-1]]:
            top = stack.pop()
            result[top] = array[circularIdx]
        stack.append(circularIdx)
    return result


simpleAssert(nextGreaterElement([2, 5, -3, -4, 6, 7, 2]), [5, 6, 6, 6, 7, -1, 5])
