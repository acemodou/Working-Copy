from validate_answers import simple_assert

# O(n) time | O(1) space 
def longestPeak(array):
   peak = 0
   idx = 1 
   N = len(array)-1
   
   while idx < N:
       isPeak = array[idx] > array[idx -1] and array[idx] > array[idx + 1]
       if not isPeak:
           idx += 1
           continue
       leftIdx = idx -2 
       while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
           leftIdx -= 1
       
       rightIdx = idx + 2
       while rightIdx <= N and array[rightIdx] < array[rightIdx - 1]:
           rightIdx += 1 
       peak = max(peak, (rightIdx - leftIdx - 1))
       idx = rightIdx
   return peak  
       

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
expected = 6
simple_assert(longestPeak(array), expected)
