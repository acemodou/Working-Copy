def simpleAssert(a : int, b : int) -> None:
    assert a == b, f'{a}!{b}'

# Space is O(n) & Time is (2^n)
# def getNthFib(n : int) -> int:
#     if n == 2:
#         return 1 
#     elif n == 1:
#         return 0
#     else:
#         return getNthFib(n - 1) + getNthFib(n - 2)

# Space is O(n) & Time is (n)
# def getNthFib(n : int) -> int:
#     return fib(n, memoize ={1:0, 2: 1}) 

# def fib(n : int,  memoize : dict) -> int:
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = fib(n - 1, memoize) + fib(n - 2, memoize)
#     return memoize[n]

# Space is O(1) & Time is (n)
def getNthFib(n : int) -> int:
    result = [0, 1]

    for _ in range(3, n+1):
        temp = result[0]
        prev = result[1]
        curr = temp + prev 
        result = [prev, curr]
    return result[1] if n > 1 else result[0]





simpleAssert(getNthFib(0), 0)
simpleAssert(getNthFib(4), 2)
simpleAssert(getNthFib(1), 0)
simpleAssert(getNthFib(5), 3)