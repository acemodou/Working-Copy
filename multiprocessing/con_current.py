import time
import concurrent.futures


def get_someSleep(seconds):
    print(f'Sleeping for {seconds} ...')
    time.sleep(seconds)
    return f'Done sleeping ...{seconds}'


if __name__ == "__main__":

    """
    Map function maps the list with the function
    """
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(get_someSleep, secs)

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s')