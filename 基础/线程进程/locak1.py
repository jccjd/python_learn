# 下面的程序就是线程同时获取多个资源而造成的死锁
# 由于两个线程获取锁的顺序是相反的,对于互斥资源lock1,和lock2
# 如果是正常推进，线程1得到lock1,lock2 执行完成后，释放资源
# 线程2 在去执行，这样是没有问题的，但是
# 在线程1 的到lock1时有一点延迟，导致线程2 的到了 lock2,那么线程1 无法继续
# 线程2同样因为lock1的阻塞而无法教学执行，这就是产生了死锁的过程，由于同时获取多个资源
# 那么如何解决呢，python3 cook-book 中给出的方案是，给每一个锁分配一个唯一的id，然后只允许
# 按照升序规则来使用多个锁，代码实现如下， 注意 要为每个线程设置守护进程为True
# 而这种方法呢，算是将程序从死锁状态解除，
# 等等，这个好像只需要加个守护进程，就行了，如果线程死锁了，那么直接就结束了

import threading
import time

import threading
from contextlib import contextmanager


lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with (lock2):
        # time.sleep(1)
        with (lock1):
            print('-----thread 1 finish----')

def thread2():

    with lock1, lock2:
        print('-----thread 2 finish ---')
t1 = threading.Thread(target=thread1)
# t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread2)
# t2.daemon = True
t2.start()
