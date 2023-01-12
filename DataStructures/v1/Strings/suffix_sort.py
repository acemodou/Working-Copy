def simple_assert(a, b):
    assert a == b, f"{a}!{b}"

class SuffixArray:
    def __init__(self, S):
        self.N = len(S)
        self.suffixes = [0] * self.N 
        for i in range(self.N):
            self.suffixes[i] = S[i::]
        self.suffixes.sort()
    
    def length(self):
        return self.N
    
    def select(self,i):
        return self.suffixes[i]
    
    def lcp(self, i):
        return self.longest_comom_prefix(self.suffixes[i], self.suffixes[i-1])

    def longest_comom_prefix(self, str1, str2):
        N = min(len(str1), len(str2))
        for i in range(N):
            if ord(str1[i]) != ord(str2[i]):
                return i 
        return N 
    
    def longest_repeated_string(self):
        lrs = ""
        for i in range(self.N-1):
            length = self.longest_comom_prefix(self.suffixes[i], self.suffixes[i+1])
            if length > len(lrs):
                lrs = self.suffixes[i][0:length:]
        return lrs 
    
    def rank(self):
        # Understand how rank works then implement it 
        pass


if __name__ == "__main__":
    s = SuffixArray("aacaagtttacaagc")
    print(s.longest_repeated_string())
# simple_assert(longest_comom_prefix("acctgttaac", "accgttaa"), 3)
