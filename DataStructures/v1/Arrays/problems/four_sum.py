import pytest

# def fourNumberSum(array, targetSum):
#     quadruplets = []
#     n = len(array)
    
#     for i in range(n - 3):
#         for j in range(i + 1, n - 2):
#             for k in range(j + 1, n - 1):
#                 for l in range(k + 1, n):
#                     if array[i] + array[j] + array[k] + array[l] == targetSum:
#                         quadruplets.append([array[i], array[j], array[k], array[l]])
    
#     return quadruplets

def fourNumberSum(array, targetSum):
    quadruplets = []
    allPairSum = {}
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            currSum = array[i] + array[j]
            diff = targetSum - currSum
            if diff in allPairSum:
                for pair in allPairSum[diff]:
                    quadruplets.append(pair + [array[i], array[j]])
        
        for k in range(0, i):
            currSum = array[k] + array[i]
            if currSum not in allPairSum:
                allPairSum[currSum] = [[array[i], array[k]]]
            else:
                allPairSum[currSum].append([array[i], array[k]])
    return quadruplets
        

def fourNumberSum(array, targetSum):
    #Write your code here.
    quadruplets = []
    allPairSum = {}
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            currSum = array[i] + array[j]
            diff = targetSum - currSum
            if diff in allPairSum:
                for pair in allPairSum[diff]:
                    quadruplets.append(pair + [array[i], array[j]])
        
        for k in range(0, i):
            currSum = array[i] + array[k]
            if currSum not in allPairSum:
                allPairSum[currSum] = [[array[i], array[k]]]
            else:
                allPairSum[currSum].append([array[i], array[k]])
    return quadruplets


                
        

@pytest.mark.parametrize(
    'array, targetSum, expected',
    [
        ([], 11, []),
        ([7, 6, 4, -1, 1, 2], 16, [[6, 7, 4, -1], [6, 7, 1, 2]]),
        ([1, 2, 3, 4, 5, 6, 7], 10, [[2, 1, 3, 4]])
    ]
)
def test_fourNumberSum(array, targetSum, expected):
    assert fourNumberSum(array, targetSum) == expected


def test_does_not_mutate_input():
    array = [7, 6, 4, -1, 1, 2]
    fourNumberSum(array, 16)
    assert array == [7, 6, 4, -1, 1, 2]


if __name__ == "__main__":
    pytest.main([__file__])
