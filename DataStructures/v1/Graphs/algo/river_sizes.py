# and methods to the class.
def simple_assert(a, b):
    assert a == b, f"{a}!{b}"

# time O(w.h) | space O(w.h) 
def riverSizes(matrix):
    # Write your code here.
    sizes = []
    visited = [[False for _ in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue 
            traverseNode(i, j, visited, matrix, sizes)
    return sizes

def traverseNode(i, j, visited, matrix, sizes):
    currentRiverSize = 0    
    nodesToExplore = [[i, j]]
    
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        
        if visited[i][j]:
            continue
        visited[i][j] = True 
        
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, visited, matrix)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

def getUnvisitedNeighbors(i, j, visited, matrix):
    unvisitedNeighbors = []
    if i > 0 and not visited[i-1][j]:
        unvisitedNeighbors.append([i-1, j])
    if i < len(matrix)-1 and not visited[i+1][j]:
        unvisitedNeighbors.append([i+1, j])
    if j > 0 and not visited[i][j-1]:
        unvisitedNeighbors.append([i, j-1])
    if j < len(matrix[0])-1 and not visited[i][j+1]:
        unvisitedNeighbors.append([i, j+1])
    return unvisitedNeighbors

testInput = [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
        ]
expected = [1, 2, 2, 2, 5]
simple_assert(sorted(riverSizes(testInput)), expected)