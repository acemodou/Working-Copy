from typing import List
from simpleAssert import simple_assert

def optimalAssemblyLine(stepDurations : List[int], numStations : int) -> int:
    left, right = max(stepDurations), sum(stepDurations)
    maxDuration = float("inf")

    while left <= right:
        potentialMaxDuration = (left + right) // 2

        if _isPotentialSolution(stepDurations, numStations, potentialMaxDuration):
            maxDuration = potentialMaxDuration 
            right = potentialMaxDuration -1 
        else:
            left = potentialMaxDuration + 1
            
    return maxDuration

def _isPotentialSolution(stepDurations : List[int], numStations : int, potentialMaxDuration : int) -> bool:
    stationsRequired = 1
    currentStations = 0 

    for stepDuration in stepDurations:
        if currentStations + stepDuration > potentialMaxDuration:
            stationsRequired += 1
            currentStations = stepDuration
        else:
            currentStations += stepDuration
    return stationsRequired <= numStations


simple_assert(optimalAssemblyLine([21, 14, 7, 42, 35, 28], 3), 63)