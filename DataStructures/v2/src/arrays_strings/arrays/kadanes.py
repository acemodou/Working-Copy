from validate_answers import simple_assert

# def kadanesAlgorithm(array, k=4):
#     curr_sum = 0 
#     max_so_far = float("-inf")
#     startIdx = endIdx = tempIdx = 0
#     for i in range(len(array)):
#         curr_sum += array[i]
#         if i >= k - 1:
#             if curr_sum > max_so_far:
#                 max_so_far = curr_sum
#                 startIdx = tempIdx
#                 endIdx = i + 1
#             curr_sum -=array[i - k + 1]
#             tempIdx += 1
#     return max_so_far, array[startIdx : endIdx]
            
# def kadanesAlgorithm(array):
#     curr_sum = array[0] 
#     max_so_far = float("-inf")
#     startIdx = endIdx = tempIdx = 0
#     for i in range(1, len(array)):
#         if array[i] > curr_sum + array[i]:
#             tempIdx = i 
#             curr_sum = array[i]
#         else:
#             curr_sum += array[i]
        
#         if curr_sum > max_so_far:
#             max_so_far = curr_sum
#             startIdx = tempIdx
#             endIdx = i+1
#     return max_so_far, array[startIdx : endIdx] 

def kadanesAlgorithm(array):
    curr_so_far = max_so_far = array[0]
    for i in range(1, len(array)):
        curr_so_far = max(array[i], curr_so_far + array[i])
        max_so_far = max(max_so_far, curr_so_far)
    return max_so_far
        

input = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# max_sum, subarray = kadanesAlgorithm(input)
# simple_assert((max_sum, subarray), (43, [18, 20, -7, 12]))
max_sum = kadanesAlgorithm(input)
simple_assert(max_sum, 43)

