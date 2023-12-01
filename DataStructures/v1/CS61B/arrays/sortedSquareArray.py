def simpleAssert(a, b):
    assert a == b, f'{a}!{b}'

# def sortedSquaredArray(array):
#     sortedArray = [0]  * len(array)
#     startPos = 0 
#     endPos = len(array)-1
#     for val in array:
#         if abs(array[startPos]) > abs(array[endPos]):
#             sortedArray[endPos] = val * val
#             endPos -= 1
#         else:
#             sortedArray[startPos] = val * val 
#             startPos += 1 
#     return sortedArray
    
def sortedSquaredArray(array):
    sortedArray = [0]  * len(array)
    startPos = len(array)-1 if abs(array[0]) > abs(array[-1]) else 0
    step  = -1 if abs(array[0]) > abs(array[-1]) else 1 

    idx = startPos 
    for val in array:
        sortedArray[idx] = val * val 
        idx += step 

    return sortedArray

simpleAssert(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]),[1, 4, 9, 25, 36, 64, 81])
simpleAssert(sortedSquaredArray([-5, -4, -3, -2, -1]),[1, 4, 9, 16, 25])