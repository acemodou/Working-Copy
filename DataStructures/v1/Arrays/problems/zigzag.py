import pytest 

def zigzagTraverse(array):
    row, col = 0, 0 
    height, width = len(array)-1, len(array[0])-1
    result = []
    goingDown = True 

    while not out_of_bounds(row, col, height, width):
        result.append(array[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row +=1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True 
                if col == width:
                    row += 1 
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result

def out_of_bounds(row, col, height, width):
    return 0 < row > height or 0 < col > width  

@pytest.mark.parametrize(
    'array, expected',
    [
    ([
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    ]
)
def test_zigzag_traverse(array, expected):
    assert zigzagTraverse(array) == expected

if __name__ =="__main__":
    pytest.main([__file__])