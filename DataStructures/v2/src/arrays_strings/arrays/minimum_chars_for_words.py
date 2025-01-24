from validate_answers import simple_assert
def minimumCharactersForWords(words):
    maxCharacterFrequencies = {}
    for word in words:
        currFreq = countCharFrequencies(word)
        updateMaxFreq(maxCharacterFrequencies , currFreq)
    
    return maxArrayFromCharacterFreq(maxCharacterFrequencies)

        
def countCharFrequencies(word):
    characterFreq = {}
    for char in word:
        if char not in characterFreq:
            characterFreq[char] = 0 
        characterFreq[char] += 1
    return characterFreq

def updateMaxFreq(maxFreq, currFreq):
    for key in currFreq:
        freq = currFreq[key]
        
        if key not in maxFreq: 
            maxFreq[key] = freq 
        elif key in maxFreq:
            maxFreq[key] = max(freq, maxFreq[key])
            
def maxArrayFromCharacterFreq(maxFreq):
    result = []
    for key, value in maxFreq.items():
        for _ in range(value):
            result.append(key)
    return result 
    



input = ["this", "that", "did", "deed", "them!", "a"]
expected = ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
actual = minimumCharactersForWords(input)
simple_assert(actual, expected)