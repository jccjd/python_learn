# 进程间不同共享全局变量
from multiprocessing import Process
import os
import time
nums = [11, 22]
def work1():
    print(f'{os.getpid(),nums}')
    for i in range(3):
        nums.append(i)
        time.sleep(1)
        print(f'{(os.getpid(), nums)}')

def work2():
    print(f'in process2 pid={os.getpid()}, nums={nums}')

p1 = Process(target=work1)
p1.start()
p1.join()

p2 = Process(target=work2)
p2.start()