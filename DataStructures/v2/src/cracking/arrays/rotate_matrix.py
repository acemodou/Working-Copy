def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        # Transpose the matrix 
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse rows
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return matrix
    
