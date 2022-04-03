from socket import *


while True:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 2500))

    msg = input('Enter the message("send mboxId message" or "receive mboxId"):')

    if msg == 'quit':
        s.send(msg.encode())
        s.close()
        break
    else:
        s.send(msg.encode())
        print(s.recv(1024).decode())
    s.close()