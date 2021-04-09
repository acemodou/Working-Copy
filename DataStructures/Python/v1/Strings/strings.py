def togglestrings(str):
    '''
    If character is Caps we flip, if it's small we make cap
    '''
    str1 = ''
    for i in str:
        if i >= chr(65) and i <= chr(90):
            i = chr(ord(i) + 32)
            str1 += i 
        else:
            i = chr(ord(i) - 32)
            str1 += i 
    return str1 
            

def revStrings(str):
    rev_str = ''
    ln = len(str)
    for i in range(ln-1, -1,-1):
        rev_str += str[i] 
    return rev_str

def palindrome(str):
    if str == revStrings(str):
        return 'Is Palindrome!'

def countDuplicates(str):
    hash_table = dict.fromkeys(range(26), 0)
    str1 = ''
    for i in range(len(str)):
        hash_table[str[i]] = hash_table.get(str[i], 0) + 1
    for keys, values in hash_table.items():
        if values > 1:
            str1 += keys
    return str1

def bitwiseDuplicates(str):
    str1 = ''
    h = 0
    for i in str:
        x = 1
        x =  x << (ord(i) - 97)
        if x & h > 0:
            str1 += i 
        else:
            h = x | h
    return str1
           
def anagram(str1, str2):
    if len(str1) != len(str2):
        return 'is not anagram'
    hash_table = dict.fromkeys(range(26), 7)
    for i in range(len(str1)):
        hash_table[str1[i]] = hash_table.get(str1[i], 0) + 1
    for i in range(len(str2)):
        hash_table[str2[i]] = hash_table.get(str2[i], 0) - 1
    for _ , values in hash_table.items():
        if values < 0:
            return 'is not anagram'
    return 'is anagram'

def toString(str):
    return ''.join(str)

arr = [0,0,0]
res = ['','','']
def perm(str, k):
    if k == 3:
        print(toString(res))
    else:
        for i in range(len(str)):
            if arr[i] == 0:
                res[k] = str[i]
                arr[i] = 1
                perm(str, k+1)
                arr[i] = 0
    return toString(res)
  
def perm1(str, low, high):
    if low == high:
        print(toString(str))
    else:
        for i in range(low, high + 1):
            str[i], str[low] = str[low], str[i]
            perm1(str, low + 1, high)
            str[i], str[low] = str[low], str[i] # backtracking 









