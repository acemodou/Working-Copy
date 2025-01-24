from validate_answers import simple_assert

def zigzagTraverse(array):
    row, col = 0, 0 
    width, bottom = len(array[0])-1, len(array)-1
    goingDown = True 
    res = []
    
    while not isOutOfBound(row, col, width, bottom):
        res.append(array[row][col])
        if goingDown:
            if col == 0 or row == bottom:
                goingDown = False
                if row == bottom:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1 
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                col += 1
                row -= 1 
    return res 


def isOutOfBound(row, col, top, bottom):
    return row > bottom or col > top or row < 0 or col < 0 


test = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
simple_assert(zigzagTraverse(test), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
