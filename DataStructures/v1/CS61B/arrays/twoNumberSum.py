from typing import List 

def simpleAssert(a : int, b: int) ->None:
    assert a == b, f'{a} != {b}'

# ON^2 and O(1) space 
# def twoNumberSum(array : List[int], targetSum : int) -> List[int]:
#     for i in range(len(array) -1):
#         firstNum = array[i]
#         for j in range(i + 1, len(array)):
#             secondNum = array[j]
#             if firstNum + secondNum == targetSum:
#                 return [firstNum, secondNum]
#     return []



def twoNumberSum(array : List[int], targetSum : int) -> List[int]:
    seen ={}
    for idx in range(len(array)):
        num = array[idx]
        cacheValue = targetSum - num 
        if cacheValue in seen:
            return [cacheValue, num]
        seen[num] = idx  
    return []



simpleAssert(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10), [11, -1])
simpleAssert(twoNumberSum([4, 6], 10), [4, 6])
