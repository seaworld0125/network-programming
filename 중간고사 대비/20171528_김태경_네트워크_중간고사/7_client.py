from socket import *
import threading

def handler(sock):
    while True:
        msg = sock.recv(1024)
        print(msg.decode())

svr_addr = ('localhost', 2500)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(svr_addr)

my_id = input('ID를 입력하세요: ')

th = threading.Thread(target=handler, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = '[' + my_id + '] ' + input()
    sock.send(msg.encode())