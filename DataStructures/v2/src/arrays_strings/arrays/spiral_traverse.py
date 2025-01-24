from validate_answers import simple_assert

# O(n) time | (n) space 
def spiralTraverse(array):
    left , right = 0,  len(array[0])
    top, bottom = 0 , len(array)
    spiral = []
    while left < right and top < bottom:
        for topRow in range(left, right):
            spiral.append(array[top][topRow])
        top += 1

        for lastCol in range(top, bottom):
            spiral.append(array[lastCol][right -1])
        right -= 1

        if not (left < right and top < bottom):
            break
        
        for bottom_row in reversed(range(left, right)):
            spiral.append(array[bottom -1][bottom_row])
        bottom -= 1

        for firstCol in reversed(range(top, bottom)):
            spiral.append(array[firstCol][left])
        left += 1

    return spiral



matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
simple_assert(spiralTraverse(matrix), expected)