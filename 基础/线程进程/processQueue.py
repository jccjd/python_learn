from multiprocessing import Queue
q = Queue(3)
q.put('消息1')
q.put('消息2')
print(q.full())

q.put('消息3')
print(q.full())

try:
    q.put('消息4',True, 2)
except:
    print(f"消息队列已经满，现有消息数量{q.qsize()}")

try:
    q.put_nowait("消息4")
except:
    print(f'消息队列已满, 现有消息{q.qsize()}')

if not q.full():
    q.put_nowait('消息4')

if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())