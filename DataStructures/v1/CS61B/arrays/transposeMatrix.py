from typing import List
from simpleAssert import simple_assert

# O(n^2) time | O(n^2) space 
def transposeMatrix(matrix : List[List[int]]) -> List[List[int]]:
    result = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        result.append(new_row)
    return result 


simple_assert(transposeMatrix([[1]]), [[1]])
simple_assert(transposeMatrix([[1, 4],[2, 5],[3, 6]]), [[1, 2, 3],[4, 5, 6]])
