def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

# O(wh) time | O(wh) space 
# def removeIslands(matrix):
#     onesConnectedToBorder = [[False for col in matrix[0]] for row in matrix]
    
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             rowIsBorder = row == 0 or row == len(matrix) - 1 
#             colIsBorder = col == 0 or col == len(matrix[row]) - 1
#             isBorder = rowIsBorder or colIsBorder
#             if not isBorder:
#                 continue
            
#             if matrix[row][col] != 1:
#                 continue
            
#             findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder)
    
#     for row in range(1, len(matrix)-1):
#         for col in range(1, len(matrix[row])-1):
#             if onesConnectedToBorder[row][col]:
#                 continue
#             if matrix[row][col] != 1:
#                 continue
            
#             matrix[row][col] = 0
#     return matrix 
                

# def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectedToBorder):
#     stack = [(startRow, startCol)]
    
#     while len(stack) > 0:
#         currentPosition = stack.pop()
#         currRow, currCol = currentPosition
        
#         alreadyVisited = onesConnectedToBorder[currRow][currCol]
#         if alreadyVisited:
#             continue
#         onesConnectedToBorder[currRow][currCol] = True 
        
#         neighbors = getNeighbors(matrix, currRow, currCol)
#         for neighbor in neighbors:
#             row, col = neighbor
#             if matrix[row][col] != 1:
#                 continue
            
#             stack.append(neighbor)


# def getNeighbors(matrix, row, col):
#     numRows = len(matrix)
#     numCols = len(matrix[row])
    
#     neighbor = []
#     if row - 1 >= 0:
#         neighbor.append((row - 1, col))
#     if row + 1 < numRows:
#         neighbor.append((row + 1, col))
#     if col - 1 >= 0:
#         neighbor.append((row, col - 1))
#     if col + 1 < numCols:
#         neighbor.append((row, col + 1))
    
#     return neighbor
        

def removeIslands(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix) - 1 
            colIsBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = rowIsBorder or colIsBorder
            if not isBorder:
                continue
            
            if matrix[row][col] != 1:
                continue
            
            changeOnesConnectedToBordeToTwos(matrix, row, col)
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            color =  matrix[row][col]
            
            if color == 1:
                matrix[row][col] = 0 
            
            elif color == 2:
                matrix[row][col] = 1
            
            elif matrix[row][col] != 1:
                continue

    return matrix 
                

def changeOnesConnectedToBordeToTwos(matrix, startRow, startCol):
    stack = [(startRow, startCol)]
    
    while len(stack) > 0:
        currentPosition = stack.pop()
        currRow, currCol = currentPosition
        
        matrix[currRow][currCol] = 2
        
        neighbors = getNeighbors(matrix, currRow, currCol)
        for neighbor in neighbors:
            row, col = neighbor
            if matrix[row][col] != 1:
                continue
            
            stack.append(neighbor)


def getNeighbors(matrix, row, col):
    numRows = len(matrix)
    numCols = len(matrix[row])
    
    neighbor = []
    if row - 1 >= 0:
        neighbor.append((row - 1, col))
    if row + 1 < numRows:
        neighbor.append((row + 1, col))
    if col - 1 >= 0:
        neighbor.append((row, col - 1))
    if col + 1 < numCols:
        neighbor.append((row, col + 1))
    
    return neighbor
        
    
        
    
   
   
   
   
input = [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]
expected = [
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]
actual = removeIslands(input)
simple_assert(actual, expected)