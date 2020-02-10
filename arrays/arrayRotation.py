
#TODO : Store [ele 1 & ele 2 ]  in a temp variable

def array_rotation(arr, d, n):
    """
    Store ele1 and ele2 in a temp variable
    loop through the array starting index 3
    append ele1 and ele2 at the end of the array
    :param arr:
    :param d: 2
    :param n: 7
    :return: new_ array
    """

    temp = [arr[0], arr[1]]
    if len(temp) == d:
        new_arr = [i for i in arr[2:]]
        print(new_arr + temp)
    else:
        print("The value of temp: {}, should match the value of d: {}".format(len(temp), d))


def rotate_by_one(arr, n):
    """
    Store the first element in a temp variable
    shift all elements to the left
    put temp at the last index
    :param arr: [1,2,3,4,5,6,7]
    :param n:  7
    :return: shifted array complexity O(n * d) auxiliary space : O(1)
    """

    temp = arr[0]

    for i in range(len(arr)-1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def rotate_by_d(arr, d, n):
    """
    loop by range of d
    call rotate_by_one d times
    :param arr:
    :param d:
    :param n:
    :return:
    """

    for i in range(d):
        rotate_by_one(arr, n)
    print(arr)


def shift_elements_right(arr, n):
    """
    Store last element in a variable say temp
    shift all elements one position ahead
    Replace first element of array with x
    :param arr: [1,2,3,4,5]
    :param n:
    :return: [5,1,2,3,4]
    """

    temp = arr[-1]
    for i in range(n-1, 0, -1):# start end: stop at index 0, step by -1, -2 etc
        arr[i] = arr[i-1]
    arr[0] = temp

    print(arr)




def gcd(n, k):
    if k == 0:
        return n
    else:
        return gcd(k, n % k)


def juggling_algorithm(A, n, k):
    # O(n) space O(1)
    num_sets = gcd(n, k)
    for i in range(num_sets):
        j = i
        temp = A[i]
        while 1:
            d = (j + k) % n
            if d == i:
                break
            A[j] = A[d]
            j = d
        A[j] = temp

    print(A)


def sum_array(arr, n):

    sum = 0
    for i in range(len(arr)):
        sum += (arr[i] * i)
    return sum

def max_sum_value(arr, n):

    max_val = 0

    for i in range(len(arr)):
        max_sum = sum_array(arr, n)
        if max_sum > max_val:
            max_val = max_sum
            print("Array is {}, rotation is {}".format(arr, i))
        rotate_by_one(arr, n)

    print("max_sum is {}".format(max_val))
    return max_val

def rotate_get_maximum(arr, n):
    # This module takes and array and multiply each value with their index
    # store the max value as final result

    #TODO: multiply arr[i] * i
    #TODO: rotatebyone and multiply arr[i] * i
    #TODO: keep the maximum value as final result


def find_rotation_count(arr, n):
    # This module will return the index of the minimum value in an array

    #TODO: minimum value in a sorted and rotated array will show you array rotation
    #TODO: get the minimum value in the array
    #TODO: return the index as the number of times array is rotated

def find_multiple_left_rotation(arr, n):
    #This module will get an array and display how many times we rotate as output
    #Input : arr[] = {1, 3, 5, 7, 9}
    #Input : k1 = 1
    #Output : 3 5 7 9 1
    #Input : k4: 6
    #Output: 3 5 7 9 1

    #TODO: call rotatebyone
    #TODO: Undsrstand juggling algorithm and call here


def find_minimum_element_in_sorted_array(arr, n):
    # This module will return the minimum element in an array

    #TODO: from the library class called return minimum value

def right_rotation(arr, n):
    # This module will shift elements on the left

    #TODO: Shift elements using right rotation
    #TODO: Call the api implement during review code



if __name__=="__main__":
    arr = [1, 20, 2, 10]
    #array_rotation(arr, 2, 4)
    #rotate_by_d(arr, 3, 7)
    #shift_elements_right(arr,  5)
    #juggling_algorithm(arr, 7, 2)
    max_sum_value(arr, len(arr))

