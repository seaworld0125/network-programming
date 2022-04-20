import binascii
from socket import *
import random
import struct

port = 7777
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

client, addr = sock.accept()

while True:
    data = client.recv(BUFFSIZE)
    if not data:
        break

    order = int(data.decode())

    temp = 0
    humid = 0
    illum = 0

    if order == 1:
        temp = random.randrange(1, 50)
    elif order == 2:
        humid = random.randrange(1, 100)
    elif order == 3:
        illum = random.randrange(1, 150)

    data = b''
    data += struct.pack('!I', temp)
    data += struct.pack('!I', humid)
    data += struct.pack('!I', illum)

    client.send(data)