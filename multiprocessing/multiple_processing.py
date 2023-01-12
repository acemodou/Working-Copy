#!/usr/bin/env python3

""" Threads that waste cpu cycles """
import os 
import threading
import multiprocessing as mp 

# a simple function that waste cpu cycles 
def cpu_waster():
    while True:
        pass 

print('Hi my name is ', __name__) # This is just a check to show what will have happen if we didn't launch MP inside IFs block
if __name__ =='__main__':

    # Display information about this process 
    print('\n: Process ID: ', os.getpid())
    print('Thread Count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)

    print('\nStarting 12 CPU Wasters...')
    for _ in range(4):
        mp.Process(target=cpu_waster).start()

    print('\n: Process ID: ', os.getpid())
    print('Thread Count: ', threading.active_count())
    for thread in threading.enumerate():
        print(thread)
