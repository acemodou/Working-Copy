def simple_assert(a, b):
    assert a == b, f'{a}!{b}'

# def compressed_string(s : str) -> str:
#     dup_count = 1
#     comp_str =""
#     for i in range(1, len(s)):
#         if s[i] != s[i-1]:
#             comp_str += f"{s[i-1]}{dup_count}"
#             dup_count = 1
#         else:
#             dup_count += 1
#     comp_str += f"{s[i-1]}{dup_count}"
#     return comp_str if len(comp_str) < len(s) else s 


# String Concatenation operates in O(n^2)
# O(p + n^2) time | O(n) space 
# def compressed_string(s : str) -> str:
#     compressed = ""
#     count_consecutive = 0
#     for i in range(len(s)):
#         count_consecutive += 1
#         if i + 1 >= len(s) or s[i] != s[i+1]:
#             compressed += f"{s[i]}{count_consecutive}"
#             count_consecutive = 0
#     return compressed if len(compressed) < len(s) else s 


def compressed_string(s : str) -> str:
    count_consecutive = 1
    comp_str = []
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            comp_str.append(f"{s[i-1]}{count_consecutive}")
            count_consecutive = 1
        else:
            count_consecutive += 1
    comp_str += f"{s[i-1]}{count_consecutive}"

    comp_str = "".join(comp_str)
    return comp_str if len(comp_str) < len(s) else s 

simple_assert(compressed_string("aabcccccaaa"), "a2b1c5a3")