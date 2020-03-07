import multiprocessing

def square_list(my_list, result, square_sum):
    """
    Function to square a given list
    square and sum value
    print square sum value
    """
    for i, num in enumerate(my_list):
        result[i] = num * num

    square_sum.value = sum(result)

    print(F"Result (in process p1): {result[:]}")
    print(F"Sum of squares (in process p1): {square_sum.value}")


if __name__ == "__main__":
    my_list = [1, 2, 3, 4]

    """
    Creating Array of int data type with space for 4 integers
    """
    result = multiprocessing.Array('i', 4)

    """
    Creating value of int data type
    """
    square_sum = multiprocessing.Value('i')

    """
    Creating new process
    """
    p1 = multiprocessing.Process(target=square_list, args=(my_list, result, square_sum))

    """
    Starting new process
    """
    p1.start()

    """
    Wating for process to finish
    """
    p1.join()

    """
    print array result and square_sum
    """
    print(F"Result (in main() program): {result[:]}")
    print(F"Sum of squares (in main() program): {square_sum.value}")

    """
    Check if P1 is dead
    """
    print(F"Is P1 alive ?: {p1.is_alive()}")




