from socket import *
from time import sleep

port = 2500
bufsize = 1024
addr = ('localhost', port)

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(addr)

while True:
    msg = input('msg :')
    sock.send(msg.encode())

    if msg == 'bye':
        break

    data = sock.recv(bufsize)
    print('receive :', data.decode())

sock.close()