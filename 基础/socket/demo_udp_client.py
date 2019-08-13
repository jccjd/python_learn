import socket
server_ip = ('127.0.0.1',9102)
client_ip = ('127.0.0.1',9101)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(client_ip)
while True:
    msg = 'hello'
    s.sendto(msg.encode(),server_ip)
    break
