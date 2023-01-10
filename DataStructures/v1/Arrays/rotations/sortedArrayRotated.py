import searching_arrays
import arrayRotation


def findArrayRotation(arr, n):
    print(F"-I- Kicking off array rotation {arr}")
    print(F"-I- Calling the juggling algorithm")

    rotated_arr = arrayRotation.juggling_algorithm(arr, n, d=4)
    print(F"-I- Finding the minimum element in a rotated array {rotated_arr} ")
    find_piv = searching_arrays.find_pivot(arr, n, 0, n - 1)
    return find_piv


def two_sum_pair(arr, x):
    """
    This check if there is a pair that sums up to x
    "and " to ensure result and values are distinct.
    Making sure the index of result is not the same as key
    Ex [11, 15, 6, 8, 9, 10]. If target is 12
    12 -6 = 6 . however, result shouldn't be = value
    """
    dic = dict(enumerate(arr))
    for keys, values in dic.items():
        result = x - values

        if result in dic.values() and list(dic.values()).index(result) != keys:
            print(f' There is a pair {values, result} with sum {x}')
            return list(dic.values()).index(result), keys
    print(f' There is no pair with sum {x}.')
    return False


if __name__ == "__main__":

    # arr = [5, 6, 8, 10, 12, 15, 22, 23, 28, 31, 38]
    arr = [11, 15, 26, 38, 9, 10]
    #print(F"Array is rotated and the pivot is : {findArrayRotation(arr,11)} respectively")
    #print(F'pivot is :{pair_in_sorted_rotated_array(arr, 6)}')
    two_sum_pair(arr, 45)




