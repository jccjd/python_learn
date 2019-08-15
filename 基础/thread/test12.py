import threading
from time import sleep, ctime
def sing():
    for i in range(3):
        print(f'{i}sing')
        sleep(1)

def dance():
    for i in range(3):
        print(f'{i}dance')
        sleep(1)
# print(ctime())
t1 = threading.Thread(target=sing)
t2 = threading.Thread(target=dance)

t1.start()
t2.start()
while True:
    length = len(threading.enumerate())
    print("------",length)
    if length <= 1:
        break
    sleep(0.5)
# print(ctime())