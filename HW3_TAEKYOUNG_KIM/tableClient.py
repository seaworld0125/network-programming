from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 2500))

while True:
    msg = input('Number to send (1~10): ')
    if msg == 'q':
        sock.send(msg.encode())
        break

    try:
        num = int(msg)
    except:
        print('Try again')
    else:
        sock.send(msg.encode())
        print('Received msg: ', sock.recv(1024).decode())
    
sock.close()