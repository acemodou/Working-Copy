from unit_test import simple_assert

# def moveElementToEnd(array, toMove):
#     # Write your code here.
#     start_idx = 0
#     end_idx = len(array)-1
#     while start_idx < end_idx:
#         while array[start_idx] != toMove and start_idx < len(array)-1:
#             start_idx += 1
#         while array[end_idx] == toMove and end_idx > start_idx:
#             end_idx -= 1
#         if start_idx < end_idx:
#             array[start_idx], array[end_idx] = array[end_idx], array[start_idx]
#     return array 


def moveElementToEnd(array, toMove):
    #     # Write your code here.
    start_idx = 0
    end_idx = len(array)-1
    while start_idx < end_idx:
        while array[end_idx] == toMove and end_idx > start_idx:
            end_idx -= 1
        if array[start_idx] == toMove:
            array[start_idx], array[end_idx] = array[end_idx], array[start_idx]
        start_idx += 1
    return array 


simple_assert(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2), [4, 1, 3, 2, 2, 2, 2, 2])
