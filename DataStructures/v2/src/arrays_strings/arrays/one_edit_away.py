def simple_assert(a, b):
    assert a == b, f'{a}!{b}'
    
def one_edit_away(str1 : str, str2 : str) -> bool:
    if len(str1) != len(str2):
        return one_insert_or_remove_away(str1, str2)
    return one_replace_away(str1, str2)
  

def one_insert_or_remove_away(str1, str2):
    idx1 = 0 
    idx2 = 0
    found_diff = False 
    
    while idx1 < len(str1) and idx2 < len(str2):
        if str1[idx1] == str2[idx2]:
            idx1 += 1
            idx2 += 1
        else:
            if found_diff:
                return False 
            found_diff = True 
            if len(str1) > len(str2):
                idx1 += 1
            else:
                idx2 += 1
    return True 
        
    

def one_replace_away(str1, str2):
    found_diff = False 
    
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if found_diff:
                return False 
            found_diff = True 
    return True                          

list_tuple =[("pale", "ple"), ("pales", "pale"), ("pale", "bale")]
for values in list_tuple:
    str1, str2 = values
    actual = True 
    expected = one_edit_away(str1, str2)
    simple_assert(actual, expected)


actual = False 
expected = one_replace_away("pale", "bake")
simple_assert(actual, expected)