from collections import Counter


def simple_assert(a, b) -> None:
    assert a == b, f'{a}!{b}'

# def isAnagram(s: str, t: str) -> bool:
#     return sorted(s) == sorted(t)

# def isAnagram(s: str, t: str) -> bool:
#     return Counter(s) == Counter(t)

def isAnagram(s: str, t: str) -> bool:
    # Count the letters then decrement count 
    # Check if there are non zeros
    if len(s) != len(t):
        return False 
    counter =   {}
    for words in s:
        counter[words] = counter.get(words, 0) + 1
    for words in t:
        counter[words] = counter.get(words, 0) - 1
    for _, values in counter.items():
        if values != 0:
            return False
    return True

simple_assert(isAnagram("anagram", "nagaram"), True)
simple_assert(isAnagram("rat", "car"), False)
simple_assert(isAnagram('aaaaaa', 'a'), False)
simple_assert(isAnagram('a', 'aaaaaa'), False)
