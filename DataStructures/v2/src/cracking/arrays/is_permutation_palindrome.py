def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

# def is_permutation_palindrome(s):
#     s = [c.lower() for c in s if c.isalpha()]

#     char_count = {}
#     for char in s:
#         count_freq(char_count, char)

#     odd_count = 0
#     for value in char_count.values():
#         if odd(value):
#             odd_count += 1
#         if odd_count > 1:
#             return False 
#     return True 
   

# def is_permutation_palindrome(s):
#     s = [c.lower() for c in s if c.isalpha()]

#     odd_count = 0
#     char_count = [0] * 26
#     for char in s:
#         x = ord(char) - 96
#         char_count[x] += 1
#         if char_count[x] & 0x1:
#             odd_count -= 1
#         else:
#             odd_count += 1
#     return odd_count <= 1

def is_permutation_palindrome(s):
    s = [c.lower() for c in s if c.isalpha()]

    bit_set = 0
    for c in s:
        bit_set ^= 1 << ord(c)
    return bit_set == 0 or bit_set & (bit_set -1) == 0


def odd(n):
    return n & 0x1 

def count_freq(d, char):
    d[char] = d.get(char, 0) + 1   


   
simple_assert(is_permutation_palindrome("civic"), True)
simple_assert(is_permutation_palindrome("Hello"), False)
simple_assert(is_permutation_palindrome("Tact Coa"), True)


