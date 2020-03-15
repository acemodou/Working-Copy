import time
import multiprocessing


def do_something(seconds):
    print(f'Sleeping {seconds} second(s) ...')
    time.sleep(1)
    print('Done Sleeping  ...')


if __name__ == "__main__":
    start = time.perf_counter()
    """This will take 5 seconds"""
    # print("Without multiprocessing it will take 5 seconds ")
    # for _ in range(5):
    #     do_something()

    """
    We can use multiprocessing to improve performance.
    Same 5 iteration takes 1 seconds 
    """

    processes = []

    for _ in range(5):
        p = multiprocessing.Process(target=do_something, args=([1.5],))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()


    """
    We use performance counter to measure the highest available resolution
    to measure a short duration 
    """

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)}')