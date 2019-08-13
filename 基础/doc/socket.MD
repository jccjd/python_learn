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

当有客户端去连接该server时,依然会返回
    
    client, msg = serverclient.accept()


    


    
    
    
