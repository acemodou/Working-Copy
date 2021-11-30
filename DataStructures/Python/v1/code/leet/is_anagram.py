import pprint

from collections import Counter

def simple_assert(a, b):
    assert a == b, f'Assertion {a} != {b}'

def is_anagram(str1: str, str2: str) ->bool:
    '''
    Time is O(n log n) time, O(n) space
    '''
    return sorted(str1) == sorted(str2)

# Test cases 
simple_assert(is_anagram('anagram', 'nagaram'), True)
simple_assert(is_anagram('rat', 'car'), False)
simple_assert(is_anagram('aaaaaa', 'a'), False)
simple_assert(is_anagram('a', 'aaaaaa'), False)

def is_anagram_2(str1: str, str2: str) -> bool:
    '''
    Time is O(n) time, O(n) space
    '''
    return Counter(str1) == Counter(str2)

simple_assert(is_anagram_2('anagram', 'nagaram'), True)
simple_assert(is_anagram_2('rat', 'car'), False)
simple_assert(is_anagram_2('aaaaaa', 'a'), False)
simple_assert(is_anagram_2('a', 'aaaaaa'), False)

def is_anagram_3(str1: str, str2: str) -> bool:
    '''
    Time is O(n) time, O(n) space
    '''
    if len(str1) != len(str2):
        return False
    hash_table = {}
    for char in str1:
        hash_table.setdefault(char, 0)
        #hash_table[char] = hash_table[char] + 1 This is the same as below 
        hash_table[char] = hash_table.get(char, 0) + 1
    for char in str2:
        hash_table[char] = hash_table.get(char, 0) - 1
    for _, values in hash_table.items():
        if values < 0:
            return False
    return True 
      
simple_assert(is_anagram_3('anagram', 'nagaram'), True)
simple_assert(is_anagram_3('rat', 'car'), False)
simple_assert(is_anagram_3('aaaaaa', 'a'), False)
simple_assert(is_anagram_3('a', 'aaaaaa'), False)

def is_anagram_4(str1: str, str2: str) -> bool:
    '''
    Time is O(n) time, O(n) space
    '''
    if len(str1) != len(str2):
        return False 
    h = 0
    y = 0
    for char in str1:
        x = 1
        x = x << (ord(char) - 97)
        h = h | x 
    for char in str2:
        x = 1
        x = x << (ord(char) - 97)
        y = y | x 
    return h == y 

simple_assert(is_anagram_4('anagram', 'nagaram'), True)
simple_assert(is_anagram_4('rat', 'car'), False)
simple_assert(is_anagram_4('aaaaaa', 'a'), False)
simple_assert(is_anagram_4('a', 'aaaaaa'), False)
# simple_assert(is_anagram_4('aacc', 'ccac'), False) #This doesn't work 

def count_values(msg):
    count = {}
    for chars in msg:
        count.setdefault(chars, 0)
        count[chars] = count[chars] + 1
    pprint.pprint(count) 

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count_values(message)