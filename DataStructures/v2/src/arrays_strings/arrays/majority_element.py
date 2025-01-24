from validate_answers import simple_assert
# def majorityElement(array):
#     majority = {}
#     halfOfElement = len(array) // 2
#     for num in array:
#         updateMajority(majority, num)
    
#     majorityElement = max(majority, key=majority.get)
#     return majorityElement

# def updateMajority(majority, num):
#     if num not in majority:
#         majority[num] = 0
#     majority[num] += 1

def majorityElement(array):
    majority = 0
    count = 0 
    for num in array:
        if count == 0:
            majority = num 
        if num != majority:
            count -= 1
        else:
            count += 1
    return majority


input = [1, 2, 3, 2, 2, 1, 2]
expected = 2
actual = majorityElement(input)
simple_assert(actual, expected)