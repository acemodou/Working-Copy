def binary_rep(n):
    bin_res = list()
    while (n >= 1):
        result = n % 2
        print(result)
        bin_res.append(result)
        n = n // 2
        print("n is", n)
    bin_res.reverse()
    return bin_res

print(binary_rep(100))

https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/
