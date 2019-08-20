import os
import multiprocessing
from gevent import monkey
import gevent
import random
import time

def copy_file_path(path1,filename, path2):
    try:
        os.mkdir(path2)
    except:
        pass
    f_read = open(path1+'/'+filename,'rb')
    f_write = open(path2+'/'+filename,'wb')
    while True:
        time.sleep(0.1)
        context = f_read.read(1024)
        if context:
            f_write.write(context)
        else:
            break
    f_read.close()
    f_write.close()


# copy_file_path('test','demo.py','test1')

po = multiprocessing.Pool(3)
filenames = os.listdir('test')
for filename in filenames:
    po.apply_async(copy_file_path,args=('test',filename,'test1'))

po.close()
po.join()
