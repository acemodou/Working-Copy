from typing import Any 

def simple_assert(a : Any, b : Any) -> bool:
    assert a == b, f'{a}!{b}'

# O(N^2) time | O(N^2) space 
# def rotate_matrix(matrix):
#     row = len(matrix)
#     col = len(matrix[0])
    
#     rotated = [[0] * row for _ in range(col)]
    
#     for i in range(col):
#         for j in range(row):
#             rotated[i][col - j - 1] = matrix[j][i]
#     return rotated 

# O(N^2) time | O(1) space 
def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer 
        last = n - layer -1
        for i in range(first, last):
            offset = i - first 
            # save top 
            top = matrix[first][i] 
            
            # copy first bottom element to top
            matrix[first][i] = matrix[last - offset][first]
            
            # move bottom right to left 
            matrix[last - offset][first] = matrix[last][last - offset]
            
            # move top right to bottom 
            matrix[last][last - offset] = matrix[i][last]
            
            # Copy top to top right 
            matrix[i][last] = top 
    return matrix             
            
  

mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

actual =  [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]
expected = rotate_matrix(mat)
simple_assert(actual, expected)