from typing import List

def simple_assert(a, b):
    assert a == b, f'Assertion {a} == {b} failed'

def longestCommonPrefix(strs: List[str]) -> str:
    '''
    '''
    h = 0
    prefix = ''
    plen = len(strs)
    if plen == 0:
        return ''
    elif plen == 1:
        return strs[0]
    else:
        for char in strs[0]:
            x = 1
            x = x << (ord(char) -97)
            h = h | x

        temp_len = (plen -1)
        for char in strs[temp_len]:
            x = 1
            x = x << (ord(char) -97)
            if x & h > 0 and (plen - temp_len) !=0:
                prefix += char
            else:
                temp_len -=1

    if len(prefix) > 0:
        return prefix
    return ''

def toString(str):
    return ''.join(str)

def longestCommonPrefix(strs: List[str]) -> str:
    '''
    ['flower', 'flow', 'flight']
    zip(*str) = {'f', 'f', 'f'}, {'l', 'l', 'l'}, {'o', 'o', 'i'}
    check the len(set(chars)) == 1
    str += fl 
    otherwise
       break 
    return str
    Time is O(zip's complexity), O(n) space
    '''
    str = []
    for prefix in zip(*strs):
        if len(set(prefix)) == 1:
            str.append(prefix[0])
        else:
            break 
    return toString(str)

simple_assert(longestCommonPrefix(["flower","flow","flight"]), 'fl')
simple_assert(longestCommonPrefix(["dog","racecar","car"]), '')


