import mimetypes
from socket import *
from time import sleep

def createData(fname):
    try:
        mimeType = mimetypes.guess_type(fname)[0]
        if mimeType == 'text/html':
            f = open(fname, 'r', encoding='UTF-8')
        else:
            f = open(fname, 'rb')
    except Exception as e:
        print('not found error')
        header_ = 'HTTP/1.1 404 Not Found\r\n\r\n'.encode()
        body_ = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'.encode('euc-kr')
        CNotFoundErr = True
    else:
        header_ = ('HTTP/1.1 200 OK/r/n' + 'Content-Type: ' + mimeType + '\r\n\r\n').encode()
        body_ = f.read()
        if mimeType == 'text/html':
            body_ = body_.encode('euc-kr')
        CNotFoundErr = False
    finally:
        return header_, body_, CNotFoundErr

def clientConnect(sock):
    while True:
        client, addr = sock.accept()
        data = client.recv(1024)
        print('---- data : ', data)
        if len(data) == 0: 
            client.close()
            break

        data = data.decode().split(' ')
        fname = data[1][1:]
        print('recv request : ' + fname)

        header_, body_, CNotFoundErr = createData(fname)
        client.send(header_)
        client.send(body_)
        client.close()
        if CNotFoundErr: break

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 80))
sock.listen(5)
try:
    clientConnect(sock)
except:
    print('occur socket.timeout, socket close')
finally:
    sock.close()

sleep(5)