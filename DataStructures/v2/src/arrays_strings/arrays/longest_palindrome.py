from validate_answers import simple_assert

def longestPalindromicSubstring(string):
    currentLongest = [0, 1]
    for idx in range(1, len(string)):
        odd =  getPalindrome(string, idx - 1, idx + 1)
        even =  getPalindrome(string, idx - 1, idx )
        longestSubst = max(even, odd, key= lambda x: x[1] - x[0])
        currentLongest = max(currentLongest, longestSubst, key = lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]
        

def getPalindrome(string, leftIdx, rightIdx):
    while leftIdx >=0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx, rightIdx]

simple_assert(longestPalindromicSubstring("abaxyzzyxf"), "xyzzyx")