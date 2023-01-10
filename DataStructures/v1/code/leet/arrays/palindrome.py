import math

def simple_assert(a, b) -> None:
    assert a == b, f'{a}!{b}'

def reversed_int(x):
    # ToDO: handle the case where we get a negative number
    # Limit the digits not to surpass our constraint
    if x < 0 or x > math.pow(2,31):
        return False
    res = 0
    while x > 0:
        res = res * 10 + x % 10
        x = x // 10
    return res
    
def is_palindrome(x:int) ->bool:
    return reversed_int(x) == x

def isPalindrome(x:int) -> bool:
    # More efficient 
    div = 1
    while x > div * 10:
        div *= 10
    while x:
        if x % 10 != x // div: return False 
        x = (x % div ) // 10 
        div /= 100
    return True  


simple_assert(isPalindrome(121), True)
simple_assert(isPalindrome(-121), False)
simple_assert(isPalindrome(10), False)