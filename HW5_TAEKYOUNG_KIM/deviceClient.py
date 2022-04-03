from asyncio.windows_utils import BUFSIZE
from socket import *
import os.path
import time

def recreateData(data, port):
    newData = time.strftime('%c', time.localtime(time.time()))
    if port == 2501:
        newData += ': Device1: '
        newData += ('Temp=' + data[0]) 
        newData += (', Humid=' + data[1]) 
        newData += (', Temp=' + data[2] + '\n') 
    else:
        newData += ': Device2: '
        newData += ('Heartbeat=' + data[0]) 
        newData += (', Steps=' + data[1]) 
        newData += (', Cal=' + data[2] + '\n')
    return newData 


while True:
    BUFSIZE = 1024
    port = input('input order : ')
    
    if port == 'quit':
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 2501))
        s.send(b'quit')
        s.close()

        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 2502))
        s.send(b'quit')
        s.close()
        break

    try:
        if int(port) == 1:
            port = 2501
        elif int(port) == 2:
            port = 2502
        else:
            port = -1
    except:
        print('please input 1 or 2')

    if port == 2501 or port == 2502:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', port))
        print('connected to device : ', port)
    
        s.send(b'Request')
        data = s.recv(BUFSIZE).decode().split(' ')
        data = recreateData(data, port)
        
        with open("data.txt", "a") as f:
            f.write(data)
        s.close()