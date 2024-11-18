def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

# O(n) time | O(n) space 
# def urlify(string: str, length: int) -> str:
#     string_edit = string.strip()
#     result = ''.join([char if char  != ' ' else '%20' for char in string_edit ])
#     return result 

# O(n) time | O(n) space 
def urlify(string: str, length: int) -> str:
    string_edit = string.strip()

    count_spaces = 0
    for char in string_edit:
        if char == ' ':
            count_spaces += 1
    
    res_len = length + (2 * count_spaces)
    result_string = [""] * res_len 
    
    for char_idx in reversed(range(length)):
        if string[char_idx] == ' ':
            result_string[res_len - 1] = '0'
            result_string[res_len - 2] = '2'
            result_string[res_len - 3] = '%'
            res_len -= 3
        else:
            result_string[res_len-1] = string[char_idx]
            res_len -= 1
    return "".join([char for char in result_string])

            
        
    

actual = urlify("Mr John Smith  ", 13)
expected = "Mr%20John%20Smith"
simple_assert(actual, expected)