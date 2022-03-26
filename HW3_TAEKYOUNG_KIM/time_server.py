import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 2500))
sock.listen(5)

while True:
    client, addr = sock.accept()
    print('connection from ', addr)
    client.send(time.ctime(time.time()).encode())
    client.close()