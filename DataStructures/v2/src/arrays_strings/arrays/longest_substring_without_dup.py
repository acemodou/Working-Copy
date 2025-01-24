from validate_answers import simple_assert

def longestSubstringWithoutDuplication(string):
    
    startIdx = 0 
    lastSeen = {}
    subStr = [0, 1]
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char]+1)
        if i + 1 - startIdx > subStr[1] - subStr[0]:
            subStr = [startIdx, i+1]
        lastSeen[char] = i 
    return string[subStr[0] : subStr[1]]
                


simple_assert(longestSubstringWithoutDuplication("clementisacap"), "mentisac")
