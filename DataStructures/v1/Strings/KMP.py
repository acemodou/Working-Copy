from typing import List 
def KMP(text : str, pat: str):
    # Preprocess the pattern (calculate lps[] array)
    M = len(pat)
    lps = [0] * M 
    i, j = 0, 0

    computeLPSArray(pat, M, lps)

    while i < len(text):
        if text[i] == pat[j]:
            i += 1 
            j += 1
        
        if j == len(pat):
            return i - j 
        
        elif i < len(text) and pat[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def computeLPSArray(pat, M, lps):
    lps[0] = 0
    i = 1
    j = 0
    while i < M:
        if pat[j] == pat[i]:
            j += 1
            lps[i] = j
            i += 1
        
        else:
            if j != 0:
                j = lps[j-1]
            
            else:
                lps[i] = 0
                i += 1
    return lps 

assert KMP("ababcabcabababd", "ababd") == 10
