import selectors
from socket import *

port = 2500
BUFFSIZE = 1024

sel = selectors.DefaultSelector()
clients = []

def acceptClient(sock, mask):
    conn, addr = sock.accept()
    print('connected from', addr)
    sel.register(conn, selectors.EVENT_READ, data=readData) # 클라이언트 소켓 감시
    clients.append(conn)

def readData(conn, mask):
    data = conn.recv(BUFFSIZE)
    if not data:
        sel.unregister(conn)
        clients.remove(conn)
        conn.close()
        return
    for cs in clients:
        if cs != conn:
            cs.send(data)
    
s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind(('', 2500))
s_sock.listen(5)

sel.register(s_sock, selectors.EVENT_READ, data=acceptClient) # 서버 소켓 등록

while True:
    events = sel.select() # 이벤트 발생 여부 검사
    for key, mask in events:
        callback = key.data # 콜백 함수
        callback(key.fileobj, mask) # 소켓, 이벤트 종류