import threading
import time
lock_gun = threading.Lock()
lock_blt = threading.Lock()

class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.gun()
        self.blt()

    def gun(self):
        lock_gun.acquire()
        print(f'{self.name},get gun')

        lock_blt.acquire()
        print(f'{self.name},get blt')
        lock_blt.release()
        lock_gun.release()

    def blt(self):
        lock_blt.acquire()
        print(f'{self.name} get blt')
        time.sleep(1)

        lock_gun.acquire()
        print(f'{self.name} get gun')
        lock_gun.release()
        lock_blt.release()

for i in range(2):
    my_th = myThread()
    my_th.start()