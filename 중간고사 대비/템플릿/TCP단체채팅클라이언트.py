import socket
import threading

def handler(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode())

svr_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(svr_addr)

my_id = input('ID를 입력하세요: ')

th = threading.Thread(target=handler, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = input()
    data = '[' + my_id + '] ' + msg
    sock.send(data.encode())

    if msg == 'quit':
        break