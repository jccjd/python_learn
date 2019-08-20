from multiprocessing import Queue,Pool, Manager
import os,time,random
def read(q):
    while not q.empty():
        print(q.get_nowait())

def writer(q):
    while not q.full():
        q.put(random.randint(1,10))

q = Manager().Queue(4)
po = Pool()
po.apply_async(writer, (q,))

time.sleep(1)
po.apply_async(read,(q,))
po.close()
po.join()

