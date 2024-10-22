def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

# O(n) time | O(n) space 
# def permutation_palindrome(phrase : str) -> bool:
#     char_count = {}
#     for char in phrase:
#         if char != ' ':
#             char_count[char] = char_count.get(char, 0) + 1
            
#     found_odd = False 
#     for _, v  in char_count.items():
#         if v % 2 == 1:
#             if found_odd : 
#                 return False 
#             found_odd  = True 
#     return True 


def is_odd(value: int):
    return value & 1

# O(n) time  | O(1) space 
# def permutation_palindrome(phrase : str) -> bool:
#     table = [0] * (ord('z') - ord('a') + 1)
#     odd_count = 0 
    
#     for char in phrase:
#         x = get_char_num(char)
#         if x != -1:
#             table[x] += 1
#             if is_odd(table[x]):
#                 odd_count += 1
#             else:
#                 odd_count -= 1
#     return odd_count <= 1   

# def get_char_num(char):
#     val = ord(char.lower())
#     if ord('a')  <= val <= ord('z'):
#         return val - ord('a')
#     return -1 

def permutation_palindrome(phrase : str) -> bool:
    bit_vector = create_bit_vector(phrase)
    return bit_vector == 0 or check_exactly_one_bit_set(bit_vector)


def create_bit_vector(phrase):
    bit_vector = 0 
    for char in phrase:
        char_num = get_char_num(char)
        bit_vector = toggle_bit_vector(char_num, bit_vector)
    return bit_vector

def check_exactly_one_bit_set(bit_vector):
    return bit_vector & (bit_vector - 1) == 0

def get_char_num(char):
    value = ord(char.lower())
    if ord('a') <= value <= ord('z'):
        return value - ord('a')
    return -1 

def toggle_bit_vector(index, bit_vector):
    if index < 0:
        return bit_vector
    mask = 1 << index
    if bit_vector & mask == 0:
        bit_vector |= mask 
    else:
        bit_vector &= ~mask 
    return bit_vector

actual = True 
expected = permutation_palindrome("tact coa")
simple_assert(actual, expected)




