from socket import AF_INET


class TCPServer:
    def __init__(self, port):
        import socket
        self.sock = socket.create_server(('', port), family=AF_INET, backlog=1)
        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.bind(('', port))
        # self.sock.listen(5)

    def Accept(self):
        return self.sock.accept()

if __name__ == '__main__':
    sock = TCPServer(2500)
    client, addr = sock.Accept()
    print('connected by ', addr)
    client.send(b'Hello Client')
    client.close()