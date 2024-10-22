def simple_assert(a, b):
    assert a == b, f'{a}!{b}'


def largestIsland(matrix):
    islandNumber = 2
    islandSizes = []
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0: 
                continue
            islandSizes.append(getSizeFromNode(row, col, matrix, islandNumber))
            islandNumber += 1
    
    maxSize = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 1: 
                continue
        
            islands = set()
            landNeighbors = getIslandNeighbors(row, col, matrix)
            
            for neighbor in landNeighbors:
                islands.add(matrix[neighbor[0]][neighbor[1]])
            
            sizes = 1
            for island in islands:
                sizes += islandSizes[island - 2]
            maxSize = max(maxSize, sizes)
    return maxSize

def getSizeFromNode(row, col, matrix, islandNumber):
    nodesToExplore = [[row, col]]
    sizes = 0 
    while len(nodesToExplore) > 0:
        currentRow, currentCol = nodesToExplore.pop()
        
        if matrix[currentRow][currentCol] != 0:
            continue
        
        matrix[currentRow][currentCol] = islandNumber
        sizes += 1
        nodesToExplore += getIslandNeighbors(currentRow, currentCol, matrix)
    return sizes
        
def getIslandNeighbors(row, col, matrix):
    numRows = len(matrix) -1 
    numCols = len(matrix[row]) -1 
    neighbors = []
    
    if row > 0 and matrix[row -1][col] != 1:
        neighbors.append([row-1, col])
    if row < numRows and matrix[row + 1][col] != 1:
        neighbors.append([row+1, col]) 
    if col > 0 and matrix[row][col -1] != 1:
        neighbors.append([row, col-1])
    if col < numCols and matrix[row][col + 1] != 1:
        neighbors.append([row, col + 1])
    
    return neighbors        
    


input = [[0, 1, 1], [0, 0, 1], [1, 1, 0]]
expected = 5
actual = largestIsland(input)
simple_assert(actual, expected)