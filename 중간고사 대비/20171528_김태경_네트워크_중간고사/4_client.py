from socket import *
import time

servAddr = ('localhost', 2500)
sock = socket(AF_INET, SOCK_DGRAM)

count = 1

while count < 3:
    sendTime = time.time()
    sock.sendto(b'ping', servAddr)
    
    sock.settimeout(1)
    try:
        data, _ = sock.recvfrom(1024)
        print('Success (RTT: {:0.6f})'.format(sendTime - time.time()))
        break
    except:
        count += 1

if count == 3:
    print('Fail')

time.sleep(2)