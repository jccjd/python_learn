import socket
server_ip = ('127.0.0.1',9102)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(server_ip)

while True:
    client_data, client_address = s.recvfrom(1122)
    print(client_data.decode(), client_address)

