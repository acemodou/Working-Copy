from typing import List

# Modou solution
def setZeroes(matrix: List[List[int]]) -> None:
  ''' Time complexity is: O(n^2) and Space Complexity is: O(1) '''

  # Step 0: Check if the matrix is valid or have any elements 
  if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
    return

  firstRow, firstCol = False, False 

  # Step 1: Check if there is any zero in the first row then set a flag
  firstRow = 0 in [matrix[i][0] for i in range(len(matrix))]
  
  # Step 2: Check if there is any zero in the first col then set a flag
  firstCol = 0 in matrix[0]
  
  # Step 3: Now we can skip the first row and first column. Check if there is any zero. 
  # Then set the previous row and col as 0 and the current row and previous col to zero
  for row in range(1, len(matrix)):
      for col in range(1, len(matrix[0])):
          if matrix[row][col] == 0:
              matrix[0][col] = 0
              matrix[row][0] = 0
          
  # Step 4: Check if there is any zero on the first col or on the top row. 
  # Set 0 on the current location
  for row in range(1, len(matrix)):
      for col in range(1, len(matrix[0])):
          if matrix[row][0] == 0 or matrix[0][col] == 0:
              matrix[row][col] = 0

  # Step 5: Check if we detect a zero in the first_row set that entire column to 0
  if firstRow:
      for col in range(len(matrix[0])):
          matrix[0][col] = 0
          
  # Step 6: Check if there is a zero in the first column. Set that entire row to 0
  if firstCol:
      for row in range(len(matrix)):
          matrix[row][0] = 0
  return matrix 

assert setZeroes([[1,1,1],[1,0,1],[1,1,1]]) == [[1,0,1],[0,0,0],[1,0,1]]
assert setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]



