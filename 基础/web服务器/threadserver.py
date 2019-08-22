import threading
import re
import socket

class WSGIServer(object):
    def __init__(self, socket_addr=('',8888)):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        self.server_socket.bind(socket_addr)
        self.server_socket.listen(128)

    def start_server(self):
        while True:
            client_socket, client_add = self.server_socket.accept()
            print(client_socket)
            threading.Thread(target=self.handle, args=(client_socket,)).start()


    def handle(self, client_socket):
        recv_data = client_socket.recv(1024).decode('utf-8')
        recv_data = recv_data.splitlines()
        for line in recv_data:
            print(line)

        if recv_data:

            filename = re.findall('.*? /(.*?) HTTP', recv_data[0])[0]
            if filename == '':
                response_body = '/html/index.html'
            try :
                f = open('./html/index.html','rb')
                response_header = "HTTP/1.1 200 ok\r\n"
                response_header += "\r\n"
                response_body = f.read()
            finally:
                client_socket.send(response_header.encode('utf-8'))
                client_socket.send(response_body)
                client_socket.close()

if __name__ == '__main__':
    httpd = WSGIServer()
    httpd.start_server()
