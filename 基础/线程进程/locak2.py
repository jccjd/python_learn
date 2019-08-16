import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def do_something1():
    lock1.acquire()
    print('Something 1 started')
    time.sleep(0.1)
    lock2.acquire()

    lock1.release()
    lock2.release()

def do_something2():
    lock2.acquire()
    print('Something 2 ended')
    lock1.acquire()

    lock2.release()
    lock1.release()

thread1 = threading.Thread(target=do_something1)
thread2 = threading.Thread(target=do_something2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()