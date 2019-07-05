# threading example
# https://pythonbasics.org/

import threading
import time

# function that prints hello world and current thread
def task():
    for i in range(0,10):
        print(" thread " + format(threading.current_thread()), end=''),
        print(" = " + str(i))
        time.sleep(1)

# create a thread and start it
thread1 = threading.Thread(target=task)
thread1.start()

# create a thread and start it
thread2 = threading.Thread(target=task)
thread2.start()


