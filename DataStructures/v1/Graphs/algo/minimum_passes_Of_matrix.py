def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

def minimumPassesOfMatrix(matrix):
    passes = convertNegatives(matrix)
    return passes -1 if not containNegative(matrix) else -1 

def convertNegatives(matrix):
    nextPassQueue = getAllPositivePositions(matrix)
    
    passes = 0 
    
    while len(nextPassQueue) > 0:
        currentPassQueue = nextPassQueue 
        nextPassQueue = []
        
        while len(currentPassQueue) > 0:
            currRow, currCol = currentPassQueue.pop(0)
            
            adjacentPositions = getadjacentPositions(currRow, currCol, matrix)
            for position in adjacentPositions:
                row, col = position
                
                value = matrix[row][col]
                
                if value < 0:
                    matrix[row][col] = value * -1 
                    nextPassQueue.append([row, col])
        passes += 1
    return passes

def getAllPositivePositions(matrix):
    positivePositions = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 0:
                positivePositions.append([row, col])
    return positivePositions
                
def containNegative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True 
    return False 


def getadjacentPositions(row, col, matrix):
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
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1],
]
expected = 3
actual = minimumPassesOfMatrix(input)
simple_assert(actual, expected)