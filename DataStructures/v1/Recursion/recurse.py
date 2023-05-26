def sumofNaturalNumbers(n):
    return n * (n + 1) / 2

def iterativeNaturalNumbers(n):
    s = 0
    for i in range(n+1):
        s +=i
    return s

def recursiveNaturalNumbers(n):
    if n == 0:
        return 0
    return recursiveNaturalNumbers(n-1) + n

def TaylorSeries(x, n):
    '''
    e^4 = 1+x/1+x/2+x/3+x/4
    '''
    TaylorSeries.p = 1 #This is how we make a function static in python. Weird
    TaylorSeries.f = 1 
    if n == 0:
        return 1
    r = TaylorSeries(x, n-1)
    TaylorSeries.p *= x 
    TaylorSeries.f *= n
    return r + (TaylorSeries.p // TaylorSeries.f)

def Factorial(n):
    if n == 0:
        return 1
    return Factorial(n-1)*n

def Power(m, n):
    if n == 0:
        return 1
    return Power(m, n-1) * m

def powers(m, n):
    if n == 0:
        return 1 
    if n % 2 == 0:
        return powers(m * m, n//2)
    else:
        return m * powers(m*m , (n-1) //2)

def Fibonacci(n):
    if n <= 1:
        return n
    return Fibonacci(n-2) + Fibonacci(n-1)

fibonacci_cache = {}
def MemoizationFibonaaci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n <= 1:
        return n
    elif n > 1:
        value = MemoizationFibonaaci(n-1) + MemoizationFibonaaci(n-2)
    
    # Cache the value and return it s
    fibonacci_cache[n] = value
    return value

def squareNumbers(numList):
    for i in numList:
        yield(i * i)

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y 
        yield x 

def TOH(n, a, b, c):
    if n > 0:
        TOH(n-1, a, c, b)
        print(f'Move disk from {a} to {c}')
        TOH(n-1, b, a, c)

def recurse_mult(x, y):
    ''' Multiply without using the * operator '''
    if x == 0 or y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return recurse_mult(x, y-1) + x

def perm(S):
    res = [""] * len(S)
    A = [0] * len(S)
    backtrack(S, 0, res, A)

def backtrack(S, k, res, A):
    if k == len(S):
        print(''.join(res))
    for i in range(len(S)):
        if A[i] == 0:
            res[k] = S[i]
            A[i] = 1
            backtrack(S, k+1, res, A)
            A[i] = 0



if __name__ =="__main__":
    # for n in range(1, 5):
    #     print(n, ":", MemoizationFibonaaci(n))
    # print(TaylorSeries(2,4))
    # print(recurse_mult(4, 5))
    S = "abc"
    perm(S)
 
    