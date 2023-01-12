import multiprocessing
import os


def worker1():
    """
     Printing worker 1 ID
    """
    print(f"ID of processing running worker1:  {os.getpid()}")


def worker2():
    """
    Printing worker 2 ID
    """
    print(f"ID of processing running worker1:  {os.getpid()}")


if __name__ == "__main__":
    """
    printing main program process ID
    """
    print(f"ID of main process: {os.getpid()}")

    """
    Creating processes
    """
    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)

    """
    Starting processes
    """
    p1.start()
    p2.start()

    """
    Process IDs
    """
    print(f"ID of process p1: {p1.pid}")
    print(f"ID of process p2: {p2.pid}")

    """
    Wait until processes are finished
    """
    p1.join()
    p2.join()

    """
    Processes should finished execution 
    """
    print(f"Process P1 and P2 finished execution")

    """
    Check if processes are alive 
    """
    print(f"Is p1 alive ?: {p1.is_alive()}")
    print(F"Is p2 alive ?: {p2.is_alive()}")

