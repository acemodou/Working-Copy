from validate_answers import simple_assert

def largestRange(array):
    bestRange = []
    largestLength = 0
    seen = {}
    
    for num in array:
        seen[num] = True
    
    for num in array:
        if not seen[num]:
            continue 
        
        seen[num] = False 
        currentLength = 1
        left = num - 1 
        right = num + 1
        while left in seen:
            seen[left] = False 
            currentLength += 1 
            left -= 1 
        
        while right in seen:
            seen[right] = False 
            currentLength += 1
            right += 1 
        
        if currentLength > largestLength:
            largestLength = currentLength
            bestRange = [left +1, right -1]
    return bestRange
            


simple_assert(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), [0, 7])
