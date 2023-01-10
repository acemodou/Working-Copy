sparse_matrix = [[0,1,0,0],[0,0,0,0],[0,5,0,2],[9,0,0,6],[7,0,0,0]]

# Count the number of non_zeroes 
non_zeros = 0
for i in range(len(sparse_matrix)):
    for j in range(len(sparse_matrix[0])):
        if sparse_matrix[i][j] != 0:
            non_zeros += 1

# Create the size of the coordinate array 
rows, cols = (3, non_zeros)
coordinate_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# Mark the visited rows, cols and store values
k = 0
for row in range(len(sparse_matrix)):
    for col in range(len(sparse_matrix[0])):
        if sparse_matrix[row][col] != 0:
            coordinate_matrix[0][k] = row 
            coordinate_matrix[1][k] = col
            coordinate_matrix[2][k] = sparse_matrix[row][col]
            k += 1

# Display values in coordinates matrix 
for values in coordinate_matrix:
    print(values)




