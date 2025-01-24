from validate_answers import simple_assert
def zeroSumSubarray(nums):
    subArraySum = set()
    subArraySum.add(0)
    currSum = 0
    
    for num in nums:
        currSum += num 
        if currSum in subArraySum:
            return True
        subArraySum.add(num) 
    return False 




input = [4, 2, -1, -1, 3]
expected = True
actual = zeroSumSubarray(input)
simple_assert(actual, expected)