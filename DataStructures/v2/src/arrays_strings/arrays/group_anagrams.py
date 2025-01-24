# def groupAnagrams(words):
#   if len(words) == 0:
#       return []

#   sortedWords = ["".join(sorted(w)) for w in words]
#   indices = [i for i in range(len(words))]
#   indices.sort(key=lambda x: sortedWords[x]) 
  
#   anagrams = []
#   similarAnagrams = []
#   currAnagram = sortedWords[indices[0]]
  
#   for idx in indices:
#       word = words[idx]
#       sortedWord = sortedWords[idx]
      
#       if sortedWord == currAnagram:
#           similarAnagrams.append(word)
#           continue
      
#       anagrams.append(similarAnagrams)
#       currAnagram = sortedWord
#       similarAnagrams = [word]
#   anagrams.append(similarAnagrams)
#   return anagrams

# O(w * n * log(n) time | O(NW) space 
def groupAnagrams(words):
    anagram = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagram:
            anagram[sortedWord].append(word)
            continue 
        anagram[sortedWord] = [word]
    return list(anagram.values())
        

words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
expected = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
output = list(map(lambda x: sorted(x), groupAnagrams(words)))
