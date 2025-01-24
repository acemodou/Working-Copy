from validate_answers import simple_assert

def sweetAndSavory(dishes, target):
    bestPair = [0, 0]
    bestDiff = float("inf")
    sweetDishes = sorted([dish for dish in dishes if dish < 0], key=abs)
    savoryDishes = sorted([dish for dish in dishes if dish > 0])
    sweetIdx, savoryIdx = 0, 0
    while sweetIdx < len(sweetDishes) and savoryIdx < len(savoryDishes):
        combinedDishes = sweetDishes[sweetIdx] + savoryDishes[savoryIdx]
        if combinedDishes <= target:
            currdiff = target - combinedDishes  
            if currdiff < bestDiff:
                bestDiff = currdiff
                bestPair = [sweetDishes[sweetIdx],  savoryDishes[savoryIdx]]
            savoryIdx += 1
        else:
            sweetDishes += 1
        
    return bestPair
        
    


dishes = [-3, -5, 1, 7]
target = 8
expected = [-3, 7]
actual = sweetAndSavory(dishes, target)
simple_assert(actual, expected)