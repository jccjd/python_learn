import socket

sk = socket.socket()
addr = ('127.0.0.1', 9102)
sk.bind(addr)
sk.listen(128)
sk.setblocking(False)  # 设置非阻塞模式,accept,recv等方法均不阻塞，而是抛出异常

conn_lst = []  # 建立一个列表存储接收到的连接
del_lst = []  # 建立一个列表存储已经关闭的连接
while True:
    try:
        conn, addr_client = sk.accept()  # 没有连接时--BlockingIOError
        print('接收到一个连接')  # 如果上一步没有异常发生，则表示收到一个连接
    except BlockingIOError:
        for conn in conn_lst:  # 循环接收到的连接,尝试接收消息
            try:
                msg = conn.recv(1024)
                print(msg)
                if not msg:
                    del_lst.append(conn)
                    continue
                print(msg)
            except BlockingIOError:
                for conn in del_lst:
                    conn.close()
                    conn_lst.remove(conn)
                del_lst.clear()  # 清空已关闭的连接记录
