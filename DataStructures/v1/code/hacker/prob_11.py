import os
import sys 

def readfiles():
    _DATAPATH = os.path.dirname(os.path.realpath(__file__)) 
    filename = os.path.join(_DATAPATH, 'hourglass.txt')
    rows = []
    for line in open(filename).readlines():
        arr = [int(x) for x in line.split()]
        rows.append(arr)
    return rows 

def hourglass():
    arr = readfiles()
    max_sum =  -sys.maxsize
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            result = (arr[i][j] + arr[i][j+1] + arr[i][j+2]) + \
                (arr[i+1][j+1]) + (arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            if result > max_sum:
                max_sum = result
    return max_sum

print(hourglass())

   