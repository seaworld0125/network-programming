from socket import *
import sys

port = 2500
BUFSIZE = 1024

if len(sys.argv) > 1:
    port = int(sys.argv[1])

print('use port ', port)

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
print('waiting connect...')

conn, addr = sock.accept()

print('connected by', addr)

data = conn.recv(BUFSIZE)
print('receive data : ', data.decode())
conn.close()    