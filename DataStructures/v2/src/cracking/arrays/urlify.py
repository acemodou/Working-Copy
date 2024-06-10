def simple_assert(a, b):
    assert a == b, f'{a}!{b}'


def urlify(strs, length):
    number_of_spaces = 0
    for i in range(length):
        if strs[i] == ' ':
            number_of_spaces += 1
    
    urlify_space = length  + number_of_spaces * 2
    if len(strs) < urlify_space:
        extended_space =  urlify_space - len(strs)
        strs.extend([''] * extended_space)
    
    for i in reversed(range(length)):
        if strs[i] == " ":
            strs[urlify_space -1] = '0'
            strs[urlify_space -2] = '2'
            strs[urlify_space -3] = '%'
            urlify_space -= 3 
        else:
            strs[urlify_space -1] = strs[i]
            urlify_space -= 1
    return "".join(strs)


input_strs = list("Mr John Smith   ")


simple_assert(urlify(input_strs, 13), "Mr%20John%20Smith")