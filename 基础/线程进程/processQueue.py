from multiprocessing import Queue
from multiprocessing import Process
import os, time, random
# q = Queue(3)
# q.put('消息1')
# q.put('消息2')
# print(q.full())
#
# q.put('消息3')
# print(q.full())
#
# try:
#     q.put('消息4',True, 2)
# except:
#     print(f"消息队列已经满，现有消息数量{q.qsize()}")
#
# try:
#     q.put_nowait("消息4")
# except:
#     print(f'消息队列已满, 现有消息{q.qsize()}')
#
# if not q.full():
#     q.put_nowait('消息4')
#
# if not q.empty():
#     for i in range(q.qsize()):
#         print(q.get_nowait())
def write(q):
    for value in ['a', 'b', 'c']:
        print(f'put{value} to queue')
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print(f'Get {value} from queue')
            time.sleep(random.random())
        else:
            break
q = Queue()
pw = Process(target=write, args=(q,))
pr = Process(target=read,args=(q,))
pw.start()
pw.join()
