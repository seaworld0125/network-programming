from socket import *
import sys

port = 2500
BUFSIZE = 1024

if len(sys.argv) > 1:
    port = int(sys.argv[1])

print('use port ', port)

addr = ('localhost', port)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(addr)
print('connected to', addr)

sock.send(input('input msg...').encode())
sock.close()