
def pascal_stars(num, sign):
    for i in range(num):
        for _ in range(num-i-1):
            print(end=" ")
        for _ in range(i+1):
            print(sign, end=" ")
        print()

def reverse_pascal(num, sign):
    for i in range(num, 0, -1):
        for _ in range(num-i):
            print(end=" ")
        for _ in range(i):
            print(sign, end=" ")
        print()

def pascal_triangle(num):
    pascal = list()
    for row in range(num):
        temp_storage = []
        for col in range(row+1):
            if col == 0 or col == row:
                temp_storage.append(1)
            else:
                temp_storage.append(pascal[row-1][col] + pascal[row-1][col-1])
        pascal.append(temp_storage)

    # Putting pascal in a pyramid
    for row in range(num):
        for _ in range(num-row-1):
            print(end=" ")
        for col in range(row+1):
            print(pascal[row][col], end=" ")
        print()

def pascal_triangle_recurse(row, col):
    '''
    This return the specific pascal value 
    '''
    storage = []
    if col == 0 or col == row:
        return 1
    pattern = pascal_triangle_recurse(row-1, col) + pascal_triangle_recurse(row-1, col-1)
    return pattern 

def right_angle_triangle(num, sign):
    k = 1
    for i in range(num):
        print("".ljust(k, sign))
        k +=2

def print_pattern(num, sign):
    """
    We added one since ljust won't print anything for zero
    range() is exclusive 
    """
    for i in range(num+1):
        star = ""
        print(star.ljust(i, sign))

def print_pattern1(num, sign):
    """
    We added one since ljust won't print anything for zero
    range() is exclusive 
    """
    for i in range(num, 0, -1):
        star = ""
        print(star.ljust(i, sign))

def print_pattern2(num, sign):
    numOfSpace = num -1 
    star =''
    for i in range(1, num+1, 1):
        for j in range(numOfSpace):
            print('-', end='')
        print(star.rjust(i, sign))
        print()
        numOfSpace -=1

def print_pattern3(num, sign):
    numOfSpace = 0
    star = ''
    for i in range(num, 0, -1):
        for j in range(numOfSpace):
            print('-', end='')
        print(star.rjust(i, sign))
        print()
        numOfSpace +=1

def multiply_pattern(num):
    for i in range(1, num+1, 1):
        for j in range(1, i+1, 1):
            print(i * j, end=' ')
        print()

def multiply_pattern1(num):
    for i in range(1, num+1, 1):
        for j in range(1, i+1, 1):
            if j % 2 == 0: 
                print(0, end=' ')
            else:
                print(1, end=' ')
        print()

def print_A_star(num, sign):
    for row in range(num):
        for col in range(5):
            if ((col == 0 or col == 4) and row != 0) or (row == 3) or (row ==0 and (col != 0 and col !=4)):
                print(sign, end="")
            else:
                print(end=" ")
        print()
        
def print_B_star(num, sign):
    for row in range(num):
        for col in range(5):
            if (col == 0) or (col == 4 and (row !=0 and row !=3 and row !=6)) or ((row == 0 or row == 3 or row == 6) and (col !=4)):
                print(sign, end="")
            else:
                print(end=" ")
        print()

def print_C_star(num, sign):
    for row in range(num):
        for col in range(5):
            if ((row ==0 or row == 6) and (col !=0)) or ((col == 0) and (row !=0 and row !=6)):
                print(sign, end="")
            else:
                print(end=" ")
        print()

def print_D_star(num, sign):
    for row in range(num):
        for col in range(5):
            if (col == 0) or ((col == 4) and (row != 0 and row != 6)) or ((row == 0 or row ==6) and (col < 4)):
                print(sign, end="")
            else:
                print(end=" ")
        print()

    

if __name__ =="__main__":
    print_D_star(7, "*")

   

  



    