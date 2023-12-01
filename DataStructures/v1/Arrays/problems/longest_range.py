import pytest 

def largestRange(array):
    # Write your code here.
    longest_length = 0
    best_range = []

    seen = {}

    for num in array:
        seen[num] = True 
    
    for num in array:
        if not seen[num]:
            continue 
        seen[num] = False
        current_length = 1
        left_side = num - 1
        while left_side in seen:
            seen[left_side] = False
            current_length += 1
            left_side -= 1
        
        right_side = num + 1
        while right_side in seen:
            seen[right_side] = False
            current_length += 1
            right_side += 1
        
        if current_length > longest_length:
            longest_length = current_length
            best_range = [left_side + 1, right_side -1]
    return best_range



@pytest.mark.parametrize(
    'input, expected',
    [
        ([4, 2, 1, 3], [1, 4]),
        ([4, 2, 1, 3, 6], [1, 4]),
        ([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6], [0, 7])
    ]
)

def test_largest_range(input, expected):
    assert largestRange(input) == expected

if __name__ =="__main__":
    pytest.main([__file__])