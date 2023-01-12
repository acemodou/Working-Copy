
#TODO : Store [ele 1 & ele 2 ]  in a temp variable

def array_rotation(arr, d, n):
    """
    Store ele1 and ele2 in a temp variable
    loop through the array starting index 2
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





if __name__=="__main__":
    arr = [1, 2, 3, 4, 5]
    #array_rotation(arr, 3, 7)
    #rotate_by_d(arr, 3, 7)
    shift_elements_right(arr,  5)
    #juggling_algorithm(arr, 7, 2)
