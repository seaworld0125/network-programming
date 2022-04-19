from http import client
from socket import *
import threading
from time import sleep

port = 2500
BUFFSIZE = 1024

clientList = []

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

def connectThread(client, addr):
    global BUFFSIZE
    global clientList

    def checkNewClient():
        if (client, addr) not in clientList: # 첫 접속 client
            print('new client', addr)
            clientList.append((client, addr))

    def sendToAllClient(data):
        for clientSock, clientAddr in clientList:
            if clientAddr != addr:
                clientSock.send(data)

    def deleteClient():
        clientList.remove(addr)

    checkNewClient()

    while True:
        data = client.recv(BUFFSIZE)
        
        if not data:
            deleteClient()
            break
        
        msg = data.decode()
        print('receive msg >> {} from {}'.format(msg, addr))

        if msg == 'quit':
            deleteClient()
            break

        sendToAllClient(data)

while True:
    client, addr = sock.accept()
    t = threading.Thread(target=connectThread, args=(client, addr))
    t.setDaemon(True)
    t.start()