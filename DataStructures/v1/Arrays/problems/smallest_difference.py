
from unit_test import simple_assert

def smallestDifference(arrayOne, arrayTwo):
    closest_to_zero = float("inf")
    arrayOne.sort()
    arrayTwo.sort()
    idx_one= 0 
    idx_two = 0
    output = [0, 0]
    while idx_one  < len(arrayOne) and idx_two < len(arrayTwo):
        first_num, second_num = arrayOne[idx_one], arrayTwo[idx_two]
        running_sum = 0
        if first_num > second_num:
            running_sum = first_num - second_num
            idx_two +=1
        elif second_num > first_num:
            running_sum = second_num - first_num
            idx_one += 1
        else:
            return [first_num, second_num]
        if running_sum < closest_to_zero:
            closest_to_zero = running_sum
            output = [first_num, second_num]
    
    return output

    



simple_assert(smallestDifference([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17]),[28, 26])
simple_assert(smallestDifference([-1, 5, 10, 20, 3],[26, 134, 135, 15, 17]),[20, 17])
simple_assert(smallestDifference([10, 0, 20, 25],[1005, 1006, 1014, 1032, 1031]),[25, 1005])
