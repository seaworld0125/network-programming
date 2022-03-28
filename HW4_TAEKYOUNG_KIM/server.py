import mimetypes
from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.settimeout(5)
sock.bind(('', 80))
sock.listen(5)
print('waiting...\n')

try:
    while True:
        client, addr = sock.accept()
        
        data = client.recv(1024).decode().split(' ')
        fname = data[1][1:]
        print('recv request : ' + fname)

        try:
            mimeType = mimetypes.guess_type(fname)[0]
            if mimeType == 'text/html':
                f = open(fname, 'r', encoding='UTF-8')
            else:
                f = open(fname, 'rb')
        except Exception as e:
            print('Err : ' + e)
            header_ = 'HTTP/1.1 404 Not Found\r\n\r\n'.encode()
            body_ = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'.encode()
        else:
            header_ = ('HTTP/1.1 200 OK/r/n' + 'Content-Type: ' + mimeType + '\r\n\r\n').encode()
            body_ = f.read()
            if mimeType == 'text/html':
                body_ = body_.encode('euc-kr')
        finally:
            client.send(header_)
            client.send(body_)
            client.close()
except:
    print('\nShut down the server because there are no more requests')
finally:
    sock.close()

