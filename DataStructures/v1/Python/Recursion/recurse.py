def SumofNaturalNumbers(n):
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
    return r + TaylorSeries.p/TaylorSeries.f

def Factorial(n):
    if n == 0:
        return 1
    return Factorial(n-1)*n

def Power(m, n):
    if n == 0:
        return 1
    return Power(m, n-1) * m

def Fibonacci(n):
    if n <= 1:
        return n
    return Fibonacci(n-2) + Fibonacci(n-1)

fibonacci_cache = {}
def MemoizationFibonaaci(n):
    if n in fibonacci_cache:
        yield fibonacci_cache[n]
    if n <= 1:
        yield n
    elif n > 1:
        value = MemoizationFibonaaci(n-1) + MemoizationFibonaaci(n-2)
    
    # Cache the value and return it s
    fibonacci_cache[n] = value
    yield value

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


if __name__ =="__main__":
    # for n in range(1, 5):
    #     print(n, ":", MemoizationFibonaaci(n))
    TOH(1, 1,2,3)
    
 
    