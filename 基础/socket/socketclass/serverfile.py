import socket
import os
class ServerFile(object):
    def __init__(self,ip="127.0.0.1", port=9999):
        self.ip = ip
        self.port = port
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((self.ip,self.port))
        self.server.listen(5)
        self.client = None
        self.message = ''


    def startServer(self):
        while True:
            client, address = self.server.accept()

            print(address)
            self.client = client
            self.client.send('connection success'.encode())

            self.message = self.getmessage()
            if self.message == 'test.txt':
                self.download(self.message)
            self.client.close()

    def download(self,message):
        with open(message,'rb') as f:
            contxt = f.read()
        self.client.send(contxt)
    def getpwd(self):
        print(os.path)

    def getmessage(self):
        message = self.client.recv(1024)
        return message.decode()

server = ServerFile()
server.startServer()
