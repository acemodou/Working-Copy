from validate_answers import simple_assert
def bestSeat(seats):
    bestSeat = -1
    maxSpace = 0  
    idx = 1 
    while idx < len(seats):
        if seats[idx] == 1:
            idx += 1
            continue
            
        leftSide = idx -1
        while leftSide >= 0 and seats[leftSide] != 1:
            leftSide -= 1
        rightSide = idx + 1
        while rightSide < len(seats) and seats[rightSide] != 1:
            rightSide += 1
        currSpace = rightSide - leftSide -1 
        if currSpace > maxSpace:
            maxSpace = currSpace
            bestSeat = (leftSide + rightSide) // 2
        idx = rightSide
    return bestSeat
         



input = [1, 0, 1, 0, 0, 0, 1]
expected = 4
actual = bestSeat(input)
simple_assert(actual, expected)