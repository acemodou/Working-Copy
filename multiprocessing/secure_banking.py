import multiprocessing


def withdraw(balance, lock):
    """
    Function to withdraw from your account
    """
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


def deposit(balance, lock):
    """
    Function to deposit from your account
    """
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def perform_transactions():
    """
    Initial balance in shared memory
    """
    balance = multiprocessing.Value('i', 100)

    """
    Create a lock object
    """
    lock = multiprocessing.Lock()

    """
    Creating new processes 
    """
    p1 = multiprocessing.Process(target=withdraw, args=(balance, lock))
    p2 = multiprocessing.Process(target=deposit, args=(balance, lock))

    """
    Starting Processes 
    """

    p1.start()
    p2.start()

    """
    Waiting until processes are finished
    """
    p1.join()
    p2.join()


    print(f"Final balance is: {balance.value} ")

    # print(F"Is p1 alive ? : {p1.is_alive()}")
    # print(f"Is p2 alive ? : {p2.is_alive()}")


if __name__ == "__main__":

    """
    Perform transaction 10 times 
    """
    for _ in range(10):
        perform_transactions()