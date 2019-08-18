

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return abs(num1 + num2)

def mult(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 // num2

print("please select operation: -\n"\
    "1.Add\n"\
    "2.sub\n"\
    "3.mul\n"\
    "4.div\n"\
      )

input1 = input("Select input from the user: 1,2,3,4 \n")

num1 = int(input("Enter first num: "))
num2 = int(input("Enter 2nd num: "))

if input1 == "1":
    print("Adding two numbers", add(num1, num2))
elif input1 == "2":
    print("Subtract two numbers", sub(num1, num2))
elif input1 == "3":
    print("mult two numbers", mult(num1, num2))
elif input1 == "4":
    print("div two numbers", div(num1, num2))
else: print("Invalid input")