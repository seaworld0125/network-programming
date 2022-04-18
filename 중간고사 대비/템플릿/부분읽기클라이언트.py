from socket import *
from time import sleep

sock = create_connection(('localhost', 2500))

msgSize = len('This is IoT world!!!')

sock.send(str(htonl(msgSize)).encode())
sleep(1)

sock.send(b'This is IoT world!!!')
sock.close()
sleep(2)