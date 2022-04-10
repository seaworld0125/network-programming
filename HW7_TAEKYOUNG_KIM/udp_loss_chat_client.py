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

    c_sock.settimeout(9)
    try:
        while True:
            data, _ = c_sock.recvfrom(BUFF_SIZE)
        
            if random.random() <= 0.5:
                continue
            else:
                c_sock.sendto(b'ack', addr)
                print('<-', data.decode())
                break
    except:
        print('연결 상태가 양호하지 않습니다')
        break
c_sock.close()