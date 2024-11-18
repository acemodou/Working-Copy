from validate_answers import simple_assert

# O(n * m ) time | O(1) space 
# def smallestDifference(arrayOne, arrayTwo):
#     small_diff = float("inf")
#     smallDiffRes = [0, 0]
    
#     for i in range(len(arrayOne)):
#         for j in range(len(arrayTwo)):
#             arrayOneVal = arrayOne[i]
#             arrayTwoVal = arrayTwo[j]
            
#             diff = arrayOneVal - arrayTwoVal if arrayOneVal > arrayTwoVal else arrayTwoVal - arrayOneVal
#             if diff < small_diff:
#                 small_diff = diff
#                 smallDiffRes = [arrayOneVal, arrayTwoVal]
#     return smallDiffRes


# O(nlog(n)) + O(mlog(m)) | O(1) space 
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    small_diff = float("inf")
    smallDiffRes = [0, 0]
    
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        arrayOneVal = arrayOne[idxOne]
        arrayTwoVal = arrayTwo[idxTwo]
            
        if arrayOneVal > arrayTwoVal:
            idxTwo += 1
        elif arrayTwoVal > arrayOneVal:
            idxOne += 1
        else:
            return [arrayOneVal, arrayTwoVal]
        
        diff = arrayOneVal - arrayTwoVal if arrayOneVal > arrayTwoVal else arrayTwoVal - arrayOneVal
        if diff < small_diff:
                small_diff = diff
                smallDiffRes = [arrayOneVal, arrayTwoVal]
    return smallDiffRes



arrayOne = [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123]
arrayTwo =  [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]

simple_assert(smallestDifference(arrayOne, arrayTwo), [-123, -124])
        


