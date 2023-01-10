from typing import List 

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

# Modou's solution

def permute(nums: List[int], k: int) -> List[List[int]]:
  #TODO: Initialize static array as length of numlist 
  #TODO: Initialize a result array as static 
  #TODO: Iterate over the array and check if the current index is 0. We copy this in place 
  #TODO: Backtrack and then set the current index of the array as 0 then interate 
  # permute.arr = [0]* len(nums)
  # permute.result = [0] * len(nums)
  #When does recursion knows i hit my max? 
  
  if k == len(nums):
    return res 
  else:
    for i in range(len(nums)):
      if arr[i] == 0:
        res[k] = nums[i]
        arr[i] = 1
        permute(nums, k+1)
        arr[i] = 0

def permute_1(nums: List[int], low: int) -> List[List[int]]:
  perm =[]
  if low == len(nums)-1:
      perm.append(nums.copy()) #Snapshot current nums
  else:
    for i in range(low, len(nums)):
      nums[i], nums[low] = nums[low], nums[i]
      perm.extend(permute_1(nums, low+1))
      nums[i], nums[low] = nums[low], nums[i]
  return perm 

for input, expected in [
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]),
    ([0,1], [[0,1],[1,0]]),
    ([1], [[1]]),
]:

  output = permute_1(input, 0)
  assert output == expected, f'{output} not in  {expected}'
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.perm = []
        self.perm_sol(nums, 0)
        return self.perm 
        
    def perm_sol(self, nums: List[int], low: int) -> List[List[int]]:
        if low == len(nums)-1:
            self.perm.append(nums.copy())
        else:
            for i in range(low, len(nums)):
                nums[i], nums[low] = nums[low], nums[i]
                self.perm_sol(nums, low+1)
                nums[i], nums[low] = nums[low], nums[i]
# def permute(nums: List[int], k: int) ->List[int]:

#     if k == len(nums):
#         return res
#     else:
#         for i in range(len(nums)):
#             if arr[i] == 0:
#                 res[k] = nums[i]
#                 arr[i] = 1
#                 permute(nums, k+1)
#                 arr[i] = 0

# if __name__ == '__main__':
#     # bitwiseDuplicates('finding')
#     # permute([1,2,3], 0)
#     str1 = ['a','b','c']
#     perm1(str1, 0, len(str1)-1)






