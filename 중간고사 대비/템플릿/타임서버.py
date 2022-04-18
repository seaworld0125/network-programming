from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 2500))
s.listen(5)

while True:
    client, addr = s.accept()
    print('connection from', addr)
    client.send(time.ctime(time.time()).encode())
    client.close()