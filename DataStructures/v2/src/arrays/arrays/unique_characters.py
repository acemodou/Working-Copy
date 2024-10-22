def simple_assert(a, b):
    assert a == b, f'{a}!{b}'  

# O(n) time | O(1) space 
# def is_unique(string : str) -> bool:
#     """
#     Implement an algorithm to determine if a string has all unique characters. 
#     Without using additional DS. A
#     finding
#     [1, 2, 1, 1, 1] 
#     """     
#     unique_chars = [0] * 26 
#     for char in string:
#         ascii_repr = ord(char) - 97
#         if unique_chars[ascii_repr] == 1:
#             return False  
#         unique_chars[ascii_repr] += 1
#     return True 


def is_unique(string : str) -> bool:
    """
    bit_masking : Turn on the bit but check if the bit is already on
    Return False if it is already on  
    """                                                                  
    checker = 0 
    for i in range(len(string)):
        val = ord(string[i]) - 97 
        if checker & (1 << val) > 0:
            return False 
        checker |= (1 << val)  
    return True
    

expected = False  
actual = is_unique("finding")
simple_assert(actual, expected) 
    