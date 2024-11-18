from validate_answers import simple_assert

HASH_KEY = 26

# O(n) time | O(n) space 
# def caesarCipherEncryptor(string, key):
#     new_key = key % HASH_KEY
#     encrypt = []
#     for letter in string:
#         nl = getNewLetter(letter, new_key)
#         print(nl)
#         encrypt.append(nl)
#     return "".join(encrypt)

def caesarCipherEncryptor(string, key):
    new_key = key % 26 
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    encode = []
    for letter in string:
        new_letter = ord(getNewLetter(letter, new_key)) - 97
        encode.append(alphabets[new_letter])
    return "".join(encode)

def getNewLetter(letter, key):
    new_letter =  ord(letter) + key
    return  chr(new_letter) if new_letter <= 122 else chr(96 + new_letter % 122)

    




simple_assert(caesarCipherEncryptor("xyz", 2), "zab")
    