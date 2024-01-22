from simpleAssert import simple_assert
from typing import List

# O(n + m) | O(n + m) space 
# def medianOfTwoSortedArrays(arrayOne : List[int], arrayTwo : List[int]) -> int or float:
#     mergeSortedArray = []

#     idxOne, idxTwo = 0, 0 
#     while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
#         if arrayOne[idxOne] < arrayTwo[idxTwo]:
#             mergeSortedArray.append(arrayOne[idxOne])
#             idxOne += 1
#         else:
#             mergeSortedArray.append(arrayTwo[idxTwo])
#             idxTwo += 1
#     if idxOne < len(arrayOne):
#         mergeSortedArray.extend(arrayOne[idxOne: ])
#     if idxTwo < len(arrayTwo):
#         mergeSortedArray.extend(arrayTwo[idxTwo : ])
    
#     return getMedian(mergeSortedArray)


# def getMedian(array : List[int]) -> int or float:
#     median = (len(array) - 1) // 2

#     if len(array) % 2:
#         return array[median]
#     else:
#         return (array[median] + array[median  + 1]) / 2

# O(n + m) | O(1) space 
# def medianOfTwoSortedArrays(arrayOne : List[int], arrayTwo : List[int]) -> int or float:
#     idxOne, idxTwo = 0, 0
#     midIdx = ((len(arrayOne) + len(arrayTwo)) -1) // 2

#     while idxOne + idxTwo < midIdx:
#         if idxOne >= len(arrayOne):
#             idxTwo += 1
#         elif idxTwo >= len(arrayTwo):
#             idxOne += 1
#         elif arrayOne[idxOne] < arrayTwo[idxTwo]:
#             idxOne += 1
#         else:
#             idxTwo += 1
    
#     if (len(arrayOne) + len(arrayTwo)) % 2 == 0:
#         allValuesInArrayOne = idxTwo >= len(arrayTwo) or (
#             idxOne + 1 < len(arrayOne) and arrayTwo[idxTwo] > arrayOne[idxOne + 1]
#         )

#         allValuesInArrayTwo = idxOne >= len(arrayOne) or (
#             idxTwo + 1 < len(arrayTwo) and arrayOne[idxOne] > arrayTwo[idxTwo + 1]
#         )

#         valueOne = arrayOne[idxOne + 1] if allValuesInArrayOne else arrayTwo[idxTwo]
#         valueTwo = arrayTwo[idxTwo + 1] if allValuesInArrayTwo else arrayOne[idxOne]
#         return (valueOne + valueTwo) / 2
    
#     valueOne = arrayOne[idxOne] if idxOne < len(arrayOne) else float("inf")
#     valueTwo = arrayTwo[idxTwo] if idxTwo < len(arrayTwo) else float("inf")
#     return min(valueOne, valueTwo)

#O(n + m) | O(1) space 
def medianOfTwoSortedArrays(arrayOne : List[int], arrayTwo : List[int]) -> float:
    smallArray = arrayOne if len(arrayOne) <= len(arrayTwo) else arrayTwo
    bigArray = arrayOne if len(arrayOne) > len(arrayTwo) else arrayTwo

    leftIdx = 0 
    rightIdx = len(smallArray)-1 
    mergeLeftIdx = (len(smallArray) + len(bigArray) -1) // 2

    while True:
        smallPartionIdx = (leftIdx + rightIdx ) // 2
        bigPartitionIdx = mergeLeftIdx - smallPartionIdx -1 

        smallMaxLeftValue = (
            smallArray[smallPartionIdx] if smallPartionIdx >= 0 else float("-inf")
        )
        smallMinRightValue = (
            smallArray[smallPartionIdx + 1] if smallPartionIdx + 1 < len(smallArray) else float("inf")
        )

        bigMaxLeftValue = bigArray[bigPartitionIdx] if bigPartitionIdx >= 0 else float("-inf")
        bigMinRightValue = (
            bigArray[bigPartitionIdx + 1] if bigPartitionIdx + 1 < len(bigArray) else float("inf")
        )

        if smallMaxLeftValue > bigMinRightValue:
            rightIdx = smallPartionIdx - 1
        elif bigMaxLeftValue > smallMinRightValue:
            leftIdx = smallPartionIdx + 1
        else:
            if (len(smallArray) + len(bigArray)) % 2 == 0:
                return (max(smallMaxLeftValue, bigMaxLeftValue) + min(smallMinRightValue, bigMinRightValue)) / 2
            return max(smallMaxLeftValue, bigMaxLeftValue)

simple_assert(medianOfTwoSortedArrays([1, 3, 4, 5],[2, 3, 6, 7]), 3.5)
simple_assert(medianOfTwoSortedArrays([1, 3, 4, 5, 7, 9],[0, 1, 2, 2, 4]), 3)
