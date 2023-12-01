import pytest

def subarraySort(array):
    min_out_of_order = float("inf")
    max_out_of_order = float("-inf")
    
    for i in range(len(array)):
        num = array[i]
        if is_out_of_order(i, num, array):
            min_out_of_order = min(min_out_of_order, num)
            max_out_of_order = max(max_out_of_order, num)
    
    if min_out_of_order == float("inf"):
        return [-1, -1]
    
    left_sorted_side = 0
    while min_out_of_order >= array[left_sorted_side]:
        left_sorted_side += 1
    
    right_sorted_side = len(array)-1
    while max_out_of_order <= array[right_sorted_side]:
        right_sorted_side -=1

    return [left_sorted_side, right_sorted_side]

def is_out_of_order(i, num, array):
    if i == 0:
        return num > array[i+1]
    if i == len(array)-1:
        return num < array[i-1]

    return num < array[i-1] or num > array[i+1]

    

        

@pytest.mark.parametrize(
    "array, expected",
    [
        ([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19], [3, 9]),
        ([1, 2], [-1, -1]),
        ([2, 1], [0, 1])
    ]
)

def test_subarray_sort(array, expected):
    assert subarraySort(array) == expected


def test_does_not_mutate_array():
    array = [1, 2]
    subarraySort(array)
    assert array == [1, 2]


if __name__=="__main__":
    pytest.main([__file__])