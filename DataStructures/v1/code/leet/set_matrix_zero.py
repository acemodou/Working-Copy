from typing import List 
def setZeroes(matrix: List[List[int]]) ->None:

    if not matrix:
        return 
    row_vector = set()
    col_vector = set() 
    
    # Detect Zeros, record zero location . 
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                row_vector.add(row)
                col_vector.add(col)
    
    # set detected rows/cols to 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
                if row in row_vector or col in col_vector:
                    matrix[row][col] = 0
                # elif col in col_vector:
                #     matrix[row][col] = 0
    return matrix 







assert setZeroes([[1,1,1],[1,0,1],[1,1,1]]) == [[1,0,1],[0,0,0],[1,0,1]]
assert setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]