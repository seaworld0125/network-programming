import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 2500))
print("Time: ", sock.recv(1024).decode())
sock.close()