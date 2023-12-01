from minmaxstack import simpleAssert
from typing import List 

def largestPark(land : List[int]) -> int:
    heights = [0] * len(land[0])
    maxArea = 0 

    for row in land:
        for columnIdx in range(len(land[0])):
            heights[columnIdx] = heights[columnIdx] + 1 if row[columnIdx] == False else 0
        maxArea = max(maxArea,largestRectangeHistogram(heights))
    return maxArea

def largestRectangeHistogram(buildings) -> int:
    stack = []
    maxArea = 0 

    for idx, height in enumerate(buildings + [0]):
        while len(stack) != 0 and buildings[stack[-1]] >= height:
            pillerHeight = buildings[stack.pop()]
            width = idx if len(stack) == 0 else idx - stack[-1] -1
            maxArea = max(pillerHeight * width, maxArea)
        stack.append(idx)
    return maxArea


land = [[False, True, True, True, False],
        [False, False, False, True, False],
        [False, False, False, False, False],
        [False, True, True, True, True]]

simpleAssert(largestPark(land), 6)