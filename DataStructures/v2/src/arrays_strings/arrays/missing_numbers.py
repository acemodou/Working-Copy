from validate_answers import simple_assert

# def missingNumbers(nums):
#     totalLen = len(nums) + 2
#     missingNums = [0] * totalLen
#     res = []
#     for num in nums:
#         missingNums[num -1] = num 
#     for i in range(totalLen):
#         if missingNums[i] == 0:
#             res.append(i+1)
#     return res 
            
            
# def missingNumbers(nums):
#     totalLen = len(nums) + 2
#     nonMissing = set(nums)
#     res = []
    
#     for i in range(1, totalLen+1):
#         if i not in nonMissing:
#             res.append(i)
#     return res 

def missingNumbers(nums):
    N = len(nums) + 2
    total = N * (N + 1) // 2
    
    for num in nums:
        total -= num 
    diff = total // 2 
    
    firstMissing = 0 
    secondMissing = 0 
    for num in nums:
        if num <= diff:
            firstMissing += num 
        else:
            secondMissing += num 
    expectedFirstHalf = sum(range(1, diff+1))
    expectedSecondHalf = sum(range(diff+1, N+1))
    return [expectedFirstHalf - firstMissing, expectedSecondHalf - secondMissing]

input = [4, 5, 2, 3]
expected = [1, 6]
actual = missingNumbers(input)
simple_assert(actual, expected)