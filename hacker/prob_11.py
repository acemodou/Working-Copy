import sys


def _getvalues(path):

    with open(path, 'r') as f:
        lines = f.read()
        hour_glass = lines.split("\n")
        output_list = []
        for rec in hour_glass:
            numbers_as_strings = rec.split()
            print(numbers_as_strings)  ## while testing
            inner_list = []
            for num in numbers_as_strings:
                inner_list.append(int(num))
            output_list.append(inner_list)
    #
    print("\noutput_list =", output_list)


def _hourglass(arr):
    print("arr is : ", arr)
    max_value, curr_max = -sys.maxsize, 0
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

    # _hourglass(hour_glass)
    _getvalues('hourglass.txt')
