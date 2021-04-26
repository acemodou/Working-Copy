import time

def factorial(n):
    if n < 1:
        result = 1
    else:
        result = n *factorial(n -1)
    return result


start_time = time.time()
for i in range(2, 900):
    print(i, "factorial is: {}".format(factorial(i)))
end_time = time.time()

print("Execution time is : {}".format(end_time - start_time))
# This takes 2.1 seconds with only 900 iterations


# Now lets use memoization

fac_cache = {}

# def fact(n):
#     if n in fac_cache:
#         return fac_cache[n]
#     elif n < 1:
#         result = 1
#     else:
#         result = n * fact(n - 1)
#     fac_cache[n] = result
#     return result
#
# start_time = time.time()
# for i in range(2, 1000):
#     print(i, "factorial is: {}".format(fact(i)))
# end_time = time.time()
#
# print("Execution time is : {}".format(end_time - start_time))
# 1000 iteration takes 0.5 seconds with memoization