from socket import *
import select
import threading

r_socks = [] # 읽기 소켓 리스트

BUFFSIZE = 1024
PORT = 2500

s_sock = socket(AF_INET, SOCK_STREAM) # TCP 소켓
s_sock.bind(('', PORT))
s_sock.listen(5)
r_socks.append(s_sock) # 서버 소켓 추가

print(PORT, '에서 접속 대기 중')

def connectThread(client):
    global BUFFSIZE
    global r_socks

    def checkNewClient():
        if client not in r_socks: # 첫 접속 client
            r_socks.append(client)

    def sendToAllClient(data):
        for clientSock in r_socks:
            if clientSock != client and clientSock != s_sock:
                clientSock.send(data)

    def deleteClient():
        r_socks.remove(client)

    checkNewClient()

    while True:
        try:
            data = client.recv(BUFFSIZE)
            
            if not data:
                deleteClient()
                break
            
            msg = data.decode()
            print('receive msg >> {}'.format(msg))

            if 'quit' in msg:
                deleteClient()
                break

            sendToAllClient(data)
        except Exception as e:
            print(e)
        finally:
            break

while True:
    r_sock, w_sock, e_sock = select.select(r_socks, [], [])

    for s in r_sock:
        if s == s_sock: # 새로운 연결
            c_sock, addr = s_sock.accept()
            r_socks.append(c_sock)
            print('Client ({}) connected'.format(addr))
        else: 
            th = threading.Thread(target=connectThread, args=(s,))
            th.setDaemon(True)
            th.start()