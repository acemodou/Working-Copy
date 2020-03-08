import multiprocessing


def square_list(my_list, q):
    """
    Function to square a given list
    """
    for num in my_list:
        q.put(num * num)


def print_queue(q):
    """
    Function to print queue elements
    """
    print("Queue elements")
    while not q.empty():
        print(q.get())
    print("Queue is now empty!")


if __name__ == "__main__":
    my_list = [1, 2, 3, 4]

    """
    Building multiprocessing queue
    """
    q = multiprocessing.Queue()

    """
    Creating new processes 
    """
    p1 = multiprocessing.Process(target=square_list, args=(my_list, q))
    p2 = multiprocessing.Process(target=print_queue, args=(q,))

    """
    Starting process and waiting until process is finished
    """
    p1.start()
    p1.join()

    p2.start()
    p2.join()

    """
    Checking if processes are alive 
    """
    print(f"Is p1 alive ? {p1.is_alive()}")
    print(f"Is p2 alive ? {p2.is_alive()}")