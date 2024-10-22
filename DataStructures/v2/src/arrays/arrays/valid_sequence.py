from typing import List 

def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

# O(n) time | O(1) space 
# def isValidSubsequence(array : List[int], sequence : List[int]):
#     if len(sequence) > len(array):
#         return False 
    
#     i, j = 0, 0 
#     while i < len(array) and j < len(sequence):
#         if array[i] == sequence[j]:
#             j += 1
#         i += 1
#     return j == len(sequence)
       

# O(n) time | O(1) space 
def isValidSubsequence(array : List[int], sequence : List[int]):
    seqIdx = 0 
    for value in array:
        if seqIdx == len(sequence):
            break 
        if sequence[seqIdx] == value:
            seqIdx += 1 
    return seqIdx == len(sequence)       

expected = True 
actual = isValidSubsequence([5, 1, 22, 6, -1, 8, 10], [1, 6, -1, 10])
simple_assert(expected, actual)