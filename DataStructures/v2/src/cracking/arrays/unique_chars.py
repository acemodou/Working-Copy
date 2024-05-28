def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

# O(N^2) time |  and O(1) space
# def is_unique(strings):
#     for i in range(len(strings)-1):
#         for j in range(i+1, len(strings)):
#             if strings[i] == strings[j]:
#                 return False 
#     return True  

# O(N) time | O(N) space
# def is_unique(strings):
#     return len(set(strings)) == len(strings)


# O(1) time: assuming is all ascii and O(1) space 
# def is_unique(strings):
#     char_set = [0] * 128
#     for char in strings:
#         char_val = ord(char) - 97
#         if char_set[char_val]:
#             return False
#         char_set[char_val] = True 
#     return True 

#O(1) time | O(1) space : Reduce the space by just the size of checker
def is_unique(strings):
    checker = 0
    for char in strings:
        val = ord(char) - 97
        # Check if the bit is on 
        if checker & (1 << val) > 0:
            return False 
            # Turn that bit on 
        checker |= (1 << val)
    return True  

simple_assert(is_unique("hello"), False)
simple_assert(is_unique("world"), True)
simple_assert(is_unique("copilot"), False)
simple_assert(is_unique(""), True)
