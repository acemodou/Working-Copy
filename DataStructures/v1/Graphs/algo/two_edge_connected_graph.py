def simple_assert(a, b):
    assert a == b, f"{a}!{b}"

def twoEdgeConnectedGraph(edges):
    if len(edges) == 0:
        return True 
    
    arrivalTimes = [-1] * len(edges)
    startVertex = 0 
    
    if getMinimumArrivalTimeOfAncestors(startVertex, -1, 0, arrivalTimes, edges) == -1:
        return False
    
    return areAllVerticesVisited(arrivalTimes)

def areAllVerticesVisited(arrivalTimes):
    for time in arrivalTimes:
        if time == -1:
            return False 
    return True 

def getMinimumArrivalTimeOfAncestors(currentVertex, parent, currentTime, arrivalTimes, edges):
    arrivalTimes[currentVertex] = currentTime
    minimumArrivalTime = currentTime
    
    for destination in edges[currentVertex]:
        if arrivalTimes[destination] == -1:
            minimumArrivalTime = min(minimumArrivalTime,
                                     getMinimumArrivalTimeOfAncestors(destination, currentVertex, currentTime+1, arrivalTimes, edges))
        elif destination != parent:
            minimumArrivalTime = min(minimumArrivalTime, arrivalTimes[destination])
    
    # A bbridge was detected, which means the graph isn't two-edge-connected. 
    if minimumArrivalTime == currentTime and parent != -1:
        return -1
    
    return minimumArrivalTime
        

input = [[1, 2, 5], [0, 2], [0, 1, 3], [2, 4, 5], [3, 5], [0, 3, 4]]
expected = True
actual = twoEdgeConnectedGraph(input)
simple_assert(actual, expected)