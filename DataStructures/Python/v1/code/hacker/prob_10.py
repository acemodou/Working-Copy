# def binary_rep(n):
#     bin_res = list()
#     while (n >= 1):
#         result = n % 2
#         bin_res.append(result)
#         n = n // 2
#     bin_res.reverse()
#     return bin_res


# def binaryToDecimal(binary):
#     i, decimal = 0, 0
#     while binary != 0:
#         dec = binary % 10
#         decimal += dec * pow(2, i)
#         i += 1
#         binary //=10
#     print(decimal)

def decimal_to_bin(n):
    print('{0:b}'.format(n))

def decimal_to_binary(n):
    if n >= 1:
        decimal_to_binary(n // 2)
        print(n % 2, end='')

def decimalToBinary(n):
    binary = []
    while n > 0:
        binary.append(n % 2)
        n = n // 2
    return binary 


def consecutive_ones(n):
    max_counter, counter = 0,0
    ones = decimalToBinary(n)
    for i in range(len(ones)):
        if ones[i] == 1:
            counter += 1
            if counter > max_counter:
                max_counter = counter
        else:
            counter = 0 
    return max_counter

def binaryToDecimal(binary_value):
    '''
    1 0 1 % 10 to grab the last digit
    1 * pow(2, 0) = 1
    0 * pow(2, 1) = 0
    1 * pow(2, 2) = 4
    '''
    i, result  = 0, 0
    while binary_value != 0:
        last_digit = binary_value % 10 
        result += last_digit * pow(2, i)
        i += 1 
        binary_value = binary_value // 10 
    return result


def check_bits_on(n):
    for i in range(30):
        if (n & (1 << i)) != 0:
            print(i)

def binary_2(n):
    for i in range(2, -1, -1):
        if (n & (1 << i)) != 0:
            print(1, end='')    
        else:
            print(0, end='')

# decimalToBinary(5)
# print(consecutive_ones(6))
# decimal_to_binary(2)
# print(binaryToDecimal(110))
# decimal_to_bin(5)
binary_2(6)