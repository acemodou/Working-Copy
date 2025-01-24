from validate_answers import simple_assert

def reverseWordsInString(string):
    words = string.split()
    reverseWords = words[::-1]
    return " ".join(reverseWords)
        
    
# def reverseWordsInString(string):
#     revStr = ""
#     word = ""
#     for char in string:
#         if char == " ":
#             revStr = " " + word + revStr
#             word = ""
#         else:
#             word += char 
#     revStr = word + revStr
#     return revStr

# def reverseWordsInString(string):
#     startWord = 0 
#     words = []
#     for idx in range(len(string)):
#         char = string[idx]
#         if char == " ":
#             words.append(string[startWord: idx])
#             startWord = idx 
#         elif string[startWord] == " ":
#             words.append(" ")
#             startWord = idx 
    
#     words.append(string[startWord: ])
#     reverseList(words)
#     return "".join(words)



def reverseWordsInString(string):
    chars = [char for char in string]
    reverseList(chars, 0, len(string)-1)
    
    startOfWord = 0 
    while startOfWord < len(chars):
        endOfWord = startOfWord
        while endOfWord < len(chars) and chars[endOfWord] != " ":
            endOfWord += 1
        reverseList(chars, startOfWord, endOfWord -1)
        startOfWord = endOfWord + 1 
    return "".join(chars)
    
    

def reverseList(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1 




input = "AlgoExpert is the best!"
expected = "best! the is AlgoExpert"
actual = reverseWordsInString(input)
simple_assert(actual, expected)
