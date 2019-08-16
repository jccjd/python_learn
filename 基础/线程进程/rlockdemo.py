import threading
import time
rlock2 = threading.RLock()

def thread1():
    with rlock2.acquire():
        time.sleep(1)
        with rlock2.acquire():
            print('html')

def thread2():
    with rlock2.acquire():
        time.sleep(1)
        with rlock2.acquire():
            print('html')
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start()
t2.start()
