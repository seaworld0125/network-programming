from socket import *
from time import sleep

port = 2500
bufsize = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(bufsize)
    msg = data.decode()

    if msg == 'bye':
        conn.close()
        break

    print('receive msg : ', data.decode())
    conn.send(data)

sock.close()