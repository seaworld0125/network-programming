from socket import *

serverAddr = ('localhost', 2500)

sock = socket(AF_INET, SOCK_DGRAM)
sock.sendto('hello~!'.encode(), serverAddr)
msg, addr = sock.recvfrom(1024)
print('receive {} from {}'.format(msg.decode(), addr))