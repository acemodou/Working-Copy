from validate_answers import simple_assert

def countSquares(points):
    pointSet = set()
    for point in points:
        pointSet.add(toString(point))
    count = 0 
    
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue 
            
            midPoint  = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
            xDist = p1[0]  - midPoint[0]
            yDist = p2[0]  - midPoint[1]
            
            p3 = (midPoint[0] + yDist, midPoint[1] - xDist)
            p4 = (midPoint[0] - yDist, midPoint[1] + xDist)
            
            if toString(p3) in pointSet and toString(p4) in pointSet:
                count += 1
    return count // 4

def toString(point):
    if point[0] % 1 == 0 or point[1] % 1 == 0:
        point = [int(coordinate) for coordinate in point]
    return ",".join([str(coordinate) for coordinate in point])
           

input = [[1, 1], [0, 0], [0, 1], [1, 0]]
expected = 1
actual = countSquares(input)
simple_assert(actual, expected)