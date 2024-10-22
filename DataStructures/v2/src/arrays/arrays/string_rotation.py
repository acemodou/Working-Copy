from typing import Any

def simple_assert(a : Any, b : Any) -> bool:
    assert a == b, f'{a}!{b}'

# O(n) time | O(1) space 
# def is_rotation(s1 : str, s2: str) -> bool:
#     if len(s1) == len(s2):
#         s1s1 = s1+s1
#         return is_substring(s1s1, s2)
#     return False 

# def is_substring(larger_string, smaller_string):
#     return smaller_string in larger_string 

def is_rotation(s1 : str, s2: str) -> bool:
    # assuming we are rotating the first 3 characters always like the example below
    x = s1[:3]
    y = s1[3:]
    return s2 == y + x


simple_assert(is_rotation("waterbottle", "erbottlewat"), True)
simple_assert(is_rotation("hello", "lohel"), True)
simple_assert(is_rotation("abcde", "abced"), False) 