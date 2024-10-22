def simple_assert(a, b):
    assert a == b, f'{a}!{b}'


# O(nlog(n)) time  | O(n) space 
# def is_palindrome(string1, string2):
#     return sorted(string1) == sorted(string2)

# O(n + m) time | O(1) space 
# def is_palindrome(string1, string2):
#     if len(string1) != len(string2):
#         return False 
    
#     counted_words = [0] * 26
    
#     for letter in string1:
#         counted_words[ord(letter) - 97] += 1
    
#     for letter in string2:
#         counted_words[ord(letter) - 97]  -= 1
    
#     for idx in range(26):
#         if counted_words[idx] != 0:
#             return False 
#     return True 


# O(n + m) time | O(1)
def is_palindrome(string1, string2):
    checker = 0 
    for char in string1:
        checker |= 1 << (ord(char) -97)
    
    for char in string2:
        if checker & (1 << ord(char) - 97) == 0:
            return False 
    return True 
   

s1 = 'rac'
s2 = 'cars'
expected = True 
actual = actual = is_palindrome(s1, s2)
simple_assert(expected, actual)
