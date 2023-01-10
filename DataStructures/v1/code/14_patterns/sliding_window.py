from typing import List

def simple_assert(a, b):
    assert a == b, f'{a} != {b}'

def max_sum_subarray(A:List[int], k: int) -> int:
    ''' Sliding window with fixed size K '''
    start_index, curr_sum, max_sum = 0, 0, float('-inf')
    for i in range(len(A)):
        curr_sum += A[i]
        if (i+1) - start_index == k:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= A[start_index]
            start_index += 1
    return max_sum

def min_subarray_size(A: List[int], s: int) -> int:
    ''' Sliding window with dynamic sliding size s'''
    min_size, curr_sum, start_index = float('inf'), 0, 0
    for values in range(len(A)):
        curr_sum += A[values]
        while curr_sum >= s:
            min_size = min(min_size, values + 1 - start_index)
            curr_sum -= A[start_index]
            start_index += 1 
    return min_size


def longest_substring(s: str, k: int) -> int:
    ''' Longest substring Length with k distinct characters '''
    hash_map, max_sum, = {}, float('-inf')
    for char in s:
        hash_map[char] = hash_map.get(char, 0) + 1
        while len(hash_map.items()) > k:
            max_sum = max(max_sum, sum(hash_map.values())-1)
            current_window = next(iter(hash_map.items()))[0]
            hash_map.pop(current_window)
    return max_sum

# Bruteforce approach N^2 time 
# def find_maximum_sub_array(arr):
#     max_sum = float("-inf")
#     buy, sell = 0, 0
#     for lo in range(1, len(arr)):
#         sum = 0
#         for hi in range(lo, len(arr)):
#             sum += arr[hi]
#             if sum > max_sum:
#                 max_sum = sum
#                 buy = lo
#                 sell = hi 
#     return(buy, sell, max_sum)

def find_maximum_sub_array(arr):
    max_sum = float("-inf")
    buy, sell = 0, 0
    sum = 0
    for stocks in range(len(arr)):
        hi = stocks 
        if sum > 0:
            sum += arr[stocks]
        else:
            lo = stocks
            sum = arr[stocks]
        if sum > max_sum:
            max_sum = sum
            buy = lo
            sell = hi 
    return(buy, sell+1, max_sum)


simple_assert(max_sum_subarray([2,3,4,1,5], 3), 10)
simple_assert(min_subarray_size([2,4,2,5,1], 7), 2)
simple_assert(longest_substring('AAAHHIBC', 2), 5)
simple_assert(find_maximum_sub_array([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]), (7, 11, 43))
