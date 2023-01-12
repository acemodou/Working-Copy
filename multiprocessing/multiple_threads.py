#!/usr/bin/env python3

""" Threads that waste cpu cycles """
import os 
import threading

# a simple function that waste cpu cycles 
def cpu_waster():
    while True:
        pass 

# Display information about this process 
print('\n: Process ID: ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)


print('\nStarting 12 CPU Wasters...')
for _ in range(4):
    threading.Thread(target=cpu_waster).start()

# Note the cpu usage won't be high even though we have 4 threads running because GIL 
# GIL is only allowing one thread to execute at a time . It can only utilize one cpu resource
# Display information about this process 
print('\n: Process ID: ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)
