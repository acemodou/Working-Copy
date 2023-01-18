from typing import List

def simple_assert(a , b):
    assert a == b, f'{a} != {b}'

# O(n^2) time and O(1) space 
# def two_sums(array : List[int], target : int) -> List:
#     # iterate from the begining of the list 
#     for i in range(len(array)):
#         # iterate from i + 1 until the end of the array 
#         for j in range(i+1, len(array)):
#             if array[i] + array[j] == target:
#                 return [array[i], array[j]]
#     return []

# O(n) time  and O(1) space 
def two_sums(array : List[int], target : int) -> List:
    cache_results = {}
    for idx, value in enumerate(array):
        if target - value in cache_results:
            return [target-value, array[idx]]
        
        cache_results[value] = idx
    return []

simple_assert(two_sums([3, 5, -4, 8, 11, 1, -1, 6], 10), [11, -1])
simple_assert(two_sums([4,6], 10), [4, 6])
simple_assert(two_sums([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163),[210, -47])
simple_assert(two_sums([3, 9], 11),  [])
