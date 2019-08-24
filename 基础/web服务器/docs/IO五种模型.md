### 网络请求的原理
客户端发起网络请求，到达服务器网卡，在内核空间中拷贝到内核缓冲区，再由内核缓冲区拷贝到用户空间的web服务器进程，然后进程处理完成再原路返回，

> 对于一个套接字上的输入和输出操作，通常是等待分组的所有数据到达，复制到内核中的某个缓冲区，然后在从内核复制到服务应用进程的缓冲区，这些步骤都是由操作系统的内核决定的

主要就是
- 获取请求数据
- 处理请求
- 返回数据
### 并发模型的两个关键
- 管理连接
- 处理请求
### 阻塞和非阻塞
- 阻塞是指请求方请求后一直在等待
- 非阻塞是指请求方请求后不等待

（对于一个网页的加载，如果有较大资源的请求，比如图片，视频的加载，我们当然是希望，这些资源能延后加载，而不能在加载的过程中，一直等待，某一资源而停止阻塞在这里，所以一般这些资源都会用ajax去异步请求，当整个页面渲染完成后，异步的资源已经准备好了再去加载该资源）

I/O一般分为阻塞和非阻塞模型，阻塞是指在请求的过程中，是否在一直等待返回，如果有等待即为阻塞模型，在所有的I/O模型或多或少都是有阻塞的，可以说阻塞是I/O的常态。
### 阻塞，非阻塞同步和异步
- 阻塞和非阻塞是指客户端是否等待
- 同步和异步是指服务端是否在请求后立刻服务
### 文件描述符
指向内核为每一个进程所维护的该进程打开文件的记录表。当程序打开一个现有文件或者创建一个新文件时，内核向进程返回一个文件描述符
本质是一个索引号，系统用户层可以根据它找到内核层的文件数据，
### 文件句柄
windows下的概念。句柄是windows下各种对象的标识符，和文件描述符类似，也用于定位数据在内存中的位置
### blocking I/O
在socket编程中拿TCP请求来说，当TCP服务端accept阻塞，等待客户端的连接,客户端`send`请求，然后用`recv`等待数据
在这种典型阻塞式I/O模型中，应用程序在从调用`recv`开始到它返回有数据报准备好的这段时间是阻塞的
下面是一段简单的server端和服务端的代码
 - server
 
    
    import socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9102
    
    server.bind((host, port))
    server.listen(128)
    
    while True:
        client, address = server.accept()
        print(address,'--->>>','connection' )
    
        servermsg = 'connection server'
        client.send(servermsg.encode())
    
        clientmsg = client.recv(1024)
        print(f'{address} message is : {clientmsg.decode()}')
    server.close()
- client
    
   
    import socket

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    serveraddr = (socket.gethostname(), 9102)
    client.connect(serveraddr)
    servermsg = client.recv(1024)
    clientmessage = 'hello server'
    client.send(clientmessage.encode())
    
    print(servermsg)
    client.close()
进程阻塞在`recv`上，根据上面的一个流程，当数据报准备好了发给用户空间进程，处理完成后
再回复客户端，`recv` 收到数据请求完成，这种服务器简单，每个连接都需要独立的进程/线程，
当并发量大的时候，内存，线程的切换也是非常大的

### non-blocking I/O
非阻塞模型显然是对阻塞模型的一种优化，即是当请求时不再等待直接返回，应用程序把一个套接口设为非阻塞，当进程无法进行I/O操作时不要将进程睡眠而是返回一个错误，（这里要设置异常捕获） 然后recv就会不断的轮询，直到数据是否准备好了，将数据从内核复制到用户空间
复制成功，返回成功指示。下面是一个非阻塞的简单模型代码，客户端依然沿用上面的代码

- server


    from socket import *
    import time
    
    g_socket_list = list()
    
    def main():
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR  , 1)
        # server_socket.bind(('', 7890))
        server_socket.bind(('', 9102))
        server_socket.listen(128)
        server_socket.setblocking(False)

    while True:

        time.sleep(0.5)

        try:
            newClientInfo = server_socket.accept()
        except Exception as result:
            pass
        else:
            print("----new client-----" )
            newClientInfo[0].setblocking(False)  #非堵塞
            g_socket_list.append(newClientInfo)

        for client_socket, client_addr in g_socket_list:
            try:
                recvData = client_socket.recv(1024)
                if recvData:
                    print('recv[%s]:%s' % (str(client_addr), recvData))
                else:
                    print('[%s]客户端关闭' % str(client_addr))
                    client_socket.close()
                    g_socket_list.remove((client_socket,client_addr))
            except Exception as result:
                pass

        print(g_socket_list,time.sleep(5)) #每5秒打印一次当前的客户端连接

    if __name__ == '__main__':
        main()
        
