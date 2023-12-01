def simpleAssert(a : int, b : int) ->None:
    assert a == b, f'{a}!{b}'

# time is O(n) | space is O(d)
def productSum(array, multiplier = 1):
    sum = 0
    for elements in array:
        if type(elements) is list:
            sum += productSum(elements, multiplier + 1)
        else:
            sum += elements
    return sum * multiplier
    
    

simpleAssert(productSum([1, 2, [3], 4, 5]), 18)
simpleAssert(productSum([[1, 2],3,[4, 5]]), 27)
simpleAssert(productSum([1, 2, 3, 4, 5]), 15)
simpleAssert(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]), 12)

