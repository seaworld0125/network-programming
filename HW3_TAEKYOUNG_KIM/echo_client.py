import socket

port = int(input("Port No :"))
address = ("localhost", port)
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)

while True:
    msg = input("Message to send: ")
    try:
        byteSent = sock.send(msg.encode())
    except:
        print('connection closed')
        break
    else:
        
        print("{} bytes send".format(byteSent))

    try:
        data = sock.recv(BUFSIZE)
    except:
        print('connection closed')
        break
    else:
        if not data:
            break
        print("Received message: %s" % data.decode())

sock.close()