import multiprocessing
import os

def square(n):
    print(F"Workers process ID for {n}: {os.getpid()}")
    return n * n


if __name__ == "__main__":
    mylist = [1, 2, 3, 4]

    """
    Create a pool of objects
    """
    p = multiprocessing.Pool()

    """
    Map list to target function
    """

    result = p.map(square, mylist)

    print(result)