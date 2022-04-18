from datetime import datetime
from socket import *
import argparse, random

BUFFSIZE = 1024

def Server(ipaddr, port, prob):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((ipaddr, port))
    print('Waiting in {}...'.format(sock.getsockname()))

    while True:
        data, addr = sock.recvfrom(BUFFSIZE)
        if random.random() < prob:
            print('Message from {} is lost'.format(addr))
            continue
        
        print('{} client message {!r}'.format(addr, data.decode()))
        text = 'The length is {} bytes'.format(len(data))
        sock.sendto(text.encode(), addr)
    
def Client(port, sendMaxCount):
    sock = socket(AF_INET, SOCK_DGRAM)
    
    index = 1 # 메시지 index
    time = 0.1 # 대기 시간

    while True:
        date = str(datetime.now())

        print('send data: ', date)
        sock.sendto(date.encode(), ('localhost', port))

        print('{} waiting for {} sec'.format(index, time))
        sock.settimeout(time)

        try:
            data, addr = sock.recvfrom(BUFFSIZE)
        except timeout:
            time *= 2
            if time > 2:
                print('{}th packet is lost'.format(index))
                if index >= sendMaxCount:
                    break
                index += 1
                time = 0.1
        else:
            print('receive msg ({!r}) from ({})'.format(data.decode(), addr))
            if index >= sendMaxCount:
                break
            index += 1
            time = 0.1
            
if __name__ == '__main__':
    mode = {'c': Client, 's': Server}

    parser = argparse.ArgumentParser(description='Send and receive UDP packets drop probability')
    parser.add_argument('role', choices=mode, help='which role to take between server(s) and client(c)')
    parser.add_argument('-s', default='localhost', help='server that client sends to')
    parser.add_argument('-p', type=int, default=2500, help='UDP port (default:2500)')
    parser.add_argument('-prob', type=float, default=0, help='dropping probability (0~1)')
    parser.add_argument('-count', type=int, default=10, help='number of sending packets')

    args = parser.parse_args()

    if args.role == 's':
        mode[args.role](args.s, args.p, args.prob)
    else:
        mode[args.role](args.p, args.count)