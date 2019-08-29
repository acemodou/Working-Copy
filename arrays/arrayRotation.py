
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
    new_arr = list()

    if len(temp) == d:
        new_arr = [i for i in arr[2:]]
        print(new_arr + temp)
    else:
        print("The value of temp: {}, should match the value of d: {}".format(len(temp), d))




if __name__=="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    array_rotation(arr, 3, 7)

