from minmaxstack import simpleAssert
from typing import List 

# def largestRectangleUnderSkyline(buildings : List[int]) -> int:
#     maxArea = 0 
#     for buildingIdx in range(len(buildings)):
#         currentBuildingHeight = buildings[buildingIdx]

#         leftBuilding = buildingIdx 
#         while leftBuilding > 0 and buildings[leftBuilding-1] >= currentBuildingHeight:
#             leftBuilding -= 1
        
#         rightBuilding = buildingIdx 
#         while rightBuilding < len(buildings) - 1 and buildings[rightBuilding +1] >= currentBuildingHeight:
#             rightBuilding += 1
        
#         areaWithCurrentBuilding = (rightBuilding - leftBuilding + 1) * currentBuildingHeight
#         maxArea = max(areaWithCurrentBuilding, maxArea)
#     return maxArea

def largestRectangleUnderSkyline(buildings : List[int]) -> int:
    stack = []
    maxArea = 0 

    for idx, height in enumerate(buildings + [0]):
        while len(stack) != 0 and buildings[stack[-1]] >= height:
            pillerHeight = buildings[stack.pop()]
            width = idx if len(stack) == 0 else idx - stack[-1] -1
            maxArea = max(pillerHeight * width, maxArea)
        stack.append(idx)
    return maxArea


simpleAssert(largestRectangleUnderSkyline([1, 3, 3, 2, 4, 1, 5, 3, 2]), 9)