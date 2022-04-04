from socket import *


while True:
    sock = socket(AF_INET, SOCK_DGRAM)
    addr = ('localhost', 2500)

    msg = input('Enter the message("send mboxId message" or "receive mboxId"):')

    if msg == 'quit':
        sock.sendto(msg.encode(), addr)
        sock.close()
        break

    sock.sendto(msg.encode(), addr)
    data, _ = sock.recvfrom(1024)
    print(data.decode())
    sock.close()