import os
import multiprocessing
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
        time.sleep(1)
        context = f_read.read(1024)
        if context:
            f_write.write(context)
        else:
            break
    f_read.close()
    f_write.close()
    queue.put(filename)

# copy_file_path('test','demo.py','test1')
queue = multiprocessing.Queue()
po = multiprocessing.Pool(3)
filenames = os.listdir('test')
for filename in filenames:
    po.apply_async(copy_file_path,args=('test',filename,'testcopy'))

po.close()
po.join()
all_file_name = len(filenames)
while True:
    file_name = queue.get()
    if file_name in filenames:
        filenames.remove(file_name)

    copy_rate = (all_file_name - len(filenames)) * 100 // all_file_name

    print('-'*(copy_rate//2)+'>',copy_rate,'%')

    time.sleep(random.random())
    if copy_rate == 100:
        print('Done')
        break


