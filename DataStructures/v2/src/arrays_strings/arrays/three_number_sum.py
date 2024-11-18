from valid_sequence import simple_assert


def threeNumberSum(array, targetSum):
    threeNumberSum = []
    array.sort()
    for i in range(len(array)):
        j = i + 1
        k = len(array) -1 
        while j < k:
            threeSum = array[i] + array[j] + array[k]
            if threeSum > targetSum:
                k -= 1
            elif threeSum < targetSum:
                j += 1
            else:
                threeNumberSum.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
    return threeNumberSum



simple_assert(
threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0),
            [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]],
        )




