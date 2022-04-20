from socket import *
from time import sleep

addr = ('localhost', 2500)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(addr)

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"):')
    if msg == 'quit':
        sock.send(msg.encode())
        break

    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())

sock.close()