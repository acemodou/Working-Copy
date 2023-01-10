def reverseWords(s):
        # """
        # Design:
        # Input: s = "the sky is blue"
        # Output: "blue is sky the"
        # blue is sky the   
        # """
        return ' '.join(reversed([word for word in s.split(' ') if word]))
        
s = "the sky is blue"
print(reverseWords(s))
