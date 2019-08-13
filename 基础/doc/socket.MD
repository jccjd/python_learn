### udp
通信的过程肯定需要 ip 和端口的
    
    server_ip = ('127.0.0.1', 9102)
建立udp连接，创建upd连接的实体,绑定address
    
    s = socket.socket(socket.AF_INET, socket.DGRAM)
    
收取信息，作为已经绑定的目标端，发送端一定是已知目标端的ip，当发送端发数据时

会将自己的ip和端口都会一起发来,服务端确定一次接受的大小
    
    client_data, client_address = s.recvfrom(1024)
    
那么这是一次接受过程

当有一个发送端时，目标ip已知
    
    s.sendto(msg.encode(),server_ip)

- 创建实体 
- 绑定ip
- 接受信息
- 发送信息

upd 是数据报的形式进行通信，不需要进行双方回复确认，发送之后就不会对此次发送维护

### TCP

tcp 创建一个tcp连接
创建 一个tcp实体,参数是数据流
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = server.gethostname
    port = 9102

依然需要bind
    
    server.bind((host, port))

还需要个监听，允许连接个数
    
    server.listen(2)

当有客户端去连接该server时,会返回一个client，和客户端的ip和端口
    
    client, msg = serverclient.accept()
    
如果没有客户端连接，那么就会阻塞，直到有客户端连接
回复客户端
    
    client.send(message)
那么客户端的一个流程,仍然是要先建立一个socket实体
    
    client = socket(socket.AF_INET,socket.STREAM)

然后直接连接目标地址
    
    client.conn(server_ip)

获取服务器信息,指定大小
    
    msg =  client.recv(1024)
    
关闭连接`client.close()`

注意的是，在TCP 连接传输数据完成，关闭连接，挥手完成后，服务器仍然要等待
等待两个最大存活时间,一个MSL 一般是30s，如果操作不当 会有`address already in use`
错误
也就是当前的TCP服务端依然在存活，一分钟后就不会报错了

具体原因 :
   
客户端请求服务器 发送一个同步申请SYN=1,和seq=x的随机数

服务端收到回复ACK=1的确认和seq=x+1,并又生成一个随机数 ack=y，和同步信号syn=1

客户端回复ACK=1 随机数ack=y+1,
这里三次握手就建立了

然后在挥手的过程中
客户端 发送 完成信号FIN=1，和随机数字seq=x 进入完成等待状态

服务器收到回复确认信号ACK=1，和随机数字加一seq+1，并又产生一个随机数ack=y

带这个过程可能服务器并没有完成数据传输，等到数据传输完成

发送完成信息FIN=1，和 数字Ｍ 这就是为什么要四次挥手

然后客户端在回复 给服务器发送确认ACK=1 

然后结束这次通信，

在客户端等待服务器信号的时候，要等待2ＭＳＬ如果fin信号丢失依然能够在服务端
检测到超时从新发送fin，然后回应给服务端ＡＣＫ





    
    
    
