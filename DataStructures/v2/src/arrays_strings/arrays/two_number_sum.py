
def simple_assert(a, b):
    a == b, f'{a}!{b}'
    
from typing import List
 

# O(n^2) time | O(n) space 
# def two_number_sum(array : List[int], target : int) -> List[int]:
#     seen = []
#     for idx in range(len(array)):
#         target_sum = target - array[idx]
#         if target_sum in seen: # O(n)
#             return [array[idx], target_sum]
#         seen.append(array[idx])
#     return []


# O(n) time | O(n) space 
def two_number_sum(array : List[int], target_sum : int) -> List[int]:
    seen = {}
    for key, value in enumerate(array):
        target = target_sum - value 
        if target in seen: # O(1)
            return [value, target]
        seen[value] = key 
    return []
    

expected = [-1, 11] 
actual = two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10 )

simple_assert(expected, actual)