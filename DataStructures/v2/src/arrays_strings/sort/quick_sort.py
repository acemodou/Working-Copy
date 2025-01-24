from validate_answers import simple_assert

def quickSort(array):
    quickSortHelper(0, len(array)-1, array)
    return array 

def quickSortHelper(low, high, array):
    if low < high:
        j = partion(array, low, high)
        quickSortHelper(array, low, j-1)
        quickSortHelper(array, j+1, high)

def partion(array, start, end):
    pivotIdx  = start
    pivot = array[pivotIdx]
    
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1 
        
        if start < end:
            array[start], array[end] = array[end], array[start]
    array[pivotIdx], array[end] =  array[end], array[pivotIdx]
    return end 
    









arr = [8, 5, 2, 9, 5, 6, 3]
expected = [2, 3, 5, 5, 6, 8, 9]
actual = quickSort(arr)
simple_assert(actual, expected)