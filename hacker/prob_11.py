import sys


def _getvalues(path):

    with open(path, 'r') as f:
        lines = [line.strip().split() for line in f]
        isinstance(lines, list)
        arr_glass = int(lines)
        arr_glass = arr_glass
        print(arr_glass)
        # hour_glass = [int(i) for i in arr_glass.strip()]
        # print(hour_glass)


def _hourglass(arr):
    print("arr is : ", arr)
    max_value = -sys.maxsize
    curr_max =  0
    print("Max Value = ", max_value)
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            curr_max = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + \
             arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            print("curr_max", curr_max)
            if curr_max > max_value:
                max_value = curr_max
    print("max_value", max_value)
    return max_value


if __name__ =="__main__":

    hour_glass = [[1, 1, 1, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0],
                  [1, 1, 1, 0, 0, 0],
                  [0, 0, 2, 4, 4, 0],
                  [0, 0, 0, 2, 0, 0],
                  [0, 0, 1, 2, 4, 0]]

    _hourglass(hour_glass)
