from socket import *
from collections import deque

storage = {} # dict

def storageData(data, index):
    try:
        len(storage[index])
    except:
        storage[index] = deque()
    storage[index].append(data)
    return 'OK'

def popData(index):
    try:
        if len(storage[index]) == 0:
            return 'No messages'
    except:
        return 'No messages'
    return storage[index].popleft()

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)
    
while True:
    conn, addr = sock.accept()
    data = conn.recv(BUFSIZE).decode().split(' ')

    if(data[0] == 'quit'):
        conn.close()
        break

    try:
        order = data[0]
        index = int(data[1])
        msg = ''

        if order == 'send':
            for d in data[2:]: # msg append
                msg += (d + ' ')
            if msg == '':
                msg = 'input error : no message'
            else :
                msg = storageData(msg, index)
        elif order == 'receive':
            msg = popData(index)
        else:
            msg = 'message error : bad order'
        conn.send(msg.encode())
              
    except Exception as e:
        conn.send('message error'.encode())

    conn.close()

sock.close()