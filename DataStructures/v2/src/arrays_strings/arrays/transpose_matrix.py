from typing import List 

def simple_assert(a, b):
    assert a == b, f'{a}!{b}'
    
def transposeMatrix(matrix : List[List[int]]):
    # Write your code here.
    transpose = []
    for row in range(len(matrix)):
        newRow = []
        for col in range(len(matrix[0])):
            newRow.append(matrix[col][row])
        transpose.append(newRow)
    return transpose


input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
actual = transposeMatrix(input)
simple_assert(actual, expected)