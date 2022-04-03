from socket import *
import random

# Temp, Humid, Illum

def getTemp():
    return str(random.randrange(40, 140))

def getHumid():
    return str(random.randrange(2000, 6000))

def getIllum():
    return str(random.randrange(1000, 4000))

def getResponse():
    return getTemp() + ' ' + getHumid() + ' ' + getIllum()

port = 2502
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