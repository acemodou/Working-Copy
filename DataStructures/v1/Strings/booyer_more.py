def boyer_moore(text, pat):
    badMatchTable = {}
    """ Store the position of the last occurrence of each character 
        in the pattern 
    """
    for i in range(len(pat)):
        badMatchTable[pat[i]] = i 

    i = 0
    while i <= (len(text) - len(pat)):
        skip = 0
        for j in reversed(range(len(pat))):
            if pat[j] != text[i+j]:
                skip = max(1, j - badMatchTable.get(text[i+j], 0))
                i += skip 
                break 
        if skip == 0:
            return i 
    return -1 


assert boyer_moore("ababcabcabababd", "ababd") == 10
