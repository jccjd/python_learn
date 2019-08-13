import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

server.bind((host, port))
server.listen(2)

while True:
    client, address = server.accept()
    print(address,'--->>>','connection' )

    servermsg = 'connection server'
    client.send(servermsg.encode())

    clientmsg = client.recv(1024)
    print(f'{address} message is : {clientmsg.decode()}')
server.close()