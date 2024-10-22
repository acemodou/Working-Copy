def simple_assert(a, b):
    assert a == b, f'{a}!{b}'
 
   
def compression(str):
    compressed_res = []
    count = 0
    for i in range(len(str)-1):
        count += 1
        if str[i] != str[i+1]:
            compressed_res.append(f'{str[i]}{count}')
            count = 0 
    compressed_res += f'{str[i]}{count}'
    return ''.join([r for r in compressed_res]) 


actual = 'a2b1c5a3'
expected = compression('aabcccccaaa')
simple_assert(actual, expected)
    