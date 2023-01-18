def simple_assert(a:int, b:int):
    assert a == b, f'{a}!{b}'

# Time is O(n) and space is O(1)
# def isValidSubsequence(array, sequence):
#     
#     j = 0 
#     for val in array:
#         if val == sequence[j]:
#             j += 1
#         if j == len(sequence):
#             return True 
#     return False 


# Time is O(n) and space is O(1)
def isValidSubsequence(array, sequence):
    seqIdx, arrIdx = 0, 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx +=1
    return seqIdx == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

simple_assert(isValidSubsequence(array, sequence), True)
