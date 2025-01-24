from validate_answers import simple_assert
def firstDuplicateValue(array):
    for i in range(len(array)):
        idx = abs(array[i]) - 1
        if array[idx] < 0:
            return abs(array[i])
        array[idx] *= -1 
    return -1 


input = [2, 1, 5, 2, 3, 3, 4]
expected = 2
actual = firstDuplicateValue(input)
simple_assert(actual, expected)