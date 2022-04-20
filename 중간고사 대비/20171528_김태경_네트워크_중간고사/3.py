import socket

ip = '220.69.189.125'
port = 443

host = socket.gethostbyaddr(ip)[0]
serv = socket.getservbyport(port)
byte = socket.inet_aton(ip)

print(host)
print(serv)
print(serv + '://' + host)
print(byte)