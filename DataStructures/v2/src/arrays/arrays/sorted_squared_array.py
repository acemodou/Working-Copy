from typing import List 

def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

def sortedSquaredArray(array):
    result = [0] * len(array)
    start_idx = 0 
    end_idx = len(array)-1
    insert_idx = end_idx
    
    while start_idx <= end_idx:
        start_idx_value = array[start_idx]
        end_idx_value = array[end_idx]
        value_to_be_inserted = start_idx_value if abs(start_idx_value) > abs(end_idx_value) else end_idx_value
        if value_to_be_inserted == array[start_idx]:
            start_idx += 1
        else:
            end_idx -= 1
        result[insert_idx] = (value_to_be_inserted * value_to_be_inserted)
        insert_idx -= 1
    return result 
        



array = [1, 2, 3, 5, 6, 8, 9]
actual = [1, 4, 9, 25, 36, 64, 81]
expected = sortedSquaredArray(array)

simple_assert(actual, expected)
