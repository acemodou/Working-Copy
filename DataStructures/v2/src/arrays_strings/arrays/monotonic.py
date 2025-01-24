from validate_answers import simple_assert

# O(n) time | O(1) space 
def isMonotonic(array):
    isNonDecreasing = True 
    isNonIncreasing = True 
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            isNonDecreasing = False
        if array[i] < array[i-1]:
            isNonIncreasing = False
    
    return isNonIncreasing or isNonDecreasing

def isMonotonic(array):
    if len(array) < 2:
        return True 
    
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i-1]
            continue
        if breakDirection(direction, array[i], array[i-1]):
            return False 
    return True 

def breakDirection(direction, currInt, prevInt):
    diff = currInt - prevInt 
    if direction > 0:
        return diff < 0
    return diff > 0 

input = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
expected = True 
actual = isMonotonic(input)
simple_assert(actual, expected)
