# def sunsetViews(buildings, direction):
#   result = []
#   if direction == "WEST":
#       buildings.reverse()
  
#   i = 0 
#   while i < len(buildings):
#       j = i + 1
#       while j < len(buildings):
#           if buildings[i] <= buildings[j]:
#               break 
#           j += 1
      
#       if j == len(buildings):
#           result.append(i)
#       i += 1
      
#   if direction == "WEST":
#       return [len(buildings)-1 -val for val in result[::-1]]
#   return result


# def sunsetViews(buildings, direction):
#     startIdx = 0 if direction == "WEST" else len(buildings)-1
#     step = 1 if direction == "WEST" else -1 

#     buildingsWithSunsetViews = []
#     maxBuildingHeight = 0

#     idx = startIdx
#     while idx >= 0 and idx < len(buildings):
#         buildingHeight = buildings[idx]

#         if buildingHeight > maxBuildingHeight:
#             buildingsWithSunsetViews.append(idx)
#         maxBuildingHeight = max(buildingHeight, maxBuildingHeight)
        
#         idx += step
    
#     if direction == "EAST":
#         return buildingsWithSunsetViews[::-1]
        
#     return buildingsWithSunsetViews

def sunsetViews(buildings, direction):
    startIdx = 0 if direction == "EAST" else len(buildings)-1
    step = 1 if direction == "EAST" else -1 

    idx = startIdx
    buildingsWithSunsetViews = []
    while idx >= 0 and idx < len(buildings):
        currBuildingHeight = buildings[idx]

        while len(buildingsWithSunsetViews) > 0 and currBuildingHeight >= buildingsWithSunsetViews[-1]:
            buildingsWithSunsetViews.pop()
        buildingsWithSunsetViews.append(idx)

        idx += step
    if direction == "WEST":
        return buildingsWithSunsetViews[::-1]
    return buildingsWithSunsetViews
       