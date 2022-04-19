import random, time
from socket import *

port = 2502
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

client, addr = sock.accept()

msg = client.recv(BUFFSIZE).decode()

while True:
    Heartbeat = random.randrange(40, 140)
    Steps = random.randrange(2000, 6000)
    Cal = random.randrange(1000, 4000)

    data = '{}: Device1: Heartbeat={}, Steps={}, Cal{}\n'.format(time.ctime(time.time()), Heartbeat, Steps, Cal)

    client.send(data.encode())
    time.sleep(3)