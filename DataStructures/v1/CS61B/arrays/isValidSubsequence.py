def simpleAssert(a, b):
    assert a == b, f'{a}!{b}'

def isValidSubsequence(array, sequence):
    # Write your code here.
    j = 0
    for val in array:
        if val == sequence[j]:
            j += 1
            if j == len(sequence):
                return True 
    return False 




simpleAssert(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]), True)