from validate_answers import simple_assert

# def apartmentHunting(blocks, reqs):
#    blockDistance = [float("-inf")] * len(blocks)
   
#    for i in range(len(blocks)):
#        for req in reqs:
#            closestDistance = float("inf")
#            for j in range(len(blocks)):
#                if blocks[j][req]:
#                    closestDistance = min(closestDistance, distanceBetweenBlocks(i, j))
#            blockDistance[i] = max(blockDistance[i], closestDistance)
#    return get_min_index(blockDistance)
               
# def distanceBetweenBlocks(i, j):
#     return abs(i - j) 

# def get_min_index(lst):
#     if not lst:
#         return None
#     return min(range(len(lst)), key=lambda i: lst[i])

def apartmentHunting(blocks, reqs):
    blockDistances = list(map(lambda req: getDistancesFromBlocks(blocks, req), reqs))
    maxColumnBlockDistances = getMaxColumnDistances(blockDistances)
    return getMinDistanceIndex(maxColumnBlockDistances)

def getMinDistanceIndex(lst):
    if not lst:
        return None 
    
    return min(range(len(lst)), key=lambda i: lst[i])
    
    

def getMaxColumnDistances(blockDistances):
    maxDistances = [0] * len(blockDistances[0])
    for i in range(len(blockDistances[0])):
        maxBlock = max(row[i] for row in blockDistances)
        maxDistances[i] = maxBlock
    return maxDistances        
    
def getDistancesFromBlocks(blocks, req):
    blockDistances = [0] * len(blocks)
    closestDistance = float("inf")
    
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestDistance  = i 
        blockDistances[i] = distancesBetweenBlocks(i, closestDistance)
    
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestDistance  = i 
        blockDistances[i] = min(blockDistances[i], distancesBetweenBlocks(i, closestDistance))
    return blockDistances

def distancesBetweenBlocks(a , b):
    return abs(a - b)
    

blocks = [
            {"gym": False, "school": True, "store": False},
            {"gym": True, "school": False, "store": False},
            {"gym": True, "school": True, "store": False},
            {"gym": False, "school": True, "store": False},
            {"gym": False, "school": True, "store": True},
        ]
reqs = ["gym", "school", "store"]

simple_assert(apartmentHunting(blocks, reqs), 3)
