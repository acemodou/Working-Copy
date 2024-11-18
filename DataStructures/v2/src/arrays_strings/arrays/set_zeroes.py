from typing import Any, List  

def simple_assert(a : Any, b : Any) -> bool:
    assert a == b, f'{a}!{b}'

# O(n^2) time | O(n) space 
# def zero_matrix(matrix : List[int]):
#     rows = [0] * len(matrix)
#     cols = [0] * len(matrix[0])
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 0:
#                 rows[i] = True 
#                 cols[j] = True 
    
#     # Nullify row 
#     for i in range(len(matrix)):
#         if rows[i] == True:
#             nullify_row(i, matrix)
    
#     # nullify column 
#     for j in range(len(matrix[0])):
#         if cols[j] == True:
#             nullify_col(j, matrix)
    
#     return matrix 


def nullify_row(i, matrix):
    for j in range(len(matrix[0])):
        matrix[i][j] = 0

def nullify_col(col, matrix):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def zero_matrix(matrix : List[int]):
    first_row_has_zero = False 
    first_col_has_zero = False 
    
    # Check first row has zero 
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            first_row_has_zero = True 
            break
    
    # Check first col has zero 
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break 
        
    
    # Check if rows other than first row and first col has zero
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0 
    
    #Nullify row 
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(i, matrix)
    
    # nullify column 
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            nullify_col(j, matrix)
    
    if first_row_has_zero:
        nullify_row(0, matrix)
    
    if first_col_has_zero:
        nullify_col(0, matrix)
    return matrix 

    
        

matrix =  [ [1, 1, 1],
[1, 0, 1],
[1, 1, 1]]

actual = [ [1, 0, 1],
[0, 0, 0],
[1, 0, 1]]

expected = zero_matrix(matrix)
simple_assert(actual, expected)