"""         Objecive ?
    1. Store the values to rotate in a temp
    2. store new array copy
    3.combine new array with the temp array
    4. Time complexity is 0(n) space complexity is 0(d)
"""


def left_rotate_by_d(arr, n):
    temp = arr[0], arr[1]
    result = []
    for i in arr[2:]:
        result.append(i)
    answer = [*result, *temp]




"""
 1. Store the first element in a temporal variable 
 2. shift all elements to the left
 3. store the fist element in the last index
"""


def rotate_by_one(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def rotate_by_d(arr, d, n):
    for i in range(d):
        rotate_by_one(arr, n)


# display the array in horizontal line

def print_array(arr, size):
    for i in range(size):
        print("%d"% arr[i], end= " ")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    rotate_by_d(arr,2, 7)
    print(arr)
