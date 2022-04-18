from socket import *
from time import sleep

port = 2500
BUFSIZE = 1024

sock = create_server(('', port), family=AF_INET, backlog=1)
conn, (remotehost, remoteport) = sock.accept()

print('connected by', remotehost, remoteport)

while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break

    print("receive message: ", data.decode())
    conn.send(data)

conn.close()

sleep(2)