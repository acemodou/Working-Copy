from validate_answers import simple_assert

# def fourNumberSum(array, targetSum):
#     N = len(array)
#     quadruplets = []
    
#     for i in range(N-3):
#         for j in range(i+1, N -2):
#             for k in range(j+1, N -1):
#                 for l in range(k+1, N):
#                     if array[i] + array[j] + array[k] + array[l] == targetSum:
#                         quadruplets.append([array[i], array[j], array[k],  array[l]])
#     return quadruplets
                        

def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            currSum = array[i] + array[j]
            diff = targetSum - currSum
            if diff in allPairSums:
                for pair in allPairSums[diff]:
                    quadruplets.append(pair + [array[i], array[j]])
        
        for k in range(0, i):
            currSum = array[k] + array[i]
            if currSum not in allPairSums:
                allPairSums[currSum] = [[array[k], array[i]]]
            else:
                allPairSums[currSum].append([array[k], array[i]])
            
    return quadruplets


output = fourNumberSum([7, 6, 4, -1, 1, 2], 16)
quadruplets = [[7, 6, 4, -1], [7, 6, 1, 2]]
simple_assert(output, quadruplets)




