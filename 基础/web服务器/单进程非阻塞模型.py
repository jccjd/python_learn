import time
from socket import *
g_socket_list = list()
def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('', 7890))
    server_socket.listen(128)

    server_socket.setblocking(False)

    while True:
        time.sleep(0.5)
        try:
            newClientInfo = server_socket.accept()
        except Exception as result:
            pass
        else:
            print(f'--->{str(newClientInfo)}')
            newClientInfo[0].setblocking(False)
            g_socket_list.append(newClientInfo)
        for client_socket, client_addr in g_socket_list:
            try:
                recvData = client_socket.recv(1024)
                if recvData:
                    print('recv[%s]:%s'%(str(client_addr), recvData))
                else:
                    print(f'--->off{str(client_addr)}')
                    client_socket.close()
                    g_socket_list.remove(client_socket,client_addr)
            except Exception as result:
                pass
    print(g_socket_list)

main()