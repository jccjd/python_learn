import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serveraddr = (socket.gethostname(), 9999)
client.connect(serveraddr)

servermsg = client.recv(1024)
print(servermsg)

clientmessage = 'test.txt'
client.send(clientmessage.encode())

contxt = client.recv(1024)

with open('down/text.tx','wb+') as  f:
    f.write(contxt)

client.close()