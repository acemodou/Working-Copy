from validate_answers import simple_assert

def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    firstYPos = getCountsAndFirstYPos(newPattern, counts)
    
    if counts['y'] != 0:
        for xlen in range(1, len(string)):
            ylen = (len(string) - counts['x'] * xlen) / counts['y']
            if ylen <= 0 or ylen % 1 != 0:
                continue
            lenOfY = int(ylen) 
            yidx = firstYPos * xlen 
            x = string[:xlen]
            y = string[yidx: yidx + lenOfY]
            potentialMatch = list(map(lambda char: x if char == "x" else y, newPattern))
            if string == "".join(potentialMatch):
                return [x, y] if not didSwitch else [y, x]
    
    lenOfX = len(string) / counts['x']
    if lenOfX % 1 == 0:
        lenOfX = int(lenOfX)
        x = string[:lenOfX]
        potentialMatch = list(map(lambda char: x, newPattern))
        if string == "".join(potentialMatch):
            return [x, ""] if not didSwitch else ["", x]
    return []
        

def getNewPattern(pattern):
    patternLetters = list(pattern)
    if patternLetters[0] == 'x':
        return patternLetters
    return list(map(lambda char: 'x' if char == 'y' else 'y', patternLetters))

def getCountsAndFirstYPos(newPattern, count):
    firstYPos = None
    for pos,  char in enumerate(newPattern):
        count[char] += 1
        if char == 'y' and firstYPos is None:
            firstYPos = pos 
    return firstYPos

simple_assert(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"),["go", "powerranger"])