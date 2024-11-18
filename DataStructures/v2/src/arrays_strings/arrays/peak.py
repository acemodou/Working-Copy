import random
from validate_answers import simple_assert

# problem: Find a peak if it exists in an array 

# O(n) time | O(1) space 
# def find_peak(array):
#     for i in range(len(array)):
#         if i == 0 and array[i] > array[i+1] or i == len(array)-1 and array[i] > array[i-1]:
#             return i
#         if array[i - 1] < array[i] > array[i+1]:
#             return i 
#     return None 
         

# O(log(n)) | O(1)
# def find_peak(array):
#     start = 0 
#     end = len(array) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if mid > 0 and array[mid] < array[mid -1]:
#             end = mid - 1
#         elif mid < len(array)-1 and array[mid] < array[mid + 1]:
#             start = mid + 1
#         else:
#             return mid 
#     return None  
     
    


# A= [1, 2, 6, 5, 3, 7, 4]
# actual = 2
# expected = find_peak(A)
# simple_assert(actual, expected)


array = [
    [1, 2, 3, 4, 5],
    [8, 7, 6, 7, 6],
    [9, 8, 9, 8, 7],
    [6, 7, 8, 9, 10],
    [5, 4, 3, 2, 1]
]

# O(max_iteratins) time | O(1) space 
def hill_climb_2d(array, start=None, max_iterations=10):
    rows = len(array) - 1
    cols = len(array[0]) if rows > 0 else 0 
    curr_pos = start if start else (random.randint(0, rows -1), random.randint(0, cols -1))
    curr_val = array[curr_pos[0]][curr_pos[1]]
    
    for _ in range(max_iterations):
        curr_row, curr_col = curr_pos
        
        neighbors = {}
        if curr_row > 0: # up
            neighbors[(curr_row - 1, curr_col)] = array[curr_row - 1][curr_col]
        if curr_row < rows: # down 
            neighbors[(curr_row + 1, curr_col)] = array[curr_row + 1][curr_col]
        if curr_col > 0: # left 
            neighbors[(curr_row, curr_col -1)] = array[curr_row][curr_col -1]
        if curr_col > cols: # right
            neighbors[(curr_row, curr_col + 1)] = array[curr_row][curr_col + 1]
        
        best_neighbor = max(neighbors, key=neighbors.get, default=None)
        best_value = neighbors.get(best_neighbor, curr_val)
        
        if best_value > curr_val:
            curr_val = best_value
            curr_pos = best_neighbor
        else:
            return curr_pos, curr_val
    return curr_pos, curr_val
            
        
            




peak_position, peak_value = hill_climb_2d(array, (0, 0))
print(f"Peak found at {peak_position} with value {peak_value}")