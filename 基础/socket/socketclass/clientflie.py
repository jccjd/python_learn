import socket

import os
root = os.getcwd()

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print (root)   #os.walk()所在目录
        print (dirs)   #os.walk()所在目录的所有目录名
        print (files)   #os.walk()所在目录的所有非目录文件名
        print (" ")

file_name(root)
class ClientFile(object):
    SERVERHOST = '127.0.0.1'
    SERVERPORT = 9999

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.message = ''


    def linkServer(self,host,port):
        self.client.connect((host,port))
        self.message = self.client.recv(1024)
        print(self.message.decode())

    def seedMesage(self,message):
        self.client.send(message.encode())

    def getMessage(self):
        self.message = self.client.recv(1024)
        print(self.message.decode())
    def download(self):

        with open('down/qq.txt','w+') as f:
            f.write(self.message.decode())

client = ClientFile()
client.linkServer('127.0.0.1',9999)
client.seedMesage('test.txt')
client.getMessage()
client.download()

