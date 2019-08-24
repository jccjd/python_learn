#coding=utf-8
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
            newClientInfo[0].send(b'hello')
        for client_socket, client_addr in g_socket_list:
            try:
                recvData = client_socket.recv(1024)
                if recvData:
                    print('recv[%s]:%s' % (str(newClientInfo[1]), recvData))
                else:
                    print('[%s]客户端关闭' % str(client_addr))
                    client_socket.close()
                    g_socket_list.remove((client_socket,client_addr))
            except Exception as result:
                pass

        # print(g_socket_list,time.sleep(5)) #每5秒打印一次当前的客户端连接

if __name__ == '__main__':
    main()