

def array_rotation(arr, d, n):
    """
    store the fist two elements
    check if number of values stored is equal to the amount of rotation
    shift the array starting from the third index
    append the stored element to the end of the new array
    Time complexity is 0(n) and space is 0(d)
    """
    temp = [arr[0], arr[1]]
    if len(temp) == d:
        new_arr = [_ for _ in arr[2:]]
        return new_arr + temp
    else:
        print(F" length of temp : {len(temp)} is not equal to the number of rotations {d}")
        exit()


def rotate_left_by_one(arr, n):
    """
    Cyclically rotate an array anti clock wise
    Store the first element
    shift the array by one to the left
    place the stored element to the end of the array
    """
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[-1] = temp


def rotate_right_by_one(arr, n):
    """
    Cyclically rotate an array close wise
    Store the last element in a temp variable
    iterate array backwards
    shift n-2 to n-1 position, n-3 to n -2 etc
    put temp at the 1st index
    """
    temp = arr[-1]
    for i in range(n-1, 0, -1):# start from end: stop at index 0, step by -1
        arr[i] = arr[i-1]
    arr[0] = temp


def rotate_by_d(arr, d, n):
    """
    call rotate by d times
    time complexity O(n * d) and space complexity O(1).
    """
    if d == 0:
        print(F"There is nothing to rotate. \n Exiting !!!")
        exit()
    for _ in range(d):
        #rotate_left_by_one(arr, n)
        rotate_right_by_one(arr, n)
    return arr


def gcd(n, k):
    if k == 0:
        return n
    return gcd(k, n % k)


def juggling_algorithm(A, n, d):
    """
    refer to types of algorithm
    Time complexity is O(n) and space is O(1)
    """

    number_of_sets = gcd(n, d)
    for i in range(number_of_sets):
        j = i
        temp = A[i]

        while True:
            k = (j + d) % n
            if k == i:
                break
            A[j] = A[k]
            j = k
        A[j] = temp
    print(A)
    return A


def sum_array(arr, n):

    max_sum = 0
    for i in range(len(arr)):
        max_sum += (arr[i] * i)
    return max_sum


def max_sum_value(arr, n):

    max_val = 0

    for i in range(len(arr)):
        max_sum = sum_array(arr, n)
        if max_sum > max_val:
            max_val = max_sum
            print("Array is {}, rotation is {}".format(arr, i))
        rotate_left_by_one(arr, n)

    print("max_sum is {}".format(max_val))
    return max_val


def rotate_get_maximum(arr, n):
    # This module takes and array and multiply each value with their index
    # store the max value as final result

    #TODO: multiply arr[i] * i
    #TODO: rotatebyone and multiply arr[i] * i
    #TODO: keep the maximum value as final result
    pass


def find_rotation_count(arr, n):
    # This module will return the index of the minimum value in an array

    #TODO: minimum value in a sorted and rotated array will show you array rotation
    #TODO: get the minimum value in the array
    #TODO: return the index as the number of times array is rotated
    pass


def find_multiple_left_rotation(arr, n):
    #This module will get an array and display how many times we rotate as output
    #Input : arr[] = {1, 3, 5, 7, 9}
    #Input : k1 = 1
    #Output : 3 5 7 9 1
    #Input : k4: 6
    #Output: 3 5 7 9 1

    #TODO: call rotatebyone
    #TODO: Undsrstand juggling algorithm and call here
    pass


def find_minimum_element_in_sorted_array(arr, n):
    # This module will return the minimum element in an array

    #TODO: from the library class called return minimum value
    pass


def right_rotation(arr, n):
    # This module will shift elements on the left

    #TODO: Shift elements using right rotation
    #TODO: Call the api implement during review code
    pass


if __name__=="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    #print(rotate_by_d(arr, 0, 7))
    #juggling_algorithm(arr, 7, 3)
    max_sum_value(arr, len(arr))




