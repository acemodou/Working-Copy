def simple_assert(a, b):
    assert a == b, f'{a}!{b}'


def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if len(arrayOne) != len(arrayTwo):
        return False
    
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True 
    
    if arrayOne[0] != arrayTwo[0]:
        return False
    
    leftOne = getSmallerValues(arrayOne)
    leftTwo = getSmallerValues(arrayTwo)
    rightOne = getBiggerOrEqualValues(arrayOne)
    rightTwo = getBiggerOrEqualValues(arrayTwo)
    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)

def getSmallerValues(array):
    smaller = []

    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller

def getBiggerOrEqualValues(array):
    biggerOrEqual = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            biggerOrEqual.append(array[i])
    return biggerOrEqual

arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]

def getBiggerOrEqualValues(array):
    biggerOrEqual = []
    for i in range(1, len(array)):
        if array[0] <= array[i]:
            biggerOrEqual.append(array[i])
    return biggerOrEqual

arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]

simple_assert(sameBsts(arrayOne, arrayTwo), True)