def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

def one_edit_away(s1 : str, s2 : str) -> bool:
     if abs(len(s1) - len(s2)) > 1:
          return False 
     
     if len(s1) == len(s2):
          return _one_edit_replace(s1, s2) 
     if len(s1) > len(s2):
          return _one_edit_insert(s1, s2) 
     return _one_edit_insert(s1, s2)


def _one_edit_replace(str1 : str, str2: str) -> bool:
     found_diff = 0 
     for i in range(len(str1)):
          if str1[i] != str2[i]:
               if found_diff:
                    return False 
               found_diff = True 
     return True 


def _one_edit_insert(str1: str, str2: str) -> bool:
     idx1, idx2 = 0, 0

     while idx1 < len(str1) and idx2 < len(str2):
          if str1[idx1] != str2[idx2]:
               if idx1 != idx2:
                    return False 
               idx1 += 1
          else:
               idx1 += 1
               idx2 += 1
     return True 
           
        


simple_assert(one_edit_away("pale", "ple"), True)
simple_assert(one_edit_away("pales", "pale"), True)
simple_assert(one_edit_away("pale", "bale"), True)
simple_assert(one_edit_away("pale", "bae"), False)