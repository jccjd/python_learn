import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serveraddr = (socket.gethostname(), 9999)
client.connect(serveraddr)
servermsg = client.recv(1024)
clientmessage = 'hello server'
client.send(clientmessage.encode())

print(servermsg)
client.close()
