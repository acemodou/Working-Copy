from validate_answers import simple_assert


def runLengthEncoding(string):
    currentRunLength = 1
    encoding = []
    i = 0
    while i < len(string)-1:
        if string[i] != string[i+1] or currentRunLength == 9:
            encoding.append(f'{currentRunLength}{string[i]}')
            currentRunLength = 1
        else:
            currentRunLength += 1
        i += 1 
    encoding.append(f'{currentRunLength}{string[i]}')
    encode = stringify(encoding)
    return encode
        
def stringify(array):
    return "".join(array)

string = "AAAAAAAAAAAAABBCCCCDD"
expected = "9A4A2B4C2D"
actual = runLengthEncoding(string)
simple_assert(actual, expected)
