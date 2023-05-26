# def dec(func):
#     return func 

# def f(x):
#     print(f'hello {x}')

# f = dec(f)

# f(1)



# above code is thesame as 
def dec(func):
    return func 

@dec 
def f(x):
    print(f'hello {x}')


f(1)