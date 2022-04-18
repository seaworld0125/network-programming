from socket import *
from time import sleep

sock = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', 9000)

sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
msg = sock.recv(1024)
print(int.from_bytes(msg, 'big')) # 정수 변환
sock.close()

sleep(2)