def brute_force_search(text: str, pattern: str) -> int:
    for i in range(len(text) - len(pattern)+1):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break 
        if j+1 == len(pattern):
            return i 
    return -1 
        

assert brute_force_search("abcdef", "def") == 3 
assert brute_force_search("abcdef", "xyz") == -1
