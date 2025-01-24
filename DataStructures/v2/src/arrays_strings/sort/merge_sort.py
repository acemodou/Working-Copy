
from validate_answers import validate_answers

def mergeSort(array):
    N = len(array)
    winSize = 1
    while winSize < N:
        i = 0
        while i < N:
            low = i
            mid = min(i + winSize - 1, N - 1)
            high = min(i + 2 * winSize - 1, N - 1)
            merge(array, low, mid, high)
            i += 2 * winSize
        winSize *= 2
    return array

def merge(array, low, mid, high):
    i, j, k = low, mid + 1, low
    B = array[:]
    
    while i <= mid and j <= high:
        if array[i] <= array[j]:
            B[k] = array[i]
            i += 1
        else:
            B[k] = array[j]
            j += 1
        k += 1
    
    while i <= mid:
        B[k] = array[i]
        i += 1
        k += 1
    while j <= high:
        B[k] = array[j]
        j += 1
        k += 1
    
    for i in range(low, high + 1):
        array[i] = B[i]

             
validate_answers(mergeSort)
