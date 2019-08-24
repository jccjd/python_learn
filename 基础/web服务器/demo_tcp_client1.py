import socket
from threading import Thread
import time
def client():
    sk = socket.socket()
    addr = ('',9102)
    sk.connect(addr)
    sk.send(b'hello')
    sk.close()
if __name__ == '__main__': # 模拟20个客户端并发连接服务端
    for i in range(20):
        Thread(target=client).start()
