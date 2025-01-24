from validate_answers import simple_assert

# O(N^2) time | O(1) space 
# def firstNonRepeatingCharacter(string):
#     for i in range(len(string)):
#         found_dup  = False  
#         for j in range(len(string)-1):
#             if string[i] == string[j] and i != j:
#                 found_dup = True 
#         if not found_dup:
#             return i 
#     return -1 

def firstNonRepeatingCharacter(string):
    charCount = {}
    for char in string:
        if char not in charCount:
            charCount[char] = 0
        charCount[char] += 1
    return nonReaptingIdx(charCount, string)
      
def nonReaptingIdx(charCount, string):
    
    for i in range(len(string)):
        char = string[i]
        if charCount[char] == 1:
            return i 
    return -1 


input = "abcdcadbf"
expected = 8
actual = firstNonRepeatingCharacter(input)
simple_assert(actual, expected)