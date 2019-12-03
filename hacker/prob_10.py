def binary_rep(n):
    bin_res = list()
    while (n >= 1):
        result = n % 2
        bin_res.append(result)
        n = n // 2
    bin_res.reverse()
    return bin_res



def decimalToBinary(n):
    if n > 1:
        decimalToBinary(n // 2)
    print(n % 2, end=' ')

def binaryToDecimal(binary):
    i, decimal = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal += dec * pow(2, i)
        i += 1
        binary //=10
    print(decimal)

def consecutive_ones(decimal):
    list1 = binary_rep(decimal)
    print(list1)
    counter, max_counter = 0, 0
    for i in range(len(list1)):
        if list1[i] == 1:
            counter += 1
            if counter > max_counter:
                max_counter = counter
        else:
            counter = 0
    print(max_counter)


consecutive_ones(6)




