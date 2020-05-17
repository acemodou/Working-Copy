"""This file contains only library calls """


def median_point(arr):
    """
    We return the midpoint for even and odd numbers
    Can't use for binary because it will return same array all the time
    need improvement
    """
    if len(arr) <= 0 and not isinstance(arr, list):
        print(f"Wrong arguments given: {arr}. Exiting !!!")
        exit()

    n = len(arr)
    if n % 2 == 0:
        return ((n // 2) + (n - 1) // 2) // 2
    else:
        return n // 2


def iterative_binary(arr, value_search):
    left_side = 0
    right_side = len(arr) - 1
    while left_side <= right_side:
        array_mid = (left_side + right_side) // 2
        if value_search == arr[array_mid]:
            return array_mid, arr[array_mid]
        elif arr[array_mid] > value_search >= arr[left_side]:
            right_side = array_mid - 1
        elif arr[array_mid] < value_search <= arr[right_side]:
            left_side = array_mid + 1
        else:
            print(f"The value we are searching {value_search}  does not exist. \n Exiting !!!")
            exit()


def recursive_binary(arr, value_search,  left_side, right_side):

    array_mid = (left_side + right_side) // 2
    if value_search == arr[array_mid]:
        return array_mid, arr[array_mid]
    elif arr[array_mid] > value_search >= arr[left_side]:
        return recursive_binary(arr, value_search, left_side, array_mid - 1)
    elif arr[array_mid] < value_search <= arr[right_side]:
        return recursive_binary(arr, value_search, array_mid + 1, right_side)
    else:
        print(F"The value we are searching {value_search} does not exist. \n Exiting !!!")
        exit()


def find_minimum_index(arr):
    """
    We know the pivot is the smallest element in sorted and rotated array.
    This is a simpler method of finding rotation count
    time complexity is 0(n)
    """
    min_element = arr[0]
    max_element = arr[0]
    min_index = 0
    max_index = 0
    for idx, value in enumerate(arr):
        if value < min_element:
            min_element = value
            min_index = idx
        if value > max_element:
            max_element = value
            max_index = idx

    # printing the array and position
    print(F'The max is {max_element} at position {max_index + 1}')
    print(F'The min is {min_element} at position {min_index + 1}')
    return max_element, max_index + 1, min_element, min_index + 1


def findMinimumIndex(arr):
    """
    Finding minimum value using library
    """

    min_pos = arr.index(min(arr))

    max_pos = arr.index(max(arr))

    # printing the array and position
    print(F'The max is {arr[max_pos]} at position {max_pos + 1}')
    print(F'The min is {arr[min_pos]} at position {min_pos + 1}')


def find_pivot(arr, n, left_side, right_side):
    """
    We know the pivot is the smallest element in sorted and rotated array
    This is a bit more complicated but is more efficient
    """

    array_mid = (left_side + right_side) // 2
    before_pivot = (array_mid + n - 1) % n
    after_pivot = (array_mid + 1) % n
    if arr[left_side] <= arr[right_side]:
        return left_side
    elif arr[before_pivot] >= arr[array_mid] <= arr[after_pivot]:
        return array_mid
    elif arr[array_mid] <= arr[right_side]:
        return find_pivot(arr, n, left_side, array_mid - 1)
    elif arr[array_mid] >= arr[left_side]:
        return find_pivot(arr, n, array_mid + 1, right_side)
    else:
        print(F"The array {arr} is not rotated. \n Exiting !!!")
        exit()


if __name__ == "__main__":
    arr = [11, 15, 26, 38, 9, 10]

    find_minimum_index(arr)
    findMinimumIndex(arr)







