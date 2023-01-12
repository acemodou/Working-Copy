def reverseWords(s):
        """
        Design:
        Input: s = "the sky is blue"
        Output: "blue is sky the"
        blue is sky the   
        """
        copy_str = ""
        final_str = ""
        
        for strs in range(len(s)-1, -1, -1):
            if s[strs] != " ":
                copy_str += s[strs]
            final_str += str(reversed(copy_str))
            final_str += " "
        s = final_str[::]
        return s 

s = "the sky is blue"
print(reverseWords(s))
