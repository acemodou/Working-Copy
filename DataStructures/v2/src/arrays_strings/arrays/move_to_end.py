from validate_answers import simple_assert


def moveElementToEnd(array, toMove):
    startIdx = 0
    end_idx = len(array) - 1 
    
    while startIdx < end_idx:
        while startIdx < end_idx and array[end_idx] == toMove:
            end_idx -= 1
        if array[startIdx] == toMove:
            array[startIdx], array[end_idx] = array[end_idx], array[startIdx]
        startIdx += 1
   
    return array 



array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
expectedStart = [1, 3, 4]
expectedEnd = [2, 2, 2, 2, 2]
output = moveElementToEnd(array, toMove)
outputStart = sorted(output[0:3])
outputEnd = output[3:]
simple_assert(outputStart, expectedStart)
simple_assert(outputEnd, expectedEnd)