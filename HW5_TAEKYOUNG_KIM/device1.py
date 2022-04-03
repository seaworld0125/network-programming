from socket import *
import random

# Temp, Humid, Illum

def getTemp():
    return str(random.randrange(0, 40))

def getHumid():
    return str(random.randrange(0, 100))

def getIllum():
    return str(random.randrange(70, 150))

def getResponse():
    return getTemp() + ' ' + getHumid() + ' ' + getIllum()

port = 2501
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
# sock.settimeout(5)
sock.listen(5)

while True:
    conn, args = sock.accept()

    data = conn.recv(BUFSIZE).decode()
    
    if data == 'Request':
        conn.send(getResponse().encode())
    elif data == 'quit':
        break
    conn.close()

conn.close()
sock.close()