def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

# O(n) time | O(n)
def missing_elements(arr):
    missing_elements = []
    diff = arr[0] - 0
    for i in range(len(arr)):
        while (arr[i] - i) != diff:
            missing_elements.append(diff + i)
            diff += 1
        i += 1 
    return missing_elements

simple_assert(missing_elements([6, 7, 8, 9, 11, 12, 15, 16, 17, 18, 19]), [10, 13, 14])

