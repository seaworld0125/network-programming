from socket import *
import random
import time

BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 3333))

while True:
    sock.settimeout(None)
    endFlag = False
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        msg = data.decode()

        if random.random() <= 0.85:
            continue
        else:
            if msg == 'exit':
                endFlag = True
            else:
                print('<-', msg)
            sock.sendto(b'ack', addr)
            break

    if endFlag:
        print('exit system : bad connection')
        break

    msg = input('-> ')
    reTx = 0

    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break

    if reTx >= 4:
        while True:
            sock.sendto('exit'.encode(), addr)
            sock.settimeout(1)
            try:
                data, _ = sock.recvfrom(BUFF_SIZE)
            except timeout:
                continue
            else:
                break
        print('exit system : bad connection')
        break
sock.close()