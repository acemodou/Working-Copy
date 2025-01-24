from validate_answers import simple_assert

# O(n) time | O(n) space 
# def arrayOfProducts(array):
#     arrayLen = len(array)
#     leftSide = [0] * arrayLen
#     rightSide = [0] * arrayLen 
    
#     runningProduct = 1
#     for i in range(arrayLen):
#         leftSide[i] = runningProduct
#         runningProduct *= array[i]
    
#     runningProduct = 1 
#     for j in reversed(range(arrayLen)):
#         rightSide[j] = runningProduct
#         runningProduct *= array[j]
    
#     for i in range(arrayLen):
#         array[i] = leftSide[i] * rightSide[i]
#     return array

def arrayOfProducts(array):
    arrayLen = len(array)
    products = [0] * arrayLen
    
    runningProduct = 1
    for i in range(arrayLen):
        products[i] = runningProduct
        runningProduct *= array[i]
    
    runningProduct = 1 
    for j in reversed(range(arrayLen)):
        products[j] = runningProduct * products[j]
        runningProduct *= array[j]
    return products
    
 

array = [5, 1, 4, 2]
expected = [8, 40, 10, 20]
actual = arrayOfProducts(array)
simple_assert(actual, expected)
            
