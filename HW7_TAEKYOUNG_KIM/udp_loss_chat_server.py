from socket import *
import random
import time

BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 3333))

while True:
    sock.settimeout(9)
    try:
        while True:
                data, addr = sock.recvfrom(BUFF_SIZE)
            
                if random.random() <= 0.5:
                    continue
                else:
                    sock.sendto(b'ack', addr)
                    print('<-', data.decode())
                    break
    except:
        print('연결 상태가 양호하지 않습니다')
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
sock.close()