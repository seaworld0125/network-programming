from socket import *
from time import sleep

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    sendBytes = client.send(b'Hello ' + addr[0].encode())
    print('sendBytes : ', sendBytes)
    sendBytes = client.send((2058).to_bytes(4, 'big')) # 정수 변환
    print('sendBytes : ', sendBytes)
    client.close()
    break

sleep(2)