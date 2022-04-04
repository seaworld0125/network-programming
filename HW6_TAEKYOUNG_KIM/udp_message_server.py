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
    
while True:
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('', port))

    data, addr = sock.recvfrom(BUFSIZE)
    data = data.decode().split(' ')

    if(data[0] == 'quit'):
        sock.close()
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
        sock.sendto(msg.encode(), addr)
              
    except Exception as e:
        sock.sendto('Exception error'.encode(), addr)

    sock.close()