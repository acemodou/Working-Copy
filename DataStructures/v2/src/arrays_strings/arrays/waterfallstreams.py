from validate_answers import simple_assert


# O(w^2) time | O(w) space 
def waterfallStreams(array, source):
    rowAbove = array[0][:]
    rowAbove[source] = -1 
    
    for row in range(1, len(array)):
        currRow = array[row][:]
        
        for idx in range(len(rowAbove)):
            valueAbove = rowAbove[idx]
            
            hasWater = valueAbove < 0 
            hasBlock = currRow[idx] == 1
            
            if not hasWater:
                continue 
            
            if not hasBlock:
                currRow[idx] += valueAbove
                continue 
            
            splitWater = valueAbove / 2 
            
            rightIdx = idx
            while rightIdx + 1 < len(rowAbove):
                rightIdx += 1 
                if rowAbove[rightIdx] == 1:
                    break 
                if currRow[rightIdx] != 1:
                    currRow[rightIdx] += splitWater
                    break 
            
            leftIdx = idx 
            while leftIdx -1 >= 0:
                leftIdx -= 1 
                if rowAbove[leftIdx] == 1:
                    break 
                if currRow[leftIdx] != 1:
                    currRow[leftIdx] += splitWater
                    break 
        rowAbove = currRow

    return list(map(lambda num: num * -100, rowAbove))
                

array = [
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
        ]
source = 3
expected = [0, 0, 0, 25, 25, 0, 0]
actual = waterfallStreams(array, source)
simple_assert(expected, actual)