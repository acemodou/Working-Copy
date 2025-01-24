from validate_answers import simple_assert

# def longestSubarrayWithSum(array, targetSum):
#     subArray = []
#     for i in range(len(array)):
#         sum = 0
#         for j in range(i, len(array)):
#             sum += array[j]
#             if sum  == targetSum:
#                 if len(subArray) == 0 or  j - i > subArray[1] - subArray[0]:
#                  subArray = [i, j]
#     return subArray

def longestSubarrayWithSum(array, targetSum):
    subArray = [0, 0]
    startIdx = 0 
    currSum = 0 
    maxSoFar = 0 
    for i in range(len(array)):
        currSum += array[i]
        
        while currSum > targetSum and startIdx < i:
            currSum -= array[startIdx]
            startIdx += 1 
            
        if currSum == targetSum:
            runningSum =  i  - startIdx
            if runningSum > maxSoFar:
                maxSoFar = runningSum
                subArray = [startIdx, i]
                
    return subArray
            

array = [1, 2, 3, 4, 3, 3, 1, 2, 1]
targetSum = 10
expected = [4, 8]
actual = longestSubarrayWithSum(array, targetSum)
simple_assert(actual, expected)