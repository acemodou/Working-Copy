from simpleAssert import simple_assert 
from typing import List  

# # O(nxm) time | O(1) space
# def searchInSortedMatrix(matrix, target):
#     # Write your code here.
#     for row in range(len(matrix)):
#         for col in range(len(matrix[0])):
#             if matrix[row][col] == target:
#                 return [row, col]
#     return [-1, -1] 


# O(n+m) time | O(1) space 
def searchInSortedMatrix(matrix : List[List[int]], target : int) -> List[int]:
    
    row = 0
    col = len(matrix[0]) -1 
    
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -=1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1, -1]


matrix =[
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]]
target =44

simple_assert(searchInSortedMatrix(matrix, target), [-3, -3])