- client


    import socket

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # serveraddr = (socket.gethostname(), 9999)
    serveraddr = ('', 9102)
    client.connect(serveraddr)
    servermsg = client.recv(1024)
    clientmessage = 'hello server'
    client.send(clientmessage.encode())
    
    print(servermsg)
    client.close()

好处显然不用阻塞，每次发送I/O立刻返回实时性很好，但是轮询要不断的访问内核，将占用大量的CPU时间。

### I/O multiplexing
实现多路复用的三种方式 select， poll， epoll(这种三种方式是逐渐被递增优化的，) 都是负责管理多个I/O操作，然后轮询所管理的`socket`
当有数据到达了，就通知用户。当用户调用了`select`，那么这个进程会被block，然后内核会监视`select`负责的socket，当任何一个`socket`的数据准备好了（意味着全部的请求包已经到达系统内核空间），`select`就会返回可读条件，调用该socket的recv，阻塞等待数据复制到用户空间，web进程处理数据后然后返回请求。
> select 和 poll 都是需要遍历所有的文件句柄状态效率都不高。而且select有句柄上限,epoll则是poll的增强版，无无文件描述符，epoll是基于内核的反射机制，在有活跃的socket时，系统会调用我们提前设置的回调函数，而poll和select都是遍历而epoll使用一个文件描述符的事件存放到内核的一个事件表，这样在用户空间和内核空间的copy只需一次

下面是python实现epoll的一个简单例子

- server 


    import socket
    import select
    
    # 建立tcp
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.bind(("",9102))
    s.listen(128)
    
    # 创建一个epoll对象
    epoll = select.epoll()
    
    # 注册事件到epoll中
    epoll.register(s.fileno(), select.EPOLLIN|select.EPOLLET)
    
    connections = {}
    addresses = {}
    
    while True:
    
        # epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待
        epoll_list = epoll.poll()
    
        # 对事件进行判断
        for fd, events in epoll_list:
    
            print(epoll_list)
    
            # 如果是socket创建的套接字被激活
            if fd == s.fileno():
                new_socket, new_addr = s.accept()
    
                print('有新的客户端到来%s' % str(new_addr))
    
                # 将 conn 和 addr 信息分别保存起来
                connections[new_socket.fileno()] = new_socket
                addresses[new_socket.fileno()] = new_addr
    
                # 向 epoll 中注册 新socket 的 可读 事件
                epoll.register(new_socket.fileno(), select.EPOLLIN|select.EPOLLET)
                new_socket.send(b'hello')
            # 如果是客户端发送数据
            elif events == select.EPOLLIN:
                # 从激活 fd 上接收
                recvData = connections[fd].recv(1024).decode("utf-8")
    
                if recvData:
                    print('recv:%s' % recvData)
                else:
                    # 从 epoll 中移除该 连接 fd
                    epoll.unregister(fd)
    
                    # server 侧主动关闭该 连接 fd
                    connections[fd].close()
                    print("%s---offline---" % str(addresses[fd]))
                    del connections[fd]
                    del addresses[fd]
### signal-driven
在信号驱动式模型中，应用程序使用套接口进行信号驱动I/O并安装一个信号处理函数，进程继续运行不阻塞，当数据准备好时，内核发送一个SIGIO信号，
可以在信号处理函数中调用I/O操作函数处理数据

信号驱动I/O尽管对于处理UDP套接字来说有用，即这种信号通知意味着到达一个数据报，或者返回一个异步错误，但是对于TCP而言，信号驱动的I/O几乎
无用
因为导致这种通知的条件为数众多，没一个来进行判别会消耗很大

### asynchronous I/O
异步I/O,用户进程发起`aio_read`系统调用后无论 `kernel`数据是否准备好都不会阻塞用户进程，用户进程返回，等到`socket`的数据准备好了，内核直接复制数据给进程web进程，处理完成后直接返回。


















