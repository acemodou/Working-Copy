# def set_zeros(matrix):
#     rows = [False] * len(matrix)
#     columns = [False] * len(matrix[0])

#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 0:
#                 rows[i] = True 
#                 columns[j] = True 
    
#     for i in range(len(matrix)):
#         if rows[i]:
#             nullify_row(matrix, i)
    
#     for j in range(len(matrix[0])):
#         if columns[j]:
#             nullify_col(matrix, j)
#     return matrix

def set_zeros(matrix):
    # Check first row has zero 
    row_has_zero = False 
    col_has_zero = False

    # Check if first row has a zero 
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            row_has_zero = True
            break 
    
    # Check if first col has a zero 
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            col_has_zero = True
            break 

    # Check for zeros in the rest of the array 
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0 
                matrix[0][j] = 0
    
    # Nullify rows based on values in first column 
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)
    
    # Nullify columns based on values in first row
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            nullify_col(matrix, j)
    
    # Nullify first row 
    if row_has_zero:
        nullify_row(matrix, 0)
    
    # Nullify first col
    if col_has_zero:
        nullify_col(matrix, 0)
    
    return matrix

def nullify_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0

def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0

 
    # Check for zeros in any row starting row 1 and 
    # make the first column and top row zero 
    # Check for zeros in first row beyond and nullify 
    # Check for zeros in first column and nullify 
    # Check for zeros in the first row and first column and nullify 


matrix = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]

print(set_zeros(matrix))