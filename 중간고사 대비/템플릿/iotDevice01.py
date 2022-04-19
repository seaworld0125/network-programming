import random, time
from socket import *

port = 2501
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

client, addr = sock.accept()

msg = client.recv(BUFFSIZE).decode()

while True:
    Temp = random.randrange(0, 40)
    Humid = random.randrange(0, 100)
    Illum = random.randrange(70, 150)

    data = '{}: Device1: Temp={}, Humid={}, Illum{}\n'.format(time.ctime(time.time()), Temp, Humid, Illum)

    client.send(data.encode())
    time.sleep(3)