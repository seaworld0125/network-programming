import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp socket
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())

    name = client.recv(1024).decode()
    print(name)
    client.send(int(20171528).to_bytes(4, 'big'))

    client.close()