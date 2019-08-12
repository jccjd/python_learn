import socket

serverclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9000

serverclient.bind((host, port))

serverclient.listen(2)
while True:
    client, msg = serverclient.accept()

    print(msg)
    client.send('hello'.encode())
    client.close()