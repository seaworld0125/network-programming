import TCP서버모듈 as mys
import sys

if len(sys.argv) > 1:
    port = int(sys.argv[1])

bufsize = 1024
port = 2500

sock = mys.TCPServer(port)
conn, addr = sock.Accept()
print('연결 : ', addr)

while True:
    data = conn.recv(bufsize)
    if not data:
        break
    print('받은 메시지 : ', data.decode())
    conn.send(data)

conn.close()