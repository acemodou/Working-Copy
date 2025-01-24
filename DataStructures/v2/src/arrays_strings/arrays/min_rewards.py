from validate_answers import simple_assert

# def minRewards(scores):
#     rewards = [1] * len(scores)

#     for i in range(1, len(scores)):
#         j = i -1 
#         if scores[i] > scores[j]:
#             rewards[i] = rewards[j] + 1 
        
#         while j >=0 and scores[j] > scores[j+1]:
#             rewards[j] = max(rewards[j], rewards[j+1] + 1)
#             j -= 1 
#     return sum(rewards) 

# def minRewards(scores):
#     rewards = [1] * len(scores)
#     localMins = getLocalMins(scores)
#     for mins in localMins:
#         expandFromLocalMinIdx(mins, scores, rewards)
#     return sum(rewards)

# def expandFromLocalMinIdx(mins, scores, rewards):
#     leftMin = mins - 1 
#     rightMin = mins + 1
#     while leftMin >=0 and scores[leftMin] > scores[leftMin + 1]:
#         rewards[leftMin] = max(rewards[leftMin +1] + 1, rewards[leftMin])
#         leftMin -= 1 
#     while rightMin < len(scores) and scores[rightMin -1] < scores[rightMin]:
#         rewards[rightMin] = rewards[rightMin - 1] + 1
#         rightMin += 1
          

# def getLocalMins(array):
#     if len(array) == 1:
#         return [0]
#     localMins = []
#     for idx in range(len(array)):
#         if idx == 0 and array[idx] < array[idx+1]:
#             localMins.append(idx)
#         if idx == len(array)-1 and array[idx] < array[idx-1]:
#             localMins.append(idx)
        
#         if idx == 0 or idx == len(array)-1:
#             continue 
      
#         if array[idx-1] > array[idx] < array[idx + 1]:
#             localMins.append(idx)
#     return localMins 
        

def minRewards(scores):
    rewards = [1] * len(scores)
    
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1]+ 1
    
    for i in reversed(range(len(scores)-1)):
        if scores[i] > scores[i+1]:
            rewards[i] = max(rewards[i], rewards[i+1] +1)
    return sum(rewards)
        

simple_assert(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]), 25)