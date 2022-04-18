from socket import *

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 2500))

msg, addr = sock.recvfrom(1024)
print('receive msg : ', msg.decode())
sock.sendto(msg, addr)