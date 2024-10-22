def simple_assert(a, b):
    assert a == b, f'{a}!{b}'  

# O(n) time | O(n) space 
# def is_palindrome(strs : str) -> bool:
#     return strs == strs[::-1] 

# O(n) time | O(1) space 
def is_palindrome(strs : str) -> bool:
    i = 0
    j = len(strs) - 1
    while i != j:
        if strs[i] != strs[j]:
            return False 
        i += 1
        j -= 1
    return True 


expected = True 
actual = is_palindrome("abcdcba")
simple_assert(actual, expected)