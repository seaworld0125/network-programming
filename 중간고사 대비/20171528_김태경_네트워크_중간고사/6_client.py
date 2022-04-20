from socket import *
import struct

BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 7777))

while True:
    order = str(input('order >> '))
    sock.send(order.encode())

    data = sock.recv(BUFFSIZE)
    unpackData = struct.unpack('!3I', data)

    print('Temp={}, Humid={}, Lumi={}'.format(unpackData[0], unpackData[1], unpackData[2]))