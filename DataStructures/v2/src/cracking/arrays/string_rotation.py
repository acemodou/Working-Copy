def simple_assert(a, b):
    assert a == b, f"{a}!{b}"


def is_rotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        # Concatenate s1 with S1 and check if s2 is a substring of s1
        s1s1 = s1 + s1
        return is_substring(s1s1, s2)

def is_substring(s1, s2):
    return s2 in s1





simple_assert(is_rotation("waterbottle", "erbottlewat"), True) 