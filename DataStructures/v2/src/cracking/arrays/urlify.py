
# def urlify(strs, true_length):
#     strings = strs.strip()
#     print(strings)

#     new_urlify = [char if char != ' ' else '%20' for char in strings]
#     return "".join(new_urlify)

# def urlify(strs, true_length):
#     strings = strs.strip()
#     strs = strings.replace(' ', '%20')
#     return strs 


# def urlify(strs, true_length):
#     strings = strs.strip()
#     print(strings)

#     new_urlify = [char if char != ' ' else '%20' for char in strings]
#     return "".join(new_urlify)

def urlify(strs, true_length):
    space_count = 0 
    for i in range(true_length):
        if strs[i] == ' ':
            space_count += 1
    
    index = true_length + space_count * 2
    strings = list(strs)
    if len(strings) < index:
        strings.extend([' '] * (index - len(strings)))
    
    for i in reversed(range(true_length)):
        if strings[i] == ' ':
            strings[index - 1] = '0'
            strings[index - 2] = '2' 
            strings[index - 3] = '%'
            index -= 3 
        else:
            strings[index - 1] = strings[i] 
            index -= 1 
    return ''.join(strings)
    

print(urlify("Mr John Smith  ", 13))