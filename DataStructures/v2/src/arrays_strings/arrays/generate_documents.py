from valid_sequence import simple_assert


ASCII_TABLE_= 128 

# O(n + m) time | O(1) space 
def generateDocument(characters, document):
    list_of_docs = [0] * ASCII_TABLE_
    for char in characters:
        list_of_docs[ord(char)] += 1
    for w in document:
        list_of_docs[ord(w)] -= 1
    
    for i in range(ASCII_TABLE_):
        if list_of_docs[i] < 0:
            return False 
    return True 
        




characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
expected = True
actual = generateDocument(characters, document)
simple_assert(actual, expected)