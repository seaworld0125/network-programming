import socket

port = int(input("Port No :"))
address = ("localhost", port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)

while True:
    msg = input("Message to send: ")

    if msg == 'q':
        sock.send(msg.encode())
        print("Connection close")
        break

    try:
        sock.send(msg.encode())
    except:
        print('connection closed')
        break

    try:
        data = sock.recv(1024)
    except:
        print('connection closed')
        break
    else:
        if not data:
            break
        print("ans: %s" % data.decode())

sock.close()