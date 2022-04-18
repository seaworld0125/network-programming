from socket import *
from time import sleep

port = 2500
BUFSIZE = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

client, addr = sock.accept()

targetMsgSize = ntohl(int(client.recv(1024).decode()))
totalMsgSize = 0
totalMsg = []

while totalMsgSize < targetMsgSize:
    data = client.recv(BUFSIZE)
    if not data:
        break

    totalMsgSize += len(data)
    totalMsg.append(data.decode())
    print(totalMsg)

client.close()
sock.close()

message = ''.join(totalMsg)
print(message)
sleep(2)