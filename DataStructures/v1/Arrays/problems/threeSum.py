def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    output = []
    for idx in range(len(array)):
        start = idx + 1
        end = len(array)-1
        while start < end:
            first_value = array[idx]
            second_value = array[start]
            third_value = array[end]
            if first_value + second_value + third_value == targetSum:
                output.append([first_value, second_value, third_value])
                start += 1
                end -= 1
            elif first_value + second_value + third_value < targetSum:
                start +=1 
            else:
                end -=1
            
    return output


simple_assert(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0),[[-8, 2, 6],[-8,3,5],[-6,1,5]])
