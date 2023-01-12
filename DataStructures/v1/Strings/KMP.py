from typing import List 
def KMP(text : str, pat: str):
    # Preprocess the pattern (calculate lps[] array)
    M = len(pat)
    lps = [0] * M 

    computeLPSArray(pat, M, lps)

def computeLPSArray(pat : str, M : int, lps :List[int]):
    lps[0] = 0 # lps[0] is always 0
    len = 0 # length of the previous longest prefix suffix
    i = 1 

    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len 
            i += 1
        else:
            # This is tricky. Consider the example.
	        # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len -1]
            else:
                lps[i] = 0
                i += 1
            

        
