from multiprocessing import Queue,Process
import os
q=Queue(3)

def putnum(q):
    i = 0
    while not q.full():
        q.put(i)
        i += 1
def getnum(q):
    while not q.empty():
        print(q.get_nowait(),os.getpid())
    if q.empty():
        print('----')

p1 = Process(target=putnum,args=(q,))
p2 = Process(target=getnum,args=(q,))
p3 = Process(target=getnum,args=(q,))
p1.start()
p2.start()
p3.start()