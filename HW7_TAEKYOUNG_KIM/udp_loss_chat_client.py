from socket import *
import random
import time

BUFF_SIZE = 1024

c_sock = socket(AF_INET, SOCK_DGRAM)
addr = ('localhost', 3333)

while True:
    msg = input('-> ')
    reTx = 0

    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        c_sock.sendto(resp.encode(), addr)
        c_sock.settimeout(2)

        try:
            data, _ = c_sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break
    
    if reTx >= 4:
        while True:
            c_sock.sendto('exit'.encode(), addr)
            c_sock.settimeout(1)
            try:
                data, _ = c_sock.recvfrom(BUFF_SIZE)
            except timeout:
                continue
            else:
                break
        print('exit system : bad connection')
        break

    c_sock.settimeout(None)
    endFlag = False
    while True:
        data, _ = c_sock.recvfrom(BUFF_SIZE)
        msg = data.decode()
    
        if random.random() <= 0.85:
            continue
        else:
            if msg == 'exit':
                endFlag = True
            else:
                print('<-', msg)
            c_sock.sendto(b'ack', addr)
            break

    if endFlag:
        print('exit system : bad connection')
        break
    
c_sock.close()