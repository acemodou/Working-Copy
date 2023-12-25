
from binarySearch import simple_assert
from typing import List 

# O(n) time | O(1) space 
def findThreeLargestNumbers(array : List[int]) -> List[int]:
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest : List[int], num : int) -> List[int]:
    if threeLargest[2] == None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2) 
    elif threeLargest[1] == None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1) 
    elif threeLargest[0] == None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0) 
    
def shiftAndUpdate(threeLargest : List[int], num : int, position : int) -> None:

    for i in range(position + 1):
        if i == position:
            threeLargest[i] = num 
        else:
            threeLargest[i] = threeLargest[i+1]


simple_assert(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])
