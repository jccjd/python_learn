import multiprocessing
import time

def cook1():

    print('炖汤.....')
    time.sleep(5)
    queue.put(1)
    print('汤顿好了')
def cook2():

    print('炒菜ing....')
    time.sleep(2)
    print('菜抄好了')

def listen_music():

    while True:
        print('听歌ing......')
        if queue.get():
            print('听歌结束.....')
            break
queue = multiprocessing.Queue()
po = multiprocessing.Pool(3)
po.apply_async(listen_music)
po.apply_async(cook1)
po.apply_async(cook2)

po.close()
po.join()