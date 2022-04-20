from socket import *
from collections import deque
import select
import threading

storage = {} # dict
r_socks = [] # 읽기 소켓 리스트

lock = threading.Lock()

def newTask(client, data):
    global storage
    global lock

    def storageData(msg, index):
        lock.acquire() # 점유
        try:
            len(storage[index])
        except:
            storage[index] = deque()
        storage[index].append(msg)
        lock.release() # 해제
        return 'OK'

    def popData(index):
        lock.acquire() # 점유
        msg = ''
        try:
            if len(storage[index]) == 0:
                msg = 'No messages'
            else:
                msg = storage[index].popleft()
        except:
            msg = 'No messages'
        finally: 
            lock.release() # 해제
            return msg


    #main
    if client not in r_socks:
        return

    try:
        data = data.decode().split(' ')
        order = data[0]
        index = int(data[1])
        msg = ''
    except:
        return

    try:
        if order == 'send':
            for d in data[2:]: # msg append
                msg += (d + ' ')
            if msg == '':
                msg = 'input error : no message'
            else :
                msg = storageData(msg, index)
        elif order == 'receive':
            msg = popData(index)
        else:
            msg = 'message error : bad order'
    except:
        msg = 'message error : bad order'
    finally:
        client.send(msg.encode())

BUFSIZE = 1024
port = 2500
    
s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind(('', 2500))
s_sock.listen(5)
r_socks.append(s_sock) # 서버 소켓 추가

while True:
    r_sock, w_sock, e_sock = select.select(r_socks, [], [])

    for s in r_sock:
        if s == s_sock: # 새로운 연결
            c_sock, addr = s_sock.accept()
            r_socks.append(c_sock)
            print('Client ({}) connected'.format(addr))
        else: 
            try:
                data = s.recv(BUFSIZE)
                if not data or data == 'quit':
                    s.close()
                    r_socks.remove(s)
                    continue
                else:
                    th = threading.Thread(target=newTask, args=(s, data,))
                    th.setDaemon(True)
                    th.start()
            except:
                s.close()
                r_socks.remove(s)
                continue