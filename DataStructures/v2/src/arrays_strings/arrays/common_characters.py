from validate_answers import simple_assert

# What's the time and space cmplexity of this function?

# def commonCharacters(strings):
#     dups =  {}
#     initial_set = set(strings[0])
#     for i in range(1, len(strings)):
#         letter = strings[i]
#         for char in set(letter):
#             if char in initial_set:
#                 update_common(char, dups)
#     return common_in_all(strings, dups)


# O(n * m) time where m is the length of the longest string and O(c) space 
# def commonCharacters(strings):
#     charCount = {}
#     for word in strings:
#         uniqueCharCount = set(word)
#         for uniqueChar in uniqueCharCount:
#             updateCharCount(charCount, uniqueChar)
#     return commonToAll(strings, charCount)

# def updateCharCount(dict, char):
#     if char not in dict:
#         dict[char] = 0
#     dict[char] += 1

# def commonToAll(strings, charCount):
#     common = []
#     for key, val in charCount.items():
#         if val == len(strings):
#             common.append(key)
#     return common


def commonCharacters(strings):
    potentialMatch = getSmallestChar(strings)
    removeNonExistingChar(strings, potentialMatch)
    return list(potentialMatch)

def getSmallestChar(strings):
    smallest = strings[0]
    for i in range(1, len(strings)):
        if len(strings[i]) < len(smallest):
            smallest = strings[i]
    return set(smallest)            

def removeNonExistingChar(strings, potentialMatch):
    for word in strings:
        uniqueChars = set(word)
        for char in list(potentialMatch):
            if char not in uniqueChars:
                potentialMatch.remove(char)
    
        
                

input = ["abc", "bcd", "cbad"]
expected = ["b", "c"]
actual = commonCharacters(input)
actual.sort()
simple_assert(actual, expected)