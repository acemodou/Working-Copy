from typing import List
from binarySearch import simple_assert

def quickselect(array : List, k : int) -> int:
    position = k - 1
    return quickselectHelper(array, 0, len(array)-1, position)


def quickselectHelper(array : List[int], startIdx : int, endIdx : int, position : int) -> int:
    while True:
        if startIdx > endIdx:
            raise Exception("Your algorithm should never arrive here!")
        pivot = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx

        while leftIdx <= rightIdx:
            if array[leftIdx] > array[pivot] and array[rightIdx] < array[pivot]:
                swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivot]:
                leftIdx += 1
            if array[rightIdx] >= array[pivot]:
                rightIdx -=1
        swap(pivot, rightIdx, array)
        if rightIdx == position:
            return array[rightIdx]
        elif rightIdx < position:
            startIdx += 1
        else:
            endIdx -= 1

def swap(one : int, two : int, array : List[int]) -> None:
    array[one], array[two] = array[two], array[one]






simple_assert(quickselect([8, 5, 2, 9, 7, 6, 3], 3), 5)