import multiprocessing
import re
import socket


class WSGIServer(object):
    def __init__(self, socketaddress):
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind(socketaddress)
        self.listen_socket.listen(128)

    def start_server(self):
        while True:
            client_socket, client_address = self.listen_socket.accept()

            newprocess = multiprocessing.Process(target=self.handleResquest, args=(client_socket,))
            newprocess.start()


    def handleResquest(self,client_socket):
        recvdata = client_socket.recv(1024).decode('utf-8')
        requestHandlelines = recvdata.splitlines()
        for line in requestHandlelines:
            print(line)

        requestline = requestHandlelines[0]


        filename = re.findall('.*?/(.*?) HTTP', requestline)

        real_filename = direct + filename[0]
        try:
            f = open(real_filename, 'rb')
        except IOError:
            responsebody = ''
            response_header = "HTTP/1.1 404 not found\r\n"
            response_header += "\r\n"
            response_body = "====sorry ,file not found===="
        else:
            response_header = "HTTP/1.1 200 ok\r\n"
            response_header += "\r\n"
            response_body = f.read()
        finally:
            client_socket.send(response_header.encode())
            client_socket.send(response_body)
            client_socket.close()

direct = './html/'
server_address = (HOST,PORT) = '', 9000
if __name__ == '__main__':
    httpd = WSGIServer(server_address)
    print('web server port is --->', PORT)
    httpd.start_server()
