from validate_answers import simple_assert
import math 

def knightConnection(knightA, knightB):
    possibleMoves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
    queue = [[knightA[0], knightA[1], 0]]
    visited = {postionToString(knightA)}
    
    while True:
        
        currentPosition = queue.pop(0)
        
        if currentPosition[0] == knightB[0] and currentPosition[1] == knightB[1]:
            return math.ceil(currentPosition[2] / 2)
        
        for move in possibleMoves:
            position = [currentPosition[0] + move[0], currentPosition[1] + move[1]]
            positionString = postionToString(position)
            if positionString not in visited:
                position.append(currentPosition[2] + 1)
                queue.append(position)
                visited.add(positionString)
                
            


def postionToString(position):
    p1, p2 = position
    return f"{p1},{p2}"

knightA = [0, 0]
knightB = [2, 1]
expected = 1
actual = knightConnection(knightA, knightB)
simple_assert(actual, expected)
