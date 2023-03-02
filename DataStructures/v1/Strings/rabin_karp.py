
def rabinKarp(text: str, pattern: str) -> int:
    N = len(text)
    M = len(pattern)
    if N < M:
        return -1
    p = 31 
    hash_text = 0
    hash_pattern = 0 
    for i in range(M):
        hash_pattern = (hash_pattern * p + ord(pattern[i]) % (1000000007))
        hash_text = (hash_text * p + ord(text[i]) % (1000000007))
    for i in range(N-M+1):
        if hash_text == hash_pattern and text[i: i+M] == pattern:
            return i 
        if i < N-M:
            hash_text = ((hash_text - ord(text[i]) * p**(M-1)) * p + ord(text[i+M])) % (10**9 + 7)
    return -1 


assert rabinKarp("aaaaab", "aab") == 3
assert rabinKarp("ababcabcabababd", "ababd") == 10
assert rabinKarp("aaaaab", "baa") == -1
