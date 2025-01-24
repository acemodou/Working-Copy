from validate_answers import simple_assert

def subarraySort(array):
    minOutOrder = float("inf")
    maxOutOrder = float("-inf")
    for idx in range(len(array)):
        num = array[idx]
        if isOutOrder(num, idx, array):
            minOutOrder = min(minOutOrder, num)
            maxOutOrder = max(maxOutOrder, num)
    if minOutOrder == float("inf"):
        return [-1, -1]
    
    subarrayLeftIdx = 0 
    while minOutOrder >= array[subarrayLeftIdx]:
        subarrayLeftIdx += 1
    
    subarrayRightIdx = len(array) -1 
    while maxOutOrder <= array[subarrayRightIdx]:
        subarrayRightIdx -= 1
    
    return [subarrayLeftIdx, subarrayRightIdx]

def isOutOrder(num, idx, array):
    if idx == 0:
        return num > array[idx +  1]
    if idx == len(array)-1:
        return num < array[idx -1]
    return num < array[idx -1 ] or num > array[idx + 1] 


simple_assert(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])