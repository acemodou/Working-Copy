def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

# O(Nlog(n)) time | O(n) space 
# def permutation(str1, str2):
#     if len(str1) != len(str2):
#         return False 
#     return sorted(str1) == sorted(str2)

# O(Nlog(n)) time | O(n) space 
def permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    # Initialize a list to count character frequencies 
    char_count = [0] * 26 
    
    # Count the frequency of each character in the first string
    for char in str1:
        val = ord(char) - 97
        char_count[val]+= 1
    
    # Decrease the frequency based on the second string
    for char in str2:
        val = ord(char) - 97
        char_count[val] -= 1
        if char_count[val] < 0:
            return False 
    return True 


     



# Test cases for permutation function
simple_assert(permutation('abc', 'cba'), True)
simple_assert(permutation('abc', 'cab'), True)
simple_assert(permutation('abc', 'def'), False)
simple_assert(permutation('abc', 'abcd'), False)
simple_assert(permutation('abc', 'ab'), False)