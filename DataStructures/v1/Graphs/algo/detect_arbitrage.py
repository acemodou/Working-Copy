import math 

def simple_assert(a, b):
    assert a == b, f"{a}!{b}"

# O(n^3) time | O(n^2) space 
def detectArbitrage(exchangeRates):
    # Relax the weights 
    logExchangeRates = convertToLogMatrix(exchangeRates)
    return foundNegativeWeightCycles(logExchangeRates, 0)


def convertToLogMatrix(exchangeRates):
    logMatrix = []
    for idx, rates in enumerate(exchangeRates):
        logMatrix.append([])
        for rate in rates:
            logMatrix[idx].append(-math.log10(rate))
    return logMatrix

def foundNegativeWeightCycles(graph, start):
    distancesFromStart = [float('inf')] * len(graph)
    distancesFromStart[start] = start
     
    for _ in range(len(graph) - 1):
        # If no update occur that means there is no negative cycle 
        if not relaxAndUpdateWeights(graph, distancesFromStart):
            return False
        
    return relaxAndUpdateWeights(graph, distancesFromStart)

def relaxAndUpdateWeights(graph, distance):
    update = False  
    for sourceIdx, edges in enumerate(graph):
        for distanceIdx, edgeWeights in enumerate(edges):
            newDistanceToDestination = distance[sourceIdx] + edgeWeights
            if newDistanceToDestination < distance[distanceIdx]:
                update = True
                distance[distanceIdx] = newDistanceToDestination
    return update

    

input = [[1.0, 0.8631, 0.5903], [1.1586, 1.0, 0.6849], [1.6939, 1.46, 1.0]]
expected = True
actual = detectArbitrage(input)
simple_assert(actual, expected)