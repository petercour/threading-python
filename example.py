# threading example
# https://pythonbasics.org/
import threading

# function that prints hello world and current thread
def task():
    print("Hello World: {}".format(threading.current_thread()))

# create a thread and start it
thread1 = threading.Thread(target=task)
thread1.start()
