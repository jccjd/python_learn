import socket
import threading

def send_msg(udp_socket):
    while True:
        msg = input('\nyou msg: ')
        dest_ip = input('\n server ip')
        dest_port = int(input('port'))
        udp_socket.sendto(msg.encode('utf-8'), (dest_ip, dest_port))

def recv_msg(udp_socket):
    while True:
        recv_msg, recv_ip = udp_socket.recvfrom(1024)

        print(recv_ip,recv_msg)

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', 7890))
    t = threading.Thread(target=recv_msg, args=(udp_socket,))
    t.start()

    send_msg(udp_socket)

main()
