def simple_assert(a, b):
    assert a == b, f'{a}!{b}'
    
def oneEdit(stringOne, stringTwo):
    if abs(len(stringOne) - len(stringTwo)) > 1:
        return False 
    if len(stringOne) == len(stringTwo):
        return one_replace_away(stringOne, stringTwo)
    else:
        return one_insert_or_remove_away(stringOne, stringTwo)
  

def one_insert_or_remove_away(str1, str2):
    idxOne, idxTwo = 0, 0 
    lenOne = len(str1)
    lenTwo = len(str2)
    found = False 
    while idxOne < lenOne and idxTwo < lenTwo:
        if str1[idxOne] != str2[idxTwo]:
            if found:
                return False 
            if lenOne > lenTwo:
                idxOne += 1
            else:
                idxTwo += 1
            found = True
            continue 
        idxOne += 1
        idxTwo += 1
    return True 
        

def one_replace_away(str1, str2):
    found = False 
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if found:
                return False 
            found = True 
    return True                        

list_tuple =[("pale", "ple"), ("pales", "pale"), ]
for values in list_tuple:
    str1, str2 = values
    actual = True 
    expected = oneEdit(str1, str2)
    simple_assert(actual, expected)

actual = False 
expected = oneEdit("pale", "bake")
simple_assert(actual, expected)