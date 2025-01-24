from validate_answers import validate_answers

# O(n^2) time | O(1) space: Its adaptive and stable 
def bubble_sort(array):
    for i in range(len(array)):
        is_sorted  = True 
        for j in range(len(array) - i - 1):
            if array[j+1] < array[j]:
                array[j], array[j+1] = array[j+1], array[j]
                is_sorted = False
        if is_sorted:
            return array
    return array
            
validate_answers(bubble_sort)
