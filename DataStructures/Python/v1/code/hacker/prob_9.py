import time


fac_cache = {}
def factorial(n):
    if n in fac_cache:
        return fac_cache[n]
    elif n < 1:
        return 1
    else:
        value =  n * factorial(n-1)
        fac_cache[n] = value 
    return value 


start_time = time.time()
for i in range(2, 12):
    print(f'factorial of {i} is: {factorial(i)}')
end_time = time.time()
print(f'Execution time is: {end_time - start_time}')