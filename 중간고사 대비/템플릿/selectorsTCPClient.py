import selectors
from socket import *

port = 2500
BUFFSIZE = 1024

sel = selectors.DefaultSelector()

def acceptClient(sock, mask):
    conn, addr = sock.accept()
    print('connected from', addr)
    sel.register(conn, selectors.EVENT_READ, data=readData) # 클라이언트 소켓 감시

def readData(conn, mask):
    data = conn.recv(BUFFSIZE)
    if not data:
        sel.unregister(conn)
        conn.close()
        return
    saveData(data.decode())
    
def saveData(data):
    with open("data.txt", "a") as f:
            f.write(data)

sock1 = socket(AF_INET, SOCK_STREAM)
sock1.connect(('localhost', 2501))
sock1.send(b'Register')

sock2 = socket(AF_INET, SOCK_STREAM)
sock2.connect(('localhost', 2502))
sock1.send(b'Register')

sel.register(sock1, selectors.EVENT_READ, data=readData) # 소켓 등록
sel.register(sock2, selectors.EVENT_READ, data=readData) # 소켓 등록

while True:
    events = sel.select() # 이벤트 발생 여부 검사
    for key, mask in events:
        callback = key.data # 콜백 함수
        callback(key.fileobj, mask) # 소켓, 이벤트 종류