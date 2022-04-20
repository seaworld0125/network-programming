import random
from socket import *
from time import sleep

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFSIZE)
    if not data:
        break

    msg = data.decode()

    if msg != 'ping': # ping이 아니면 무시
        continue

    if random.random() < 0.5: # 무시
        continue

    sock.sendto(b'pong', addr)

client.close()
sock.close()

sleep(2)