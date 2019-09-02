
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
    :return: shifted array
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
    temp = arr[-1]

    for i in arr[0:6]:
        arr[i] = i
    arr[0] = temp
    print(arr)


    print(arr)
if __name__=="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    #array_rotation(arr, 3, 7)
    #rotate_by_d(arr, 3, 7)
    shift_elements_right(arr,  7)

